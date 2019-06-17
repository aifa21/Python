# search()

import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

#split()
import re

#Split the string at every white-space character:

str = "The rain in Spain"
x = re.split("\s", str)
print(x)


#sub()

import re

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

#finditer()

import re

str = "The rain in Spain"
for i in re.finditer("rain",str):

  ss=i.span()
print(ss)



import re

str = "The, rain, in, spain"

ss=re.findall("[riS]at",str)
for i in ss:
         print(i)

         import re

         str = "The, rain, in, Spain"

         ss = re.findall("[m-z]at", str)
         for i in ss:

           print(i)



import re

randstr='''
keep the
blue flg
aifa
'''

print(randstr)

regex=re.compile("\n")
randstr=regex.sub(" ",randstr)

print(randstr)