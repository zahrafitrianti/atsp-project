What we have to do for the project

- submit APK and analyze it
- select features
- decide what kind of output to get
- try to automate the process (go over the dataset) [done]
- Calculate:
security/vulnerability score; how many vulnerabilities it has, bad security practices.
output -> combine the (right) different tools


I tried
- Static analyzer tool = androwarn (require >=Python3.x)
- App vulnerability scanner = AndroBugs (require Python2.x)
- Qark - destroys my pip3 + entire python env (would advise against it)
- Dynamic Analysis Tools = Mobile-Security-Framework MobSF (Only considered, not tried)

TO-DO:
- parse output txt file
- calculate vulnerability score -> higher (bad) (androbugs)
For androbugs, score can be calculated as:
Score(app) = (c*NumofCriticals) + (w*NumofWarnings) + (n*NumofNotices) + (i*NumofInfo), where c, w, n, and i are weights.

For androwarn:
score(app) = num of features

- calculate runtime per app, and per analyzer
- report

Extension:
- go further into the output file and count the number of times a certain feature occurs
- find some malicious apps and compare the scores with the benign ones

