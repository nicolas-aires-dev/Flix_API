from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.')
        ]
        )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.title


# from django.db import models
# from genres.models import Genre
# from actors.models import Actor

# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
#     release_date = models.DateField(null=True, blank=True)
#     actors = models.ManyToManyField(Actor, related_name='movies')
#     resume = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.title
