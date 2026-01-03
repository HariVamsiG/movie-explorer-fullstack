# Movies Explorer Backend

A Django REST API for exploring movies, actors, directors, genres, and reviews. Built with Django REST Framework, PostgreSQL, and Swagger documentation.

## Features

- **Complete CRUD operations** for Movies, Actors, Directors, Genres, and Reviews
- **Advanced filtering** capabilities for all entities
- **Custom API endpoints** for specialized queries
- **Comprehensive API documentation** with Swagger/OpenAPI
- **Relationship management** between all entities
- **Comprehensive test suite** with 59+ test cases
- **Docker support** with PostgreSQL
- **Sample data** for testing and development
- **Admin interface** for data management
- **Review system** with featured reviews

## Tech Stack

- **Backend**: Django 5.2.8, Django REST Framework 3.15.2
- **Database**: PostgreSQL 15
- **Documentation**: drf-spectacular (Swagger/OpenAPI)
- **Filtering**: django-filter
- **Testing**: Django TestCase, APITestCase
- **Containerization**: Docker & Docker Compose

## API Endpoints

### Movies

- `GET /api/movies/` - List all movies with filtering
- `POST /api/movies/` - Create a new movie
- `GET /api/movies/{id}/` - Get movie details
- `PUT /api/movies/{id}/` - Update movie
- `PATCH /api/movies/{id}/` - Partial update movie
- `DELETE /api/movies/{id}/` - Delete movie
- `GET /api/movies/by_genre/?name={genre}` - Movies by genre
- `GET /api/movies/by_director/?name={director}` - Movies by director
- `GET /api/movies/top_rated/` - Get top rated movies

### Actors

- `GET /api/actors/` - List all actors with filtering
- `POST /api/actors/` - Create a new actor
- `GET /api/actors/{id}/` - Get actor details with movies
- `PUT /api/actors/{id}/` - Update actor
- `PATCH /api/actors/{id}/` - Partial update actor
- `DELETE /api/actors/{id}/` - Delete actor

### Directors

- `GET /api/directors/` - List all directors with filtering
- `POST /api/directors/` - Create a new director
- `GET /api/directors/{id}/` - Get director details with movies
- `PUT /api/directors/{id}/` - Update director
- `PATCH /api/directors/{id}/` - Partial update director
- `DELETE /api/directors/{id}/` - Delete director

### Genres

- `GET /api/genres/` - List all genres
- `POST /api/genres/` - Create a new genre
- `GET /api/genres/{id}/` - Get genre details
- `PUT /api/genres/{id}/` - Update genre
- `PATCH /api/genres/{id}/` - Partial update genre
- `DELETE /api/genres/{id}/` - Delete genre

### Reviews

- `GET /api/reviews/` - List all reviews with filtering
- `POST /api/reviews/` - Create a new review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review
- `PATCH /api/reviews/{id}/` - Partial update review
- `DELETE /api/reviews/{id}/` - Delete review
- `GET /api/reviews/featured/` - Get featured reviews

## Filtering Options

### Movies

- `title` - Filter by title (contains)
- `release_year` - Filter by exact year
- `release_year_gte` - Filter by year greater than or equal
- `release_year_lte` - Filter by year less than or equal
- `director` - Filter by director name (contains)
- `director_id` - Filter by director ID
- `actor` - Filter by actor name (contains)
- `actor_id` - Filter by actor ID
- `genre` - Filter by genre name (contains)
- `genre_id` - Filter by genre ID
- `rating_gte` - Filter by rating greater than or equal
- `rating_lte` - Filter by rating less than or equal

### Actors

- `name` - Filter by name (contains)
- `nationality` - Filter by nationality (contains)
- `movie` - Filter by movie title (contains)
- `movie_id` - Filter by movie ID
- `genre` - Filter by genre of movies acted in
- `genre_id` - Filter by genre ID of movies acted in

### Directors

- `name` - Filter by name (contains)
- `nationality` - Filter by nationality (contains)
- `movie` - Filter by movie title (contains)
- `movie_id` - Filter by movie ID

### Reviews

- `movie` - Filter by movie title (contains)
- `movie_id` - Filter by movie ID
- `reviewer_name` - Filter by reviewer name (contains)
- `rating` - Filter by exact rating
- `rating_gte` - Filter by rating greater than or equal
- `rating_lte` - Filter by rating less than or equal
- `is_featured` - Filter by featured status (boolean)

## Quick Start

### Local Development with Docker (Recommended)

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd movie-explorer-backend
   ```
2. **Start the development environment**

   ```bash
   docker-compose up --build
   ```

   This will:

   - Build the Django application
   - Start PostgreSQL database
   - Run migrations automatically
   - Load sample data
   - Start the development server
3. **Access the application**

   - API: http://localhost:8000/api/
   - Swagger Documentation: http://localhost:8000/api/docs/
   - ReDoc Documentation: http://localhost:8000/api/redoc/
   - Admin Interface: http://localhost:8000/admin/
4. **Create superuser (optional)**

   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```
   
   **Note:** Create a superuser to access the Django admin interface at http://localhost:8000/admin/
