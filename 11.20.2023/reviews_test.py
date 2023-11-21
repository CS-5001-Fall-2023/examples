from review import Review
from reviews import Reviews


review1 = Review("a", 1, 5.0)
review2 = Review("b", 2, 4.5)
review3 = Review("b", 1, 3.2)

reviews = Reviews()
reviews.add_review(review1)
reviews.add_review(review2)
reviews.add_review(review3)

print(reviews.get_top_rated(2))
