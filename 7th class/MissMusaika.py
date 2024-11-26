# ## Compare Strings and List

# #Insert elements in strings
# s = "Python"
# print(s[0:2] + 'q' +s[3:5])
# #Insert Elements in list 
# my_list = ['apple','banana']
# my_list.append('cherry')
# print('list after inserting a value : ',my_list)

# #Delete Elements in string
# S="JavaScript"
# print(S[0:4] +S[5:10])
# #Delete Elements in a list
# list = ['Mango',"Apple","Cherry"]
# list.remove("Apple")
# print(list)

# # Replace in strings
# text = "Python is Fun"
# result = text.replace("Python",'Coding')
# print('Replace in new variable ::',result)
# # Replace in List
# R_list = [1,4,4,7,5,6]
# print(R_list)
# R_list[4]=8
# print('After Replace:',R_list)


# #Check if the strings ends with world!! 
# txt = 'Hello World'
# if txt.endswith("World"):
#     print("True")
# else:
#     print('False')



# #Join a list in a string 
# Join_list = ["Coding",'is','Fun']
# print(Join_list)
# sentence = ' '.join(Join_list)
# print(sentence)


# # Case Sensitive
# str1 = "Hello"
# str2 = 'hello'
# if str1 == str2 :
#     print("The String is same")
# else :
#     print('The String is not same')



# if str1.lower() == str2.lower() :
#     print("The String is same")
# else:
#     print('The String is not same')


# # Check if all elements in a list is same

# list = [1,2,3,4]
# if list[0] == list[1] == list[2]:
#     print('True')
# else :
#     print('False')


# Remove Apple with pop
fruit = ['Apple','Mango','Cherry','Banana']
r_fruit = fruit.pop(0)
print(fruit)
# Remove Apple with remove method
Fruit = ['Apple','Mango','Cherry','Banana']
Fruit.remove('Apple')
print(Fruit)
# Remove Apple with del method
Fruits = ['Apple','Mango','Cherry','Banana']
del Fruits[0]
print(Fruits)



