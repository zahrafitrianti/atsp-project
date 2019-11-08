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

			# calculate the scores (count the number of features)
			score = len(features) / len(os.listdir(directory))

			# compile output to a dict object
			app_dict['app_name'].append(name)
			app_dict['score'].append(score)
			app_dict['features'].append([', '.join(features.keys())])
	
	# make a dataframe and save results to csv
	df = pd.DataFrame(app_dict)
	print('Save results to csv...')
	df.to_csv('./result/result_androwarn_normalized.csv', index=False)

if __name__ == '__main__':
   main()