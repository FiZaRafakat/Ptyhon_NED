# first_Dic = {
#     "Pakistan" : "Karachi",
#     "India" : "Delhi",
#     "Iran" : "Tehran"
# }

# b={'a':1, 'b' : 2 , 'c' : 10}

# # Key + value ==> 1key-value pair
# print(len(first_Dic))  # length of dictionary
# print(type(first_Dic))  #type of dictionary 
# print(type([1,2,3])) #type of list
# print(first_Dic)
# # print(int(first_Dic))    not possible , type error
# print(type(str(first_Dic)))   # type string now
# print(type(first_Dic))
# print(type(list(first_Dic)))

# e = first_Dic.keys()
# print(list(e))
# print(e)

# f = first_Dic.values()
# print(list(f))
# print(f)

# first_Dic.clear()
# print(first_Dic)

# del first_Dic
# print(first_Dic)  # gives error => beacuse the string is clear 

second_Dic = {
'a' : 1,
'b' : 2,
'c' : 3,
'd' : 4,
'f' : 5
}
second_Dic.pop('a')  # always gives here argument / without argument it will throw an error
print(second_Dic)

second_Dic.popitem() #this popitem behaves like a pop in list   


print(second_Dic)
myDict = {
    1 , 2 , 3 , 4 , 5 , 6, 
}
dictionary = dict.fromkeys(myDict, 4)    # fromkeys hm tb use krty hain jb hamrai keys k 1 hi value rkhni ho 
print(dictionary)

my_dict = {}
my_keys = {'1','2','3','4','5'}
dictionary = my_dict.fromkeys(my_keys,8)
print(dictionary)