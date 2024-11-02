# Copyright (c) 2024 Dinghao Zhou  (hamddct@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import io

import pydub
from pysilero import SileroVAD
from wenet.cli.paraformer_model import load_model


def batch_audio_iterator(
    vad,
    vad_fobj,
    audio,
    batch_size=1,
    max_speech_duration_s=60,
):
    batch = []
    timestamps_iterator = vad.get_speech_timestamps(
        vad_fobj,
        save_path=None,
        flat_layout=False,
        return_seconds=True,
        max_speech_duration_s=max_speech_duration_s)
    for ts in timestamps_iterator:
        start, end = ts['start'], ts['end']
        clip = audio[start * 1000:end * 1000]
        clip.set_frame_rate(16000)
        clip.set_sample_width(2)
        with io.BytesIO() as fobj:
            clip.export(
                fobj,
                format='wav',
            )
            fobj.seek(0)
            clip = fobj.read()
        batch.append({'start': start, 'end': end, 'wav': clip})
        if len(batch) == batch_size:
            yield batch
            batch = []
    if len(batch) != 0:
        yield batch


def main(in_path):

    vad = SileroVAD(min_silence_duration_ms=100)
    recognizer = load_model()

    audio = pydub.AudioSegment.from_file(in_path)
    audio.set_frame_rate(16000)
    audio.set_sample_width(2)

    with io.BytesIO() as vad_fobj:
        audio.export(vad_fobj, format='wav')
        vad_fobj.seek(0)
        for (_, batch) in enumerate(batch_audio_iterator(vad, vad_fobj,
                                                         audio)):
            audio_batch = [io.BytesIO(sample['wav']) for sample in batch]
            for i, result in enumerate(
                    recognizer.transcribe_batch(audio_batch, True)):
                for token in result['tokens']:
                    token['start'] += batch[i]['start']
                    token['end'] += batch[i]['start']
                print(batch[i]['end'], result)
            for clip_fobj in audio_batch:
                clip_fobj.close()


def get_args():

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('audio_file', help='audio file to transcribe')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    main(args.audio_file)
