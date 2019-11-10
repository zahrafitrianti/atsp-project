import os
import numpy as np
import sys
import pandas as pd
import re
from sklearn.preprocessing import MinMaxScaler


"""
Extract features from the output txt file.
It reads each txt file line by line, starting from the line: '-----' in the output file
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


"""
Count the number of features per app.
Features = [Critical], [Warning], [Notice], [Info]
"""
def count_features(final_list):
	
	critical = []
	warning = []
	notice = []
	info = []

	for f in final_list:
		substr1 = re.findall(r'\[Critical\]', f)
		substr2 = re.findall(r'\[Warning\]', f)
		substr3 = re.findall(r'\[Notice\]', f)
		substr4 = re.findall(r'\[Info\]', f)
		if substr1:
			critical.append(substr1)
		elif substr2:
			warning.append(substr2)
		elif substr3:
			notice.append(substr3)
		elif substr4:
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

"""
Calculate score using the following formula:
score(app) = c * numOfCritical + w * numOfWarning + n * numOfNotice + i * numOfInfo
c, w, n, i are weights for each respective feature
"""
def calculate_score(features):
	
	# initialize score
	scores = 0

	# initialize weights
	c = 10
	w = 8.5
	n = 5
	i = 1

	# calculate score and return it
	scores += (c*features['critical']) + (w*features['warning']) + (n*features['notice']) + (i*features['info'])
	return scores



def main():

	# directory of the output file
	directory = './report_androbugs'
	
	# initialize a dictionary for the results
	app_dict = {'app_name': [], 'score': [], 'features': []}

	# loop over all txt files
	for filename in os.listdir(directory):
		if filename.endswith(".txt"):
			print(f"Analyzing file {filename}...")
			fname = os.path.join(directory, filename)
			name = filename.split('_')[0] + '.apk'
			
			# extract features from each app
			final_list = extract_features(fname)

			# count the number of features per app
			features = count_features(final_list)

			# calculate score per app
			score = calculate_score(features)

			# compile output to a dict object
			app_dict['app_name'].append(name)
			app_dict['score'].append(score)
			app_dict['features'].append(features)
	

	x = np.asarray(app_dict['score']).reshape(-1, 1)
	scaler = MinMaxScaler()
	score_scaled = scaler.fit_transform(x)
	app_dict['score'] = np.asarray(score_scaled).flatten()


	# make a dataframe and save results to csv
	df = pd.DataFrame(app_dict)
	print('Save results to csv...')
	df.to_csv('./result/result_androbugs_scaled.csv', index=False)

if __name__ == '__main__':
   main()