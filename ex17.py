from sys import argv
from os.path import exists

script, source, destination = argv

print "Copying from %s to %s" % (source, destination)

in_file = open(source)
source_data = in_file.read()

print "The input file is %d bytes long" % len(source_data)

print "Does output file exists? %r" % exists(destination)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(destination, 'w')
out_file.write(source_data)

print "Alrighty, done"

out_file.close()
in_file.close()
