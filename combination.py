import math as a
st=input("Enter 3 or 4 letter word : ")
n=len(st)
n2=n
terms=a.factorial(n2)
if n<4:
    while n!=4:
        st=st+" "
        n+=1
for i in range(4):
    for j in range(4):
        if j!=i:
            for k in range(4):
                if k!=j and k!=i:
                    for l in range(4):
                        if l!=i and l!=j and l!=k:
                            if n2==4 and terms!=0:
                                print(st[i]+st[j]+st[k]+st[l])
                                terms-=1
                            if n2==3 and st[i]==" " and terms!=0:
                                print(st[j]+st[k]+st[l])
                                terms-=1
                            if n2==2 and st[i]==" " and st[j]==" " and terms!=0:
                                print(st[k]+st[l])
                                terms-=1
                            if n2==1 and st[i]==" " and st[j]==" " and st[k]==" " and terms!=0:
                                print(st[l])
                                terms-=1
                            if terms==0:
                                break
                if terms==0:
                    break
        if terms==0:
            break
    if terms==0:
        break