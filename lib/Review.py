class Review:
    def __init__(self, customer, restaurant, rating) :
        self._customer =  customer
        self._restaurant = restaurant
        self._rating = int(rating)

    def rating(self):
        return self._rating
    
    def all(self, rating):
        rating_list = []
        rating = self._rating
        rating_list.append(rating)
        return rating_list