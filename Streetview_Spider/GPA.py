a=input()
a=a.split("\n")
b=[]

def pku()

for i in a:
 if(len(i)>0):
  b.append(i.split("a"))
print(b)
total_credit=0
for i in b:
 total_credit+=float(i[2])
n=len(b)

ans=0
for i in b:
 ans+=1.0*b[1]/(1.0*total_credit)*float(i[2])

print(ans)
