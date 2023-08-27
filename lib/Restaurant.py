
from Review import Review
class Restaurant:
    def __init__(self, name, restaurant_id):
        self._name = str(name)
        # self.review_id = review_id
        self.restaurant_id = restaurant_id
        # self.customer_id = customer_id
        self.reviews = []

    def get_name(self):
        return self._name
    
    def get_customers(self):
        unique_customers = set(review.customer_id for review in self.reviews)
        return list(unique_customers)

    def get_reviews(self):
        return self.reviews
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        
        total_rating = sum(review.rating for review in self.reviews)
        average_rating = total_rating / len(self.reviews)
        return average_rating
    
reviews_data = [
    Review("customer_1","restaurant_A", 4),
     Review("customer_2","restaurant_A", 5),
      Review("customer_3","restaurant_A", 3),
       Review("customer_4","restaurant_A", 2),
        Review("customer_5","restaurant_A", 5),
    
]

    
restaurant_A = Restaurant("restaurant_A","Restaurant A"),
restaurant_B = Restaurant("restaurant_B","Restaurant B"),
restaurant_C = Restaurant("restaurant_C","Restaurant C"),
restaurant_D = Restaurant("restaurant_D","Restaurant D"),
restaurant_E = Restaurant("restaurant_E","Restaurant E"),

for review in reviews_data:
    if review.restaurant_id == "restaurant_A":
        restaurant_A.reviews.append(review)
    elif  review.restaurant_id == "restaurant_B":
         restaurant_B.reviews.append(review)
    elif  review.restaurant_id == "restaurant_C":
         restaurant_C.reviews.append(review)
    elif  review.restaurant_id == "restaurant_D":
         restaurant_D.reviews.append(review)
    elif  review.restaurant_id == "restaurant_E":
         restaurant_E.reviews.append(review)
      

avg_rating_A = restaurant_A.average_star_rating()
print(f"Average Rating for {restaurant_A.get_name} : {avg_rating_A:.2f}")

   
        

