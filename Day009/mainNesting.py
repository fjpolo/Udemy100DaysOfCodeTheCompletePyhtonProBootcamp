#
# Imports
#
import random


#
# Global variables
#
capitals = {"France": "Paris", "Germany": "Berlin", "Spain":"Madrid"}
# List inside list
# travel_log = {
#                 "France":["Paris"., "Marseille", "Clermont", "Corsiga"],
#                 "Spain":["Malaga", "Granada", "Cordoba"],
#              }  
# list inside dictionary
# travel_log = {
#                 "France":{"cities_visited":["Paris", "Marseille", "Clermont", "Corsiga"], "total_visits":12},
#                 "Spain":{"cities_visited":["Malaga", "Granada", "Cordoba"], "total_visits":23},
#              }   
# dictionary inside list
travel_log = [
                {
                    "country":"France", 
                    "cities_visited":["Paris", "Marseille", "Clermont", "Corsiga"], 
                    "total_visits":6
                },
                {
                    "country":"Spain", 
                    "cities_visited":["Malaga", "Granada", "Cordoba"], 
                    "total_visits":14
                },
             ]   

#
# Private functions
#



#
# main
#
if __name__ == "__main__":
    print(travel_log)
    # print("France: ", travel_log["France"]["total_visits"])
    # print(travel_log["France"]["cities_visited"])