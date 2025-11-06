import tkinter as tk
from tkinter import filedialog
import csv

#function to open the dialog box
#you will choose the fule locationa nd fuledialog

def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

choose_file()
#Function that will read the CSV file
def read_file(file_path):
    if file_path:
        with open(file_path, mode = "r", newline ='', encoding = 'utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    else: 
        print("No file selected.")

#Count the rows and columns
def count_rows_columns(file_path):
    with open(file_path, mode = "r", newline ='', encoding = 'utf-8') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        num_rows = len(rows)
        num_columns = len(rows[0]) if num_rows > 0 else 0
    return num_rows, num_columns

file_path = choose_file() #prompt user to choose file
read_file(file_path) #read and display the content of the csv
print(choose_file)

