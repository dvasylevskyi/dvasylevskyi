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
  surmane = st.text_input("Enter your surname").lower()
  forename = st.text_input("Enter your forename").lower()
  birthday = st.text_input("Enter your birthday like this (DD/MM/YY)")
  password = st.text_input("Enter your password")
  username = surname[0] + surname[1] + forename[1] + birthday[2] 
  
    
    




  

