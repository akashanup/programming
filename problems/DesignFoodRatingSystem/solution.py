from typing import List
from sortedcontainers import SortedSet


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRatings = {}
        self.foodCuisines = {}
        self.cuisineFoods = {}

        for i in range(len(foods)):
            self.foodRatings[foods[i]] = ratings[i]
            self.foodCuisines[foods[i]] = cuisines[i]
            if cuisines[i] not in self.cuisineFoods:
                self.cuisineFoods[cuisines[i]] = SortedSet()
            self.cuisineFoods[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodCuisines[food]
        initialItem = (-self.foodRatings[food], food)
        self.cuisineFoods[cuisine].remove(initialItem)
        self.cuisineFoods[cuisine].add((-newRating, food))
        self.foodRatings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        highestRatingFood = self.cuisineFoods[cuisine][0]
        return highestRatingFood[0]
