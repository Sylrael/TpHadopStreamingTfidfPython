#!/usr/bin/python

import sys
import re
import os
from string import digits

stopwords = []
with open('stopwords_en.txt', 'r') as stopWordsFile:
	for stopline in stopWordsFile:
		stopline = stopline.strip()
		stopwords.append(stopline)
for line in sys.stdin:
	line = re.sub('[^\w]',' ',line)
	line = line.strip().translate(None, digits)
	words = line.lower().split()
	words = [word for word in words if (len(word)>2 and word not in stopwords)]
	for word in words:
		filename = os.environ['mapreduce_map_input_file'].rsplit('/',1)[-1]
		print '%s %s\t%s' %(word,filename,1)
#			print '%s\t%s' %(word,1)
