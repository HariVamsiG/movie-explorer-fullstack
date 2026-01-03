from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Movie, Actor, Director, Genre, Review
from .serializers import (
    MovieListSerializer, MovieDetailSerializer,
    ActorSerializer, ActorDetailSerializer,
    DirectorSerializer, DirectorDetailSerializer,
    GenreSerializer, ReviewSerializer
)
from .filters import MovieFilter, ActorFilter, DirectorFilter, GenreFilter, ReviewFilter


@extend_schema_view(
    list=extend_schema(description="Get list of all movies with filtering options"),
    create=extend_schema(description="Create a new movie"),
    retrieve=extend_schema(description="Get detailed information about a specific movie"),
    update=extend_schema(description="Update a movie"),
    partial_update=extend_schema(description="Partially update a movie"),
    destroy=extend_schema(description="Delete a movie"),
)
class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Movie model with comprehensive filtering capabilities
    
    Supports filtering by:
    - title (contains)
    - release_year (exact, gte, lte)
    - director (name contains, id)
    - actor (name contains, id)
    - genre (name contains, id)
    - rating (gte, lte)
    """
    queryset = Movie.objects.select_related('director').prefetch_related('actors', 'genres', 'reviews')
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        return MovieDetailSerializer

    @extend_schema(description="Get movies by specific genre")
    @action(detail=False, methods=['get'])
    def by_genre(self, request):
        """Get movies filtered by genre name"""
        genre_name = request.query_params.get('name')
        if not genre_name:
            return Response(
                {'error': 'Genre name parameter is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        movies = self.get_queryset().filter(genres__name__icontains=genre_name)
        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = MovieListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    @extend_schema(description="Get movies by specific director")
    @action(detail=False, methods=['get'])
    def by_director(self, request):
        """Get movies filtered by director name"""
        director_name = request.query_params.get('name')
        if not director_name:
            return Response(
                {'error': 'Director name parameter is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        movies = self.get_queryset().filter(director__name__icontains=director_name)
        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = MovieListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    @extend_schema(description="Get top rated movies")
    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        """Get movies ordered by average rating"""
        movies = self.get_queryset().filter(reviews__isnull=False).distinct().order_by('-rating')[:10]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(description="Get list of all actors with filtering options"),
    create=extend_schema(description="Create a new actor"),
    retrieve=extend_schema(description="Get detailed information about a specific actor including their movies"),
    update=extend_schema(description="Update an actor"),
    partial_update=extend_schema(description="Partially update an actor"),
    destroy=extend_schema(description="Delete an actor"),
)
class ActorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Actor model with filtering by movies and genres
    
    Supports filtering by:
    - name (contains)
    - nationality (contains)
    - movie (title contains, id)
    - genre (name contains, id)
    """
    queryset = Actor.objects.prefetch_related('movies')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ActorFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ActorDetailSerializer
        return ActorSerializer


@extend_schema_view(
    list=extend_schema(description="Get list of all directors with filtering options"),
    create=extend_schema(description="Create a new director"),
    retrieve=extend_schema(description="Get detailed information about a specific director including their movies"),
    update=extend_schema(description="Update a director"),
    partial_update=extend_schema(description="Partially update a director"),
    destroy=extend_schema(description="Delete a director"),
)
class DirectorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Director model with filtering by movies
    
    Supports filtering by:
    - name (contains)
    - nationality (contains)
    - movie (title contains, id)
    """
    queryset = Director.objects.prefetch_related('movies')
    filter_backends = [DjangoFilterBackend]
    filterset_class = DirectorFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DirectorDetailSerializer
        return DirectorSerializer


@extend_schema_view(
    list=extend_schema(description="Get list of all genres"),
    create=extend_schema(description="Create a new genre"),
    retrieve=extend_schema(description="Get detailed information about a specific genre"),
    update=extend_schema(description="Update a genre"),
    partial_update=extend_schema(description="Partially update a genre"),
    destroy=extend_schema(description="Delete a genre"),
)
class GenreViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Genre model
    
    Supports filtering by:
    - name (contains)
    """
    queryset = Genre.objects.prefetch_related('movies')
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenreFilter


@extend_schema_view(
    list=extend_schema(description="Get list of all reviews with filtering options"),
    create=extend_schema(description="Create a new review"),
    retrieve=extend_schema(description="Get detailed information about a specific review"),
    update=extend_schema(description="Update a review"),
    partial_update=extend_schema(description="Partially update a review"),
    destroy=extend_schema(description="Delete a review"),
)
class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Review model with filtering capabilities
    
    Supports filtering by:
    - movie (title contains, id)
    - reviewer_name (contains)
    - rating (exact, gte, lte)
    - is_featured (boolean)
    """
    queryset = Review.objects.select_related('movie')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter

    @extend_schema(description="Get featured reviews")
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured reviews"""
        reviews = self.get_queryset().filter(is_featured=True)
        page = self.paginate_queryset(reviews)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)
