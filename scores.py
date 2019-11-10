import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})


"""
Calculate combined scores from both analyzers
"""
def combine_scores(androwarn, androbugs):

	# take the scores for all app from each analyzer
	scores_androwarn = androwarn.score.values
	scores_androbugs = androbugs.score.values

	# add them up to compute the combined score and normalize it
	combined_scores = [sum(x) for x in zip(scores_androwarn, scores_androbugs)]
	return combined_scores


"""
Plot function.
Create a histogram of scores for all apk files.
"""
def plot_scores(df, analyzer):

	if analyzer == 1:
		title = 'Scores per app for Androwarn'
		y = df['score']
		ylabel = 'scores'
		filename = 'plot_scores_androwarn.png'
	elif analyzer == 2:
		title = 'Scores per app for Androbugs'
		y = df['score']
		ylabel = 'scores'
		filename = 'plot_scores_androbugs.png'
	elif analyzer == 3:
		title = 'Combined scores per app'
		y = df['combined score']
		ylabel = 'combined scores'
		filename = 'plot_combined_scores.png'

	plt.figure(figsize=(12,7))
	plt.title(title)
	plt.bar(np.arange(0, df.shape[0]), y)
	plt.xlabel('number of apk files')
	plt.ylabel(ylabel)
	plt.savefig(filename)
	plt.show()
	

def main():

	# csv files of the results
	result_androwarn = './result/Result AndroWarn/result_androwarn.csv'
	result_androbugs = './result/Result Androbugs/result_androbugs.csv'

	# csv files of the malicious apps results
	# result_androwarn = './result/result_androwarn/result_androwarn_malicious.csv'
	# result_androbugs = './result/Androbugs/result_androbugs_malicious.csv'

	# read csv files
	androwarn = pd.read_csv(result_androwarn)
	androbugs = pd.read_csv(result_androbugs)
	filenames = androwarn.app_name.values

	# extract features
	features = list(zip(androwarn.features.values, androbugs.features.values))
			
	# calculate combined scores
	score = combine_scores(androwarn, androbugs)
	
	# initialize a dictionary for the results
	app_dict = {}
	app_dict['app_name'] = filenames
	app_dict['combined score'] = score
	app_dict['combined features'] = features


	# make a dataframe and save results to csv
	df = pd.DataFrame(app_dict)
	print('Save output to csv file...')
	df.to_csv('./result/final_scores.csv', index=False)
	# df.to_csv('./result/final_scores_malicious.csv', index=False)

	# plot histogram of scores
	plot_scores(androwarn, 1)
	plot_scores(androbugs, 2)
	plot_scores(df, 3)

if __name__ == '__main__':
   main()