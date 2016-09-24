exDict = {'Jack': [15, 'blone'], 'Bob': [22, 'brown'], 'Alice': [12, 'black'], 'Keven': [17, 'red']}

print(exDict)

print(exDict['Jack'])

# add
exDict['Tim'] = 33
print(exDict)

# delete
del exDict['Tim']
print(exDict)


print(exDict['Jack'][1])
