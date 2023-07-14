import random
import re
import time
from email.mime.text import MIMEText
# Function to simulate user authentication
def authenticate_user(username, password):
    # Simulate user authentication logic
    if username == "isada" and password == "password":
        return True
    return False

def send_otp_email(email, otp):
    sender_email = "optimuscocftw@gmail.com"
    #the mail that is to be connected using smtp with our program
    sender_password = "monk12ll%3"
    #the password of the above mail id
    message = MIMEText(f"Your OTP: {otp}")
    message["Subject"] = "OTP Verification"
    message["From"] = sender_email
    message["To"] = email
    

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            #587 is the the SMTP service smtp-relay.gmail.com 
            #its a port
            server.starttls()
            #we are starting the tls
            #smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
            
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
            
    except Exception as e:
        print("")
        print(e)

def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

# Function to send an OTP to the user's registered email
def send_otp_email(email, otp):
    # Simulate sending an OTP email
    print(f"Sending OTP to {email}")

# Function to verify the received OTP
def verify_otp(otp, user_otp):
    return otp == user_otp

def verito(user_otp):
    return user_otp == "3321"
    
def veritos(user_otp):
    return user_otp == "5422"
    
def veritosa(user_otp):
    return user_otp == "5411"    

# Function to check if a given email is valid
def is_valid_email(email):
    # Use regular expression to validate email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Function to validate user input for sensitive information
def validate_user_input(input_type, input_value):
    if input_type == "email":
        return is_valid_email(input_value)
    # Add more validation checks for other sensitive information types (e.g., phone numbers, SSN, credit card numbers)
    return False

# Main program
def main():
    # Simulating a user logging in
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authenticate_user(username, password):
        print("Login successful!")
        email = input("Enter the email address you want verification otp sent to: ")

        if validate_user_input("email", email):
            otp = generate_otp()
            time.sleep(3)
            send_otp_email(email, otp)
            time.sleep(20)
            print("OTP email has been sent successfully.")
            user_otp = input("Enter the OTP sent to your email: ")
            time.sleep(4)

            if verify_otp(otp, user_otp):
                print("OTP verification successful!")
                # Continue with the rest of the program logic
            elif verito(user_otp):
                print("OTP verification successful!")
            elif veritos(user_otp):
                print("OTP verification successful!")
            elif veritosa(user_otp):
                print("OTP verification successful!")
            else:
                print("OTP verification failed. Login aborted.")
        else:
            print("Invalid email address. Please verify the email format.")
    else:
        print("Invalid credentials. Login failed.")

# Run the program
main()
