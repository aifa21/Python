#\A
import re

str = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", str)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")


#\b	Returns a match where the specified characters are at the beginning or at the end of a word

import re

str = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


#\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word


import re

str = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")




#\d	Returns a match where the string contains digits (numbers from 0-9)

import re

str = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", str)

print(x)

if (x):
   print("Yes, there is at least one match!")
else:
  print("No match")




import re

str = "12345"

#Check if the string contains any digits (numbers from 0-9):

x =len(re.findall("\d", str))

print("Matches: ",x)


import re

str = "12345"

#Check if the string contains any digits (numbers from 0-9):

x =len(re.findall("\d{5}", str))

print("Matches: ",x)


import re

str = "123  1234 12345 123456 1234567"

#Check if the string contains any digits (numbers from 0-9):

x =len(re.findall("\d{5,7}", str))

print("Matches: ",x)


#\D	Returns a match where the string DOES NOT contain digits


import re

str = "The rain in Spain"

#Return a match at every no-digit character:

x = re.findall("\D", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")




#\s	Returns a match where the string contains a white space character

import re

str = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")



#\S	Returns a match where the string DOES NOT contain a white space character
import re

str = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")



#\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

import re

str = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#phone no. verification


import re

phn="444-555-6666"

if re.search("\w{3}-\w{3}-\w{4}",phn):
    print("YES it is phone no.")

#full name valid

import re
str="Aifa Faruque"

if re.search("\w{2,20}\s\w{2,20}",str):
    print("Full Name")

#\W	Returns a match where the string DOES NOT contain any word characters

import re

str = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")



