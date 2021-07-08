#Getting started
#insertion sort
    # sorting problem 
    # efficient sorting algorithm for a small number of elements

# input => sequence of numbers 
# output => reordering of the input array so it is sorted
#Pseudocode 
x = [1,3,5,2,5,1]
def insertionSort(array):
    for i in range(2,len(array)):
        #loop skozi vsakega, od drugega do zadnjega
        # current number je trenutno stevilo
        currentNumber=array[i]
        #naredimo se en index, ki je prejsnji od tega zdaj
        j = i-1
        #vstopimo v while loop dokler je j vecji od 0 ,torej ko pride ko konca
        # in ko je desni number vecji od
        while j > 0 and array[j] > currentNumber:
            #zamenjamo 
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = currentNumber
    print(array)


         

insertionSort(x)