import random
import string
import time
print('The Password Generator')
print(' ')
time.sleep(.5)
a=(random.choice(string.ascii_letters))
i=(random.randint(0,9))
g=(random.randint(0,9))
z=(random.choice(string.ascii_letters))
e=(random.randint(0,9))
r=(random.randint(0,9))
f=(random.randint(0,9))
o=(random.randint(0,9))
g=(random.choice(string.ascii_letters))
g=(random.choice(string.ascii_letters))
t=(random.choice(string.ascii_letters))
password=input('Password y/n:')
if password=='y':
  print(' ')
  time.sleep(.5)
  print('Your Password is:' + ' ' + a+str(i)+str(g)+str(g)+str(e)+str(r)+str(f)+str(o)+str(z)+g+t)
if password=='n':
  time.sleep(.1)
  print(' ')
  print('ESCN')

if password=='Y':
  print(' ')
  print('Case sensitive, please use lower case')
if password=='N':
  print(' ')
  print('Case sensitive, please use lower case')

