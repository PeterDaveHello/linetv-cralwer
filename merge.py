import glob
import sys

if len(sys.argv) < 3:
	print 'Usage: <path> <file name>'
	exit()

PATH = sys.argv[1]
FILE_NAME = sys.argv[2]

with open(FILE_NAME, 'wb') as outfile:
	infiles = glob.glob(PATH + '*.ts')
	infiles.sort()
	for infile in infiles:
		print infile
		with open(infile, 'rb') as input:
			outfile.write(input.read())