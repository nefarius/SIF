import re, os, time, sys
from PIL import Image
from io import BytesIO
from threading import Thread
from urllib.parse import urlsplit
from urllib.request import urlopen

base_path = 'D:\\squid\\new'
min_height = 300 # px
min_width = 300 # px

def parse_input(line):
	try:
		# get url part from squids' input
		url = line.split(' ')[0];
		# download header
		req_res = urlopen(url)
		# get header content
		http_message = req_res.info()
		# check if requested file is an image
		if http_message.get_content_maintype() == 'image':
			# download image into memory buffer
			mem_buf = BytesIO(req_res.read())
			# open image to examine properties
			img_res = Image.open(mem_buf)
			# get height and width
			height, width = img_res.size
			# check if image is large enough
			if height >= min_height and width >= min_width:
				# get domain name
				domain = urlsplit(url)[1].split(':')[0]
				# create subdirectory for every domain name
				sub_path = os.path.join(base_path, domain)
				if not os.path.exists(sub_path):
					os.makedirs(sub_path)				
				# build local file path
				local_path = os.path.join(sub_path, str(time.time()) \
								+ '.' + http_message.get_content_subtype())
				# store file to disk
				img_res.save(local_path)
				# free memory
				del(img_res)
			del(mem_buf)
		del(req_res)
	except ValueError:
		pass
	except:
		datetime = time.strftime("%Y/%m/%d %H:%M:%S| ")
		sys.stderr.write(datetime + "Failed parsing input: " + line)
		sys.stderr.write(datetime + "    Details: " + str(sys.exc_info()[0]) + '\n')

for line in sys.stdin:
	t = Thread(target=parse_input, args=(line,))
	t.start()
	print('ERR')
