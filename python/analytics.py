import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

customers = pd.read_csv(os.path.join(DATA_DIR, 'customers.csv'))
accounts = pd.read_csv(os.path.join(DATA_DIR, 'accounts.csv'))
transactions = pd.read_csv(os.path.join(DATA_DIR, 'transactions.csv'))
loans = pd.read_csv(os.path.join(DATA_DIR, 'loans.csv'))


def print_summary():
    total_customers = customers['customer_id'].nunique()
    total_accounts = accounts['account_id'].nunique()
    total_balance = accounts['balance'].sum()
    total_loan_balance = loans['current_balance'].sum()
    total_credit = transactions[transactions['transaction_type'] == 'Credit']['amount'].sum()
    total_debit = transactions[transactions['transaction_type'] == 'Debit']['amount'].sum()
    net_cash_flow = total_credit - total_debit
    avg_credit_score = customers['credit_score'].mean()
    active_kyc = customers[customers['kyc_status'] == 'Verified'].shape[0]
    kyc_percentage = (active_kyc / total_customers) * 100 if total_customers else 0

    print('===== Banking Dashboard Summary =====')
    print(f'Total Customers: {total_customers}')
    print(f'Total Accounts: {total_accounts}')
    print(f'Total Balance: ${total_balance:,.2f}')
    print(f'Total Loan Balance: ${total_loan_balance:,.2f}')
    print(f'Total Credit: ${total_credit:,.2f}')
    print(f'Total Debit: ${total_debit:,.2f}')
    print(f'Net Cash Flow: ${net_cash_flow:,.2f}')
    print(f'Average Credit Score: {avg_credit_score:.2f}')
    print(f'KYC Verified %: {kyc_percentage:.2f}%')
    print('===================================')

    top_customers = customers[['customer_name', 'annual_income', 'credit_score']].sort_values(by='annual_income', ascending=False)
    print('\nTop Customers by Annual Income:')
    print(top_customers.head().to_string(index=False))

    branch_summary = accounts.groupby('branch_code', as_index=False)['balance'].sum().sort_values('balance', ascending=False)
    print('\nBalance by Branch:')
    print(branch_summary.to_string(index=False))


if __name__ == '__main__':
    print_summary()
