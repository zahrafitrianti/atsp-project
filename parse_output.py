import os
import time
import numpy as np
import sys
import pandas as pd

"""
String preprocessing
"""
def strip_Main_Cat(category):
	return category.strip().replace('\n','').replace('[+]','').strip()	
def strip_feature(feature):
	return feature.strip().replace('\t','').replace('[.]','').replace('\n','').strip()
def strip_line(line):
	return line.strip().replace('\t\t','').lstrip(' -').strip()


"""
Extract features from the output txt file.
It reads each txt file line by line, starting from the line: '[+] Analysis Results'
Save all the features in a list and return them.
"""
def extract_features(fname):

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
				
				# skip the first line and empty lines
				if(line == '===== Androwarn Report =====' or line == '\n'):
					continue
				
				# save each category
				if line.startswith('[+]'):
					if mainCount > 0:
						Output[mainCat] = featureDict.copy()
						featureDict.clear()
					mainCount += 1
					mainCat = strip_Main_Cat(line)
				
				# save features
				if line.startswith('\t[.]'):
					if featureCount > 0:
						featureDict[featureCat] = ContentList.copy()
						contentList = []
						featureCount = 0
					featureCat = strip_feature(line)
					if featureCat == 'Description': # was treated as a feature
						continue
					featureCount += 1
				
				# save logs
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
	for filename in os.listdir(directory):
		if filename.endswith(".txt"):
			print(f"Analyzing file {filename}...")
			fname = os.path.join(directory, filename)
			name = filename[0:len(filename)-15]
			
			# extract features from each app
			features[name] = extract_features(fname)
			
			# calculate the scores (count the number of features)
			score = len(features.get(name).get(category))

			# compile output to a dict object
			app_dict['app_name'].append(name)
			app_dict['score'].append(score)
			feature_names = features.get(name).get(category).keys()
			app_dict['features'].append(', '.join(feature_names))
	
	# make a dataframe and save results to csv
	df = pd.DataFrame(app_dict)
	df.to_csv('result_androwarn.csv')

if __name__ == '__main__':
   main()