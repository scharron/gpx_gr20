import glob
import datetime

for fname in glob.glob("*.gpx"):
  out = open("dategpx/%s" % fname, "w")
  day, month = map(int, fname.replace(".gpx", "").split("-"))
  start = datetime.datetime(2016, month, day, 7, 0, 0)
  f = open(fname)
  point = 0
  for l in f:
    if "<name>" in l:
      l = "  <name>GR20 %s</name>\n" % fname
    if "<ele>" in l:
      d = (start + datetime.timedelta(minutes=point)).isoformat() + "Z"
      l = l[:-1] + "<time>%s</time>\n" % d
      point += 1
    out.write(l)
  out.close()
  f.close()
