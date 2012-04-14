import os
import sys

if len(sys.argv) != 3:
    print "Usage : python rename.py <path> <new_name.extension>"
    sys.exit()

count = 1
s = "%s/pic_folder" % sys.argv[1]
try:
    os.mkdir(s)
except OSError:
    pass

name = sys.argv[2].split('.')

try:
    for x in os.walk(sys.argv[1]):
        for y in x[2]:
            s = "%spic_folder/%s%s.%s" %(x[0], name[0], count, name[1])
            z = os.path.join(x[0],y)
            os.rename(z, s)
            count = count + 1
except OSError:
    pass
