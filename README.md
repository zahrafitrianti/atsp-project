# atsp-project
To run this project you have to change the hardcoded path for input and output inside the various class to adapt to your path for the input and output

## Structure tree
``` bash
+---Reports		                         -> Folder of all reports
|   +---Report MobSF		                  -> Folder of MobSF reports 
|   |   +---Report Benign apk		          -> MobSF reports for bening apk dataset
|   |   +---Report Malicious apk		        -> MobSF reports for malicious apk dataset 
|   |   \---Report other malicious apk (test)	-> MobSF reports for other malicious apk
|   +---report_androbugs_bening		            -> Androbugs reports for bening apk dataset
|   +---report_androbugs_malicious		        -> Androbugs reports for malicious apk dataset 
|   +---report_androwarn_bening		            -> AndroWarn reports for bening apk dataset
|   \---report_androwarn_malicious		        -> AndroWarn reports for malicious apk dataset 
\---result		                                -> Result folder, inside the result of the combined scores for the apks
    +---Result Androbugs		                -> Result for the scores of Androbugs
    \---Result AndroWarn		                -> Result for the scores of AndroWarn
```

## Relevant scripts
Below we list the relevant scripts which you can run / refer to reproduce our results.

### Running analyzers
* [run_androwarn.py](https://github.com/zahrafitrianti/atsp-project/blob/master/run_androwarn.py) - analyze all apks within a dataset using androwarn. Results will be some txt files which are stored in [Reports](https://github.com/zahrafitrianti/atsp-project/tree/master/Reports) folder.
* [run_androbugs.py](https://github.com/zahrafitrianti/atsp-project/blob/master/run_androbugs.py) - analyze all apks within a dataset using androbugs. Results will be some txt files which are stored in [Reports](https://github.com/zahrafitrianti/atsp-project/tree/master/Reports) folder.

### Parsing output, extract features, calculate scores
* [parse_androwarn.py](https://github.com/zahrafitrianti/atsp-project/blob/master/parse_androwarn.py) - parse the output files from androwarn generated from previous step and extract features and calculate scores per app. The results are in a form of a csv file which is stored in [Result Androwarn](https://github.com/zahrafitrianti/atsp-project/tree/master/result/Result%20AndroWarn) folder.
* [parse_androbugs.py](https://github.com/zahrafitrianti/atsp-project/blob/master/parse_androbugs.py) - parse the output files from androwarn generated from previous step and extract features and calculate scores per app. The results are in a form of a csv file which is stored in [Result Androwarn](https://github.com/zahrafitrianti/atsp-project/tree/master/result/Result%20AndroBugs) folder.

### Final (combined) scores and plot
* [scores.py](https://github.com/zahrafitrianti/atsp-project/blob/master/scores.py) - combine scores of the results from androwarn and androbugs analyzers and save the final scores in a csv file which is stored in [result](https://github.com/zahrafitrianti/atsp-project/tree/master/result). This script will also generate the plot of histograms of scores which we present in the report.

## Analyzer tools installation

### Androwarn
* clone this repository: [https://github.com/maaaaz/androwarn](https://github.com/maaaaz/androwarn)
* cd to the cloned repository: `cd androwarn`
* install requirements: `pip3 install -r requirements.txt`
* to test the analyzer:
```python3 androwarn.py -i <apk.file> -r <output file type> -v <verbose level> ```

### Androbugs
* clone this repository: [https://github.com/AndroBugs/AndroBugs_Framework](https://github.com/AndroBugs/AndroBugs_Framework)
* cd to the cloned AndroBugs_Framework: `cd AndroBugs_Framework`
* to test the analyzer:
```
python androbugs.py -f <apk.file> -o <output directory>
```
* NOTE: Androbugs uses Python 2.x

## Running the analysis
* Download the Benign-sample-187 directory which consists of 187 apk files from the shared drive
* Make sure you have all the analyzer tools installed (preferrably in a virtual environment)
* To run analysis using Androwarn:
```
python3 run_androwarn.py
```
* To run analysis using Androbugs:
```
python3 run_androbugs.py
```

The above commands will run the analysis for all apk files. The output txt files are saved in `report_androwarn/` folder for Androwarn and in `report_androbugs/` folder for Androbugs.

### Creating a virtual environment
* If you do not have `virtualenv` installed, type: `pip3 install virtualenv`
* To create a python environment:
```
python3 -m virtualenv <name of virtual environment>
```
* Activate the newly created environment
```
source <name of virtual environment>/bin/activate
```
* To deactivate the virtual environment
```
deactivate
```
