import os
import time
import numpy as np
import sys
import pandas as pd
import re


"""
Extract features from the output txt file.
It reads each txt file line by line, starting from the line: '[+] Analysis Results'
Save all the features in a list and return them.
"""
def extract_features(fname):

	try:
		final_list = []

		with open(fname, encoding='utf-8') as f:
			for line in f:
				if line.startswith('-'):
					break
			for line in f:
				if line.startswith('-'):
					continue
				final_list.append(line.strip())

	except IOError:
		print("Error in reading file...")
		sys.exit(0)
	finally:
		f.close()

	return final_list


def count_features(features):
	
	critical = []
	warning = []
	notice = []
	info = []

	for f in features:
		substr1 = re.findall(r'\[Critical\]', f)
		substr2 = re.findall(r'\[Warning\]', f)
		substr3 = re.findall(r'\[Notice\]', f)
		substr4 = re.findall(r'\[Info\]', f)
		if substr1:
			critical.append(substr1)
		if substr2:
			warning.append(substr2)
		if substr3:
			notice.append(substr3)
		if substr4:
			info.append(substr4) 
	
	critical = np.asarray(critical).flatten()
	warning = np.asarray(warning).flatten()
	notice = np.asarray(notice).flatten()
	info = np.asarray(info).flatten()

	features = {}
	features['critical'] = len(critical)
	features['warning'] = len(warning)
	features['notice'] = len(notice)
	features['info'] = len(info)

	return features

def calculate_score(features):
	
	# initialize score
	scores = 0

	# initialize weights
	c = 3
	w = 1
	n = 1
	i = 1

	scores += (c*features['critical']) + (w*features['warning']) + (n*features['notice']) + (i*features['info'])
	return scores




def main():

	# directory of the output file
	directory = './report_androbugs'
	# directory = './test'
	
	# initialize a dictionary for the results
	app_dict = {'app_name': [], 'score': [], 'features': []}

	# loop over all txt files
	for filename in os.listdir(directory):
		if filename.endswith(".txt"):
			print(f"Analyzing file {filename}...")
			fname = os.path.join(directory, filename)
			name = filename.split('_')[0] + '.apk'
			
			# extract features from each app
			features = extract_features(fname)
			feature_dict = count_features(features)
			score = calculate_score(feature_dict)

			# compile output to a dict object
			app_dict['app_name'].append(name)
			app_dict['score'].append(score)
			app_dict['features'].append(feature_dict)
	
	# make a dataframe and save results to csv
	df = pd.DataFrame(app_dict)
	df.to_csv('result_androbugs.csv')

if __name__ == '__main__':
   main()