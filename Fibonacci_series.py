f1=0
f2=1
n=int(input("Enter the end number:"))
print(f1)
print(f2)
for x in range(1,n):
	f3=f1+f2
	print(f3)
	f1,f2=f2,f3