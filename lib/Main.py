
from Review import Review
from Restaurant import Restaurant
from Customer import Customer

if __name__ == "__main__":
 
    customer1 = Customer("Donald", "Bean")
    customer2 = Customer("Jane", "Smith")
    customer3 = Customer("Alice", "Bean")
   
    restaurant1 = Restaurant("Tasty Burgers")
    restaurant2 = Restaurant("Pizza Palace")
    restaurant3 = Restaurant("Sushi Haven")

 
    customer1.add_review(restaurant1, 4)
    customer1.add_review(restaurant2, 3)
    customer3.add_review(restaurant1, 5)
    customer2.add_review(restaurant2, 2)
    customer3.add_review(restaurant3, 4)

  
    print(f"{customer1.get_full_name()} has reviewed:")
    for restaurant in customer1.restaurants():
        print(f"- {restaurant.name}")

    print(f"{customer3.get_full_name()} has reviewed:")
    for restaurant in customer3.restaurants():
        print(f"- {restaurant.name}")
     
    print(f"{customer2.get_full_name()} has reviewed:")
    for restaurant in customer2.restaurants():
        print(f"- {restaurant.name}")

    print(f"{restaurant1.name} has been reviewed by:")
    for customer in restaurant1.get_customers():
        print(f"- {customer.get_full_name()}")
     
    print(f"{restaurant3.name} has been reviewed by:")
    for customer in restaurant3.get_customers():
        print(f"- {customer.get_full_name()}")
     
    print(f"{restaurant2.name} has been reviewed by:")
    for customer in restaurant2.get_customers():
        print(f"- {customer.get_full_name()}")


    print(f"Average rating for {restaurant2.name}: {restaurant2.average_star_rating()}")
    print(f"Average rating for {restaurant1.name}: {restaurant1.average_star_rating()}")
    print(f"Average rating for {restaurant3.name}: {restaurant3.average_star_rating()}")


