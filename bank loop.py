from datetime import datetime
PIN =1234
balance=10000
transactions = []

while True:
    print('Welcome to SBI')
    print('Insert your ATM Card')
    inserted=int(input('1-Yes,0-No :'))

    if inserted == 1:
        user_pin=int(input('Enter your PIN :'))
        if user_pin ==PIN:
            print('''
                Available Languages:
                1.English
                2.Hindi
                       ''')
        language=int(input('Select any one of the languages above :'))
        
        print('''
              1.Deposit
              2.Withdrawal
              3.balance Check /Mini Statement)
              4.PIN Change
              ''')
        option=int(input('Select any one of the options above :'))
        if option ==1:
            amount =int(input('Feed the cash:'))
            if amount % 100 ==0:
                print('Cash has been accepted')
                balance += amount
                transactions.append(amount)
            else:
                print('Invalid Cash / Feed only multiples of hundred')
        elif option ==2:
            amount = int(input('Enter the amount:'))
            if amount<balance and amount % 100 == 0:
                print('Collect the cash')
                balance -= amount
                transactions.append(-amount)
            else:
                print('No Balance / Cash is not available')
        elif option ==3:
            datetime = datetime.now()
            date = datetime.strftime('%d/%m/%Y')
            time = datetime.strftime('%I:%M %p')
            
            print(
                f'''
                    State  Bank of India 
    Date: {date}                                    Time: {time}
    
    Transactions:
    
                 '''               
            )
            for transaction in transactions:
                print(transaction)
            print('Balance :',balance)
            
            
        elif option ==4:
            old_pin = int(input('Enter your Old PIN'))
            if old_pin == PIN:
                new_pin = int(input('Enter your New PIN'))
                PIN = new_pin
            else:
                print('Invalid PIN / Try again')
        else:
            print("You've selected invalid option")