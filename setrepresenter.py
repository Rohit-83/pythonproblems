s=["a","b","c"]
new=[" ",]
for i in range(len(s)):
	for j in range(i,len(s)+1):
		new.append(s[i:j+1])
print(new)
