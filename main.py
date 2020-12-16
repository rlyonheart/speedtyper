import time
t1=time.time()
print("\t\tType Any Sentence As Fast As You Can!")
s=input("\n\nEnter sentence :")
t2=time.time()
t=t2-t1
g=[]
w=1
for c in s:
    if c==" ":
        w+=1
    g.append(c)
print("\n\nYou typed",len(g),"characters and",w,"words in",t,"seconds!")
time.sleep(1)
print("\n\nYour typing speed is :",len(g)/t,"characters/second and",w/t,"words/second!")