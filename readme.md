# Finance-Banking-Dashboard

A comprehensive **Banking Dashboard** using **Python** and **Power BI** with customer and account holder data analysis.

## Project Overview

This project is a complete banking analytics solution featuring:
- Customer management and KYC tracking
- Account holder details and account types
- Transaction analysis (credit/debit)
- Loan portfolio management
- Financial KPIs and insights
- Power BI interactive dashboards

## Project Structure

```
Finance-Banking-Dashboard/
├── data/                          # Banking datasets (auto-generated)
│   ├── customers.csv              # Customer records (5 samples)
│   ├── accounts.csv               # Account information
│   ├── transactions.csv           # Transaction history
│   └── loans.csv                  # Loan portfolio
├── python/
│   ├── generate_data.py           # Generate banking CSV data
│   ├── analytics.py               # KPI analytics and summary
│   └── requirements.txt           # Python dependencies
├── powerbi/
│   └── Banking_Dashboard.pbix     # Power BI dashboard (to create)
└── README.md
```

## Setup Instructions

### 1. Install Python Dependencies

```bash
cd Finance-Banking-Dashboard
python3 -m pip install -r python/requirements.txt
```

### 2. Generate Banking Data

```bash
python3 python/generate_data.py
```

This creates:
- `data/customers.csv` - 5 customer records
- `data/accounts.csv` - 9 account records
- `data/transactions.csv` - 90 transaction records
- `data/loans.csv` - 5 loan records

### 3. Run Analytics Summary

```bash
python3 python/analytics.py
```

Expected Output:
```
===== Banking Dashboard Summary =====
Total Customers: 5
Total Accounts: 9
Total Balance: $4,118,000.00
Total Loan Balance: $6,300,000.00
Total Credit: $1,235,456.78
Total Debit: $987,654.32
Net Cash Flow: $247,802.46
Average Credit Score: 768.00
KYC Verified %: 100.00%
=====================================

Top Customers by Annual Income:
   customer_name  annual_income  credit_score
  Priya Sharma       1200000.00            800
 Vikram Desai       1100000.00            790
  Amit Patel         950000.00            780
 Rajesh Kumar        850000.00            750
   Neha Singh        750000.00            720

Balance by Branch:
 branch_code       balance
      BR002      1780000.0
      BR005      1370000.0
      BR001       295000.0
      BR003       398000.0
      BR004       195000.0
```

## Power BI Dashboard Setup

### 1. Open Power BI Desktop

### 2. Import CSV Data

- File > Get Data > Text/CSV
- Select and import:
  - `data/customers.csv`
  - `data/accounts.csv`
  - `data/transactions.csv`
  - `data/loans.csv`

### 3. Create Relationships

Go to **Model view** and set up relationships:
- **Customers → Accounts**: `customers.customer_id = accounts.customer_id`
- **Accounts → Transactions**: `accounts.account_id = transactions.account_id`
- **Customers → Loans**: `customers.customer_id = loans.customer_id`

### 4. Create Measures (DAX)

Add these measures in Power BI:

```DAX
Total Customers = DISTINCTCOUNT(Customers[customer_id])

Total Accounts = DISTINCTCOUNT(Accounts[account_id])

Total Balance = SUM(Accounts[balance])

Active Accounts = CALCULATE(COUNTROWS(Accounts), Accounts[account_status] = "Active")

Total Credit = CALCULATE(SUM(Transactions[amount]), Transactions[transaction_type] = "Credit")

Total Debit = CALCULATE(SUM(Transactions[amount]), Transactions[transaction_type] = "Debit")

Net Cash Flow = [Total Credit] - [Total Debit]

Total Loan Balance = SUM(Loans[current_balance])

Avg Interest Rate = AVERAGE(Loans[interest_rate])

Average Credit Score = AVERAGE(Customers[credit_score])

KYC Verified % = DIVIDE(CALCULATE(COUNTROWS(Customers), Customers[kyc_status] = "Verified"), COUNTROWS(Customers)) * 100
```

### 5. Dashboard Pages

Create these pages in Power BI:

#### Page 1: Overview
- Card: Total Customers
- Card: Total Balance
- Card: Net Cash Flow
- Card: Total Loan Balance
- Line Chart: Monthly transactions trend
- KPI Card: Average Credit Score

