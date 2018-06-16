import os
import sys
import glob
import argparse

from utils.client import Client

# constant
__version__ = '1.0'
__description__ = 'linetv-crawler'
__epilog__ = 'Report bugs to <cjyeh@cs.nctu.edu.tw>'

def parse_argv():
	parser = argparse.ArgumentParser(
		description=__description__,
		epilog=__epilog__
	)

	parser.add_argument('list', nargs='+', help='list of .ts url')

	parser.add_argument(
		'-o', '--outfile',
		action='store',
		help='Outfile name'
	)
	parser.add_argument(
		'-p', '--path',
		action='store',
		help='Storage folder path'
	)
	parser.add_argument(
		'-t', '--threads',
		action='store',
		default=4,
		help='Number of threads'
	)
	parser.add_argument(
		'-v', '-V', '--version',
		action='version',
		help='Print program version',
		version='v{}'.format(__version__)
	)

	return parser.parse_args()

def main():
	# variables
	client = Client()
	args = parse_argv()

	# set default val of args
	args.path = '.' if args.path == None else args.path
	args.path = args.path[:-1] if args.path[-1] == '/' else args.path

	client.add(list=args.list, path=args.path)
	client.run(threads=args.threads)

	# check extension
	exts = list(set([task['file'][task['file'].find('.')+1:] for task in client.tasks]))

	if len(exts) > 1:
		print('Inconsistent extension')
		exit()

	# merge into single video
	infiles = glob.glob('%s/*.%s' % (args.path, exts[0]))
	infiles.sort()

	with open('%s/%s.%s' % (args.path, args.outfile, exts[0]), 'wb') as output:
		for infile in infiles:
			with open(infile, 'rb') as input:
				output.write(input.read())

if __name__ == '__main__':
	main()
