
from Review import Review
class Restaurant:
    def __init__(self, name,review_id, restaurant_id, customer_id):
        self._name = str(name)
        self.review_id = review_id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.reviews = []

    def name(self,restaurant_name):
        restaurant_name = self._name
        return restaurant_name
    
    def customers(restaurant_id, reviews):
        restaurant_reviews = [review for review in reviews if review.restaurant_id == restaurant_id]
        unique_customers = set(reviews.customer_id for review in restaurant_reviews)

        return list(unique_customers)

    def reviews(self):
        review_list = []
        review_list.append(Review.all())
        return review_list
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        
        total_rating = sum(review.rating for review in self.reviews)
        average_rating = total_rating / len(self.reviews)
        return average_rating
    
reviews_data = [
    Restaurant.customers(1, "restaurant_A, customer_1"),
     Restaurant.customers(2, "restaurant_B, customer_2"),
      Restaurant.customers(3, "restaurant_C, customer_3"),
       Restaurant.customers(4, "restaurant_D, customer_4"),
        Restaurant.customers(5, "restaurant_E, customer_5"),
]

    
restaurants_data = [
   Restaurant("restaurant_A","Restaurant A"),
   Restaurant("restaurant_B","Restaurant B"),
   Restaurant("restaurant_C","Restaurant C"),
   Restaurant("restaurant_D","Restaurant D"),
   Restaurant("restaurant_E","Restaurant E"),
]

avg_rating = restaurants_data[0].average_star_rating()
print(f"Average Rating for {restaurants_data[0].name} : {avg_rating:.2f}")

   
        

