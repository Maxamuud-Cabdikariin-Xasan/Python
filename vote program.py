# this program determines a person who can vote and can't vote
# first, get the name of the voter
AGE = 18
name = input("Enter your name: ")
# get age
age = int(input("Enter your age: "))
if age >= AGE:
    print(name,'you can vote')
else:
    print('sorry,',name, 'you can\'t vote')