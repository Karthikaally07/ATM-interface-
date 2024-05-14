import time 
print("Please Insert ATM CARD : ")
time.sleep(6)
password = 1234
pin = int(input("Enter your Secret PIN : "))
balance = 5000

if pin==password:
    while True:
       
        print("""
           1 == Balance
           2 == Withdraw Balance
           3 == Deposit Balance 
           4 == Exit
           """)
        try:
            option = int(input("Enter your Choice :"))   
        except:
            print("Enter valid option : ")

        if option==1 :
              print(f"Current balance {balance}")    
        if option==2 :
              withdraw = int(input("Enter Withdraw amount : "))
              Balance =  balance - withdraw
              print("The Debited amount from your Account is:", withdraw) 
              print("The Updated Balance of your Account is :", Balance)
        if option==3 :
              deposit = int(input("Enter the Deposited amount :"))
              Balance = balance + deposit 
              print("The Credited amount to your account is : ", deposit )
              print("The Updated Balance of your Account is : ", Balance )
        if option==4 :
               break 

else:
    print("Try Again ! ")       
