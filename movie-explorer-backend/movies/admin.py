from django.contrib import admin
from .models import Movie, Actor, Director, Genre, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality', 'birth_date', 'created_at']
    search_fields = ['name', 'nationality']
    list_filter = ['nationality', 'created_at']
    date_hierarchy = 'birth_date'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality', 'birth_date', 'created_at']
    search_fields = ['name', 'nationality']
    list_filter = ['nationality', 'created_at']
    date_hierarchy = 'birth_date'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'director', 'rating', 'duration', 'average_rating', 'review_count', 'created_at']
    search_fields = ['title', 'director__name']
    list_filter = ['release_year', 'genres', 'director', 'created_at']
    filter_horizontal = ['actors', 'genres']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'release_year', 'duration', 'rating')
        }),
        ('Content', {
            'fields': ('plot', 'poster_url')
        }),
        ('Relationships', {
            'fields': ('director', 'actors', 'genres')
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'reviewer_name', 'rating', 'is_featured', 'created_at']
    search_fields = ['movie__title', 'reviewer_name', 'comment']
    list_filter = ['rating', 'is_featured', 'created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Review Information', {
            'fields': ('movie', 'reviewer_name', 'rating', 'is_featured')
        }),
        ('Content', {
            'fields': ('comment',)
        }),
    )
