# Split words
Implementation of tools helps to convert the rect of sentence-level and phrase-level to word-level by using linear interpolation.


## Installation

```bash 
cd convert-to-word-level
pip install .
```

## Usage

```python
from splitwords import Splitter
import re

splitter = Splitter(languages=['vi', 'en', 'teencode'])
paragraph = "Chất liệudẻo. Màu sắcđen đen. Dép đẹp lắm luônn ạ. Miksăn được k thikquá tr. shipperthân thiện"

sentence_ls = []
pat = re.compile(r"([.()!])")

paragraph = pat.sub(" \\1 ", paragraph)
new_paragraph = []
new_w = None
for w in paragraph.split():
    if len(w) > 3:
        new_w = splitter.split(w.upper())
    else:
        new_w = None
    new_paragraph += [
        ' '.join(new_w).lower() if new_w is not None else w.lower()
    ]
new_paragraph = ' '.join(new_paragraph)
print(new_paragraph)
```
Expected output:
```bash
chất liệu dẻo . màu sắc đen đen . dép đẹp lắm luôn n ạ . mik săn được k thik quá tr . shipper thân thiện
```
