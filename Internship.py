print ('hello world')
#single line comment
'''multi 
   line
   comment'''
#collecting value from a user 
value_1 = input('enter data')
#outputs collected data
print (value_1)
#variable
var1 = 12
#outputs variable
print(var1)
#outputs type of variable
print(type(var1))

#lists
fruits =['mango', 'apple', 'banana']
#lists follow an order starting from 0 and not 1 
numbers =[0, 1, 2, 3]
print(fruits[0])
print(fruits[-1]) #this is negative indexing
#negative indexing starts from -1
print(len(fruits)) #this prints the length of the list
fruits[1] = 'blueberry' #this replaces item 1 with another item
print(fruits[1]) #prints replaced fruit

#tuples
#tuples use "()"
#this follows most of the rules of lists including referencing
names = ('james','matthew','Jonan')
print(names[1]) #this prints matthew
#tuples cant be edited using functions like del or even replaced. They can only be printed

#dictionaires


