# Movies Explorer Frontend

A modern, responsive React application for exploring movies, actors, and directors. Built with TypeScript, Tailwind CSS, and test coverage.

## 🚀 Features

### Core Functionality

- **Movie Browsing**: Browse and search through extensive movie collection
- **Advanced Filtering**: Filter by genre, director, actor, year, and rating
- **Movie Details**: Comprehensive movie pages with cast, crew, and reviews
- **Favorites System**: Add/remove movies from favorites (localStorage)
- **Actor & Director Profiles**: Explore filmographies and biographies
- **Dark/Light Theme**: Toggle between themes with persistence
- **Responsive Design**: Optimized for mobile, tablet, and desktop

### Technical Features

- **TypeScript**: Full type safety and better developer experience
- **React Query**: Efficient data fetching
- **React Router**: Client-side routing with proper navigation
- **Tailwind CSS**: Modern utility-first CSS framework
- **Component Architecture**: Modular, reusable components
- **Comprehensive Testing**: 84 test cases with 100% pass rate

## 🛠️ Tech Stack

- **Framework**: React 19.2.0 with TypeScript
- **Build Tool**: Vite 7.2.4
- **Styling**: Tailwind CSS 3.4.19
- **State Management**: React Query (@tanstack/react-query)
- **Routing**: React Router DOM 7.11.0
- **HTTP Client**: Axios 1.13.2
- **Icons**: Lucide React 0.562.0
- **Form Handling**: React Hook Form with Zod validation
- **Testing**: Vitest + React Testing Library

## 🐳 Docker Deployment

### Build Docker Image
```bash
# Default API URL
docker build -t movie-explorer-frontend .

# Custom API URL
docker build --build-arg VITE_API_BASE_URL=https://your-api.com/api -t movie-explorer-frontend .
```

### Run Docker Container
```bash
docker run -p 3000:80 movie-explorer-frontend
```

### Docker Compose (with backend)
```yaml
version: '3.8'
services:
  frontend:
    build: .
    ports:
      - "3000:80"
    depends_on:
      - backend
  backend:
    build: ../movie-explorer-backend
    ports:
      - "8000:8000"
```

## 🔧 Installation & Setup

1. **Install Dependencies**

   ```bash
   npm install
   ```
2. **Start Development Server**

   ```bash
   npm run dev
   ```
3. **Build for Production**

   ```bash
   npm run build
   ```
4. **Run Tests**

   ```bash
   npm test          # Watch mode
   npm run test:run  # Single run
   ```

## 🧪 Testing

### Test Files

- **Utils Tests** (19 tests) - Utility functions
- **UI Components** (40 tests) - Button, Card, Input, Loading, ThemeToggle, Pagination
- **Layout Components** (11 tests) - Header, Layout
- **Feature Components** (12 tests) - MovieCard, MovieGrid
- **Page Components** (2 tests) - FavoritesPage

### Running Tests

```bash
npm test                    # Interactive watch mode
npm run test:run           # Single run all tests
```

## 🌐 API Integration

The frontend connects to the Django REST API backend:
- **Base URL**: Configurable via `VITE_API_BASE_URL` environment variable
- **Default**: `http://localhost:8000/api`
- **Endpoints**: Movies, Actors, Directors, Genres, Reviews
- **Features**: Pagination, filtering, search, detailed views

### Environment Configuration
Create a `.env` file in the root directory:
```bash
VITE_API_BASE_URL=http://localhost:8000/api
```

For production deployment:
```bash
VITE_API_BASE_URL=https://your-api-domain.com/api
```

## 📱 Component Architecture

### UI Components

- **Button**: Multiple variants (primary, secondary, outline, ghost)
- **Card**: Flexible card component with hover effects
- **Input**: Form input with validation support
- **Loading**: Spinner, card, and page loading states
- **Pagination**: Navigation with page numbers
- **ThemeToggle**: Dark/light mode switcher

### Feature Components

- **MovieCard**: Movie display with favorites functionality
- **MovieGrid**: Responsive grid layout for movies
- **MovieFilters**: Advanced filtering interface
- **Header**: Navigation with responsive mobile menu
- **Layout**: Main application layout wrapper

### Pages

- **HomePage**: Featured movies and reviews
- **MoviesPage**: Movie browsing with filters
- **ActorsPage**: Actor directory with search
- **DirectorsPage**: Director profiles and filmographies
- **FavoritesPage**: User's favorite movies
- **MovieDetailPage**: Detailed movie information

## 🎨 Design System

### Theme Support

- **Light Theme**: Default bright theme
- **Dark Theme**: Dark mode with proper contrast
- **Theme Persistence**: Saved in localStorage
- **System Preference**: Respects OS theme preference

### Responsive Breakpoints

- **Mobile**: < 640px (sm)
- **Tablet**: 640px - 1024px (md, lg)
- **Desktop**: > 1024px (xl, 2xl)

### Grid Systems

- **Movie Grid**: 1 → 2 → 3 → 4 columns
- **Actor/Director Grid**: 1 → 2 → 3 → 4 columns

## Key Features Detail

### Favorites System

- **Local Storage**: Persisted across sessions
- **Add/Remove**: Toggle favorite status
- **Favorites Page**: Dedicated page for favorites
- **Visual Indicators**: Heart icons show favorite status

### Advanced Filtering

- **Multiple Filters**: Genre, director, actor, year, rating
- **Real-time Search**: Instant results as you type
- **Filter Combinations**: Multiple filters work together
- **Clear Filters**: Reset all filters with one click

### Responsive Design

- **Mobile First**: Designed for mobile, enhanced for desktop
- **Touch Friendly**: Large touch targets on mobile
- **Adaptive Layout**: Components adapt to screen size
- **Navigation**: Collapsible mobile menu

## Development Guidelines

### Code Style

- **TypeScript**: Strict mode enabled
- **ESLint**: Code linting and formatting
- **Component Props**: Proper TypeScript interfaces
- **Error Handling**: Graceful error states
