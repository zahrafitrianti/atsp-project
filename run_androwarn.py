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
			
			# define output type
			report_type = 'txt'

			# set verbose level for the output
			verbose_level = 1

			# set time stamp (to avoid rewrites)
			tstart = time.time()
			timestamp = int(tstart)

			# output target
			output_dir = os.path.join(os.getcwd(), 'Reports/report_androwarn')
			# output_dir = os.path.join(os.getcwd(), 'Reports/report_androwarn_malicious')
			output_file = os.path.join(output_dir, f"{filename}_{timestamp}")
			
			# command to run the analyzer tool
			os.system(f"python3 ./androwarn/androwarn.py -i {fname} -o {output_file} -r {report_type} -v {verbose_level}")
			
			tend = time.time() - tstart 
			time_elapsed_per_app.append([filename, tend])
	
	total_time_elapsed = time.time() - start

	running_time = np.vstack([time_elapsed_per_app, ['Total time elapsed', total_time_elapsed]])
	print("Save output to file...")
	np.savetxt('./result/result_androwarn/running_time_androwarn.txt', running_time, delimiter=" ", fmt="%s")
	# np.savetxt('./result/result_androwarn/running_time_androwarn_malicious.txt', running_time, delimiter=" ", fmt="%s")

if __name__ == '__main__':
   main()