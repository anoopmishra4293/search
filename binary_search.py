a = [5,15,25,32,68,110,220,300]

x=110

l = 0
u = len(a)-1

while u>=l:
    mid=(l+u)//2
    if a[mid] == x:
        result=mid
        break
    elif x>mid:
        l=mid+1
    elif x<mid:
        u=mid-1

print(result)