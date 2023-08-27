
from Review import Review
from Restaurant import Restaurant
from Customer import Customer

if __name__ == "__main__":
 
    customer1 = Customer("Donald", "Bean")
    customer2 = Customer("Jane", "Smith")

   
    restaurant1 = Restaurant("Tasty Burgers")
    restaurant2 = Restaurant("Pizza Palace")

 
    customer1.add_review(restaurant1, 4)
    customer1.add_review(restaurant2, 3)

    customer2.add_review(restaurant1, 5)
    customer2.add_review(restaurant2, 2)

  
    print(f"{customer1.get_full_name()} has reviewed:")
    for restaurant in customer1.restaurants():
        print(f"- {restaurant.name}")

    print(f"{restaurant1.name} has been reviewed by:")
    for customer in restaurant1.get_customers():
        print(f"- {customer.get_full_name()}")

    print(f"Average rating for {restaurant2.name}: {restaurant2.average_star_rating()}")
    print(f"Average rating for {restaurant1.name}: {restaurant1.average_star_rating()}")
    


