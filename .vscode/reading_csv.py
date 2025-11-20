import tkinter as tk
from tkinter import filedialog
import csv
import statistics

# Define the lists to store data
restaurants = []
items = []
types = []
serving_sizes = []
calories = []
fats = []
sodiums = []
sugars = []

list_data = []
unique_restaurants = set()

# Read the CSV file and store the data into lists

def choose_file():
    root = tk.Tk()
    root.withdraw()  #Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    #print(file_path)
    return file_path

def read_csv(file_name):
    with open(file_name, newline='', mode='r', encoding='utf=8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            restaurants.append(row['restaurant'])
            items.append(row['item'])
            types.append(row['type'])
            serving_sizes.append(float(row['serving_size']))
            calories.append(int(row['calories']))
            fats.append(float(row['fat']))
            sodiums.append(float(row['sodium']))
            sugars.append(float(row['sugars']))
            
            list_data.append(row)
            unique_restaurants.add(row['restaurant'])
            #print(unique_restaurants)
        
def calculateAverages(list_of_values):
    average = sum(list_of_values)/len(list_of_values)
    return average

def calculateMean(list_of_values):
    return statistics.mean(list_of_values)

def calc_st_dev(list_of_values):
    return statistics.stdev(list_of_values)

def zscores(list_of_values):
    zScores = []
    mean = calculateMean(list_of_values)
    st_dev = calc_st_dev(list_of_values)
    
    for i in list_of_values:
        z_score = (i - mean) / st_dev
        zScores.append(z_score)

def countItems(list_of_values):
    return len(list_of_values)
    
def max_value(list_of_values):
    return max(list_of_values)
    
def min_value(list_of_values):
    return min(list_of_values)

def sugars_per_resaurant(list_of_values, restaurant_name):
    sugars_per=[]
    for i in range(len(restaurants)):
        if (restaurants[i] == restaurant_name):
            sugars_per.append(sugars[i])
    return sum(sugars_per)
            

def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    #read_file(file_path)
    read_csv(file_path)
if __name__ == '__main__':
    main()

print(restaurants)
print(calories)
print(fats)

def findFatInRestaurant(restaurant_name):
    fats_in_restaurant = []
    for i in range(len(restaurants)):
        if (restaurants[i] == restaurant_name):
            fats_in_restaurant.append(fats[i])
    return fats_in_restaurant
findFatInRestaurant("Burger King")

#Average Calories
average_calories = calculateAverages(calories)
print("Average Calories:", average_calories)

#Calculate the number of items per list
count_calories = countItems(calories)
print("Calorie Items Count:", count_calories)

#Calculate the highest value per list
max_calories = max_value(calories)
print("Max Calories:", max_calories)

#Calculate the lowest value per list
min_calories = min_value(calories)
print("Min Calories:", min_calories)

#Average Sugars
average_sugars = calculateAverages(sugars)
print("Average Sugars:", average_sugars)

#Calculate the number of items per list
count_sugars = countItems(sugars)
print("Sugars Items Count:", count_sugars)

#Calculate the highest value per list
max_sugars = max_value(sugars)
print("Max Sugars:", max_sugars)

#Calculate the lowest value per list
min_sugars = min_value(sugars)
print("Min Sugars:", min_sugars)


#Sugar per restaurant
def sugars_per_restaurant(sugars, restaurant_name):
   sugars_per = []
   for i in range(len(restaurants)):
        if (restaurants[i] == restaurant_name):
            sugars_per.append(sugars[i])
   return sum(sugars_per)
sugars_per_restaurant(sugars, "McDonald's")

def restaurants_sugar_report():
    report = {} #dictionary to bold restaurant:sugar total pairs
    for restaurant in unique_restaurants:
        total_sugars = 0
        for i in range (len(restaurants)):
            if restaurants[i] == restaurant:
                total_sugars += sugars[i]
        report[restaurant] = total_sugars
        
    return report



#Print a report of all restaurnats and the sum of theur sugars
print("\nList of restairants and their total sugars:\n")
report = restaurants_sugar_report()
for result in report:
    print(result, ":", report[result])
print("\n")

#Finds the sum of sugars per restaurant

"""
List of all items:
[restaurant, item, type, serving size, sodium, fat]
[0][[0],[1],[2],[3]...]
[1][[0],[1],[2],[3]...]
"""