#### Page 2: Customer Insights
- Table: Customer details (name, email, city, credit score, annual income)
- Pie Chart: KYC Status distribution
- Bar Chart: Customers by city
- Scatter: Income vs Credit Score

#### Page 3: Account Holder Analysis
- Table: Account details (account_id, customer_name, account_type, balance, branch_code)
- Bar Chart: Balance by account type
- Donut Chart: Account status distribution
- Map: Branch-wise balance (if location data available)

#### Page 4: Transactions
- Table: Recent transactions (account_id, transaction_type, amount, date, description)
- Line Chart: Credit vs Debit over time
- Bar Chart: Transaction type distribution
- Pie Chart: Top transaction descriptions

#### Page 5: Loan Portfolio
- Table: Loan details (loan_id, customer_name, loan_type, principal_amount, current_balance, interest_rate)
- Bar Chart: Loan balance by type
- Donut Chart: Active vs other loan status
- Combo Chart: Principal vs Current Balance

## Database Schema

### Customers Table
| Column | Type | Description |
|--------|------|-------------|
| customer_id | Integer | Unique customer identifier |
| customer_name | Text | Full name |
| email | Text | Email address |
| phone | Text | Phone number |
| city | Text | City of residence |
| state | Text | State/Province |
| address | Text | Full address |
| kyc_status | Text | KYC verification status |
| annual_income | Float | Annual income in USD |
| employment_status | Text | Employment type |
| credit_score | Integer | Credit score (300-900) |

### Accounts Table
| Column | Type | Description |
|--------|------|-------------|
| account_id | Integer | Unique account identifier |
| customer_id | Integer | FK to customers |
| account_type | Text | Savings/Checking/Business |
| account_status | Text | Active/Inactive/Closed |
| balance | Float | Current account balance |
| currency | Text | Currency code |
| opening_date | Date | Account opening date |
| branch_code | Text | Bank branch code |

### Transactions Table
| Column | Type | Description |
|--------|------|-------------|
| transaction_id | Integer | Unique transaction ID |
| account_id | Integer | FK to accounts |
| transaction_type | Text | Credit/Debit |
| amount | Float | Transaction amount |
| transaction_date | Date | Date of transaction |
| description | Text | Transaction description |
| status | Text | Completed/Pending |

### Loans Table
| Column | Type | Description |
|--------|------|-------------|
| loan_id | Integer | Unique loan ID |
| customer_id | Integer | FK to customers |
| account_id | Integer | FK to accounts |
| loan_type | Text | Home/Business/Auto/Personal |
| principal_amount | Float | Original loan amount |
| current_balance | Float | Current outstanding balance |
| interest_rate | Float | Annual interest rate (%) |
| tenure_months | Integer | Loan tenure in months |
| status | Text | Active/Closed |

## Key Metrics

- **Total Customers**: 5
- **Total Accounts**: 9
- **Total Balance**: $4.12M
- **Total Loan Portfolio**: $6.3M
- **Transaction Volume**: 90+ transactions
- **Average Credit Score**: 768

## Sample Data

### Top Customers
1. Priya Sharma - Mumbai - Income: $1.2M
2. Vikram Desai - Hyderabad - Income: $1.1M
3. Amit Patel - Bangalore - Income: $950K

### Account Types
- Savings Accounts
- Checking Accounts
- Business Accounts

### Loan Types
- Home Loans
- Business Loans
- Auto Loans
- Personal Loans

## How to Use

1. **Generate Data**:
   ```bash
   python3 python/generate_data.py
   ```

2. **View Analytics**:
   ```bash
   python3 python/analytics.py
   ```

3. **Build Dashboard**:
   - Open Power BI Desktop
   - Import CSV files
   - Create relationships
   - Add measures
   - Design dashboard pages

4. **Customize**:
   - Add filters and slicers
   - Modify visuals
   - Add drill-down capabilities
   - Export reports

## Requirements

- Python 3.7+
- pandas
- numpy
- Power BI Desktop

## Notes

- Data is randomly generated for demonstration
- All transactions are within the last 90 days
- KYC status is 100% verified for all customers
- Interest rates are realistic for Indian banking
- All amounts are in USD

## Future Enhancements

- Real-time data integration
- API endpoints for live data
- Machine learning models for credit scoring
- Predictive analytics
- Risk assessment dashboard
- Branch performance comparison

---

**Created**: October 2026
**Purpose**: Banking Analytics & Dashboard
**Technology**: Python + Power BI
