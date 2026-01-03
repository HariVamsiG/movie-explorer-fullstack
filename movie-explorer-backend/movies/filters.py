import django_filters
from .models import Movie, Actor, Director, Genre, Review


class MovieFilter(django_filters.FilterSet):
    """
    Filter class for Movie model with multiple filtering options
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    release_year = django_filters.NumberFilter()
    release_year_gte = django_filters.NumberFilter(field_name='release_year', lookup_expr='gte')
    release_year_lte = django_filters.NumberFilter(field_name='release_year', lookup_expr='lte')
    director = django_filters.CharFilter(field_name='director__name', lookup_expr='icontains')
    director_id = django_filters.NumberFilter(field_name='director__id')
    actor = django_filters.CharFilter(field_name='actors__name', lookup_expr='icontains')
    actor_id = django_filters.NumberFilter(field_name='actors__id')
    genre = django_filters.CharFilter(field_name='genres__name', lookup_expr='icontains')
    genre_id = django_filters.NumberFilter(field_name='genres__id')
    rating_gte = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating_lte = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    
    ordering = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('release_year', 'release_year'),
            ('rating', 'rating'),
            ('created_at', 'created_at'),
        )
    )

    class Meta:
        model = Movie
        fields = [
            'title', 'release_year', 'release_year_gte', 'release_year_lte',
            'director', 'director_id', 'actor', 'actor_id', 
            'genre', 'genre_id', 'rating_gte', 'rating_lte'
        ]


class ActorFilter(django_filters.FilterSet):
    """
    Filter class for Actor model
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    nationality = django_filters.CharFilter(lookup_expr='icontains')
    movie = django_filters.CharFilter(field_name='movies__title', lookup_expr='icontains')
    movie_id = django_filters.NumberFilter(field_name='movies__id')
    genre = django_filters.CharFilter(field_name='movies__genres__name', lookup_expr='icontains')
    genre_id = django_filters.NumberFilter(field_name='movies__genres__id')

    class Meta:
        model = Actor
        fields = ['name', 'nationality', 'movie', 'movie_id', 'genre', 'genre_id']


class DirectorFilter(django_filters.FilterSet):
    """
    Filter class for Director model
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    nationality = django_filters.CharFilter(lookup_expr='icontains')
    movie = django_filters.CharFilter(field_name='movies__title', lookup_expr='icontains')
    movie_id = django_filters.NumberFilter(field_name='movies__id')

    class Meta:
        model = Director
        fields = ['name', 'nationality', 'movie', 'movie_id']


class GenreFilter(django_filters.FilterSet):
    """
    Filter class for Genre model
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Genre
        fields = ['name']


class ReviewFilter(django_filters.FilterSet):
    """
    Filter class for Review model
    """
    movie = django_filters.CharFilter(field_name='movie__title', lookup_expr='icontains')
    movie_id = django_filters.NumberFilter(field_name='movie__id')
    reviewer_name = django_filters.CharFilter(lookup_expr='icontains')
    rating = django_filters.NumberFilter()
    rating_gte = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating_lte = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    is_featured = django_filters.BooleanFilter()

    class Meta:
        model = Review
        fields = ['movie', 'movie_id', 'reviewer_name', 'rating', 'rating_gte', 'rating_lte', 'is_featured']
