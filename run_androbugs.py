import os
import time
import numpy as np


def main():
	
	# directory of benign apk files
	directory = './Benign-sample-187'

	# directory of malicious apk files
	# directory = './malicious_apps'
	time_elapsed_per_app = []
	start = time.time()

	# loop over all apk files
	for filename in os.listdir(directory):
		if filename.endswith(".apk"):
			print(f"Analyzing file {filename}...")
			
			fname = os.path.join(directory, filename)

			tstart = time.time()

			# output directory
			output_dir = os.path.join(os.getcwd(), 'Reports/report_androbugs')
			# output_dir = os.path.join(os.getcwd(), 'Reports/report_androbugs_malicious')
			
			# command to run the analyzer tool
			# NOTE: AndroBugs requires python 2.x
			os.system(f"python ./AndroBugs_Framework/androbugs.py -f {fname} -o {output_dir}")
			
			tend = time.time() - tstart
			time_elapsed_per_app.append([filename, tend])
			
	total_time_elapsed = time.time() - start

	running_time = np.vstack([time_elapsed_per_app, ['Total time elapsed', total_time_elapsed]])
	print("Save output to file...")
	np.savetxt('./result/Result Androbugs/running_time_androbugs_benign.txt', running_time, delimiter=" ", fmt="%s")
	# np.savetxt('./result/Result Androbugs/running_time_androbugs_malicious.txt', running_time, delimiter=" ", fmt="%s")


if __name__ == '__main__':
   main()