import math

#get the word
entry = input("Enter a word: ")

#changing string to number
x = range(len(entry))
i = 0
for n in x:
    i = ord(entry[n]) + i
data_num = i

#using multiplication method to hash entry
A = 0.2072002
M = 100
rep = math.floor(M * (data_num * A % 1))
print("Your data entry is " + entry + ".") 
print("It's number is " + str(data_num) + ".")
print("It will be stored in the location " + str(rep) + ".")