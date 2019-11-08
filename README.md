# atsp-project

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
