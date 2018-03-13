#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	wordDoc, count = line.split('\t',1)
	word, doc_id = wordDoc.split(' ')
	print '%s %s\t%s' %(doc_id, word, count)
