"""i am siafullah. today i started my python new course 
and i writing my practice code using function in order to 
save time nad space so the following are my practice session
in details.  """

#function definition
def helloWord():
  print("hello world:")

def evenOdd():
  number = int(input("number: "))
  print(number)
  if(number%2 == 0):
    print("your enter no is even")
  elif(number%2 != 0):
    print("your enter no is odd:")
  else:
    print("enter correct no:")

def greatestNo():
   num1 = int(input("enter no 1:"))
   num2 = int(input("enter no 2:"))
   num3 = int(input("enter no 3:"))

   if(num1 > num2 and num1 > num3):
    print("the first no you enter is greater which  = ",num1)
   elif(num2 > num1 and num2 > num3):
    print("the second no you enter is greater which = ",num2)
   elif(num3 > num1 and num3 > num2):
    print("the third no you enter is greater = ",num3)
   else:
    print("you enter incorrect value:")

def multiple():
  number = int(input("enter no:"))
  if(number%7 == 0):
    print(number," is multiple of 7:")
  else:
    print(number," is not multiple of 7:")

def if_else():
  #using if-else statement
  gender = input("enter your gender 'm' 'M' or 'f' 'F' :")
  if(gender == "m" or gender == "M"):
    print("you are eligible:")
  elif(gender == "f" or gender == "F"):
    print("you are not eligible:")
  else:
    print("you enter wrong character")

  #program using if-else turnory statement
  a = 0
  "eligible" if a == 0 else "not eligible"

def lists():
  marks = [89,78,98,90,67,89]
  student = ["saifullah","muhammad khalid",20,3.5]
  print(marks)
  print(student)
  #slicing
  minimarks = marks[1:3]
  minimarks = marks[1:]
  print(minimarks)

  #methods in lists
  data = [1,2,5,4,6,3,7,8,6,5]
  data.append(9) #add member to end
  print(data)
  data.sort() #sorting data in assending order
  print(data)
  data.sort(reverse=True) #sorting data in descending order
  print(data)
  data.reverse() #sorting data in reverse order
  print(data)
  data.insert(3,7) #insert data at any index
  print(data)
  data.remove(1) #remove fist mention data in method from list
  print(data)
  data.pop(6) #remove data at any index
  print(data)
  

def tuples():
  data = (2,3,5,2,8,7,9,4)
  print(data)
  print(data.index(4)) #searching no at any index
  print(data.count(2)) #count any member in data

def movieList(): #user enter three movies name and i arrange it in list
  movie1 = input("enter first movie name:")
  movie2 = input("enter second movie name:")  
  movie3 = input("enter third movie name:")
  movies = [movie1 , movie2, movie3]
  print(movies)

def palindromeList(): #find if the list is palindrome
  list1 = [1,2,3,2,1]
  copyList = list1.copy()

  if(copyList == list1):
    print("your list is palindrome")
  else:
    print("your list is not palindrome:")

def trafficLight():
  color = input("light color: ")

  if(color == "red"):
    print("stop your car:")
  elif(color == "green"):
    print("go:")
  elif(color == "yellow"):
    print("ready to move:")
  else:
    print("light is broke, please wait..")

def dictionary(): #this function is about dictionary
  student = {
    "name" : "saifullah",
    "fname": "muhammad khalid",
    "age" : 20,
    "gpa" : 3.5,
    "subject" : ["dsa","cpp","python"]
  }
  
  print(student)
  print(student["subject"])
  print(student["name"])
  print(student["fname"])
  print(student["age"])
  print(student["gpa"])

  student["name"] = "salman"
  student["profession"] = "shopkeeper"
  print(student)

  #nested dictionary
  student1 = {
    "name" : "saifullah",
    "subject" : {
      "cpp" : 45,
      "python" :78,
      "c": 45,
    }
  }

  print(student1["subject"]["cpp"])
  print(student.keys()) #use to access to key of dictionary
  print(student.items()) #use to access to item in dictionary
  print(student.values()) #use to access to the the values of keys
  print(student.get("name")) #use to get value of key
  student.update(student1) #use to update dictionary

  #add three subject that the users enter to in dictionary
  subjects = {}
  sub = input("enter first subject name: ")
  marks = int(input("enter first subject marks: "))
  subjects.update({sub:marks})
  sub = input("enter second subject name: ")
  marks = int(input("enter second subject marks: "))
  subjects.update({sub:marks})
  sub = input("enter third subject name: ")
  marks = int(input("enter third subject marks: "))
  subjects.update({sub:marks})

  print(subjects)

def sets():
  data = {4,3,5,3,3,"saifullah"}
  print(data)

  #null set declaration
  # data1 = set{}
  
  #method in set
  data.add("salman") #add element to set
  print(data)
  data.remove("saifullah") #remove element from set
  print(data)
  data.pop() #remove ramdom element from set
  print(data)
  data.clear() #empty the set
  print(data)

  data2 = {1,2,3,4,5,6}
  data3 = {4,5,6,7,8}
  print(data2.union(data3)) #use to unite two sets 
  print(data2.intersection(data3)) #use to pick common element in two sets
  
  #storing meaning of words using dictionary
  words = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of fact and figures"]
  }
  
  print(words)

  #find total no of class room from raw data
  subjects = {"phyton","java","c++","phyton","jascript","phyton","java","java","c++","c"}
  print(len(subjects))

  #find a way to store 9 9.0 as separate member in set
  numbers = {9,"9.0"}
  print(numbers)


