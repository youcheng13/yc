
A = [0,1,2,3,4,5,6,7,8,9]
even = []
odd = []
while len (A) > 0:
    a = A.pop()
    if (a % 2 == 0):
        even.append (a)
    else:
        odd.append (a)

print(even)
print(odd)
