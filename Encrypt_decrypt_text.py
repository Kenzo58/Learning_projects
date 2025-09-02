import os
import json
from cryptography.fernet import Fernet

class Credintial:
    def __init__(self,username,password,data):
        self.username=username
        self.password=password
        self.data=data
        self.path="info.json"
    def sign_up(self):
        print("............................")
        print("SIGN UP")
        print("............................")
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                try:
                    self.data = json.load(file)  
                except json.JSONDecodeError:
                    self.data = {}       
        else:
            self.data = {}
        while True:
                self.username=input("Enter your username :").strip()
                if not self.username:
                    print("write something idiot")
                elif len(self.username) <=3:
                    print("Username cannot be less than 3 characters")
                elif self.username.lower() in self.data:
                        print("User already exists")
                else:
                    break
            
        while True:
            self.password=input("please enter your password :").strip()
            if len(self.password)>=8:
                print(f"Welcome {self.username.capitalize()}")
                break
            else:
                print("Password must be more than 8 characters.")

        key=Fernet.generate_key()
        self.data[self.username]={'password':self.password,'key':key.decode()}
        with open(self.path,"w") as file:
            json.dump(self.data,file,indent=4)

        
    def login(self):
         print("............................")
         print("LOGIN")
         print("............................")
         self.username=input("enter your username :")
         self.password=input("enter your password :")
         if os.path.exists(self.path):
            with open(self.path, "r") as file:
                try:    
                    self.data=json.load(file)
                except json.JSONDecodeError:
                    self.data={}
         else:
             self.data={}
         if self.username in self.data and self.data[self.username]['password']==self.password:
             print("Login succeed!")
             return self.data[self.username]['key']
         else:
             print("incorrect login")
             return None

class Encryption_decryption:
    def __init__(self,key):
        self.key=key
        self.fernet=Fernet(self.key)

    def encryption(self):
        text=input("enter the text you want to encrypt :")
        encrypted_text=self.fernet.encrypt(text.encode())
        print(f"Encrypted text: {encrypted_text.decode()}")

    def decryption(self):
        try:
            text=input("enter the text you want to decrypt :")
            decrypted_text=self.fernet.decrypt(text.encode())
            print(f"Decrypted text: {decrypted_text.decode()}")
        except:
            print("Invalid encrypted text or wrong key for decryption.")

def main():
    user= Credintial("","",{})
    running=True
    while running:
        print("Do you want to log in or sign up?")
        print("1 for Sign up")
        print("2 for Login")
        print("3 for Exit")
        choice = int(input("Enter your choice: "))
        
        if choice==1:
            user.sign_up()
        elif choice==2:
            key=user.login()
            if key:
                encryption_decryption=Encryption_decryption(key.encode())
                while True:

                    print("Do you want to encrypt or decrypt text?")
                    print("1 for Encrypt")
                    print("2 for Decrypt")
                    print("3 for Log out")
                    action = int(input("Enter your choice: "))

                    if action==1:
                        encryption_decryption.encryption()
                    elif action==2:
                        encryption_decryption.decryption()
                    elif action == 3:
                        print("Logging out...")
                        break
                    else:
                        print("Invalid input.")
        elif choice==3:
             print("Goodbye")
             running = False
        else:
            print("Incorrect input.")

if __name__=="__main__":
    main()
