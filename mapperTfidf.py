#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	docWord, wordCountWordperdoc = line.split('\t')
	doc_id, word = docWord.split(' ')
	wordCount, wordPerDoc = wordCountWordperdoc.split(' ')
	print '%s %s\t%s %s' %(word, doc_id, wordCount, wordPerDoc)