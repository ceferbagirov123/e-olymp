#№ 8852
n=int(input())
a=n//10000
b=n//1000%10
c=n//100%10
d=n//10%10
e=n%10
print(a*100+c*10+e)