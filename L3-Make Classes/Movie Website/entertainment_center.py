import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life", 
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "www.youtube.com/watch?v=uZNHIU3uHT4")
#print(avatar.storyline)
#avatar.show_trailer()
the_godfather = media.Movie("The Godfather",
                            "An aging patriarch transfers control of his mafia empire to his reluctant son",
                            "https://en.wikipedia.org/wiki/The_Godfather#/media/File:Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")
#the_godfather.show_trailer()
_2001 = media.Movie("2001: A Space Odyssey",
                   "Open to interpretation",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcQdmmLZ7lXsw1WRy7c5qN3mka2e9ANSpHIG2INi53P6OVS8KyJo",
                   "https://www.youtube.com/watch?v=lfF0vxKZRhc")
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two men bond over time in prison, eventually finding solace and redemption",
                                       "https://en.wikipedia.org/wiki/The_Shawshank_Redemption",
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")
blade_runner = media.Movie("Blade Runner",
                           "A blade runner must pursue and try to terminate four replicants",
                           "https://en.wikipedia.org/wiki/Blade_Runner#/media/File:Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")
alien = media.Movie("Alien",
                    "The crew of the commercial vessel Nostromo must terminate a life form that has boarded the vessel",
                    "https://en.wikipedia.org/wiki/Alien_(film)#/media/File:Alien_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")
movies = [toy_story, avatar, the_godfather, _2001, the_shawshank_redemption, blade_runner, alien]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
                           

                                       
                                       

                     
