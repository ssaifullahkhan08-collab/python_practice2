#program is about input and output file and edit it
#import module 
import os

#function definition

#program to make general file
def make_general_file(file):
    with open(file,"x"):
        return

#program to make file
def write_data_in_file(file,data):
    with open(file,"r+") as f:
        f.write(data)

#program to print data of file
def show_file_data(file):
    with open(file,"r") as f:
        data = f.read()
        print(data)

#program to delete file
def remove_file(file):
    os.remove(file)

#program to replace words in file
def replace_words(file,old,new):
    with open(file,"r") as f:
        data = f.read()
    # new_data = data.replace("like","love")
    new_data = data.replace(old,new)
    print(new_data)
    
    #overwrite the new world in the file
    with open(file,"w") as f:
        f.write(new_data)

#program to find word in file
def searching_word(file,word):
    with open(file,"r") as f:
        data = f.read()
    if(word in data):
        print("data found:")   
    else:
        print("data not found:")

#program to find word in exact line
def word_in_line_search(word):

    with open("saifullah.txt","r") as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no +=1
    return -1
    
#program to find even no in data
def find_even_no(file):
    count_even = 0 
    count_odd = 0 
    with open(file,"r") as f:
        data = f.read()
        num = data.split(",")
        for el in num:
            if(int(el) % 2 == 0):
                count_even +=1
            else:
                count_odd +=1

    print("total of even no: ",count_even)
    print("total of odd no: ",count_odd)

        
            
 

        
    


#function calling
# make_general_file("numbers.txt")       #this function is used to create general file
# write_data_in_file("numbers.txt","1,2,56,76,34,56,87,65,45,67,89,98,76,54,6,5,7,8,9,7,6,5,4,3,6,7,8,6,5,4")     #this function is used to add data to file
# show_file_data("numbers.txt")          #this function is used to show data of file
# remove_file("numbers.txt")             #this function is used to delete file
# replace_words("numbers.txt","1","78")  #this function is used to replace words in data and update the existing file with the new data
# searching_word(file,"python")          #this function is used to searching words in file
# word_in_line_search("python")          #this function is used to search word in line
# word_in_line_search("love")
# find_even_no("numbers.txt")         
