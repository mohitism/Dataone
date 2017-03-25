import csv
from collections import defaultdict

target_dict = defaultdict(dict)

with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row[0],row[1])

        for count in range(2,len(row)) :
            #print(row[count])
            target_dict[row[0].strip()][row[count].strip()] = float(row[1].strip())

print(target_dict)
temp=input()

while temp!="":

    que=temp.split(" ")
    mini=100000.0
    store=-1
    for i in target_dict:
            ans=0.00
            bre=0
            for count in range(0,len(que)):
                    if que[count] in target_dict[i]:
                            ans+=target_dict[i][que[count]]
                    else :
                            bre=1	
                            break
            if bre==0:
                    mini=min(mini,ans)
                    store=i

    if store == -1 :
        print("none")
    else :
        print(store,mini)

    temp=input()
