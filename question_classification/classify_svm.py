#!/usr/bin/python2.7 -tt

import commands
import sys
import ast

home = ast.literal_eval(open('.config', 'rU').read())['home']
dir = home+'question_classification/'

question = sys.stdin.readline().strip()
open(dir+'question','w').write(question)
commands.getstatusoutput(dir+'vectorize_test_file.py'+' '+dir+'question')

(status, output) = commands.getstatusoutput(dir+'svm_multiclass_classify'+' '+dir+'question.vect'+' '+home+'data/models/svm/coarse.model'+' '+dir+'c-c')
text = open(dir+'c-c', 'rU').read()
coarse_class = text[:text.find('\t')]
(status1, output1) = commands.getstatusoutput(dir+'svm_multiclass_classify'+' '+dir+'question.vect'+' '+home+'data/models/svm/fine.'+str(coarse_class)+'.model'+' '+dir+'f-c')
text = open(dir+'f-c','rU').read()
fine_class = text[:text.find('\t')]

coarse_class_mapping = ast.literal_eval(open(home+'util/coarse_class_mapping','rU').read())
class_mapping = ast.literal_eval(open(home+'util/svm_class_id_mapping', 'rU').read())
outline = ''
for clazz in coarse_class_mapping.keys():
	if coarse_class_mapping[clazz] == int(coarse_class):
		outline += clazz
		break
	
outline += ':'
for f_class in class_mapping[clazz].keys():
	if class_mapping[clazz][f_class] == int(fine_class):
		outline += f_class
		break

print(outline)


		