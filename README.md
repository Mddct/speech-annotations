# speech-annotations

speech-annotation in pure wenet way.

```bash
$ pip install -r requirments.txt

python3 annotation.py test.mp4

```
```bash
{'confidence': 0.9245624491884938, 'text': '富士康在印度工厂出现大规模感染', 'start': 0.508, 'end': 3.94, tokens': [{'token': '富', 'start': 0.598, 'end': 0.738, 'confidence': 0.96}, {'token': '士', 'start': 0.738, 'end': 0.858, 'confidence': 0.94}, {'token': '康', 'start': 0.858, 'end': 1.1179999999999999, 'confidence': 0.94}, {'token': '在', 'start': 1.1179999999999999, 'end': 1.338, 'confidence': 0.89}, {'token': '印', 'start': 1.338, 'end': 1.558, 'confidence': 0.95}, {'token': '度', 'start': 1.558, 'end': 1.838, 'confidence': 0.92}, {'token': '工', 'start': 1.8780000000000001, 'end': 2.0380000000000003, 'confidence': 0.92}, {'token': '厂', 'start': 2.0380000000000003, 'end': 2.258, 'confidence': 0.94}, {'token': '出', 'start': 2.258, 'end': 2.4379999999999997, 'confidence': 0.9}, {'token': '现', 'start': 2.4379999999999997, 'end': 2.698, 'confidence': 0.9}, {'token': '大', 'start': 2.698, 'end': 2.918, 'confidence': 0.9}, {'token': '规', 'start': 2.918, 'end': 3.078, 'confidence': 0.94}, {'token': '模', 'start': 3.078, 'end': 3.338, 'confidence': 0.94}, {'token': '感', 'start': 3.338, 'end': 3.498, 'confidence': 0.92}, {'token': '染', 'start': 3.498, 'end': 3.753, 'confidence': 0.95}, {'token': '<eos>', 'start': 3.753, 'end': 3.928, 'confidence': 0.9}]
{'confidence': 0.9131879881113388, 'text': '目前工厂产量已下降超百分之五十', 'start': 4.028, 'end': 7.428, tokens': [{'token': '目', 'start': 4.138, 'end': 4.258, 'confidence': 0.93}, {'token': '前', 'start': 4.258, 'end': 4.518, 'confidence': 0.91}, {'token': '工', 'start': 4.518, 'end': 4.678, 'confidence': 0.92}, {'token': '厂', 'start': 4.678, 'end': 4.917999999999999, 'confidence': 0.95}, {'token': '产', 'start': 4.917999999999999, 'end': 5.077999999999999, 'confidence': 0.92}, {'token': '量', 'start': 5.077999999999999, 'end': 5.318, 'confidence': 0.92}, {'token': '已', 'start': 5.318, 'end': 5.537999999999999, 'confidence': 0.91}, {'token': '下', 'start': 5.537999999999999, 'end': 5.718, 'confidence': 0.9}, {'token': '降', 'start': 5.718, 'end': 5.957999999999999, 'confidence': 0.95}, {'token': '超', 'start': 5.957999999999999, 'end': 6.2379999999999995, 'confidence': 0.93}, {'token': '百', 'start': 6.298, 'end': 6.438, 'confidence': 0.9}, {'token': '分', 'start': 6.438, 'end': 6.537999999999999, 'confidence': 0.9}, {'token': '之', 'start': 6.537999999999999, 'end': 6.7379999999999995, 'confidence': 0.9}, {'token': '五', 'start': 6.7379999999999995, 'end': 6.898, 'confidence': 0.9}, {'token': '十', 'start': 6.898, 'end': 7.212999999999999, 'confidence': 0.9}, {'token': '<eos>', 'start': 7.212999999999999, 'end': 7.4479999999999995, 'confidence': 0.9}]

```