#this function is about while loops
def whileloops():

  #while loop
  count = 1
  while count <= 100:
    print(count,"saifullah")
    count +=1

#program of number table
  number = 1
  answer = 0
  userNo = int(input("enter no to find table:"))
  while number <= 10:
    answer = userNo * number
    print(userNo," * ",number," = ",answer)
    number +=1 

#print the element
  number1 = 1
  while number1 <= 10:
    finalno = number1**2
    print(finalno)
    number1 +=1

#search for no in tuples
  data1 = (1,4,9,16,25,36,49,64,81,100)
  userNo1 = int(input("enter no: "))
  index = 0
  length = len(data1)
  while index < length:
    if(data1[index] == userNo1):
      print("your no found at index ",index)
    index +=1

#functuion about for loop
def forloop():
  data = [1,2,3,4,5,6,7,8,9,10] 
  for el in data:
    print(el)
  else:
    print("loop ended:")

  #print element of list
  data1 = [1,4,9,16,25,36,49,64,81,100]
  for el in data1:
    print(el)
  else:
    print("program ended:")

  #program to find number
  userno = int(input("enter no:"))
  data2 = (1,4,9,16,25,36,49,64,81,100)
  for el in data2:
    if(el == userno):
      print("number is found: ")
      break           
    else:
      print("searching")
  else:
    print("program end:")


#program is about range function
def rangefunction():
  #three ways to write range function
  #first way
  #range(ending no)
  data1 = range(10)  
  for el in data1:
    print(el)
  
  #second way way
  #range(start? , stop)
  data2 = range(1,10)  
  for el in data2:
    print(el)
  
  #third way
  #range(start? , stop ,step?)
  data3 = range(1,10,2)  
  for el in data3:
    print(el)

  #program to find print no from 1 to 100 using for and range 
  for el in range(1,101):
    print(el)

  #program to find print no from 100 to 1 using for and range 
  for el in range(100,0,-1):
    print(el)

  #program to find multiplication table of n number using for and range 
  number = int(input("enter no:"))
  for el in range(1,11):
    print(number," * ",el," = ", number*el)

#program used pass statement in loop or if-else statement
def pass_Statement():
  for el in range(10):
    pass
  print("program end:")
  
  i = 0
  if(i<10):
    pass
  print("program end:")


#program to find sum of natural no that the user enter
def sum_number(): 
  number = int(input("enter no:"))
  index = 1
  sum = 0
  while index <= number:
    sum = sum + index
    index +=1
  print("sum :",sum ) 


#finding factorial of number using loop
def factorial():
  number = int(input("enter no:"))
  factorial = 1
  for el in range(1,number+1):
    factorial *=el
  print("factorial :",factorial)


#program is about function

#simple function

def simple_function():
  a = 0 
  print(a)

#parameter function
def parameter_function(a,b):
  sum = a+b
  print("sum: ",sum)


#program about print length of  as list pass argument
def list_function(list):
    print(len(lists))


#print a list item in same line
def same_list_function(lists):
  for el in lists:
    print(el, end=" ")

#program to convert usd to pkr
def convert_currency(amount,rate):
  total_amount = amount * rate
  print(total_amount)


#program is about recursion 
def recursion_function(n):
    if(n == 0):
      return
    print(n)
    recursion_function(n-1)
    print(n,"end")


#program to find the factorial of n using recurrnce
def factorial_recurrence(n):
  if(n == 0 or n == 1):
    return 1
  else:
    return n * factorial_recurrence(n-1)

#program to sum natural no using recurrence
def recurrence_sum(n):
  if(n == 1):
    return 1
  else:
    return n + recurrence_sum(n-1)

#program to print element of list using recursion
def list_recurrence(lists,index = 0):
  if(index == len(lists)):
    return
  print(lists[index])
  list_recurrence(lists , index+1)



  



  


#All function calling

# helloWord()
# if_else()
# lists()
# dictionary()
# sets()
# whileloops()
# forloop()
# palindromeList()
# rangefunction()
# list_recurrence(lists = [1,2,3,4,5,6,7])
# same_list_function(lists=[1,2,3,4,5,6,7,8])
# tuples()
# pass_Statement()
# simple_function()
# parameter_function(6,8)
# recursion_function(10)
# print(recurrence_sum(10))
# print(factorial_recurrence(4))
# convert_currency(amount = 100,rate=280)
# list_function(lists= [1,2,3,4,5,6,7])
# factorial()
# sum_number()
# trafficLight()
# movieList()
# multiple()
# evenOdd()
# greatestNo()






