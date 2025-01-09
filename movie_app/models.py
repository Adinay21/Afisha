from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movie_count(self):
        return len(self.movies.all())

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='none')
    duration = models.IntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True, blank=True)

    def __str__(self):
        return self.title

    # def average_function(self):
    #     return self.reviews.aggregate(average=Avg('stars'))['average'] or 0




class Review(models.Model):
    STARS = (
        (1, '*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *'),
    )

    text = models.TextField(default='none')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(choices=STARS, null=True)

    def __str__(self):
        return self.text

