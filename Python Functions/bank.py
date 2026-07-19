all_accounts = []
import random

def open_account():
    '''
    input: title account, cnic, contact
    this function will open an account in the bank :'''
    print('Welcome to Bank')
    acc_title = input('Enter account title: ')
    cnic = input('Enter Cnic No. ')
    contact = input('Enter Contact No. ')
    initial_deposit = int(input('Initial Deposit: '))
    acc_no = random.randint(10000,10000000)
    account = {'title':acc_title,
              'cnic':cnic,
              'contact':contact,
              'balance':initial_deposit,
              'account_no':acc_no}
    all_accounts.append(account)
    print('Your account opened!')
    print(f'Your account title is {account['title']} & Account no is {account['account_no']}')

def cash_deposit(account_no, amount):
    if amount > 0:
        for acc in all_accounts:
            if acc['account_no'] == account_no:
                acc['balance'] += amount
                print('Amount deposited successfully')
                break
        else:
            print('invalid account no!')
    else:
        print('invalid ammount!')

def balance_check(account_no):
    for acc in all_accounts:
        if acc['account_no'] == account_no:
            print(f'your account balance is Rs: {acc['balance']}')
            break
    else:
        print('invalid account no!')

def cash_withdraw(account_no,amount):
    for acc in all_accounts:
            if (acc['account_no'] == account_no) and (acc['balance']>=amount):
                acc['balance'] -= amount
                print(f'Here is your amount Rs: {amount}')
                break
    else:
        print('Invalid account no / insufficient balance')

def close_account(account_no):
    for i,acc in enumerate(all_accounts):
        if acc['account_no']==account_no:
            print(f'Here is your amount {acc['balance']}')
            acc['balance'] = 0
            del all_accounts[i]
            print('Closed Successfully')
            break
    else:
        print('Invalid Account Number')

def transfer_amt(from_account, amount, to_account):
    for from_acc in all_accounts:
        if from_acc['account_no']==from_account:
            for to_acc in all_accounts:
                if to_acc['account_no']==to_account:
                    pass
                else:
                    print('Invalid to Account Number')
            acc['balance']-=amount
        else:
            print('Invalid From Account Number')