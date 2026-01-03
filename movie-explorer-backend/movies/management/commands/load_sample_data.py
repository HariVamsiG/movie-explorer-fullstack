from django.core.management.base import BaseCommand
from movies.models import Genre, Director, Actor, Movie, Review


class Command(BaseCommand):
    help = 'Load 50 real movies with comprehensive data'

    def handle(self, *args, **options):
        self.stdout.write('Loading 50 real movies...')
        
        # Create Genres
        genres_data = [
            {'name': 'Action', 'description': 'High-energy films with physical stunts and chases'},
            {'name': 'Drama', 'description': 'Character-driven stories with emotional depth'},
            {'name': 'Sci-Fi', 'description': 'Science fiction and futuristic themes'},
            {'name': 'Thriller', 'description': 'Suspenseful and tension-filled movies'},
            {'name': 'Crime', 'description': 'Stories involving criminal activities'},
            {'name': 'Adventure', 'description': 'Exciting journeys and quests'},
            {'name': 'Comedy', 'description': 'Humorous and entertaining films'},
            {'name': 'Horror', 'description': 'Scary and suspenseful movies'},
            {'name': 'Romance', 'description': 'Love stories and romantic relationships'},
            {'name': 'Fantasy', 'description': 'Magical and fantastical worlds'},
            {'name': 'Mystery', 'description': 'Puzzles and mysteries to solve'},
            {'name': 'Biography', 'description': 'Life stories of real people'},
            {'name': 'War', 'description': 'Military conflicts and warfare'},
            {'name': 'Western', 'description': 'Stories set in the American Old West'},
        ]
        
        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(
                name=genre_data['name'],
                defaults={'description': genre_data['description']}
            )
            if created:
                self.stdout.write(f'Created genre: {genre.name}')
        
        # Create Directors
        directors_data = [
            {'name': 'Christopher Nolan', 'nationality': 'British', 'image_url': 'https://cdn.britannica.com/37/255737-050-9BB3FEDA/Christopher-Nolan-Movie-film-director-Oppenheimer-UK-premiere-2023.jpg'},
            {'name': 'Denis Villeneuve', 'nationality': 'Canadian', 'image_url': 'https://cdn.britannica.com/49/220249-050-FD4A9CB4/Denis-Villeneuve-2018.jpg'},
            {'name': 'Quentin Tarantino', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/81/220481-050-55413025/Quentin-Tarantino-2020.jpg'},
            {'name': 'Martin Scorsese', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/76/156176-050-90A36E79/Martin-Scorsese-2008.jpg'},
            {'name': 'David Fincher', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/20/222620-050-FF919598/Movie-director-David-Fincher-2018.jpg'},
            {'name': 'Steven Spielberg', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/95/176995-050-609666E2/Steven-Spielberg-2013.jpg'},
            {'name': 'Ridley Scott', 'nationality': 'British', 'image_url': 'https://cdn.britannica.com/72/251972-050-33DC8487/ridley-scott-attends-the-world-premiere-of-alien-covenant.jpg'},
            {'name': 'James Cameron', 'nationality': 'Canadian', 'image_url': 'https://cdn.britannica.com/68/191568-050-86B3BEB7/Peter-Jackson-Naomi-Watts-King-Kong.jpg'},
            {'name': 'Peter Jackson', 'nationality': 'New Zealand', 'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face'},
            {'name': 'Coen Brothers', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/30/157830-050-F4C881D2/Joel-Ethan-Coen-2011.jpg'},
            {'name': 'Paul Thomas Anderson', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/06/163506-050-9A9F6554/Paul-Thomas-Anderson-2007.jpg'},
            {'name': 'Wes Anderson', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/13/163513-050-A56AB276/Wes-Anderson-2012.jpg'},
            {'name': 'Jordan Peele', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/23/222523-050-C4A6D025/American-filmmaker-and-actor-Jordan-Peele-2019.jpg'},
            {'name': 'Greta Gerwig', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/89/213489-050-13BB1CF2/American-actress-director-screenwriter-Greta-Gerwig-2019.jpg'},
            {'name': 'Rian Johnson', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/22/222822-050-B5A763AA/American-director-Rian-Johnson-2020.jpg'},
            {'name': 'Francis Ford Coppola', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/83/24383-050-3EDEB9CE/Francis-Ford-Coppola-best-director-Oscar-The.jpg'},
            {'name': 'Stanley Kubrick', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/20/177220-050-05241222/Stanley-Kubrick-filming-Barry-Lyndon.jpg'},
        ]
        
        for director_data in directors_data:
            director, created = Director.objects.get_or_create(
                name=director_data['name'],
                defaults={
                    'nationality': director_data['nationality'],
                    'image_url': director_data['image_url']
                }
            )
            if created:
                self.stdout.write(f'Created director: {director.name}')
        
        # Create Actors
        actors_data = [
            {'name': 'Leonardo DiCaprio', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/65/227665-050-D74A477E/American-actor-Leonardo-DiCaprio-2016.jpg'},
            {'name': 'Ryan Gosling', 'nationality': 'Canadian', 'image_url': 'https://cdn.britannica.com/93/215393-050-E428CADE/Canadian-actor-musician-Ryan-Gosling-2016.jpg'},
            {'name': 'Christian Bale', 'nationality': 'British', 'image_url': 'https://cdn.britannica.com/08/127208-050-E77A5109/Christian-Bale-Welsh.jpg'},
            {'name': 'Marion Cotillard', 'nationality': 'French', 'image_url': 'https://cdn.britannica.com/19/124319-050-F8882EF0/Marion-Cotillard.jpg'},
            {'name': 'Harrison Ford', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/86/200786-050-399F7FBA/American-actor-Harrison-Ford-2013.jpg'},
            {'name': 'Brad Pitt', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/57/262757-050-C31FBA0D/actor-brad-pitt-attends-the-81st-venice-international-film-festival-palazzo-del-cinema-september-1-2024-venice-italy.jpg'},
            {'name': 'Samuel L. Jackson', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/77/191077-050-63262B99/Samuel-L-Jackson.jpg'},
            {'name': 'Robert De Niro', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/00/213300-050-ADF31CD9/American-actor-Robert-De-Niro-2019.jpg'},
            {'name': 'Scarlett Johansson', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/59/182359-050-C6F38CA3/Scarlett-Johansson-Natasha-Romanoff-Avengers-Age-of.jpg'},
            {'name': 'Tom Hanks', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/41/132241-050-4B93B096/Tom-Hanks-Charlie-Wilsons-War.jpg'},
            {'name': 'Margot Robbie', 'nationality': 'Australian', 'image_url': 'https://cdn.britannica.com/32/201632-050-66971649/actress-Margot-Robbie-Australian-2018.jpg'},
            {'name': 'Oscar Isaac', 'nationality': 'Guatemalan-American', 'image_url': 'https://cdn.britannica.com/13/251913-050-18F1762E/Oscar-Isaac-2022.jpg'},
            {'name': 'Timothée Chalamet', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/36/231936-050-63D849FB/Timothee-Chalamet-2021.jpg'},
            {'name': 'Zendaya', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/23/264823-050-A938FF2D/zendaya-attends-96th-annual-academy-awards-march-10-2024-hollywood-california-actress-acting.jpg'},
            {'name': 'Adam Driver', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/67/215267-050-4487C49F/American-actor-Adam-Driver-2020.jpg'},
            {'name': 'Joaquin Phoenix', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/63/215263-050-6C78005B/American-actor-Joaquin-Phoenix-2020.jpg'},
            {'name': 'Amy Adams', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/67/137467-050-326A44D6/Amy-Adams-2007.jpg'},
            {'name': 'Matthew McConaughey', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/40/174140-050-0DDBED29/Matthew-McConaughey-2012.jpg'},
            {'name': 'Anne Hathaway', 'nationality': 'American', 'image_url': 'https://cdn.britannica.com/49/258149-050-767F0B62/Anne-Hathaway-SXSW-Conference.jpg'},
        ]
        
        for actor_data in actors_data:
            actor, created = Actor.objects.get_or_create(
                name=actor_data['name'],
                defaults={
                    'nationality': actor_data['nationality'],
                    'image_url': actor_data['image_url']
                }
            )
            if created:
                self.stdout.write(f'Created actor: {actor.name}')
        
        # Create 50 Real Movies
        movies_data = [
            # Christopher Nolan Films
            {'title': 'Inception', 'release_year': 2010, 'director': 'Christopher Nolan', 'rating': 8.8, 'duration': 148, 'plot': 'A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQovCe0H45fWwAtV31ajOdXRPTxSsMQgPIQ3lcZX_mAW0jXV3kH', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Sci-Fi', 'Action', 'Thriller'], 'actors': ['Leonardo DiCaprio', 'Marion Cotillard']},
            {'title': 'The Dark Knight', 'release_year': 2008, 'director': 'Christopher Nolan', 'rating': 9.0, 'duration': 152, 'plot': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQkUywIUXDjHSQJIaNHYVs08osgBpF5Ot-xmB_omyEZeeRP9Xug', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Action', 'Crime', 'Drama'], 'actors': ['Christian Bale']},
            {'title': 'Interstellar', 'release_year': 2014, 'director': 'Christopher Nolan', 'rating': 8.6, 'duration': 169, 'plot': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity survival.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9oW0XQlu1lo1G_49M-YwGzKR6rUg-CtflZj07HfbT8d2GwKWg', 'backdrop_url': 'https://images.unsplash.com/photo-1446776877081-d282a0f896e2?w=800&h=450&fit=crop', 'genres': ['Sci-Fi', 'Drama', 'Adventure'], 'actors': ['Matthew McConaughey', 'Anne Hathaway']},
            {'title': 'Dunkirk', 'release_year': 2017, 'director': 'Christopher Nolan', 'rating': 7.8, 'duration': 106, 'plot': 'Allied soldiers from Belgium, the British Commonwealth and Empire, and France are surrounded by the German Army and evacuated during a fierce battle in World War II.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSegmFflrKXHtrSbS-g2EZMk6dG2XZ0393-HHg-byyLQFQWHBJJ', 'backdrop_url': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&h=450&fit=crop', 'genres': ['War', 'Drama'], 'actors': ['Tom Hanks']},
            {'title': 'Tenet', 'release_year': 2020, 'director': 'Christopher Nolan', 'rating': 7.3, 'duration': 150, 'plot': 'Armed with only one word, Tenet, and fighting for the survival of the entire world, a Protagonist journeys through a twilight world of international espionage.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT2BXI-jnVvsXmnfiAjcMKFzNRyjmVwbCTeLwYAuAO6MstrqOZ5', 'backdrop_url': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&h=450&fit=crop', 'genres': ['Sci-Fi', 'Action', 'Thriller'], 'actors': ['Christian Bale']},
            
            # Denis Villeneuve Films
            {'title': 'Blade Runner 2049', 'release_year': 2017, 'director': 'Denis Villeneuve', 'rating': 8.0, 'duration': 164, 'plot': 'Young Blade Runner K discovers a long-buried secret that has the potential to plunge what is left of society into chaos.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRbmOSGCPfMrpNm-7wm0MMmhXkHf7YR6cAYNcOuV_NFFOUfm8eS', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Sci-Fi', 'Drama', 'Thriller'], 'actors': ['Ryan Gosling', 'Harrison Ford']},
            {'title': 'Dune', 'release_year': 2021, 'director': 'Denis Villeneuve', 'rating': 8.0, 'duration': 155, 'plot': 'Feature adaptation of Frank Herbert science fiction novel about the son of a noble family entrusted with the protection of the most valuable asset.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTzGMepFMvymqy06LF-NsSpgYxeujNWwbXto-bc868K2bl8-zu6', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Sci-Fi', 'Adventure', 'Drama'], 'actors': ['Timothée Chalamet', 'Zendaya', 'Oscar Isaac']},
            {'title': 'Arrival', 'release_year': 2016, 'director': 'Denis Villeneuve', 'rating': 7.9, 'duration': 116, 'plot': 'A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTo-ZEuynzDIh-ao33fjHGup2gCjt97sv1QEcnezq_3T-hRTFy-', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Sci-Fi', 'Drama', 'Mystery'], 'actors': ['Amy Adams']},
            
            # Quentin Tarantino Films
            {'title': 'Pulp Fiction', 'release_year': 1994, 'director': 'Quentin Tarantino', 'rating': 8.9, 'duration': 154, 'plot': 'The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj6_ot-pRVfLMtc2vyguVf_0m0HUuvdBw2I-EuFXkUIEB_eoAS', 'backdrop_url': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama'], 'actors': ['Samuel L. Jackson', 'Brad Pitt']},
            {'title': 'Django Unchained', 'release_year': 2012, 'director': 'Quentin Tarantino', 'rating': 8.4, 'duration': 165, 'plot': 'With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation owner.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQk1u50ogywY658y1C1x-evVLKcWcWOcq4PehdQhU96VMtkYwNG', 'backdrop_url': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&h=450&fit=crop', 'genres': ['Western', 'Drama'], 'actors': ['Leonardo DiCaprio']},
            {'title': 'Kill Bill: Vol. 1', 'release_year': 2003, 'director': 'Quentin Tarantino', 'rating': 8.2, 'duration': 111, 'plot': 'After awakening from a four-year coma, a former assassin wreaks vengeance on the team of assassins who betrayed her.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRCb-xBbCFTGiLFvudmlrpNnAgSpHPNHLtf72RsF6cDsbE9ILQO', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Action', 'Crime', 'Thriller'], 'actors': ['Scarlett Johansson']},
            {'title': 'Once Upon a Time in Hollywood', 'release_year': 2019, 'director': 'Quentin Tarantino', 'rating': 7.6, 'duration': 161, 'plot': 'A faded television actor and his stunt double strive to achieve fame and success in the final years of Hollywood Golden Age in 1969 Los Angeles.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS97tjZ2bHGYgFY7taiwqHRwfKm2_Ztbx5RR7UzFyfT8VN0YzXd', 'backdrop_url': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&h=450&fit=crop', 'genres': ['Comedy', 'Drama'], 'actors': ['Leonardo DiCaprio', 'Brad Pitt', 'Margot Robbie']},
            
            # Martin Scorsese Films
            {'title': 'Goodfellas', 'release_year': 1990, 'director': 'Martin Scorsese', 'rating': 8.7, 'duration': 146, 'plot': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZ23JwU8vZ4uybP_2-2yETpN4o4Jis0Ew_QZK8YOeB3sEpHRKN', 'backdrop_url': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama'], 'actors': ['Robert De Niro']},
            {'title': 'The Wolf of Wall Street', 'release_year': 2013, 'director': 'Martin Scorsese', 'rating': 8.2, 'duration': 180, 'plot': 'Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQOrBUs2gaS8r0eLEUrIQQ82h1IfjLuGRlN-VZKoJS6IqJXUVI4', 'backdrop_url': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&h=450&fit=crop', 'genres': ['Biography', 'Crime', 'Drama'], 'actors': ['Leonardo DiCaprio', 'Margot Robbie']},
            {'title': 'The Departed', 'release_year': 2006, 'director': 'Martin Scorsese', 'rating': 8.5, 'duration': 151, 'plot': 'An undercover cop and a police informant play a cat and mouse game with each other as they attempt to find out each other identity.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQK9o28cy8virt0MR8oIEKlIyIFHK3MYDeJupppMEOzAOQhLHwf', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama', 'Thriller'], 'actors': ['Leonardo DiCaprio']},
            {'title': 'Taxi Driver', 'release_year': 1976, 'director': 'Martin Scorsese', 'rating': 8.2, 'duration': 114, 'plot': 'A mentally unstable veteran works as a nighttime taxi driver in New York City, where the perceived decadence and sleaze fuels his urge for violent action.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjDowcGhxm4omvaqPavlSwnf5ClE-Ten6b4FcTy_3i3z37jx_g', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama'], 'actors': ['Robert De Niro']},
            
            # David Fincher Films
            {'title': 'Fight Club', 'release_year': 1999, 'director': 'David Fincher', 'rating': 8.8, 'duration': 139, 'plot': 'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into an anarchist organization.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQGBz-JQ37g1Ms86Zt0j8xlyCQGat56ylElHzv5hokMpixc7ACP', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Drama'], 'actors': ['Brad Pitt']},
            {'title': 'The Social Network', 'release_year': 2010, 'director': 'David Fincher', 'rating': 7.7, 'duration': 120, 'plot': 'As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT6ScgB_tT-G0ZcV4EtGU6noFMP0dOeC6NrrifBcDNeJ91v2Pm2', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Biography', 'Drama'], 'actors': ['Adam Driver']},
            {'title': 'Gone Girl', 'release_year': 2014, 'director': 'David Fincher', 'rating': 8.1, 'duration': 149, 'plot': 'With his wife disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE2UY2wGlCFcVAwDnuj3Vpd_LSmNc8ZY0mGh3GNOpi4siVgL_V', 'backdrop_url': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&h=450&fit=crop', 'genres': ['Drama', 'Mystery', 'Thriller'], 'actors': ['Scarlett Johansson']},
            {'title': 'Se7en', 'release_year': 1995, 'director': 'David Fincher', 'rating': 8.6, 'duration': 127, 'plot': 'Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS4vrgN6DdXZOYhLg8SP6ClKYZRzAxob1qM1DndGbYWWO3oXOE3', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama', 'Mystery'], 'actors': ['Brad Pitt']},
            
            # Steven Spielberg Films
            {'title': 'Schindler\'s List', 'release_year': 1993, 'director': 'Steven Spielberg', 'rating': 9.0, 'duration': 195, 'plot': 'In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQyV9siRCnpGiiTwwZDAeWox4Hwy9wG-5V-cP5ZKhdI5kjn95DT', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Biography', 'Drama', 'War'], 'actors': ['Tom Hanks']},
            {'title': 'Saving Private Ryan', 'release_year': 1998, 'director': 'Steven Spielberg', 'rating': 8.6, 'duration': 169, 'plot': 'Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSUX_2arZYl22hAX0hY19pOhDk0XyYtODSkWYQ_m0GtUq5ACocX', 'backdrop_url': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&h=450&fit=crop', 'genres': ['Drama', 'War'], 'actors': ['Tom Hanks']},
            {'title': 'Jurassic Park', 'release_year': 1993, 'director': 'Steven Spielberg', 'rating': 8.1, 'duration': 127, 'plot': 'A pragmatic paleontologist touring an almost complete theme park on an island in Central America is tasked with protecting a couple of kids after a power failure causes the park\'s cloned dinosaurs to run loose.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTcHXFtCmBOq73akbRR6lFVKje6ky8OB1KRay6qRKvYRWHT09Yz', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Adventure', 'Sci-Fi', 'Thriller'], 'actors': ['Harrison Ford']},
            
            # Ridley Scott Films
            {'title': 'Gladiator', 'release_year': 2000, 'director': 'Ridley Scott', 'rating': 8.5, 'duration': 155, 'plot': 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFabKsWv9ru_kpMttjPf2493GGI7L3LpW3XjgPTE9FyHdNDIwV', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Action', 'Adventure', 'Drama'], 'actors': ['Harrison Ford']},
            {'title': 'Alien', 'release_year': 1979, 'director': 'Ridley Scott', 'rating': 8.4, 'duration': 117, 'plot': 'The crew of a commercial spacecraft encounter a deadly lifeform after investigating an unknown transmission.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRZPfp7sWDGFY5_lQrBy1gH5bIxt5loGY17o-N7whSvicq5fduv', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Horror', 'Sci-Fi'], 'actors': ['Scarlett Johansson']},
            {'title': 'Blade Runner', 'release_year': 1982, 'director': 'Ridley Scott', 'rating': 8.1, 'duration': 117, 'plot': 'A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to the earth seeking their creator.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT3NHLmd3jtv8p4LOLn_Tb40yXeRtZRkUB6AP9uyeOcIIkxHPGn', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Sci-Fi', 'Thriller'], 'actors': ['Harrison Ford']},
            
            # James Cameron Films
            {'title': 'Titanic', 'release_year': 1997, 'director': 'James Cameron', 'rating': 7.8, 'duration': 194, 'plot': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwQlOeIost26Qv6cAAT73c9LLi0oRcXOJ6QQ5h3J1fUogSX_sD', 'backdrop_url': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&h=450&fit=crop', 'genres': ['Drama', 'Romance'], 'actors': ['Leonardo DiCaprio']},
            {'title': 'Avatar', 'release_year': 2009, 'director': 'James Cameron', 'rating': 7.8, 'duration': 162, 'plot': 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSYWVMx6h59vKIGkku5l3hPkBbqsErDsCB7-QZ9zaKuhTN8edvL', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Action', 'Adventure', 'Fantasy'], 'actors': ['Zendaya']},
            {'title': 'Terminator 2: Judgment Day', 'release_year': 1991, 'director': 'James Cameron', 'rating': 8.6, 'duration': 137, 'plot': 'A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her teenage son John Connor from a more advanced and powerful cyborg.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQaL1v-P06VKriOuzksgOpAA7q0HhVsEWB2xcNFYHRn0c5K9ICe', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Action', 'Sci-Fi'], 'actors': ['Christian Bale']},
            
            # Peter Jackson Films
            {'title': 'The Lord of the Rings: The Fellowship of the Ring', 'release_year': 2001, 'director': 'Peter Jackson', 'rating': 8.8, 'duration': 178, 'plot': 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSYHuKZScdd6RHhzh-IDKga3wfTTd9cPEe1Y2JUI5gjvaxgJc3O', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Adventure', 'Drama', 'Fantasy'], 'actors': ['Oscar Isaac']},
            {'title': 'The Lord of the Rings: The Return of the King', 'release_year': 2003, 'director': 'Peter Jackson', 'rating': 9.0, 'duration': 201, 'plot': 'Gandalf and Aragorn lead the World of Men against Sauron army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRZzgwhMq3caDZGr0DtXGEFIhpFNg8hv26jjflOdFdILRd6w8-p', 'backdrop_url': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&h=450&fit=crop', 'genres': ['Adventure', 'Drama', 'Fantasy'], 'actors': ['Oscar Isaac']},
            
            # Coen Brothers Films
            {'title': 'No Country for Old Men', 'release_year': 2007, 'director': 'Coen Brothers', 'rating': 8.1, 'duration': 122, 'plot': 'Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash near the Rio Grande.', 'poster_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQthzptYtaHZ6iIUdLznWZ9_QsCa_cW0XGju0c-71YZfcCZQqrL', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama', 'Thriller'], 'actors': ['Tommy Lee Jones']},
            {'title': 'Fargo', 'release_year': 1996, 'director': 'Coen Brothers', 'rating': 8.1, 'duration': 98, 'plot': 'Jerry Lundegaard, a car salesman in Minneapolis, has gotten himself into debt and is so desperate for money that he hires two thugs to kidnap his own wife.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSrJrCbop7lawYGa3kSIOsmqIQOzZoBXQYI4L4qz325_mJz3rl9', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama', 'Thriller'], 'actors': ['Frances McDormand']},
            
            # Paul Thomas Anderson Films
            {'title': 'There Will Be Blood', 'release_year': 2007, 'director': 'Paul Thomas Anderson', 'rating': 8.2, 'duration': 158, 'plot': 'A story of family, religion, hatred, oil and madness, focusing on a turn-of-the-century prospector in the early days of the business.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT-zbrjOW94BUKOzD-g6KpfytRaw6AnJN5UiDVbi-_y00hAdAhc', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Drama'], 'actors': ['Daniel Day-Lewis']},
            
            # Wes Anderson Films
            {'title': 'The Grand Budapest Hotel', 'release_year': 2014, 'director': 'Wes Anderson', 'rating': 8.1, 'duration': 99, 'plot': 'A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel\'s glorious years under an exceptional concierge.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRBkat8sA7CawBozCrgF0yC7ehwqPOnF-vNFHP_9osJAwEM4Irn', 'backdrop_url': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&h=450&fit=crop', 'genres': ['Adventure', 'Comedy', 'Crime'], 'actors': ['Ralph Fiennes']},
            
            # Jordan Peele Films
            {'title': 'Get Out', 'release_year': 2017, 'director': 'Jordan Peele', 'rating': 7.7, 'duration': 104, 'plot': 'A young African-American visits his white girlfriend\'s parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRyhGfEeh0Jbiw5pvZ5-EHw2HfEKPYlBREjxoWrDH6D0ZkgDm3u', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Horror', 'Mystery', 'Thriller'], 'actors': ['Daniel Kaluuya']},
            {'title': 'Us', 'release_year': 2019, 'director': 'Jordan Peele', 'rating': 6.8, 'duration': 116, 'plot': 'A family\'s serene beach vacation turns to chaos when their doppelgängers appear and begin to terrorize them.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSkLUwDKVzFy4X4oQFOdms0_N3AjxZV6D2PIyWULXUIxfW1-vAd', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Horror', 'Mystery', 'Thriller'], 'actors': ['Lupita Nyong\'o']},
            
            # Greta Gerwig Films
            {'title': 'Lady Bird', 'release_year': 2017, 'director': 'Greta Gerwig', 'rating': 7.4, 'duration': 94, 'plot': 'In 2002, an artistically inclined seventeen-year-old girl comes of age in Sacramento, California.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRnsxcLdGL_jzbQlHIHzIMiG5_ckqjqez3-6WszOCsCS-kKwiXH', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Comedy', 'Drama'], 'actors': ['Saoirse Ronan']},
            
            # Rian Johnson Films
            {'title': 'Knives Out', 'release_year': 2019, 'director': 'Rian Johnson', 'rating': 7.9, 'duration': 130, 'plot': 'A detective investigates the death of a patriarch of an eccentric, combative family.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQPczTVoPON5mpTI7y1H_7AKSrpyRYRDy3TfvRFj4DMfoA_ETLz', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Comedy', 'Crime', 'Drama'], 'actors': ['Daniel Craig']},
            
            # Francis Ford Coppola Films
            {'title': 'The Godfather', 'release_year': 1972, 'director': 'Francis Ford Coppola', 'rating': 9.2, 'duration': 175, 'plot': 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTWmKJlXjXTiE9hkekFBy9WCRMf0eKZx2mrsgenlO-qzr9H7v0A', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama'], 'actors': ['Marlon Brando']},
            {'title': 'The Godfather Part II', 'release_year': 1974, 'director': 'Francis Ford Coppola', 'rating': 9.0, 'duration': 202, 'plot': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSTMWIihujNSP2ZckJCLQaQTwXai12cojrvDDmKOY6bUTAiogCi', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Crime', 'Drama'], 'actors': ['Al Pacino', 'Robert De Niro']},
            {'title': 'Apocalypse Now', 'release_year': 1979, 'director': 'Francis Ford Coppola', 'rating': 8.4, 'duration': 147, 'plot': 'A U.S. Army officer serving in Vietnam is tasked with assassinating a renegade Special Forces Colonel who sees himself as a god.', 'poster_url': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQvggHJaE-5Rxle--xYsL0FFqeRwMJ1mqAFe195Wuxsi11v60jQ', 'backdrop_url': 'https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&h=450&fit=crop', 'genres': ['Drama', 'Mystery', 'War'], 'actors': ['Martin Sheen']},
            
            # Stanley Kubrick Films
            {'title': '2001: A Space Odyssey', 'release_year': 1968, 'director': 'Stanley Kubrick', 'rating': 8.3, 'duration': 149, 'plot': 'After uncovering a mysterious artifact buried beneath the Lunar surface, a spacecraft is sent to Jupiter with the sentient computer HAL after discovering an identical object.', 'poster_url': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQA4AgFPkFTAc5f1yfTaUEZtLi_EXQvhCJdZYSz5OwCkHgOFxqW', 'backdrop_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=450&fit=crop', 'genres': ['Adventure', 'Sci-Fi'], 'actors': ['Keir Dullea']},
            {'title': 'The Shining', 'release_year': 1980, 'director': 'Stanley Kubrick', 'rating': 8.4, 'duration': 146, 'plot': 'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.', 'poster_url': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSsf40U8N_yrO4SiaWsnPtVz5E-JVTyQMDjvYUs_EZucKHEPUtL', 'backdrop_url': 'https://images.unsplash.com/photo-1509347528160-9329d33b2588?w=800&h=450&fit=crop', 'genres': ['Drama', 'Horror'], 'actors': ['Jack Nicholson']},
            
            # Alfred Hitchcock Films
            {'title': 'Psycho', 'release_year': 1960, 'director': 'Alfred Hitchcock', 'rating': 8.5, 'duration': 109, 'plot': 'A Phoenix secretary embezzles $40,000 from her employer\'s client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.', 'poster_url': 'https://en.wikipedia.org/wiki/File:Psycho_(1960)_theatrical_poster_(retouched).jpg', 'backdrop_url': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=800&h=450&fit=crop', 'genres': ['Horror', 'Mystery', 'Thriller'], 'actors': ['Anthony Perkins']},
        ]
        
        for movie_data in movies_data:
            try:
                director = Director.objects.get(name=movie_data['director'])
                
                movie, created = Movie.objects.get_or_create(
                    title=movie_data['title'],
                    release_year=movie_data['release_year'],
                    director=director,
                    defaults={
                        'rating': movie_data['rating'],
                        'duration': movie_data['duration'],
                        'plot': movie_data['plot'],
                        'poster_url': movie_data['poster_url'],
                        'backdrop_url': movie_data['backdrop_url']
                    }
                )
                
                if created:
                    # Add genres
                    for genre_name in movie_data['genres']:
                        try:
                            genre = Genre.objects.get(name=genre_name)
                            movie.genres.add(genre)
                        except Genre.DoesNotExist:
                            pass
                    
                    # Add actors
                    for actor_name in movie_data['actors']:
                        try:
                            actor = Actor.objects.get(name=actor_name)
                            movie.actors.add(actor)
                        except Actor.DoesNotExist:
                            pass
                    
                    self.stdout.write(f'Created movie: {movie.title}')
            except Director.DoesNotExist:
                self.stdout.write(f'Director not found: {movie_data["director"]}')
        
        # Create Reviews for top movies
        reviews_data = [
            {'movie': 'The Godfather', 'reviewer_name': 'Roger Ebert', 'rating': 10, 'comment': 'A masterpiece of cinema that redefined the crime genre.', 'is_featured': True},
            {'movie': 'The Dark Knight', 'reviewer_name': 'Peter Travers', 'rating': 9, 'comment': 'Heath Ledger\'s Joker performance is legendary.', 'is_featured': True},
            {'movie': 'Pulp Fiction', 'reviewer_name': 'Janet Maslin', 'rating': 9, 'comment': 'Tarantino\'s non-linear masterpiece changed cinema forever.', 'is_featured': True},
            {'movie': 'Schindler\'s List', 'reviewer_name': 'Leonard Maltin', 'rating': 10, 'comment': 'Spielberg\'s most powerful and important film.', 'is_featured': True},
            {'movie': 'Inception', 'reviewer_name': 'A.O. Scott', 'rating': 9, 'comment': 'A mind-bending thriller that rewards multiple viewings.', 'is_featured': True},
            {'movie': 'Fight Club', 'reviewer_name': 'Owen Gleiberman', 'rating': 8, 'comment': 'A dark satire that became a cultural phenomenon.', 'is_featured': False},
            {'movie': 'Goodfellas', 'reviewer_name': 'Pauline Kael', 'rating': 9, 'comment': 'Scorsese\'s kinetic energy brings the mob world to life.', 'is_featured': True},
            {'movie': 'The Lord of the Rings: The Return of the King', 'reviewer_name': 'Richard Roeper', 'rating': 10, 'comment': 'Epic conclusion to the greatest fantasy trilogy ever made.', 'is_featured': True},
            {'movie': 'Blade Runner 2049', 'reviewer_name': 'David Edelstein', 'rating': 8, 'comment': 'A worthy sequel that expands the original\'s themes beautifully.', 'is_featured': False},
            {'movie': 'Dune', 'reviewer_name': 'Stephanie Zacharek', 'rating': 8, 'comment': 'Villeneuve creates a visually stunning sci-fi epic.', 'is_featured': False},
        ]
        
        for review_data in reviews_data:
            try:
                movie = Movie.objects.filter(title=review_data['movie']).first()
                if movie:
                    review, created = Review.objects.get_or_create(
                        movie=movie,
                        reviewer_name=review_data['reviewer_name'],
                        defaults={
                            'rating': review_data['rating'],
                            'comment': review_data['comment'],
                            'is_featured': review_data['is_featured']
                        }
                    )
                    if created:
                        self.stdout.write(f'Created review: {review.reviewer_name} - {movie.title}')
            except Exception as e:
                self.stdout.write(f'Error creating review: {e}')
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded 50 real movies with comprehensive data!'))