from rest_framework import serializers
from .models import Movie, Actor, Director, Genre, Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Review model
    """
    class Meta:
        model = Review
        fields = ['id', 'movie', 'reviewer_name', 'rating', 'comment', 'is_featured', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'movies_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_movies_count(self, obj):
        return obj.movies.count()


class DirectorSerializer(serializers.ModelSerializer):
    """
    Serializer for Director model
    """
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'birth_date', 'nationality', 'biography', 'image_url', 'movies_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_movies_count(self, obj):
        return obj.movies.count()


class ActorSerializer(serializers.ModelSerializer):
    """
    Serializer for Actor model
    """
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ['id', 'name', 'birth_date', 'nationality', 'biography', 'image_url', 'movies_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_movies_count(self, obj):
        return obj.movies.count()


class MovieListSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie list view (minimal fields for performance)
    """
    director_name = serializers.CharField(source='director.name', read_only=True)
    genres = serializers.StringRelatedField(many=True, read_only=True)
    average_rating = serializers.ReadOnlyField()
    review_count = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'release_year', 'rating', 'poster_url', 'backdrop_url',
            'director_name', 'genres', 'average_rating', 'review_count'
        ]


class MovieDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie detail view (all fields with nested relationships)
    """
    director = DirectorSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.ReadOnlyField()
    review_count = serializers.ReadOnlyField()
    
    # Write-only fields for creating/updating relationships
    director_id = serializers.IntegerField(write_only=True)
    actor_ids = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True, 
        required=False
    )
    genre_ids = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True
    )

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'release_year', 'duration', 'plot', 'poster_url', 'backdrop_url', 'rating',
            'director', 'actors', 'genres', 'reviews', 'average_rating', 'review_count',
            'created_at', 'updated_at', 'director_id', 'actor_ids', 'genre_ids'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        actor_ids = validated_data.pop('actor_ids', [])
        genre_ids = validated_data.pop('genre_ids', [])
        
        movie = Movie.objects.create(**validated_data)
        
        if actor_ids:
            movie.actors.set(actor_ids)
        movie.genres.set(genre_ids)
        
        return movie

    def update(self, instance, validated_data):
        actor_ids = validated_data.pop('actor_ids', None)
        genre_ids = validated_data.pop('genre_ids', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if actor_ids is not None:
            instance.actors.set(actor_ids)
        if genre_ids is not None:
            instance.genres.set(genre_ids)
        
        return instance


class ActorDetailSerializer(ActorSerializer):
    """
    Detailed Actor serializer with movies
    """
    movies = MovieListSerializer(many=True, read_only=True)

    class Meta(ActorSerializer.Meta):
        fields = ActorSerializer.Meta.fields + ['movies']


class DirectorDetailSerializer(DirectorSerializer):
    """
    Detailed Director serializer with movies
    """
    movies = MovieListSerializer(many=True, read_only=True)

    class Meta(DirectorSerializer.Meta):
        fields = DirectorSerializer.Meta.fields + ['movies']
