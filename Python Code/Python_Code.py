n=int(input())
sum=0
while n:
    sum=sum+n%10
    n=n//10
print(sum)


