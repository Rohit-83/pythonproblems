s=[1,2,3,4]
new=[0]
for i in range(len(s)):
	for j in range(i+1,len(s)+1):
		new.append(s[i:j])
print(new)
