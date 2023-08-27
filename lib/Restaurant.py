
from Review import Review
class Restaurant:
    def __init__(self, name,review_id, restaurant_id, customer_id):
        self._name = str(name)
        self.review_id = review_id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id

    def name(self,restaurant_name):
        restaurant_name = self._name
        return restaurant_name
    
    def customers(restaurant_id, reviews):
        restaurant_reviews = [review for review in reviews if review.restaurant_id == restaurant_id]
    
    def reviews(self):
        review_list = []
        review_list.append(Review.all())
        return review_list
    
   
        

