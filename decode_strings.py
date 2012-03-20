import sys

for line in sys.stdin:
  line = line.split("\t")[1].decode("string-escape").lower().replace("\n","").replace("."," ").split()
  for word in line:
    print word

