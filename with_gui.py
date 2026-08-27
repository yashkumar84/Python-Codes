import sys
import random
import math
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QTabWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt6.QtCore import Qt

class Transaction:
    def __init__(self, trans_id, trans_amount, trans_type, message):
        self.trans_id = trans_id
        self.trans_amount = trans_amount
        self.trans_type = trans_type
        self.message = message

class Account:
    def __init__(self, acc_number, acc_holder_name, password, balance=0):
        self.acc_number = acc_number
        # Removed the trailing comma from your original code to keep it a string, not a tuple
        self.acc_holder_name = acc_holder_name
        self.balance = balance
        self.password = password
        self.transactions = []
        if balance > 0:
            random_number = math.floor(random.random() * 10000)
            transaction = Transaction(random_number, balance, "Account Opening", "Opening Balance Success")
            self.transactions.append(transaction)

    def deposit(self, balance):
        self.balance += balance
        random_number = math.floor(random.random() * 10000)
        transaction = Transaction(random_number, balance, "Deposit", "Deposit Success")
        self.transactions.append(transaction)
        return f"Deposit Success! New Balance: {self.balance}"

    def withdraw(self, password, balance):
        if self.password != password:
            return "Error: Wrong Password"

        if self.balance < balance:
            return "Error: Insufficient Balance"

        self.balance -= balance
        random_number = math.floor(random.random() * 10000)
        transaction = Transaction(random_number, balance, "Withdraw", "Withdraw Success")
        self.transactions.append(transaction)
        return f"Withdraw Success! Remaining Balance: {self.balance}"

    def get_statement_data(self, password):
        if self.password != password:
            return None, "Error: Wrong Password"
        
        statement = f"Current Balance: {self.balance}\n\n=== Transaction History ===\n"
        for transaction in self.transactions:
            statement += f"[{transaction.trans_type}] Amount: {transaction.trans_amount} (ID: {transaction.trans_id}) - {transaction.message}\n"
        return statement, "Success"

class Bank:
    def __init__(self):
        self.accounts = []

    def createAccount(self, name, password, balance):
        acc_id = math.floor(random.random() * 10000)
        account = Account(acc_id, name, password, balance)
        self.accounts.append(account)
        return acc_id

    def find_account(self, acc_no):
        for account in self.accounts:
            if account.acc_number == acc_no:
                return account
        return None


# === PYQT6 GUI INTERFACE ===
class BankApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bank = Bank()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Secure Desktop Banking Application")
        self.setGeometry(100, 100, 500, 450)

        # Main Tab Widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Initialize tabs
        self.initCreateTab()
        self.initDepositTab()
        self.initWithdrawTab()
        self.initStatementTab()

    def initCreateTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.create_pass_input = QLineEdit()
        self.create_pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.initial_balance = QLineEdit()

        layout.addWidget(QLabel("Account Holder Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Set Password:"))
        layout.addWidget(self.create_pass_input)
        layout.addWidget(QLabel("Initial Deposit Balance:"))
        layout.addWidget(self.initial_balance)

        btn = QPushButton("Create Account")
        btn.clicked.connect(self.handle_create_account)
        layout.addWidget(btn)
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Create Account")

    def initDepositTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.dep_acc_input = QLineEdit()
        self.dep_amt_input = QLineEdit()

        layout.addWidget(QLabel("Account Number:"))
        layout.addWidget(self.dep_acc_input)
        layout.addWidget(QLabel("Deposit Amount:"))
        layout.addWidget(self.dep_amt_input)

        btn = QPushButton("Deposit Money")
        btn.clicked.connect(self.handle_deposit)
        layout.addWidget(btn)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Deposit")

    def initWithdrawTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.with_acc_input = QLineEdit()
        self.with_pass_input = QLineEdit()
        self.with_pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.with_amt_input = QLineEdit()

        layout.addWidget(QLabel("Account Number:"))
        layout.addWidget(self.with_acc_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.with_pass_input)
        layout.addWidget(QLabel("Withdrawal Amount:"))
        layout.addWidget(self.with_amt_input)

        btn = QPushButton("Withdraw Money")
        btn.clicked.connect(self.handle_withdraw)
        layout.addWidget(btn)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Withdraw")

    def initStatementTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.stat_acc_input = QLineEdit()
        self.stat_pass_input = QLineEdit()
        self.stat_pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.statement_display = QTextEdit()
        self.statement_display.setReadOnly(True)

        layout.addWidget(QLabel("Account Number:"))
        layout.addWidget(self.stat_acc_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.stat_pass_input)
        
        btn = QPushButton("View Transactions")
        btn.clicked.connect(self.handle_statement)
        layout.addWidget(btn)
        layout.addWidget(QLabel("Statement Log:"))
        layout.addWidget(self.statement_display)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Transactions")

    # === EVENT HANDLERS ===
    def handle_create_account(self):
        try:
            name = self.name_input.text().strip()
            password = self.create_pass_input.text()
            balance = int(self.initial_balance.text() or 0)
            
            if not name or not password:
                QMessageBox.warning(self, "Input Error", "Name and Password cannot be empty.")
                return

            acc_id = self.bank.createAccount(name, password, balance)
            QMessageBox.information(self, "Success", f"Account created successfully!\nYour Account Number is: {acc_id}")
            
            # Clear inputs
            self.name_input.clear()
            self.create_pass_input.clear()
            self.initial_balance.clear()
        except ValueError:
            QMessageBox.critical(self, "Format Error", "Balance must be a valid number.")

    def handle_deposit(self):
        try:
            acc_no = int(self.dep_acc_input.text())
            amount = int(self.dep_amt_input.text())
            
            account = self.bank.find_account(acc_no)
            if account:
                msg = account.deposit(amount)
                QMessageBox.information(self, "Success", msg)
                self.dep_acc_input.clear()
                self.dep_amt_input.clear()
            else:
                QMessageBox.warning(self, "Not Found", "Account number does not exist.")
        except ValueError:
            QMessageBox.critical(self, "Format Error", "Account and Amount must be numbers.")

    def handle_withdraw(self):
        try:
            acc_no = int(self.with_acc_input.text())
            password = self.with_pass_input.text()
            amount = int(self.with_amt_input.text())

            account = self.bank.find_account(acc_no)
            if account:
                msg = account.withdraw(password, amount)
                if "Error" in msg:
                    QMessageBox.warning(self, "Transaction Failed", msg)
                else:
                    QMessageBox.information(self, "Success", msg)
                    self.with_acc_input.clear()
                    self.with_pass_input.clear()
                    self.with_amt_input.clear()
            else:
                QMessageBox.warning(self, "Not Found", "Account number does not exist.")
        except ValueError:
            QMessageBox.critical(self, "Format Error", "Account and Amount must be numbers.")

    def handle_statement(self):
        try:
            acc_no = int(self.stat_acc_input.text())
            password = self.stat_pass_input.text()

            account = self.bank.find_account(acc_no)
            if account:
                statement, status = account.get_statement_data(password)
                if statement:
                    self.statement_display.setText(statement)
                else:
                    QMessageBox.warning(self, "Access Denied", status)
            else:
                QMessageBox.warning(self, "Not Found", "Account number does not exist.")
        except ValueError:
            QMessageBox.critical(self, "Format Error", "Account number must be a valid integer.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = BankApp()
    ex.show()
    sys.exit(app.exec())
