import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                               QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout)
from mysql_test import get_db_connection

class MiniDBApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini MySQL App")
        self.setGeometry(100, 100, 500, 400)
        
        self.layout = QVBoxLayout()
        
        # Input fields
        input_layout = QHBoxLayout()
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        input_layout.addWidget(self.name_input)
        
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        input_layout.addWidget(self.age_input)
        
        self.add_btn = QPushButton("Add User")
        self.add_btn.clicked.connect(self.add_user)
        input_layout.addWidget(self.add_btn)
        
        self.layout.addLayout(input_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age"])
        self.layout.addWidget(self.table)
        
        self.setLayout(self.layout)
        
        # Load initial data
        self.load_data()
    
    def add_user(self):
        name = self.name_input.text()
        age_text = self.age_input.text()
        
        if not name or not age_text:
            QMessageBox.warning(self, "Input Error", "Please enter both name and age.")
            return
        
        try:
            age = int(age_text)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Age must be a number.")
            return
        
        try:
            db = get_db_connection()
            cursor = db.cursor()
            sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
            cursor.execute(sql, (name, age))
            db.commit()
            db.close()
            
            QMessageBox.information(self, "Success", f"User {name} added successfully!")
            self.name_input.clear()
            self.age_input.clear()
            
            # Refresh table
            self.load_data()
            
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
    
    def load_data(self):
        try:
            db = get_db_connection()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            db.close()
            
            self.table.setRowCount(0)
            for row_number, row_data in enumerate(rows):
                self.table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiniDBApp()
    window.show()
    sys.exit(app.exec())
