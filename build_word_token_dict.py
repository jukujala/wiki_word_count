import cPickle
import cStringIO
import sys

NCOUNTLIMIT = 5
NMAXSTRINGLEN = 20

def create_token_dict(f):
  d = {}
  i = 0
  for t in f:
    if len(t) < NMAXSTRINGLEN:
      d[t] = d.setdefault(t,0)+1
  for k in d.keys():
    if d[k] < NCOUNTLIMIT:
      del d[k]
  return d

def usage():
  print "cat input | %s tokens.pickle"

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
  #dump the whole word dictionary to file, could easily prune it also, e.g. remove entries with low count or frequency
  cPickle.dump(d,outf, protocol=cPickle.HIGHEST_PROTOCOL)
  outf.close()
  print "wrote token dict to file %s" %outfn

if __name__ == "__main__":
  main()

