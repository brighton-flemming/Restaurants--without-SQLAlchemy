from Review import Review
from Restaurant import Restaurant

class Customer:
    all_customers = []

    def __init__(self, first_naame, family_name):
     self._first_name = first_naame
     self._family_name = family_name
     self.reviews = []
     Customer.all_customers.append(self)

    def given_name(self):
       return self._first_name
     
    def family_name(self):
      return self._family_name
     
    def change_family_name(self, new_family_name):
       self._family_name = new_family_name

    def full_name(self, person_name):
        person_name = print(f"{self.given_name()}  {self.family_name()}")
        return person_name
    
    def all(self):
       customer_list = []
       customer = self.full_name()
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
    
restaurants_data = [
   Restaurant("restaurant_A","Restaurant A"),
   Restaurant("restaurant_B","Restaurant B"),
   Restaurant("restaurant_C","Restaurant C"),
   Restaurant("restaurant_D","Restaurant D"),
   Restaurant("restaurant_E","Restaurant E"),
]

customers_data = [
   Customer("Customer", "1"),
    Customer("Customer", "2"),
     Customer("Customer", "3"),
      Customer("Customer", "4"),
       Customer("Customer", "5"),
]

customers_data[0].add_review(restaurants_data[3], 4)
customers_data[3].add_review(restaurants_data[1], 3)
customers_data[4].add_review(restaurants_data[2], 1)
customers_data[1].add_review(restaurants_data[4], 2)
customers_data[2].add_review(restaurants_data[0], 5)
customers_data[0].add_review(restaurants_data[1], 4)
customers_data[0].add_review(restaurants_data[4], 1)
customers_data[2].add_review(restaurants_data[2], 3)
customers_data[1].add_review(restaurants_data[3], 2)
customers_data[2].add_review(restaurants_data[0], 5)

print(customers_data[0].restaurants())
print(customers_data[1].restaurants())
print(customers_data[2].restaurants())
print(customers_data[3].restaurants())
print(customers_data[4].restaurants())
