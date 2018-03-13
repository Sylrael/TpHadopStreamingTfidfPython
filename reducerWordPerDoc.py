#!/usr/bin/python

import sys

wordCount = {}
current_doc = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()
	docWord, count = line.split('\t', 1)
	doc_id, word = docWord.split()
	wordCount[docWord]=int(count)
	if current_doc == doc_id:
		current_count += int(count)
	else:
		if current_doc:
			# write result to STDOUT
			#print wordCount
			for k, v in wordCount.items():
				print "%s\t%s %s" % (k, v, current_count)
			wordCount = {}
		current_count = int(count)
		current_doc = doc_id
	# do not forget to output the last word if needed!
if current_doc == doc_id:
	for k, v in wordCount.items():
		print "%s\t%s %s" % (k, v, current_count)