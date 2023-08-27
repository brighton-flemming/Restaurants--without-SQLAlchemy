# from Customer import Customer
# from Restaurant import Restaurant

class Review:
    def __init__(self, customer, restaurant, rating) :
        self._customer =  customer
        self.restaurant = restaurant
        self._rating = int(rating)

    def get_rating(self):
        return self._rating
    
    def get_all_ratings(self):
        rating_list = []
        rating = self._rating
        rating_list.append(rating)
        return rating_list
    
    def get_customer(self):
        return self._customer
    
    def get_restaurant(self):
        return self._restaurant
    
# customer_instance =  Customer("customer_id","John Doe")
# restaurant_instance = Restaurant("restaurant_id", "Restaurant_A")
# review_instance = Review(customer_instance, restaurant_instance, 4)

# rating = review_instance.get_rating()
# print("Rating: ", rating)

# all_ratings = review_instance.get_all_ratings()
# print("All Ratings: ", all_ratings)

# customer = review_instance.get_customer()
# restaurant = review_instance.get_restaurant()
# print("Customer: ", customer)
# print("Restaurant: ", restaurant)