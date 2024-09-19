import streamlit as st

st.title("Register or Log in")

def menu():
  select = st.text_input("enter l to log in or r to register").lower()
  
def register():
  surmane = st.text_input("enter your surname").lower()
  forename = st.text_input("enter your forename").lower()
  birthday = st.text_input("enter your birthday like this 24031988 for somepne born on 24 March 1988")
  password = st.text_input("enter your password")
  username = forename[0] + surname[1] + surname[2] + birthday 
  print("your user name is" + username)
  print("your password is" + password)
  file=open("userlist.txt","a")
  file.write("\n" + username + "," + password + "," + forename + "," + birthday + "," + surname + "," + "N")
  file.close()
  menu()
  
def adminf():
  st.write ("welcome admin")

def login():
  enterdusername = st.text_input("enter user name")
  enterdusername = st.text_input ("enter password")
  if st.butten("check user"):
  file=open ("userlist.csv","r" , encording="utf-8-sing")
  for line in file:
    lines = line.split(",")
    username = lines[0]
    password = lines[1]
    forename = lines[2]
    birthday = lines[3]
    surname = [4]
    admin = lines[5]

    if enterdusername == username and enterdpassword == password:
       if admin == "N":
          print( "welcome " + forename + " " + surname + " your birthday is " + birthday)
       else:
          adminf() 
else:
  menu()

 
  
    
    




  

