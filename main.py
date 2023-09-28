#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


flight_search = FlightSearch()

data_manager = DataManager()

notification_manager = NotificationManager()

ORIGINAL_CITY = "LON"

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    #print(sheet_data)

    data_manager.data_sheet = sheet_data
    data_manager.update_destination_code()
 

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGINAL_CITY, destination["iataCode"], from_time=tomorrow,to_time=six_month_from_today)


    if flight.price < destination["lowestPrice"]:
        notification_manager.get_notification (
            message=f"Low price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        ) 
