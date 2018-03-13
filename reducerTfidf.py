#!/usr/bin/python

import sys
import math

keyVal = {}
current_word = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()
	wordDoc, wordcountWordperdoc = line.split('\t', 1)
	word, doc_id = wordDoc.split(' ')
	wordCount, wordPerdoc = wordcountWordperdoc.split(' ')
	keyVal[wordDoc]= wordcountWordperdoc
	
	if current_word == word:
		current_count += 1
	else:
		if current_word:
			# write result to STDOUT
			#print wordCount
			for k, v in keyVal.items():
				w, d = k.split(' ')
				wc, wpd = v.split(' ')
				tfidf = (float(wc)/float(wpd)) * math.log(2.0/float(current_count))
				print "%s\t%s" % (k, tfidf)
			keyVal = {}
		current_count = 1
		current_word = word
	# do not forget to output the last word if needed!
if current_word == word:
	for k, v in keyVal.items():
		w, d = k.split(' ')
		wc, wpd = v.split(' ')
		tfidf = (float(wc)/float(wpd)) * math.log(2.0/float(current_count))
		print "%s\t%s" % (k, tfidf)