5. **Stop the environment**

   ```bash
   docker-compose down
   ```

### Alternative: Manual Local Setup

<details>
<summary>Click to expand manual setup instructions</summary>

**Prerequisites:** Python 3.11+, PostgreSQL 15+ installed and running

1. **Create and activate virtual environment**

   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL database**

   ```bash
   # Create database (requires PostgreSQL to be installed and running)
   createdb movies_explorer
   ```

4. **Configure environment variables**

   ```bash
   # Create .env file (optional)
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://user:password@localhost:5432/movies_explorer
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Load sample data**

   ```bash
   python manage.py load_sample_data
   ```

7. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```
   
   **Note:** Create a superuser to access the Django admin interface at http://localhost:8000/admin/

8. **Run development server**

   ```bash
   python manage.py runserver
   ```

**Note:** Manual setup requires PostgreSQL to be pre-installed and configured on your system. For a hassle-free setup, use the Docker Compose method above.

</details>

</details>

## Testing

### Run All Tests

```bash
python manage.py test
```

### Run Specific Test Suite

```bash
# Run comprehensive test suite
python manage.py test movies.test_cases

# Run original test suite
python manage.py test movies.tests
```

### Run Tests with Docker

```bash
docker-compose run backend python manage.py test
```

### Test Suite Coverage

The project includes comprehensive test coverage with 59+ test cases:

- **MovieAPITestCase** - 15 tests covering all movie endpoints
- **ActorAPITestCase** - 8 tests for actor operations
- **DirectorAPITestCase** - 6 tests for director operations
- **GenreAPITestCase** - 6 tests for genre operations
- **ReviewAPITestCase** - 9 tests for review operations
- **ValidationTestCase** - Data validation tests
- **PaginationTestCase** - Pagination functionality tests
- **ErrorHandlingTestCase** - Error scenario tests

## API Documentation

The API is fully documented using Swagger/OpenAPI specification:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/

## Sample API Usage

### Get all movies

```bash
curl http://localhost:8000/api/movies/
```

### Filter movies by genre

```bash
curl "http://localhost:8000/api/movies/?genre=Action"
```

### Filter movies by director and year

```bash
curl "http://localhost:8000/api/movies/?director=Nolan&release_year_gte=2010"
```

### Create a new movie

```bash
curl -X POST http://localhost:8000/api/movies/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Dune",
    "release_year": 2021,
    "director_id": 1,
    "genre_ids": [1, 2],
    "actor_ids": [1, 2],
    "rating": "8.1",
    "duration": 155,
    "plot": "A noble family becomes embroiled in a war for control over the galaxy."
  }'
```

### Create a review

```bash
curl -X POST http://localhost:8000/api/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "movie": 1,
    "reviewer_name": "John Doe",
    "rating": 9,
    "comment": "Excellent movie!",
    "is_featured": false
  }'
```

### Get featured reviews

```bash
curl http://localhost:8000/api/reviews/featured/
```

## Database Schema

### Models and Relationships

- **Movie** belongs to one **Director** (Many-to-One)
- **Movie** can have multiple **Actors** (Many-to-Many)
- **Movie** can belong to multiple **Genres** (Many-to-Many)
- **Movie** can have multiple **Reviews** (One-to-Many)
- **Review** belongs to one **Movie** (Many-to-One)

### Key Fields

- **Movie**: title, release_year, duration, plot, poster_url, backdrop_url, rating
- **Actor**: name, birth_date, nationality, biography, image_url
- **Director**: name, birth_date, nationality, biography, image_url
- **Genre**: name, description
- **Review**: reviewer_name, rating, comment, is_featured

### Data Validation

- **Movie rating**: 0.0 - 10.0 (decimal)
- **Review rating**: 1 - 10 (integer)
- **Release year**: 1900 - 2030
- **Unique constraints**: Movie (title + year + director), Review (movie + reviewer)

## Admin Interface

Access the Django admin at http://localhost:8000/admin/ to:

- Manage all entities (Movies, Actors, Directors, Genres, Reviews)
- View relationships and statistics
- Bulk operations and filtering
- User and permission management

## Environment Variables

- `DEBUG`: Django debug mode (default: True)
- `SECRET_KEY`: Django secret key (required for production)
- `DATABASE_URL`: PostgreSQL connection string
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Production Deployment

### Environment Setup

```bash
# Set production environment variables
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:password@host:port/database
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Docker Production

```bash
# Build production image
docker build -t movie-explorer-backend .

# Run with production settings
docker run -p 8000:8000 --env-file .env movie-explorer-backend
```
