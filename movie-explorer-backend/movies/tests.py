from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Actor, Director, Genre


class ModelTestCase(TestCase):
    """Test cases for models"""
    
    def setUp(self):
        self.genre = Genre.objects.create(name="Action", description="Action movies")
        self.director = Director.objects.create(name="Christopher Nolan", nationality="British")
        self.actor = Actor.objects.create(name="Leonardo DiCaprio", nationality="American")
        
    def test_genre_creation(self):
        self.assertEqual(self.genre.name, "Action")
        self.assertEqual(str(self.genre), "Action")
        
    def test_director_creation(self):
        self.assertEqual(self.director.name, "Christopher Nolan")
        self.assertEqual(str(self.director), "Christopher Nolan")
        
    def test_actor_creation(self):
        self.assertEqual(self.actor.name, "Leonardo DiCaprio")
        self.assertEqual(str(self.actor), "Leonardo DiCaprio")
        
    def test_movie_creation(self):
        movie = Movie.objects.create(
            title="Inception",
            release_year=2010,
            director=self.director,
            rating=8.8
        )
        movie.genres.add(self.genre)
        movie.actors.add(self.actor)
        
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(movie.release_year, 2010)
        self.assertEqual(movie.director, self.director)
        self.assertEqual(str(movie), "Inception (2010)")
        self.assertIn(self.genre, movie.genres.all())
        self.assertIn(self.actor, movie.actors.all())


class APITestCase(APITestCase):
    """Test cases for API endpoints"""
    
    def setUp(self):
        self.genre = Genre.objects.create(name="Sci-Fi")
        self.director = Director.objects.create(name="Denis Villeneuve")
        self.actor = Actor.objects.create(name="Ryan Gosling")
        
        self.movie = Movie.objects.create(
            title="Blade Runner 2049",
            release_year=2017,
            director=self.director,
            rating=8.0
        )
        self.movie.genres.add(self.genre)
        self.movie.actors.add(self.actor)
        
    def test_movie_list_api(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_movie_detail_api(self):
        url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Blade Runner 2049")
        
    def test_movie_filter_by_genre(self):
        url = reverse('movie-list')
        response = self.client.get(url, {'genre': 'Sci-Fi'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_movie_filter_by_director(self):
        url = reverse('movie-list')
        response = self.client.get(url, {'director': 'Denis'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_movie_filter_by_actor(self):
        url = reverse('movie-list')
        response = self.client.get(url, {'actor': 'Ryan'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_movie_filter_by_year(self):
        url = reverse('movie-list')
        response = self.client.get(url, {'release_year': 2017})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_actor_list_api(self):
        url = reverse('actor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_director_list_api(self):
        url = reverse('director-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_genre_list_api(self):
        url = reverse('genre-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_movie_creation_api(self):
        url = reverse('movie-list')
        data = {
            'title': 'Dune',
            'release_year': 2021,
            'director_id': self.director.id,
            'genre_ids': [self.genre.id],
            'actor_ids': [self.actor.id],
            'rating': 8.1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        
    def test_invalid_movie_creation(self):
        url = reverse('movie-list')
        data = {
            'title': '',  # Invalid empty title
            'release_year': 2021,
            'director_id': self.director.id,
            'genre_ids': [self.genre.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
