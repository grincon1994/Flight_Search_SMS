from pprint import pprint
import requests


SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/608a048e9dbeb3841217c2527da7461a/copiaDeFlightDeals/prices"

class DataManager:
    def __init__(self):
        self.data_sheet = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.data_sheet = data["prices"]

        print(data)

        return self.data_sheet
    
    def update_destination_code(self):
        for city in self.data_sheet:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)