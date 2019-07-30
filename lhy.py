X11=int(input())
l=list(map(int,input().split()))
Z11=1
ab=0
for p in range(1,X11):
	if l[p]>l[p-1]:
		Z11=Z11+1
	else:
		if Z11>ab:
			ab=Z11
		Z11=1
if Z11>ab:
	ab=Z11
print(ab)
