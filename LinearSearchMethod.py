#Mehraneh 30062786
# AT2.7   22/02/2023
# Create a Linear Search method for a list

#Declare a funtion to search an item in a list then return an index of the found item
def SearchList(searchTerm, fruitList):
    # for loop to read each item of a string
    for i in fruitList:
        # condition to find the item in the list
        if searchTerm == i:
            # return the index of the found item to where it called the function
            return fruitList.index(i);
        
# define a variable to put the key board value int it.
searchTerm = input("Which fruit do you search? ")
# define a list with its values
fruitList = ["mango", "watermelon", "apple", "orange", "grape", "banana"]
# call the function with its arguments. One of them a list the other one is an item we
# need to find. then the result assign to a variable
index = SearchList(searchTerm, fruitList)
# condition to found the item in a list or not and display the outputs
if index == None:
    #Disply nothing found
    print(searchTerm, "doesn't found in the fruit list!")
else:
    # Display found the item in which index
    print(searchTerm, " found at ", index)
