#!/usr/bin/python2.7 -tt

import commands
import sys
import re
sys.path.append('../')
import stop_words
import question_phrases
import ast

dir = ast.literal_eval(open('.config', 'rU').read())['home']+'question_processing/chunker/'

def	chunk(sent):
		open(dir+'.input.temp', 'w').write(sent)
		(status, output) = commands.getstatusoutput(dir+'stanford-parser-full-2015-01-30/lexparser.sh'+' '+dir+'.input.temp')
		if status == 0:
			return output
		else:
			return "-1"


def 	get_chunks(ques):
		output = chunk(ques)
		lines = output.split('\n')
		lines = lines[3:]
		index = 0
		for line in lines:
			index += 1
			if line == '':
				break
			
		lines = lines[:index-1]

		clean_lines = {}
		index = 1
		for line in lines:
			line = re.sub('\([A-Z\S+|.]+','',line)
			line = re.sub('\)', '', line)
			line = line.strip()
			line = stop_words.remove(line)
			if question_phrases.remove(line) == '':
				line = ''
			if line != '':
				clean_lines[str(index)] = line
				index += 1

		return clean_lines		
				

def	main():
		if len(sys.argv) > 1 and sys.argv[1] == '-p':	
			print(chunk(sys.stdin.readline().strip()))
		else:
			print(get_chunks(sys.stdin.readline().strip()))


if __name__ == '__main__':
	main()	
