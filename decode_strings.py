# parses text-wiki format and outputs each word at separate line
# input has a wiki article per line: "title tab string-escaped article content"

import string
import sys

for line in sys.stdin:
  line = line.split("\t")[1].decode("string-escape").lower().replace("\n","").replace("."," ").split()
  for word in line:
    print filter(str.isalnum,word)

