

from itertools import permutations
def myfunc ():
    perm = permutations([1, 2, 3])
    for i in list(perm):
        print(i)

def newfunc ():

    f=open("./passwd.test","r" )
    #print(type(f))
    for x in f:
        fields= x.split(":")
       # print(fields[0])
        print(fields[2])
        #print("ravi")
    f.close()

def subProcessRun():
    import subprocess
    import re
    myproc = subprocess.run("ls -lah /etc/", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    val = myproc.stdout
    sub1 = re.sub("total.*\n?", "", val)
    print(type(sub1))
    #print(sub1)
    sub2=sub1.split("\n")
    for i in sub2:
        print (i.split()[2]," hello bhai ",i.split()[1] )






 #   my_string='_coreml:*:280:280:CoreML Services:/var/empty:/usr/bin/false'
  #  print(my_string.split(sep=":")[0])

if __name__ == '__main__':
    #myfunc()
   # newfunc()
    subProcessRun()
