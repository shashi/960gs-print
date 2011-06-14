# script converts all occourances of pixels
# into pt so that 960px fits in  an A4 sheet.

import re

def px_to_pt(m):
    px = float(m.group(1))
    pt = round(px * (595.0 / 960), 1)
    return str(pt) + 'pt'


f = open("960.css")
contents = f.read()
f.close()

dimension = re.compile('([0-9]+)px')

print dimension.sub(px_to_pt, contents)

