from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from decimal import Decimal
from datetime import date
from .models import Movie, Actor, Director, Genre, Review


class MovieAPITestCase(APITestCase):
    """Test cases for Movie API endpoints"""
    
    def setUp(self):
        # Create test data
        self.director = Director.objects.create(
            name="Christopher Nolan",
            birth_date=date(1970, 7, 30),
            nationality="British"
        )
        
        self.genre1 = Genre.objects.create(name="Action", description="Action movies")
        self.genre2 = Genre.objects.create(name="Sci-Fi", description="Science Fiction")
        
        self.actor1 = Actor.objects.create(
            name="Leonardo DiCaprio",
            birth_date=date(1974, 11, 11),
            nationality="American"
        )
        self.actor2 = Actor.objects.create(
            name="Marion Cotillard",
            birth_date=date(1975, 9, 30),
            nationality="French"
        )
        
        self.movie = Movie.objects.create(
            title="Inception",
            release_year=2010,
            duration=148,
            plot="A thief who steals corporate secrets through dream-sharing technology",
            rating=Decimal('8.8'),
            director=self.director
        )
        self.movie.actors.set([self.actor1, self.actor2])
        self.movie.genres.set([self.genre1, self.genre2])
        
        self.review = Review.objects.create(
            movie=self.movie,
            reviewer_name="John Doe",
            rating=9,
            comment="Amazing movie!",
            is_featured=True
        )

    def test_movie_list(self):
        """Test GET /api/movies/"""
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Inception')

    def test_movie_detail(self):
        """Test GET /api/movies/{id}/"""
        url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Inception')
        self.assertEqual(len(response.data['actors']), 2)
        self.assertEqual(len(response.data['genres']), 2)

    def test_movie_create(self):
        """Test POST /api/movies/"""
        url = reverse('movie-list')
        data = {
            'title': 'Interstellar',
            'release_year': 2014,
            'duration': 169,
            'plot': 'A team of explorers travel through a wormhole in space',
            'rating': '8.6',
            'director_id': self.director.pk,
            'actor_ids': [self.actor1.pk],
            'genre_ids': [self.genre2.pk]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_movie_update(self):
        """Test PUT /api/movies/{id}/"""
        url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
        data = {
            'title': 'Inception Updated',
            'release_year': 2010,
            'duration': 148,
            'plot': 'Updated plot',
            'rating': '9.0',
            'director_id': self.director.pk,
            'actor_ids': [self.actor1.pk],
            'genre_ids': [self.genre1.pk]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Inception Updated')

    def test_movie_partial_update(self):
        """Test PATCH /api/movies/{id}/"""
        url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
        data = {'title': 'Inception Patched'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Inception Patched')

    def test_movie_delete(self):
        """Test DELETE /api/movies/{id}/"""
        url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)

    def test_movie_by_genre(self):
        """Test GET /api/movies/by_genre/?name={genre}"""
        url = '/api/movies/by_genre/'
        response = self.client.get(url, {'name': 'Action'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_movie_by_genre_missing_param(self):
        """Test GET /api/movies/by_genre/ without name parameter"""
        url = '/api/movies/by_genre/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_movie_by_director(self):
        """Test GET /api/movies/by_director/?name={director}"""
        url = '/api/movies/by_director/'
        response = self.client.get(url, {'name': 'Nolan'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_movie_by_director_missing_param(self):
        """Test GET /api/movies/by_director/ without name parameter"""
        url = '/api/movies/by_director/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_movie_top_rated(self):
        """Test GET /api/movies/top_rated/"""
        url = '/api/movies/top_rated/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_movie_filtering(self):
        """Test movie filtering capabilities"""
        url = reverse('movie-list')
        
        # Filter by title
        response = self.client.get(url, {'title': 'Inception'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # Filter by release year
        response = self.client.get(url, {'release_year': 2010})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # Filter by director
        response = self.client.get(url, {'director': 'Nolan'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # Filter by genre
        response = self.client.get(url, {'genre': 'Action'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)


class ActorAPITestCase(APITestCase):
    """Test cases for Actor API endpoints"""
    
    def setUp(self):
        self.actor = Actor.objects.create(
            name="Tom Hanks",
            birth_date=date(1956, 7, 9),
            nationality="American",
            biography="American actor and filmmaker"
        )
        
        self.director = Director.objects.create(name="Steven Spielberg")
        self.genre = Genre.objects.create(name="Drama")
        
        self.movie = Movie.objects.create(
            title="Forrest Gump",
            release_year=1994,
            director=self.director
        )
        self.movie.actors.add(self.actor)
        self.movie.genres.add(self.genre)

    def test_actor_list(self):
        """Test GET /api/actors/"""
        url = reverse('actor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_actor_detail(self):
        """Test GET /api/actors/{id}/"""
        url = reverse('actor-detail', kwargs={'pk': self.actor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tom Hanks')
        self.assertIn('movies', response.data)

    def test_actor_create(self):
        """Test POST /api/actors/"""
        url = reverse('actor-list')
        data = {
            'name': 'Meryl Streep',
            'birth_date': '1949-06-22',
            'nationality': 'American',
            'biography': 'American actress'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 2)

    def test_actor_update(self):
        """Test PUT /api/actors/{id}/"""
        url = reverse('actor-detail', kwargs={'pk': self.actor.pk})
        data = {
            'name': 'Tom Hanks Updated',
            'birth_date': '1956-07-09',
            'nationality': 'American',
            'biography': 'Updated biography'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.actor.refresh_from_db()
        self.assertEqual(self.actor.name, 'Tom Hanks Updated')

    def test_actor_delete(self):
        """Test DELETE /api/actors/{id}/"""
        url = reverse('actor-detail', kwargs={'pk': self.actor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Actor.objects.count(), 0)

    def test_actor_filtering(self):
        """Test actor filtering capabilities"""
        url = reverse('actor-list')
        
        # Filter by name
        response = self.client.get(url, {'name': 'Tom'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # Filter by nationality
        response = self.client.get(url, {'nationality': 'American'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)


class DirectorAPITestCase(APITestCase):
    """Test cases for Director API endpoints"""
    
    def setUp(self):
        self.director = Director.objects.create(
            name="Quentin Tarantino",
            birth_date=date(1963, 3, 27),
            nationality="American",
            biography="American film director"
        )
        
        self.movie = Movie.objects.create(
            title="Pulp Fiction",
            release_year=1994,
            director=self.director
        )

    def test_director_list(self):
        """Test GET /api/directors/"""
        url = reverse('director-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_director_detail(self):
        """Test GET /api/directors/{id}/"""
        url = reverse('director-detail', kwargs={'pk': self.director.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Quentin Tarantino')
        self.assertIn('movies', response.data)

    def test_director_create(self):
        """Test POST /api/directors/"""
        url = reverse('director-list')
        data = {
            'name': 'Martin Scorsese',
            'birth_date': '1942-11-17',
            'nationality': 'American',
            'biography': 'American film director'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Director.objects.count(), 2)

    def test_director_update(self):
        """Test PUT /api/directors/{id}/"""
        url = reverse('director-detail', kwargs={'pk': self.director.pk})
        data = {
            'name': 'Quentin Tarantino Updated',
            'birth_date': '1963-03-27',
            'nationality': 'American',
            'biography': 'Updated biography'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.director.refresh_from_db()
        self.assertEqual(self.director.name, 'Quentin Tarantino Updated')

    def test_director_delete(self):
        """Test DELETE /api/directors/{id}/"""
        url = reverse('director-detail', kwargs={'pk': self.director.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Director.objects.count(), 0)


class GenreAPITestCase(APITestCase):
    """Test cases for Genre API endpoints"""
    
    def setUp(self):
        self.genre = Genre.objects.create(
            name="Horror",
            description="Horror movies that scare"
        )

    def test_genre_list(self):
        """Test GET /api/genres/"""
        url = reverse('genre-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_genre_detail(self):
        """Test GET /api/genres/{id}/"""
        url = reverse('genre-detail', kwargs={'pk': self.genre.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Horror')

    def test_genre_create(self):
        """Test POST /api/genres/"""
        url = reverse('genre-list')
        data = {
            'name': 'Comedy',
            'description': 'Funny movies'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Genre.objects.count(), 2)

    def test_genre_update(self):
        """Test PUT /api/genres/{id}/"""
        url = reverse('genre-detail', kwargs={'pk': self.genre.pk})
        data = {
            'name': 'Horror Updated',
            'description': 'Updated description'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.genre.refresh_from_db()
        self.assertEqual(self.genre.name, 'Horror Updated')

    def test_genre_delete(self):
        """Test DELETE /api/genres/{id}/"""
        url = reverse('genre-detail', kwargs={'pk': self.genre.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Genre.objects.count(), 0)


class ReviewAPITestCase(APITestCase):
    """Test cases for Review API endpoints"""
    
    def setUp(self):
        self.director = Director.objects.create(name="Test Director")
        self.movie = Movie.objects.create(
            title="Test Movie",
            release_year=2023,
            director=self.director
        )
        
        self.review = Review.objects.create(
            movie=self.movie,
            reviewer_name="Jane Doe",
            rating=8,
            comment="Great movie!",
            is_featured=True
        )

    def test_review_list(self):
        """Test GET /api/reviews/"""
        url = reverse('review-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_review_detail(self):
        """Test GET /api/reviews/{id}/"""
        url = reverse('review-detail', kwargs={'pk': self.review.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reviewer_name'], 'Jane Doe')

    def test_review_create(self):
        """Test POST /api/reviews/"""
        url = reverse('review-list')
        data = {
            'movie': self.movie.pk,
            'reviewer_name': 'Bob Smith',
            'rating': 7,
            'comment': 'Good movie',
            'is_featured': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)

    def test_review_update(self):
        """Test PUT /api/reviews/{id}/"""
        url = reverse('review-detail', kwargs={'pk': self.review.pk})
        data = {
            'movie': self.movie.pk,
            'reviewer_name': 'Jane Doe Updated',
            'rating': 9,
            'comment': 'Updated comment',
            'is_featured': True
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.reviewer_name, 'Jane Doe Updated')

    def test_review_delete(self):
        """Test DELETE /api/reviews/{id}/"""
        url = reverse('review-detail', kwargs={'pk': self.review.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)

    def test_review_featured(self):
        """Test GET /api/reviews/featured/"""
        url = '/api/reviews/featured/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if response is paginated or direct list
        if 'results' in response.data:
            self.assertEqual(len(response.data['results']), 1)
        else:
            self.assertEqual(len(response.data), 1)

    def test_review_filtering(self):
        """Test review filtering capabilities"""
        url = reverse('review-list')
        
        # Filter by reviewer name
        response = self.client.get(url, {'reviewer_name': 'Jane'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # Filter by rating
        response = self.client.get(url, {'rating': 8})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
        # Filter by featured
        response = self.client.get(url, {'is_featured': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)


class ValidationTestCase(APITestCase):
    """Test cases for data validation"""
    
    def setUp(self):
        self.director = Director.objects.create(name="Test Director")

    def test_movie_invalid_year(self):
        """Test movie creation with invalid year"""
        url = reverse('movie-list')
        data = {
            'title': 'Invalid Movie',
            'release_year': 1800,  # Too early
            'director': self.director.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_movie_invalid_rating(self):
        """Test movie creation with invalid rating"""
        url = reverse('movie-list')
        data = {
            'title': 'Invalid Movie',
            'release_year': 2023,
            'rating': 15.0,  # Too high
            'director': self.director.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_invalid_rating(self):
        """Test review creation with invalid rating"""
        movie = Movie.objects.create(
            title="Test Movie",
            release_year=2023,
            director=self.director
        )
        
        url = reverse('review-list')
        data = {
            'movie': movie.pk,
            'reviewer_name': 'Test Reviewer',
            'rating': 15,  # Too high
            'comment': 'Test comment'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PaginationTestCase(APITestCase):
    """Test cases for pagination"""
    
    def setUp(self):
        self.director = Director.objects.create(name="Test Director")
        
        # Create multiple movies for pagination testing
        for i in range(15):
            Movie.objects.create(
                title=f"Movie {i}",
                release_year=2020 + i % 5,
                director=self.director
            )

    def test_movie_pagination(self):
        """Test movie list pagination"""
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertIn('results', response.data)
        self.assertEqual(response.data['count'], 15)


class ErrorHandlingTestCase(APITestCase):
    """Test cases for error handling"""
    
    def test_movie_not_found(self):
        """Test GET /api/movies/{invalid_id}/"""
        url = reverse('movie-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_actor_not_found(self):
        """Test GET /api/actors/{invalid_id}/"""
        url = reverse('actor-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_director_not_found(self):
        """Test GET /api/directors/{invalid_id}/"""
        url = reverse('director-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_genre_not_found(self):
        """Test GET /api/genres/{invalid_id}/"""
        url = reverse('genre-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_review_not_found(self):
        """Test GET /api/reviews/{invalid_id}/"""
        url = reverse('review-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
