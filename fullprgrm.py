import time
import os
start_time=time.time()
alpha=input("Enter the Alpha File as eg:filename.txt")
proton=input("Enter the Proton File as eg:filename.txt")
output=input("Enter the output File name as eg:filename.txt")
with open(alpha,"r") as file1:
    readfile=file1.readlines()
split1=readfile[1].split("\n")
split2=split1[0].split("\t")
sizeof=len(split2)-1
#print(sizeof)
x={}
val=1
for i in range(len(readfile)):
    if(i<len(readfile)-1):
        split1=readfile[i].split("\n")
        split2=split1[0].split("\t")
        index1=split2[0]
        split3=readfile[i+1].split("\n")
        split4=split3[0].split("\t")
        index2=split4[0]
        if(index1==index2):
            x.update({index1:val+1})
        else:
            val=1
event_space=max(x.values())#gives the max value of occurences
addrz=max(x, key=x. get)#gives the first address of the event with max value of occurences 
for i in range(len(readfile)):
    if(i<len(readfile)-1):
        split1=readfile[i].split("\n")
        split2=split1[0].split("\t")
        index1=split2[0]
        split3=readfile[i+1].split("\n")
        split4=split3[0].split("\t")
        index2=split4[0]
        if(index1==index2):
            splitall=split2+split4[1::]
            with open("temp.txt","a") as file2:
                for each in (splitall):
                    file2.write(each+"\t")
                file2.write("\n")#print(i,splitall)
            del readfile[i]
        else:
            with open("temp.txt","a") as file2:
                for each in split2:
                    file2.write(each+"\t")
                for m in range(sizeof*(event_space-1)):
                    file2.write("0\t")
                file2.write("\n")#print(i,split2)
    if(i==len(readfile)-1):
        ssplit1=readfile[-1].split("\n")
        ssplit2=ssplit1[0].split("\t")
        iindex1=ssplit2[0]
        ssplit3=readfile[-2].split("\n")
        ssplit4=ssplit3[0].split("\t")
        iindex2=ssplit4[0]
        if(iindex1!=iindex2):
            with open("temp.txt","a") as file2:
                for each in (ssplit2):
                    file2.write(each+"\t")
                for n in range(sizeof*(event_space-1)):
                    file2.write("0\t")
                file2.write("\n")#print(ssplit2)
with open(proton,"r") as file1:
    prot=file1.readlines()
with open("temp.txt","r") as file2:
    alpha=file2.readlines()
protL=len(prot)
alphaL=len(alpha)
ct1=0
ct2=0
#if(protL>alphaL):
for i in range(protL):
    protsplit1=prot[i].split("\n")
    protsplit2=protsplit1[0].split("\t")
    #print("First loop",i)
    for k in range(ct2,alphaL):
        alphasplit1=alpha[k].split("\n")
        alphasplit=alphasplit1[0].split("\t")
        if(protsplit2[0]==alphasplit[0]):
            #print(protsplit2[0],alphasplit[0])
            with open(output,"a") as file2:
                    for each in protsplit2:
                        file2.write(str(each)+"\t")
                    for j in range(1,len(alphasplit),1):
                        file2.write(str(alphasplit[j])+"\t")
                    file2.write("\n")
            ct2=k
            #print("Second loop",k)
            break
print("The maximum number of events found",event_space)
print("The address of first event with maximum occurence",addrz)
os.remove("temp.txt")
print ("My program took", time.time() - start_time, "to run")