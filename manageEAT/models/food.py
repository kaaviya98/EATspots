from django.db import models

from .restaurant import Restaurant

FOOD_TYPES = [
    ("Vegan", "Vegan"),
    ("Veg", "Veg"),
    ("Non-veg", "Non-veg"),
]

MENU_TYPES = [
    ("Breakfast", "Breakfast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
]


class Food(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d/")
    description = models.TextField(max_length=50, blank=True)
    food_type = models.CharField(max_length=10, choices=FOOD_TYPES, default="Veg")
    menu_type = models.CharField(max_length=10, choices=MENU_TYPES, default="Breakfast")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_food_items"
    )
