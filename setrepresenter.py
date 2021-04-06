s=[1,2,3,4]
new=[0]
for i in range(len(s)):
	for j in range(i,len(s)):
		new.append(s[i:j+1])
print(new)
