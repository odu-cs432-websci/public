# boiler-test-file.py

import requests
import sys
from boilerpy3 import extractors

# Tested on HTML documents downloaded with
# wget -O test.html "https://www.cnn.com/2021/03/03/business/wendys-breakfast-sales/index.html"
# wget -O test.html "https://www.cnn.com/2021/03/03/world/iceland-volcano-eruption-keilir-intl-latam/index.html"

# % python3 boiler-test.py
infile = "test.html"
outfile = "test.txt"

# read in file to avoid UnicodeDecodeError
inf = open(infile, "r", encoding="utf=8")
text = inf.read()
inf.close()

# strip tags
extractor = extractors.ArticleExtractor()
content = extractor.get_content(text)

# write processed output to text file
f = open (outfile, "w", encoding="utf-8")
f.write(content)
f.close()
