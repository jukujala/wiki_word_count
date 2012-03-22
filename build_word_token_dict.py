import cPickle
import cStringIO
import sys

NCOUNTLIMIT = 5
NMAXSTRINGLEN = 17

def create_token_dict(f):
  """
  Input: word per line
  Output: dictionary mapping words to the number of occurences
  Note: easy way to make this faster is to take a sample of input words, saves memory too
  """
  d = {}
  i = 0
  #count different words
  for t in f:
    if len(t) < NMAXSTRINGLEN:
      d[t] = d.setdefault(t,0)+1
  #prune words with less than NCOUNTLIMIT occurences
  for k in d.keys():
    if d[k] < NCOUNTLIMIT:
      del d[k]
  return d

def usage():
  print "cat one_word_per_line | %s token_counts.pickle"

def parse_cp():
  if len(sys.argv) != 2:
    usage()
    sys.exit(-1)
  return (sys.argv[1])

def main():
  outfn = parse_cp()
  inf = sys.stdin
  d = create_token_dict(inf)
  outf = open(outfn,"w")
  cPickle.dump(d,outf, protocol=cPickle.HIGHEST_PROTOCOL)
  outf.close()
  print "wrote token dict to file %s" %outfn

if __name__ == "__main__":
  main()

