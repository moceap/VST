#!/usr/bin/env python3
import os
import sys
import stat
import subprocess
import pathlib

ver = "0.1"

if len(sys.argv) < 2:
	print("-=-= VERY SIMPLE TESTER %s =-=-\n\n	USAGE:\n \n	vst [File To Test] [File Arguments]\n	\n You should enter file to test." % ver)
	quit()
	
infile = sys.argv[1]
outfile = os.getcwd() + infile + 'TMP.py'
attributes = ' '.join(sys.argv[2:])
linenumbers = 0
if os.path.exists(outfile):
	os.remove(outfile)
output = open(outfile,"a")
input = open(infile,"r").read().splitlines()
st = os.stat(outfile)
output.write('#!/usr/bin/env python3 \n')
output.write('TMPCOUNT = 0 \n')
for line in input:
	if not len(line) == 0 and not line[0] == '#':
		if not line.isspace():
			tabs = 0
			linetmp = line
			while linetmp.startswith("\t"):
				tabs = tabs + 1
				linetmp = linetmp[1:]
			output.write('\t' * tabs + 'TMPCOUNT = TMPCOUNT + 1 \n')
			if linetmp[0:4] == 'quit':
				output.write('\t' * tabs + 'print(TMPCOUNT)\n')
			output.write(line + '\n')
			linenumbers = linenumbers + 1
output.write('print(TMPCOUNT)\n')
output.close()
os.chmod(outfile, st.st_mode | stat.S_IEXEC)
attrs = attributes.split()
attrs.insert(0,outfile)
ranlines = 0
with subprocess.Popen(attrs, stdout=subprocess.PIPE) as proc:
	#print(proc.stdout.read().decode("utf-8"))
	ranlines = int([i for i in proc.stdout.read().decode("utf-8").split('\n') if i][-1])

print("RAN STATEMENTS: " + str(ranlines))
print("ALL STATEMENTS: " + str(linenumbers))
print("RATIO: " + str(ranlines/linenumbers))
os.remove(outfile)
