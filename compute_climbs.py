import re
import glob

d_p, d_m = 0, 0
prev = None
for fname in sorted(glob.glob("*.gpx"), key=lambda e: list(reversed(e.split("-")))):
  print(fname)
  f = open(fname)
  for l in f:
    m = re.match("^ *<ele>(.*)</ele> *$", l)
    if not m:
      continue
    f = float(m.group(1))
    if prev is None:
        prev = f
        continue
    d = f - prev
    if d > 0:
        d_p += d
    else:
        d_m += -d
    prev = f


print("D+ %i / D- %i" % (int(d_p), int(d_m)))
