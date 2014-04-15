#!/usr/bin/env python

import os
import re
import json
from subprocess import call

def ProcessEmotionLexicon( source_path, target_filename ):
	if not os.path.exists( 'rawjson' ):
		# if not which("npm"):
		# 	print("process emotion lexicon: cannot find command npm in the system!")
		# if not which("pdf2json"):
		# 	call(["sudo", "npm", "install", "pdf2json", "-g"])
		# call(["sudo", "npm", "update", "pdf2json", "-g"]) # shouldn't this go into make file?
		# for filename in os.listdir ("./papers"):
		# 	print filename
		# 	papername = "papers/" + filename
		os.makedirs ("rawjson")
		call(["sudo", "pdf2json", "-f", "papers", "-o", "rawjson"])
	
	if not os.path.exists('result_json'):
		os.makedirs("result_json")

	for filename in os.listdir ("rawjson"):
		# print filename
		paper = open("rawjson/"+filename)
		data = json.load(paper)
		paper.close()
		# print paper_data
		with open( "result_json/"+filename, 'w+' ) as f:
				json.dump( data, f, encoding = 'utf-8', indent = 2, sort_keys = True )


	# unigrams = {}
	# lexicon = {
	# 		'unigrams' : unigrams,
	# 		'bigrams' : {},
	# 		'pairs' : {}
	# 	}
	# json_data=open("papers/05669299.json")
	# data = json.load(json_data)
	# json_data.close()

	# pagelist = data["formImage"]["Pages"]
	# for p in range(5, len(pagelist)): # appendix starts at page 6
	# 	textlist = pagelist[p]["Texts"]
	# 	t = 0
	# 	while t<len(textlist):
	# 		value = gettext(textlist, t) # value: unigrams, feature%3Ascore, page number of the pdf
	# 		if value == 'positive%3A0' or value == 'positive%3A1':
	# 			term = gettext(textlist, t-1)
	# 			if "%" in term:
	# 				term = correcttext(term)
	# 			unigrams[term] = {}
	# 			for i in range(0,10):
	# 				feature = gettext(textlist, t+i).split("%3A") # split by ":"
	# 				feature_name = feature[0]
	# 				feature_score = feature[1]
	# 				unigrams[term][feature_name] = int(feature_score)
	# 			t = t + 10
	# 		t = t+1
	# with open( "json/test.json", 'w+' ) as f:
	# 		json.dump( data, f, encoding = 'utf-8', indent = 2, sort_keys = True )

ProcessEmotionLexicon("", "");