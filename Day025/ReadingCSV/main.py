
#
# Imports
#
import os
from turtle import Turtle, Screen
import csv
import pandas as pd



#
# Classes
#

#
# Global variables
#

#
# Private functions
#

# clear_console
def clear_console():
    """
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    # Read CSV
    with open("Day025/ReadingCSV/weather_data.csv") as data_file:
        # RAW
        # data = data_file.readline()
        
        # CSV
        # temperature = []
        # data = csv.reader(data_file)
        # for row in data:
        #     if row[1] != 'temp':
        #         temperature.append(int(row[1]))
        # print(temperature)

        # Pandas
        data = pd.read_csv("Day025/ReadingCSV/weather_data.csv")
        # print(data["temp"])
        data_dict = data.to_dict()
        # print(data_dict)
        temp_list = data["temp"].to_list
        # print(temp_list)
        # print(sum(temp_list)/len(temp_list))
        # print(data["temp"].mean())
        # print(data["temp"].max())
        # print(data["temp"].min())
        
        # Get data in columns
        # print(data.condition)

        # Get data in rows
        # print(data[data.day == "Monday"])
        # print(data[data.temp == data.temp.max()])

        #
        monday = data[data.day == 'Monday']
        # print(monday.condition)
        monday_temp = int(monday.temp)
        monday_temp *= (9/5)
        monday_temp += 32
        # print(f"Monday temp {monday_temp}[F]")

        # new dataframe
        data_dict = {
            "students": ["Jorge", "Juana", "Ana", "Banana"],
            "scores": [77, 66, 99, 11]
        }
        data = pd.DataFrame(data_dict)
        data.to_csv("Day025/ReadingCSV/new_data.csv")
