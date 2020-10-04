#https://www.facebook.com/100051921408118/posts/190716086002437/?app=fbl
#Subscribed by CodeHouse
# Program to sort alphabetically the words form a string provided by the user

my_str = "Hi i  am Yash"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
