from order_factory import OrderFactory
from logger import Logger

class Franchise():
    def __init__(self, location_number):
        self.location_number = location_number
    def place_order(self):
            choice = int(input("What food would you like? Type '1' for Pizza, '2' for Pasta, or '3' for Salad: "))
            OrderFactory.create_order(choice)
            Logger.log_transaction(choice, self.location_number)
           