import pandas as pd

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
	

def main():

	# csv files of the results
	result_androwarn = './result/result_androwarn_weighted.csv'
	result_androbugs = './result/result_androbugs_normalized.csv'

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
	df.to_csv('./result/final_scores_weighted.csv', index=False)

if __name__ == '__main__':
   main()