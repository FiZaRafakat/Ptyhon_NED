Time = input("Enter TimeStamp in '0h:0m:0s' ............... ")

if Time >= "05:00:00" and Time < "12:00:00" :
         print("Good Morning 🤗🥰!!")
elif Time >= "12:00:00" and Time < "15:00:00" :
        print("Good Noon 😊!!")
elif Time >= "15:00:00" and Time < "17:00:00" :
         print("Good Aftenoon 😃!!")
elif Time >= "17:00:00" and Time < "20:00:00" : 
         print("good Evening!! 🙂")
elif Time >"20:00:00" and Time < "00:00:00" :
         print("Good Night!! 🥱😴")
else : 
         print("It's not a time For Greeting..... 😜😅")
