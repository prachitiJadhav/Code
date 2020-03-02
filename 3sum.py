
num = [int(x) for x in input().split()]
target=int(input())
import math
num.sort()
c=int(num[0]+num[1]+num[2])
for i in range(len(num)):
	ls=i+1
	rs=len(num)-1
	while(ls<rs):
		sum=num[i]+num[ls]+num[rs]
		if(abs(sum-target)<abs(c-target)):
			c=sum
		if(sum==target):
			print(sum)
			exit()

		elif(sum<target):
			ls=ls+1
		else:
			rs=rs-1
	
print(sum)