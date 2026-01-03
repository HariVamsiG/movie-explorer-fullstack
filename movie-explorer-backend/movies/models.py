from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    """
    Abstract base model with common timestamp fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    """
    Genre model representing movie genres (e.g., Action, Comedy, Drama)
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Director(BaseModel):
    """
    Director model representing movie directors
    """
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)
    image_url = models.URLField(blank=True, null=True, help_text="Director's photo URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Actor(BaseModel):
    """
    Actor model representing movie actors
    """
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)
    image_url = models.URLField(blank=True, null=True, help_text="Actor's photo URL")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(BaseModel):
    """
    Movie model representing movies with relationships to genres, directors, and actors
    """
    title = models.CharField(max_length=300)
    release_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2030)]
    )
    duration = models.IntegerField(help_text="Duration in minutes", null=True, blank=True)
    plot = models.TextField(blank=True)
    poster_url = models.URLField(blank=True, null=True, help_text="Movie poster URL")
    backdrop_url = models.URLField(blank=True, null=True, help_text="Movie backdrop/banner URL")
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    
    # Relationships
    director = models.ForeignKey(
        Director, 
        on_delete=models.CASCADE, 
        related_name='movies'
    )
    actors = models.ManyToManyField(
        Actor, 
        related_name='movies', 
        blank=True
    )
    genres = models.ManyToManyField(
        Genre, 
        related_name='movies'
    )

    class Meta:
        ordering = ['-release_year', 'title']
        unique_together = ['title', 'release_year', 'director']

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    @property
    def average_rating(self):
        """Calculate average rating from reviews"""
        reviews = self.reviews.all()
        if reviews:
            return round(sum(review.rating for review in reviews) / len(reviews), 1)
        return None

    @property
    def review_count(self):
        """Get total number of reviews"""
        return self.reviews.count()


class Review(BaseModel):
    """
    Review model for movie reviews and ratings
    """
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer_name = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    comment = models.TextField()
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['movie', 'reviewer_name']

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie.title} ({self.rating}/10)"
