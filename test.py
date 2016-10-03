import math
def reversing(str1):
	S = str1.split(' ')
	Name = S[0].reverse()
	SName = S[1].reverse()
	F = Name+SName
	return F
r='Hello World'
result = reversing(r)
print(result)
