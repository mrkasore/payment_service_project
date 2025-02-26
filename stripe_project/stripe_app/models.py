from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_total_cost(self):
        self.total_cost = sum(item.price for item in self.items.all())
        self.save()

    def __str__(self):
        return f"Order {self.id}"

