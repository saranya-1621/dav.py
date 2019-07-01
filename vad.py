bb,dav=map(int,input().split())
for p in range(bb+1,dav,1):
  if(p>1):
    for m in range(2,p):
      if(p%m==0):
        break
     else:
       print(p,end="")
