

st.title("Register")
def menu():
  select =st.text_input("enter L to log in or R to register").lower()
  if select == "1":
      login()
  elif select == "r":
    register()
  else:
    menu()
def register():
  surmane = st.text_input("enter your surname").lower()
  forename = st.text_input("enter your forename").lower()
  birthday = st.text_input("enter your birthday like this (DD/MM/YY)")
  password = st.text_input("enter your password")
  username = forename[0] + surname[1] + surname[2] + birthday 
  print("your user name is" + password)
  print("your password is" + password)
  file=open("userlist.txt","a")
  file.write("\n" + username + "," + forename + "," + birthday + "," + surname 
  
    
    




  

