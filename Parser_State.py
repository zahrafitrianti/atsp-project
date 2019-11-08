import os
import time
import numpy as np
import sys
import pandas as pd

"""
Extract features from the output txt file.
It reads each txt file line by line, starting from the line: '[+] Analysis Results'
Save all the features in a list and return them.
"""
def strip_Main_Cat(category):
	return category.strip().replace('\n','').replace('[+]','').strip()
	
def strip_feature(feature):
	return feature.strip().replace('\t','').replace('[.]','').replace('\n','').strip()
def strip_line(line):
	return line.strip().replace('\t\t','').lstrip(' -').strip()
	
def extract_features(fname):
	features = []
	keywords = ['Telephony Identifiers Leakage', 
				'Device Settings Harvesting',
				'Connection Interfaces Exfiltration',
				'Suspicious Connection Establishment',
				'Telephony Services Abuse',
				'Code Execution']

	try:
		mainCat = ''
		mainCount = 0
		featureCat = ''
		featureCount = 0 
		ContentList = []
		featureDict = {}
		Output = {}
		with open(fname, encoding='utf-8') as f:
			for line in f:
				#print(line)
				#print(featureDict)
				if(line == '===== Androwarn Report =====' or line == ''):
					continue
				if line.startswith('[+]'):
					#print('main Cat: ' + line)
					if mainCount > 0:
						Output[mainCat] = featureDict.copy();
					#	print('Dict')
					#	print(Output)
						featureDict = {}
						mainCount = 0
					mainCount += 1
					mainCat = strip_Main_Cat(line)
				if line.startswith('\t[.]'):
					#print('feature: ' + line)
					if featureCount > 0:
						featureDict[featureCat] = ContentList.copy()
						contentList = []
						featureCount = 0
					featureCat = strip_feature(line)
					featureCount += 1
				if line.startswith('\t\t -'):
					ContentList.append(strip_line(line))
					
				# Keep permissions
				# elif line.startswith('\t\t - Asked:'):
				#     permissions.append(line)

	except IOError:
		print("Error in reading file...")
		sys.exit(0)
	finally:
		f.close()

	return Output


def main():

	# directory of the output file
	directory = './report_androwarn'
	category = 'Analysis Results' 
	# initialize a dictionary for the results
	app_dict = {'app_name': [], 'score': [], 'features': []}
	features = {}
	# loop over all txt files
	
	count = 0
	for filename in os.listdir(directory):
		if count == 1:
			break
		count += 1
		if filename.endswith(".txt"):
			print(f"Analyzing file {filename}...")
			fname = os.path.join(directory, filename)
			name = filename[0:len(filename)-15]
			# extract features from each app
			features[name] = extract_features(fname)
			#'''
			features.get(name).get(category).keys()
			# calculate the scores (count the number of features)
			score = len(features.get(name).get(category))

			# compile output to a dict object
			app_dict['app_name'].append(name)
			app_dict['score'] = score
			app_dict['features'].append(np.asarray(features.get(name).get(category).keys()))
	
	# make a dataframe for better visualization
	print(pd.DataFrame(app_dict))
	#'''

if __name__ == '__main__':
   main()