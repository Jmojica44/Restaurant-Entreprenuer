from pizza import Pizza
from pasta import Pasta
from salad import Salad


choice_dictionary = {
    1: 'Pizza',
    2: 'Pasta',
    3: 'Salad'
}
class OrderFactory():
   
    @staticmethod
    def create_order(choice): 
        if choice == 1:
            return Pizza()
        elif choice == 2:
            return Pasta()
        elif choice == 3:
            return Salad()
        else:
            print("Invalid choice")
            choice = int(input("What food would you like? Type '1' for Pizza, '2' for Pasta, or '3' for Salad: "))



