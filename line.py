import sys
import Queue
import threading
import urllib
import time

if len(sys.argv) < 4:
	print 'Usage: <url> <path> <part>'
	exit()

URL = sys.argv[1]
PATH = sys.argv[2]
PART = sys.argv[3]

# generate urls
query_index = URL.index('?')
ext_index = URL.index('.ts')
file_len = URL[:ext_index][::-1].index('-')

a = URL[:ext_index - file_len]
b = URL[query_index:]

class Line:
	def __init__(self, index):
		self.index = index.rjust(file_len, '0')

	def run(self):
		file = urllib.URLopener()
		file.retrieve(a + self.index + '.ts' + b, PATH + PATH + self.index + '.ts')
		print '{index}'.format(index = self.index)

# init
q = Queue.Queue()
for i in range(0, 300):
	q.put(Line('%d' % i))

def next():
	while q.qsize() > 0:  
		job = q.get()  
		job.run()  

# create threads 
t1 = threading.Thread(target=next, name='T1')
t2 = threading.Thread(target=next, name='T2')
t3 = threading.Thread(target=next, name='T3')
t4 = threading.Thread(target=next, name='T4')

t1.start()
t2.start()
t3.start()
t4.start()

while t1.is_alive() or t2.is_alive() or t3.is_alive() or t4.is_alive():
     time.sleep(1)