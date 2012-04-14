import os
import sys

#Checking whehter path and filename are given.
if len(sys.argv) != 3:
    print "Usage : python rename.py <path> <new_name.extension>"
    sys.exit()

#Splitting name and extension.
name = sys.argv[2].split('.')
if len(name) < 2:
    name.append('')
else:
    name[1] = ".%s" %name[1]

#To name starting from 1 to number_of_files.
count = 1

#Creating a new folder in which the renamed files will be stored.
s = "%s/pic_folder" % sys.argv[1]
try:
    os.mkdir(s)
except OSError:
    #If pic_folder is already present, use it.
    pass

try:
    for x in os.walk(sys.argv[1]):
        for y in x[2]:
            #Creating the rename pattern.
            s = "%spic_folder/%s%s%s" %(x[0], name[0], count, name[1])
            #Getting the original path of the file to be renamed.
            z = os.path.join(x[0],y)
            #Renaming.
            os.rename(z, s)
            #Incrementing the count.
            count = count + 1
except OSError:
    pass
