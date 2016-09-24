import re


'''
Identifiers:

\d any number
\D anything but a number
\s space
\S anthing but a space
\w any character
\W anything but a character
. = any character, except for a new line
\b the whitespace around words
\. a period


Modifiers:
{1,3} we're expectng 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
^ Matching the beginning of a string
| eigher or
[] range or "variance"
{x} expecting "x" amount

White Space Characters:
\n new line
\s Space
\e escape
\f form feed
\r return

DONT FORGET!:

. + * ? [ ] $ ^ ( ) | \
'''

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscard, is 102.
'''
ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1
print(ageDict)
