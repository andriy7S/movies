import fresh_tomatoes
import media

# These are instances of my favorite movies
# with instance viriebles
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in "
                           "space in an attempt to ensure humanity's "
                           "survival.",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1__SX1242_SY800_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")


avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a "
                     "unique mission.",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1__SX998_SY800_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


once_upon = media.Movie("Once Upon a Time in America",
                        "A former Prohibition-era Jewish gangster returns to "
                        "the Lower East Side of Manhattan over thirty years "
                        "later.",
                        "http://ia.media-imdb.com/images/M/MV5BNDMwMDcyODkzOV5BMl5BanBnXkFtZTcwNTQ1Njg3OA@@._V1__SX1242_SY800_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=mzhX2PD6Srw")


edge_of_tommorow = media.Movie("School of Rock",
                               "A military officer is brought into an alien "
                               "war against an extraterrestrial enemy.",
                               "http://ia.media-imdb.com/images/M/MV5BMTc5OTk4MTM3M15BMl5BanBnXkFtZTgwODcxNjg3MDE@._V1__SX1242_SY800_.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")

madagascar = media.Movie("Madagascar",
                         "Animals from New York Zoo escape, unwittingly "
                         "assisted by four absconding penguins, "
                         "and find themselves in Madagascar. ",
                         "http://ia.media-imdb.com/images/M/MV5BMTY4NDUwMzQxMF5BMl5BanBnXkFtZTcwMDgwNjgyMQ@@._V1__SX1242_SY800_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=dm-eiFVtRws")

raiders = media.Movie("Raiders of the Lost Ark",
                      "Archaeologist and adventurer Indiana Jones is hired "
                      "by the US government to find the Ark of the Covenant "
                      "before the Nazis.",
                      "http://ia.media-imdb.com/images/M/MV5BMjA0ODEzMTc1Nl5BMl5BanBnXkFtZTcwODM2MjAxNA@@._V1__SX1242_SY800_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=XkkzKHCx154")

# here is variable "movies" which contains list of movies
# and we open_movies_page with "fresh_tomatoes"
movies = [interstellar, avatar, once_upon, edge_of_tommorow, madagascar,
          raiders]
fresh_tomatoes.open_movies_page(movies)
