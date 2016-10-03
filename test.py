import math
def reversing(str1):
	S = str1.split(' ')
	Name = reversed(S[0])
	SName = reversed(S[1])
	F = Name+SName
	return F
r='Hello World'
result = reversing(r)
print(result)
