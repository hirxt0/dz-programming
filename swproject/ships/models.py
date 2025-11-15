from django.db import models

class Starship(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    cost_in_credits = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    max_atmosphering_speed = models.CharField(max_length=100)
    crew = models.CharField(max_length=100)
    passengers = models.CharField(max_length=100)
    cargo_capacity = models.CharField(max_length=100)
    starship_class = models.CharField(max_length=200)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']