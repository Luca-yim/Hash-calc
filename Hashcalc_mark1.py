import math
entry = input("Enter a word: ")
#get the word
x = range(len(entry))
i = 0
for n in x:
    i = ord(entry[n]) + i
data_num = i
#changing string to number
A = 0.2072002
M = 100
rep = math.floor(M * (data_num * A % 1))
print("Your data entry is " + entry + ".") 
print("It's number is " + str(data_num) + ".")
print("It will be stored in the location " + str(rep) + ".")