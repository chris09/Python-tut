str1 = "this is a string."

print('Length of a string :', len(str1))
str1 = str1.encode(); # encode
print('str1.encode() :', str1)
str1 = str1.decode();
print('str1.decode() :', str1)

# slice
print('str1[0] :', str1[0])
print('str1[5] :', str1[5])
print('str1[0:17] :', str1[0:17])
print('str1[0:17:2] :', str1[0:17:2])
print('copy a string :', str1[:])
print('reverse:', str1[::-1])
