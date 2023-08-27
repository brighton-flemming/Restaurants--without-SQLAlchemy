from Review import Review

class Customer:
    all_customers = []

    def __init__(self, first_name, family_name):
     self.first_name = first_name
     self.family_name = family_name
     self.reviews = []
     Customer.all_customers.append(self)

    def get_given_name(self):
       return self.first_name
     
    def get_family_name(self):
      return self.family_name
     
 
    def get_full_name(self):
        return f"{self.get_given_name()}  {self.get_family_name()}"
         
    
    def all(self):
      return Customer.all_customers
    
    def add_review(self, restaurant, rating):
      review = Review(self, restaurant, rating)
      self.reviews.append(review)

    def num_reviews(self):
       return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, first_name):
       for customer in cls.all_customers:
          if customer.first_name == first_name:
             return customer
       return None
          
    @classmethod
    def find_by_family_name(cls,family_name):
       return [customer for customer in cls.all_customers if customer.family_name == family_name]
    
    def restaurants(self):
       reviewed_restaurants = set(review.restaurant for review in self.reviews)
       return list(reviewed_restaurants)
    
