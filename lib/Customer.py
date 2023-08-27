from Review import Review
# from Restaurant import Restaurant

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
     
    def change_family_name(self, new_family_name):
       self.family_name = new_family_name


    def get_full_name(self, person_name):
        person_name = print(f"{self.get_given_name()}  {self.get_family_name()}")
        return person_name
    
    def __str__(self):
       return f" {self.get_given_name()} {self.get_family_name()}"
    
    def all(self):
       customer_list = []
       customer = self.get_full_name()
       customer_list.append(customer)
       return customer_list
    
    def add_review(self, restaurant, rating):
       review_id = len(self.reviews) + 1
       review = Review(review_id, restaurant, rating)
       self.reviews.append(review)
       restaurant.reviews.append(review)

    def num_reviews(self):
       return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
       for customer in cls.all_customers:
          if customer.name == name:
             return customer
       return None
          
    @classmethod
    def find_by_family_name(cls,family_name):
       for customer in cls.all_customers:
          if customer.family_name == family_name:
             return customer
       return None
       
    
    def restaurants(self):
       reviewed_restaurants = set(review.restaurant.name for review in self.reviews)
       return list(reviewed_restaurants)
    
