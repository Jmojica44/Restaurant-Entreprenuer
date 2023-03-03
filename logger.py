
class Logger():
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0
    def log_transaction(self, order, location_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open("log.txt", "a")
        file.write(f' TRX# {self.transaction_count}:  {order.dish_name} at location {location_number} for $ {order.price} . Total: $ {self.daily_sales}')
        file.close()


