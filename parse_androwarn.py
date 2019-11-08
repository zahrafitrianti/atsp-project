import os
import numpy as np
import sys
import pandas as pd


"""
String preprocessing
"""
def strip_category(category):
	return category.strip().replace('\n','').replace('[+]','').strip()	
def strip_feature(feature):
	return feature.strip().replace('\t','').replace('[.]','').replace('\n','').strip()
def strip_item(line):
	return line.strip().replace('\t\t','').lstrip(' -').strip()


"""
Read the output txt file and parse them as a dictionary object.
It creates a nested dictionary with the following structure:
{
	main_category:
		{
			features: item
		}
}
Return the dictionary of the output file
"""
def read_file(fname):

	Output = {}

	try:
		with open(fname, encoding='utf-8') as f:
			for line in f:

				# skip first line and empty lines
				if line.startswith('=') or line.startswith('\n'):
					continue

				# save main categories; a line which starts with [+]
				# set main categories as keys in the dictionary
				if line.startswith('[+]'):
					category = strip_category(line)

					# initialize an empty dictionary to create a nested dictionary
					Output[category] = {}
				
				# save features; a line which starts with [.]
				if line.startswith('\t[.]'):
					features = strip_feature(line)

					# set features as key in the nested dictionary
					# initialize an empty list for its values
					Output[category][features] = []

				# save remaining items (logs/permissions); a line which starts with -
				# items are values to the nested dictionary (features)
				if line.startswith('\t\t -'):
					Output[category][features].append(strip_item(line))
	except IOError:
		print("Error in reading file...")
		sys.exit(0)
	finally:
		f.close()

	return Output


"""
Calculate score using the following formula:
score(app) = weights[i] * features_count[i]
Feature with the highest number of occurrences (counts) is given a higher weight to indicate importance
"""
def calculate_scores(features):

	feature_count = {}

	# count the number of occurrences of each feature
	for key, value in features.items():
		feature_count[key] = len([i for i in value if i])
	
	# initialize weights
	weights = np.ones(len(features.keys()))

	# find the feature with the highest counts
	if feature_count.items():
		max_feature, _ = max(feature_count.items(), key=lambda x:x[1])
		ind = list(feature_count.keys()).index(max_feature)
	else:
		max_feature = []
	
	score = 0
	i = 0

	# calculate the score
	for key, value in feature_count.items():
		weights[ind] = 3
		score += weights[i] * feature_count[key]
		i += 1
	
	return score


def main():

	# directory of the output file
	directory = './report_androwarn'
	
	# initialize a dictionary for the results
	app_dict = {'app_name': [], 'score': [], 'features': []}
	output = {}

	# loop over all txt files
	for filename in os.listdir(directory):
		if filename.endswith(".txt"):
			print(f"Analyzing file {filename}...")
			fname = os.path.join(directory, filename)
			name = filename[0:len(filename)-15]
			
			# read output file
			output[name] = read_file(fname)

			# extract features from each app
			features = output.get(name).get('Analysis Results')

			# calculate the scores and normalize
			score = calculate_scores(features)
			score /= len(os.listdir(directory))

			# compile output to a dict object
			app_dict['app_name'].append(name)
			app_dict['score'].append(score)
			app_dict['features'].append([', '.join(features.keys())])
	
	# make a dataframe and save results to csv
	df = pd.DataFrame(app_dict)
	print('Save results to csv...')
	df.to_csv('./result/result_androwarn_weighted.csv', index=False)

if __name__ == '__main__':
   main()