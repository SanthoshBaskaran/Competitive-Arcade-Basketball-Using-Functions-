x,y,z=list(map(int,input().split()))
result=[]
dict1={}
def players():
    for i in range(x):
        name=input()
        dict1[name]=0
players()
def name_and_score():
    for j in range(z):
        p,q=input().split()
        if(dict1[p]==-1):
            continue
        dict1[p]+=int(q)
        if(dict1[p]>=int(y)):
            result.append(p)
            dict1[p]=-1
name_and_score()
if len(result)==0:
    print('No winner!')
else:
    for k in result:
        print(k,'wins!')
