# 27/Nov/2024

## Miss Musaika 

### Dictionary 

Dictionaries are used to store data values in key:value pairs.

Dictionaries are written with curly brackets, and have keys and values .

Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#### What is meant by Ordered 🤔 ?

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

#### Changeable ?🤔

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

#### Not allow for duplicates

Dictionaries cannot have two items with the same key 

#### Length Function 

To determine how many items a dictionary has, use the len() function; Here the one key: value paired considerd one item 

           Dict = {
            'name' : 'Fiza',
            'Student' : True
           }
           print(len(Dict))


#### Dictionary Items - Data Types

The values in dictionary items can be of any data type
    
      thisdict = {
      "brand": "Ford",
      "electric": False,
      "year": 1964,
      "colors": ["red", "white", "blue"]
       }

From Python's perspective, dictionaries are defined as objects with the data type 'dict':

       <class 'dict'>


## Miss Areeba 

### Task1 => Traingle Based

  - Write a program to check the type of trioangle based on the length of its sides of a , b & c  

    - If all the three sides are equal ; print "Equilateral"
    - If any two sides are equal ; print "Isosceles"
    - If no sides are eaual 
        - check if the sum of two sides are greater than third side ; print "Scalene"
        - otherwise print " Invalid Triangle"


### Task2 => TimeStamps (HomeWork)

  - Based upon the timestamp "Hours , Minutes , Seconds" , Enterd by user, Display the following Prompts ; 
      - 1) Good Morning
      - 2) Good Noon 
      - 3) Good Afternoon
      - 4) Good Evening 
      - 5) Good Night
 -  Hint: Use if else Conditions , 
 - Time Library of Python can be used (optional)
