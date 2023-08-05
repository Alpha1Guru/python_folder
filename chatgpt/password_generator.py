import random
import string
import pyclip
from verifier import verint as vi

print(""" 
Welcome user

I'm your personal password generator!

I'll generate your passwords for you

No need to wreck your brain creating passwords again

I'll save you that stress!
""")
response = input("""Want to generate some password (yes/no): """)
while True:
    if response.lower() == 'yes':
        name = input(" In which account will you use the password? (e.g avast1021@yahoo.com, proton vpn account,etc): ") 
        for char in name:
            if char in ("?","\\","/","*","\'","\"","<",">","|"):
                name = name.replace(char,"")
        filename = "_".join(name.split()) + ".txt"
        filepath = "C:/Users/DELL/Documents/github/python_folder/chatgpt/generatedpasswords/" + filename
        length = int(vi(input("How long would you want your password to be (give me an integer number): ")))
        complexity = input("Enter the complexity of the password (low, medium, high): ")
        while complexity.lower() not in ("low","medium","high"):
            print("Invalid complexity!")
            complexity = input(f"Please give me a valid complexity (low, medium, high): ")
        if complexity == "low":
            chars = string.ascii_lowercase
        elif complexity == "medium":
            chars = string.ascii_letters + string.digits
        elif complexity == "high":
            chars = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(random.choice(chars) for i in range(length))
        pyclip.copy(password)
        message = name + "\n" + "-"*len(name) + "\n" + password
        # message = f""""""
        print(f"""Your "{name}" password is: {password}
        Your password can be found in {filepath}
        NO need to copy password it is already in your clip board""")
        save_password = input("\nWant to save your password?: ")
        while save_password.lower() not in ("yes","no"):
            print("Didn't catch that")
            save_password = input("\nWant to save your password?: ")
            if save_password.lower() == "yes":
                with open(filepath,'x') as passfile:
                    passfile.write(message)
            else:
                print("Done")
    elif response.lower() == "no":
        print(f"Thanks for using password generator Bye!!")
        exit()
    else:
            print("Didn't catch that!")
    response = input("Want to generate another? ")    

