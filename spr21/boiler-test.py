# boiler-test.py

import requests
import sys
from boilerpy3 import extractors

# Tested on HTML documents downloaded with
# wget -O test.html "https://www.cnn.com/2021/03/03/business/wendys-breakfast-sales/index.html"
# wget -O test.html "https://www.cnn.com/2021/03/03/world/iceland-volcano-eruption-keilir-intl-latam/index.html"

# % python3 boiler-test.py < test.html > test.txt

# settings to avoid UnicodeDecodeError
# if you get "AttributeError: '_io.TextIOWrapper' object has no attribute 'reconfigure'"
# comment out these lines
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# read in entire input into a string
text = sys.stdin.read()

# strip tags
extractor = extractors.ArticleExtractor()
content = extractor.get_content(text)

# write processed output to stdout
print(content, file=sys.stdout)
