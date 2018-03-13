#!/usr/bin/python

import sys

current_word = None
current_count = 0
word = None


for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)
	if current_word == word:
		current_count += int(count)
	else:
		if current_word:
			# write result to STDOUT
			print "%s\t%s" % (current_word, current_count)
		current_count = int(count)
		current_word = word
# do not forget to output the last word if needed!
if current_word == word:
	print '%s\t%s' % (current_word, current_count)

