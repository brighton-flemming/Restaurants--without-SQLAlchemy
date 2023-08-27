from Review import Review
from Restaurant import Restaurant
from Customer import Customer

restaurants_data = [
   Restaurant("restaurant_A", "Restaurant A"),
   Restaurant("restaurant_B", "Restaurant B"),
   Restaurant("restaurant_C", "Restaurant C"),
   Restaurant("restaurant_D", "Restaurant D"),
   Restaurant("restaurant_E", "Restaurant E")
]

customers_data = [
   Customer("Customer", "1"),
   Customer("Customer", "2"),
   Customer("Customer", "3"),
   Customer("Customer", "4"),
   Customer("Customer", "5")
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

reviews_data = [
    Review("customer_1", "restaurant_A", 4),
    Review("customer_2", "restaurant_C", 5),
    Review("customer_3", "restaurant_E", 3),
    Review("customer_4", "restaurant_B", 2),
    Review("customer_5", "restaurant_D", 5)
]

restaurant_A = restaurants_data[0]
restaurant_B = restaurants_data[1]
restaurant_C = restaurants_data[2]
restaurant_D = restaurants_data[3]
restaurant_E = restaurants_data[4]

for review in reviews_data:
    if review.restaurant == "restaurant_A":
        restaurant_A.reviews.append(review)
    elif review.restaurant == "restaurant_B":
         restaurant_B.reviews.append(review)
    elif review.restaurant == "restaurant_C":
         restaurant_C.reviews.append(review)
    elif review.restaurant == "restaurant_D":
         restaurant_D.reviews.append(review)
    elif review.restaurant == "restaurant_E":
         restaurant_E.reviews.append(review)
      
avg_rating_A = restaurant_A.average_star_rating()
print(f"Average Rating for {restaurant_A.get_name()} : {avg_rating_A:.2f}")

avg_rating_B = restaurant_B.average_star_rating()
print(f"Average Rating for {restaurant_B.get_name()} : {avg_rating_B:.2f}")

avg_rating_C = restaurant_C.average_star_rating()
print(f"Average Rating for {restaurant_C.get_name()} : {avg_rating_C:.2f}")

avg_rating_D = restaurant_D.average_star_rating()
print(f"Average Rating for {restaurant_D.get_name()} : {avg_rating_D:.2f}")

avg_rating_E = restaurant_E.average_star_rating()
print(f"Average Rating for {restaurant_E.get_name()} : {avg_rating_E:.2f}")

customer_instance =  Customer("customer_id","John Doe")
restaurant_instance = Restaurant("restaurant_id", "Restaurant_A")
review_instance = Review(customer_instance, restaurant_instance, 4)

rating = review_instance.get_rating()
print("Rating: ", rating)

all_ratings = review_instance.get_all_ratings()
print("All Ratings: ", all_ratings)

customer = review_instance.get_customer()
restaurant = review_instance.get_restaurant()
print("Customer: ", customer)
print("Restaurant: ", restaurant)
