# Cashless Society: Managing Privacy and Security in the Technological Age

A Django web application that demonstrates transaction management, spending summaries, privacy preferences, and encryption of transaction notes.


### 1. Project Overview

As digital payments become more common, users need to understand how
transaction information is recorded, stored, and protected. The purpose
of **Cashless Society** is to demonstrate these concepts through a small
web application.

Users can create an account, sign in, record sample transactions, view
their transaction history and spending summary, try an encryption
demonstration, and manage privacy preferences.

The project brings together core Django concepts such as authentication,
forms, models, database queries, templates, URL routing, and separating
features into apps. It also demonstrates authenticated encryption for
transaction-note data.


### 2. Features
## User registration and login

Users can create an account and sign in to access protected pages.
Django's authentication system is used to authenticate users and manage
sessions.

## Transaction management

Signed-in users can enter a transaction amount, merchant name, and
optional note. The transaction is associated with the current user and
timestamped when saved.

## Transaction history

The transaction list displays the current user's saved transactions,
including the time, merchant, amount, and encrypted-note field.

## Spending dashboard

The dashboard calculates the total recorded spending and number of
transactions for the signed-in user. It also prepares merchant-level
spending data for a chart.

## Encryption demonstration

The security demo encrypts a sample memo and decrypts it again to
illustrate the process. Transaction notes are encrypted using AES in EAX
mode through the PyCryptodome library.

## Privacy preferences

Users can save preferences for consent, data sharing, and a
data-retention period. These settings demonstrate privacy-related data
modelling; their existence alone should not be interpreted as a complete
legal compliance or automatic data-deletion system.

## Web interface

The application uses Django templates, HTML, CSS, and Bootstrap-based
styling for its pages, including the dashboard, transaction forms,
history, encryption demo, and privacy settings.


### 3.High-level flow
``` text
User
  |
  v
Register / Login
  |
  v
Django authenticated session
  |
  +--------------------+
  |                    |
  v                    v
Create transaction   Dashboard / History
  |
  v
Encrypt optional note
  |
  v
Save transaction in database
  |
  v
View user-specific transaction records
```


### 4.Technologies Used
- Python
- Django
- HTML, CSS, Bootstrap
- SQLite
- PyCryptodome
- Chart.js
- Git and GitHub

### 5.How It Works
1. Users register and log in.
2. Users add sample transactions.
3. Transaction notes are encrypted before being stored.
4. Users view their transaction history and spending summary.
5. Users can try the encryption demo and update privacy preferences.

### 6.Installation

```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

### 7.Important Note
This is an academic project for learning and demonstration. It does not process real payments or connect to bank accounts. Use sample data only.

### Author
**Kuruva Rajasekhar**

GitHub: https://github.com/rajasekharkuruva583-source