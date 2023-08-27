# from Customer import Customer
# from Restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating) :
        self.customer =  customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
        customer.reviews.append(self)
        restaurant.reviews.append(self)

    def get_rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return Review.all_reviews
    
  
    
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant
    
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