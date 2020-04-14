from django.db import models


# Create your models here.
class Meal(models.Model):
    """A meal of the day, contains food items."""
    meal_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.meal_name


class FoodItem(models.Model):
    """Food items in each meals."""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.food_name
