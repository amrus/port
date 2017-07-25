import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
print(elementsList[0])

# print the last element
print(elementsList[len(elementsList)-1])
# print all the elements
print(elementsList)

# Start your search algorithm here.
countryIWant = input ('Choose a country to find from the list.')
beginningIndex = 0
endingIndex = len(elementsList)-1
index = int((endingIndex-beginningIndex)/2)
while elementsList[index]  != countryIWant:
    if  countryIWant < elementsList[index] :
        beginningIndex = beginningIndex
        endingIndex = index
        index = int(beginningIndex+(endingIndex-beginningIndex)/2)


    elif countryIWant > elementsList[index]:
        beginningIndex = index
        endingIndex = endingIndex
        index = int(beginningIndex+(endingIndex-beginningIndex)/2)
    else:
        print (index)

print (index)
