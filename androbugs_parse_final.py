import os
import nltk 
import glob
import re
import pandas as pd
def parse_androbugs():
    path = '/Users/neharajendrabaritamboli/Desktop/AdvancedSecurity/report_androbugs'
    os.chdir(path)
    app_dict = {'app_name': [], 'Score': [],'criticals': [],'warn': [],'notice': [],'info': []}

    for file in glob.glob("*.txt"):
        scores = 0
        final_list = []
        listofstring = []
        permicric = []
        permiwarn = []
        perminot = []
        permitr = []
        f = open(file,newline='')
        for i in f:
            wordList = re.sub("[[^\w]]]", " ",  i).split()
            #print(wordList)
            final_list.append(wordList)
        for list1 in final_list:
            for listoflist in list1:
                listofstring.append(listoflist)
        #listofstring
        for j in listofstring: # this list of string is for one documents
            substr1 = re.findall(r'\[Critical\]',j)
            substr2 = re.findall(r'\[Warning\]',j)
            substr3 = re.findall(r'\[Notice\]',j)
            substr4 = re.findall(r'\[Info\]',j)
            if substr1:
                permicric.append(substr1)
            if substr2:
                permiwarn.append(substr2)
            if substr3:
                perminot.append(substr3)
            if substr4:
                permitr.append(substr4)    
        #print(f)
        #print(permicric)
        #app_dict['app_name'].append(f)

    #     print(len(permicric))
       # print(len(permiwarn))
    #     print(len(perminot))
    #     print(len(permitr))
        c = 3
        w = 1
        n = 1
        inf = 1
        #
        scores = scores + c*(len(permicric)) + w*len(permiwarn) + n*len(perminot) + inf*len(permitr);
        #print((permicric))
        #print('Scores',scores,'******',f)
        #print('*************')
        app_dict['Score'].append(scores)
        app_dict['app_name'].append(file.split('_')[0])
        app_dict['criticals'].append(len(permicric))
        app_dict['warn'].append(len(permiwarn))
        app_dict['notice'].append(len(perminot))
        app_dict['info'].append(len(permitr))

    print(pd.DataFrame(app_dict))

parse_androbugs()
