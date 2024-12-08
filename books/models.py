# books/models.py
from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NON_FICTION', 'Non-Fiction'),
        ('SCIENCE', 'Science'),
        ('HISTORY', 'History'),
        ('OTHER', 'Other')
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    genre = models.CharField(
        max_length=20, 
        choices=GENRE_CHOICES, 
        default='OTHER'
    )
    available_copies = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title
