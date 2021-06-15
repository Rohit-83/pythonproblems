def primeFactor(num):
  l = []
  for i in range(2,num+1):
    while num%i == 0:
      l.append(i)
      num = num//i
  if num>2:
    l.append(2)

  return l

num=12
print(primeFactor(num))
