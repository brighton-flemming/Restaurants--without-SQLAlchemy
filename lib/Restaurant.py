
# from Review import Review
class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = str(name)
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name
    
    def get_customers(self):
        unique_customers = set(review.customer for review in self.reviews)
        return list(unique_customers)
    
  

    def get_reviews(self):
        return self.reviews
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        
        total_rating = sum(review.rating for review in self.reviews)
        average_rating = total_rating / len(self.reviews)
        return average_rating
    


   
        

