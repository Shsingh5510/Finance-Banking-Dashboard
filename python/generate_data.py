import pandas as pd
from datetime import datetime, timedelta
import random
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

customers = [
    {
        'customer_id': 1,
        'customer_name': 'Rajesh Kumar',
        'email': 'rajesh.kumar@email.com',
        'phone': '9876543210',
        'city': 'Delhi',
        'state': 'Delhi',
        'address': '123 Market Street',
        'kyc_status': 'Verified',
        'annual_income': 850000,
        'employment_status': 'Employed',
        'credit_score': 750,
    },
    {
        'customer_id': 2,
        'customer_name': 'Priya Sharma',
        'email': 'priya.sharma@email.com',
        'phone': '9876543211',
        'city': 'Mumbai',
        'state': 'Maharashtra',
        'address': '456 Park Avenue',
        'kyc_status': 'Verified',
        'annual_income': 1200000,
        'employment_status': 'Self-Employed',
        'credit_score': 800,
    },
    {
        'customer_id': 3,
        'customer_name': 'Amit Patel',
        'email': 'amit.patel@email.com',
        'phone': '9876543212',
        'city': 'Bangalore',
        'state': 'Karnataka',
        'address': '789 River Road',
        'kyc_status': 'Verified',
        'annual_income': 950000,
        'employment_status': 'Employed',
        'credit_score': 780,
    },
    {
        'customer_id': 4,
        'customer_name': 'Neha Singh',
        'email': 'neha.singh@email.com',
        'phone': '9876543213',
        'city': 'Pune',
        'state': 'Maharashtra',
        'address': '321 Mall Street',
        'kyc_status': 'Verified',
        'annual_income': 750000,
        'employment_status': 'Employed',
        'credit_score': 720,
    },
    {
        'customer_id': 5,
        'customer_name': 'Vikram Desai',
        'email': 'vikram.desai@email.com',
        'phone': '9876543214',
        'city': 'Hyderabad',
        'state': 'Telangana',
        'address': '654 Plaza Way',
        'kyc_status': 'Verified',
        'annual_income': 1100000,
        'employment_status': 'Employed',
        'credit_score': 790,
    },
]

accounts = [
    {'account_id': 101, 'customer_id': 1, 'account_type': 'Savings', 'account_status': 'Active', 'balance': 250000, 'currency': 'USD', 'opening_date': '2022-01-15', 'branch_code': 'BR001'},
    {'account_id': 102, 'customer_id': 1, 'account_type': 'Checking', 'account_status': 'Active', 'balance': 45000, 'currency': 'USD', 'opening_date': '2022-02-20', 'branch_code': 'BR001'},
    {'account_id': 103, 'customer_id': 2, 'account_type': 'Savings', 'account_status': 'Active', 'balance': 580000, 'currency': 'USD', 'opening_date': '2022-03-20', 'branch_code': 'BR002'},
    {'account_id': 104, 'customer_id': 2, 'account_type': 'Business', 'account_status': 'Active', 'balance': 1200000, 'currency': 'USD', 'opening_date': '2022-04-10', 'branch_code': 'BR002'},
    {'account_id': 105, 'customer_id': 3, 'account_type': 'Savings', 'account_status': 'Active', 'balance': 320000, 'currency': 'USD', 'opening_date': '2022-06-10', 'branch_code': 'BR003'},
    {'account_id': 106, 'customer_id': 3, 'account_type': 'Checking', 'account_status': 'Active', 'balance': 78000, 'currency': 'USD', 'opening_date': '2022-07-05', 'branch_code': 'BR003'},
    {'account_id': 107, 'customer_id': 4, 'account_type': 'Savings', 'account_status': 'Active', 'balance': 195000, 'currency': 'USD', 'opening_date': '2023-01-05', 'branch_code': 'BR004'},
    {'account_id': 108, 'customer_id': 5, 'account_type': 'Savings', 'account_status': 'Active', 'balance': 420000, 'currency': 'USD', 'opening_date': '2023-02-14', 'branch_code': 'BR005'},
    {'account_id': 109, 'customer_id': 5, 'account_type': 'Business', 'account_status': 'Active', 'balance': 950000, 'currency': 'USD', 'opening_date': '2023-03-01', 'branch_code': 'BR005'},
]

transactions = []
for account_id in [101, 102, 103, 104, 105, 106, 107, 108, 109]:
    for i in range(10):
        trans_date = datetime.now() - timedelta(days=random.randint(1, 90))
        trans_type = random.choice(['Credit', 'Debit'])
        amount = round(random.uniform(500, 25000), 2)
        description = random.choice([
            'Salary', 'ATM Withdrawal', 'Bill Payment', 'Online Purchase',
            'Utility Payment', 'Client Transfer', 'Insurance', 'Mobile Recharge'
        ])
        transactions.append({
            'transaction_id': len(transactions) + 1,
            'account_id': account_id,
            'transaction_type': trans_type,
            'amount': amount,
            'transaction_date': trans_date.strftime('%Y-%m-%d'),
            'description': description,
            'status': 'Completed'
        })

loans = [
    {'loan_id': 1, 'customer_id': 1, 'account_id': 101, 'loan_type': 'Home Loan', 'principal_amount': 2000000, 'current_balance': 1800000, 'interest_rate': 6.5, 'tenure_months': 240, 'status': 'Active'},
    {'loan_id': 2, 'customer_id': 2, 'account_id': 103, 'loan_type': 'Business Loan', 'principal_amount': 500000, 'current_balance': 450000, 'interest_rate': 8.0, 'tenure_months': 60, 'status': 'Active'},
    {'loan_id': 3, 'customer_id': 3, 'account_id': 105, 'loan_type': 'Auto Loan', 'principal_amount': 800000, 'current_balance': 650000, 'interest_rate': 7.5, 'tenure_months': 84, 'status': 'Active'},
    {'loan_id': 4, 'customer_id': 4, 'account_id': 107, 'loan_type': 'Personal Loan', 'principal_amount': 300000, 'current_balance': 200000, 'interest_rate': 9.0, 'tenure_months': 36, 'status': 'Active'},
    {'loan_id': 5, 'customer_id': 5, 'account_id': 108, 'loan_type': 'Business Loan', 'principal_amount': 1500000, 'current_balance': 1400000, 'interest_rate': 7.8, 'tenure_months': 120, 'status': 'Active'},
]

pd.DataFrame(customers).to_csv(os.path.join(DATA_DIR, 'customers.csv'), index=False)
pd.DataFrame(accounts).to_csv(os.path.join(DATA_DIR, 'accounts.csv'), index=False)
pd.DataFrame(transactions).to_csv(os.path.join(DATA_DIR, 'transactions.csv'), index=False)
pd.DataFrame(loans).to_csv(os.path.join(DATA_DIR, 'loans.csv'), index=False)

print('Generated files:')
print(' -', os.path.join(DATA_DIR, 'customers.csv'))
print(' -', os.path.join(DATA_DIR, 'accounts.csv'))
print(' -', os.path.join(DATA_DIR, 'transactions.csv'))
print(' -', os.path.join(DATA_DIR, 'loans.csv'))
