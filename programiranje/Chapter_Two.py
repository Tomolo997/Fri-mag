#Data structures
# collection of data elements, that is structured in some way
# 6 types of sequences
# tuples
# list
# ..

# tuples => cannot change it 
# list => can change it

#e Python has a basic notion of a kind of data structure called a container, which is basically any object
#that can contain other objects

# sequence operations
# indexing 
# slicing
# adding
# multiplying 
# chacking for memberships

# indexing 
x = [1,2,5123,221]
print(x[1]) # prints => 2 
print("greetins"[2]) # prints => e

# slicing 
print("mada faka"[3:7]) # prints => a fa
# you supply two indices as limits for your slice
# [0:10:2] => from 0 to 10 , but every second number
# [8:3:-1] => from 8 to 3 , but backwards 

#adding sequances 
#>>> [1, 2, 3] + [4, 5, 6]
#[1, 2, 3, 4, 5, 6]

# multiplication 
# 'python' * 5
#'pythonpythonpythonpythonpython'
#>>> [42] * 10
#[42, 42, 42, 42, 42, 42, 42, 42, 42, 42]

# none , empty lists and initilization
# initialize a list of lenth 10 
#[None]*10

# permissions
# in operatior
# permisions = "rw"
#  "w" in permision => true

# lenth
    #len(numbers)
#maximum number
    # max(numbers)
#minimum number 
    # min(numbers)


# LISTS 
# Lists are mutable
# list("Hello") => ['H', 'e', 'l', 'l', 'o']

# Basic list operations
    #item assingment
    x = [1,1,1]
    x[1] = 2
    print(x) #=> ]1,2,1]
    #deleting elements 
    del x[1] #=> deletes the second element

    # assinging to slice 
    >>> name = list('Perl')
    >>> name
    ['P', 'e', 'r', 'l']
    >>> name[2:] = list('ar')
    >>> name
    ['P', 'e', 'a', 'r']

# List methods 
    #append => list.append(2), add to the end 
    #count => list.count(1), how many 1's are there in the list
    #extend => a.extend(b) , add a list to b list 
    #index => list.index("baby") => show me the index of baby
    #insert => list.insert(3,"four"), insert "four" at the index 3
    #pop => x.pop() => pop from the stack, remove from the start
    #remove => x.remove("baby") => remove the specific from list
    #reverse => reverse the list
    #sort => sort the specific list

#Tuples 
#they can be used as keys in mappings
    #Cant be changed (1,2,3)
    #tuple function , change list to a tuple
