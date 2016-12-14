import Queue
import threading
import urllib
import time

URL = "https://tv-line.pstatic.net/global/read/"
EPISODE = "TVCAST_2016_12_12_3/b679GyoiyRA9YZz_4Z-wZ-A4cA_rmcvideo_1080P_1920_5120_192-"
KEY = "?__gda__=1481700700_e11b42ae335f01e647ac6968debe1d05"

class Line:
	def __init__(self, index):
		self.index = index
	def run(self):
		file = urllib.URLopener()
		file.retrieve(URL + EPISODE + self.index + '.ts' + KEY, self.index + '.ts')
		print '{index}'.format(index = self.index)

# init
q = Queue.Queue()
for i in range(0, 300):
	q.put(Line('%06d' % i))

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