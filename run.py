#!/usr/bin/env python3.7
from credentials import Credentials
from user import User

    def create_credentials(fname,lname,uname,password,email):
        '''
        Function to create new credentials
        '''
        new_credentials = Credentials(fname,lname,user_name,password,email)
        return new_credentials
    def create _user(user_name,email,password):
        '''
        Function that creates new user
        '''
        new_user = User(user_name, email, password)
        return new_user
        

    def save_credentials(credentials):
        '''
        Function to save credentials
        '''
        credentials.save_credentials()  

    def save_user(user):
        '''
        saves user details
        '''
        user.save_user_details()

    def del_credentials(credentials):
        '''
        Function to delete credentials
        '''
        credentials.delete_credentials()

    def find_credentials(email):
        '''
        Function that finds credentials by email and returns the credentials
        '''
        return Credentials.find_by_email(email)

    def checking_existing_credentials(email):
        '''
        Function that check if credentials exists with that email and return a Boolean
        '''
        return Credentials.credentials_exist(email)

    def display_credentials():
        '''
        Function that returns all saved credentials
        '''
        return Credentials.display_credentials()

    def display_user():
        '''
        this class has power to display users
        '''
        return User.display_users()    

    def main():
        print("Hello welcome to your credentials list. what is your name?")
                 user_name = input()

                 print(f"Hello {user_name}. what would you like?")
                 print('\n') 

                 while True:
                        print("Use thes short codes : cc - create a new_user account with a user_defined password, dc - display credential, fc -find credentials, can -create a new_user account with 
                                "auto-generated password, cad -display all user,  ex -exit ")  
                        short_code = input().lower()

                        if short_code == 'cc':
                            print("user_name")
                            print("-" * 10)
                            print("What account would like to create credentials for?")
                            site = input()
                            print("->->->")
                            
                            print("First name ....")
                            fname = input()

                            print("Last name ...")
                            lname = input()

                            print("Enter username ...")
                            user_name = input()

                            print("Email Address ...")
                            email = input()

                            print("Enter a password")
                            password = input()

                            save_user(create_user(user_name, email, password))
                            save_credentials(create_credentials(fname, lname, user_name, password, email))
                            print("\n")
                            print(f"A new {site} account by {fname} has successfully been created")
                            print(f"The username is {user_name} and the password is {password} ")
                            print("\n")

                        elif short_code ==     
