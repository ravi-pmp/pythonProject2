import datetime
import datetime as dt
import requests
import subprocess
import re

def runProcess ():
   import subprocess
   import re
   myProc = subprocess.run("ps -ef", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
   re1 = 'UID\s+PID\s.*'
   myProcStripped=re.sub(re1,"", myProc.stdout)
   myProcStripped1= myProcStripped.split("\n", 1)[1]  #remove first blank line
   myProcStripped2 = [x for x in myProcStripped1.split("\n")[:-1]] #remove last blank line
   print(type(myProcStripped2))
   '''for i in myProcStripped2:
       isub = re.search('*iCloudHelper.*', i)
       print(isub)'''


import subprocess
import re
line = (subprocess.run("ls -l ~", shell=True, stdout=subprocess.PIPE, universal_newlines=True))
sub1 = re.sub(r'total.*\n?', "", line.stdout.strip())
          # sub1 = re.sub("(total.*\n?|[])", "", line.stdout)
          # print (sub1)

    for i in sub1.split("\n"):
         print(i.split()[4], "hi", i.split()[4])
    #   print(i)
#   print (myList)


'''if __name__ == "__main__":
    #fileOpen()
    runProcess()'''
