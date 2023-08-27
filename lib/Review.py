
from Customer import Customer
from Restaurant import Restaurant
class Review:
    def __init__(self, customer, restaurant, rating) :
        self._customer =  customer
        self._restaurant = restaurant
        self._rating = int(rating)

    def rating(self):
        return self._rating
    
    def all(self, rating):
        rating_list = []
        rating = self._rating
        rating_list.append(rating)
        return rating_list
    
    def customer(self):
        self._customer = Customer
        return self._customer
    
    def restaurant(self):
        self._restaurant = Restaurant
        return self._restaurant
    