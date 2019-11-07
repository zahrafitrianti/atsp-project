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
def extract_features(fname):
	features = []
	keywords = ['Telephony Identifiers Leakage', 
				'Device Settings Harvesting',
				'Connection Interfaces Exfiltration',
				'Suspicious Connection Establishment',
				'Telephony Services Abuse',
				'Code Execution']

	try:
		with open(fname, encoding='utf-8') as f:
			for line in f:
				if line.startswith('[+] Analysis Results'):
					break
			for line in f:
				if line.startswith('\t[.]'):
					for item in keywords:
						if item in line:
							features.append(item)
				
				# Keep permissions
				# elif line.startswith('\t\t - Asked:'):
				#     permissions.append(line)

	except IOError:
		print("Error in reading file...")
		sys.exit(0)
	finally:
		f.close()

	return features


def main():

	# directory of the output file
	directory = './report_androwarn'
	
	# initialize a dictionary for the results
	app_dict = {'app_name': [], 'score': [], 'features': []}
	
	# loop over all txt files
	for filename in os.listdir(directory):
		if filename.endswith(".txt"):
			print(f"Analyzing file {filename}...")
			fname = os.path.join(directory, filename)

			# extract features from each app
			features = extract_features(fname)

			# calculate the scores (count the number of features)
			score = len(features)

			# compile output to a dict object
			app_dict['app_name'].append(filename)
			app_dict['score'] = len(features)
			app_dict['features'].append(np.asarray(features))
	
	# make a dataframe for better visualization
	print(pd.DataFrame(app_dict))
	

if __name__ == '__main__':
   main()