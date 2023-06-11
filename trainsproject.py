#list of trains
#list of passangers
#list of timeings
#ticket generation
#type of ticket
#source and generation


import time
from datetime import datetime
user_names={"gopi":'1234',"janu":'2345',"hari":'3456',"sreedhar":'4567'}
list_of_trains={"seshadri express":'17290',"yesvantpur express":'12539',"Bangalore intercity express":'22617',"Howrah express":'22864',"TATA express":'12890',"Hatia express":'12836',"Bhubaneswar express":'12846'}
username=str(input("enter your user name :"))
password=str(input("enter your password: "))
# if username in user_names:
#     if password in user_names[username]:
#           print("Your details are mached, Please select your train and train number")
#     else:
#           print("please enter your correct password")
# else:
#      print("please enter your correct user name")
# for t,n in list_of_trains.items():
#      print("train name: ",t)
#      print("train number: ",n)


for i in range(len(user_names)):
     if username not in user_names or password != user_names[username]:
          print("Invalid username or password")
          print("please enter your correct details")
          break
     else:
          print("Login successful")
          print("Please select your train name and train number")     
     for t,n in list_of_trains.items():
          print("train name: ",t,"   ","train number : ",n)
          # print("train number: ",n)
# list of trains complete

