import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/v-PjgYDrg70?si=K8sn59FKmasBqPjw")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/d/d6/Avatar_%282009_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=d9MyW72ELq0")


howls_moving_castle = media.Movie("Howl's Moving Castle",
                                  "Sophie comes across a moving castle",
                                  "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                                  "https://www.youtube.com/watch?v=iwROgK94zcM")


wish_dragon = media.Movie("Wish Dragon",
                          "Din meets wish-granting dragon while trying to meet his childhood friend",
                          "https://upload.wikimedia.org/wikipedia/en/d/d7/Wish_Dragon.png",
                          "https://www.youtube.com/watch?v=uWIRyU5fuzU")


over_the_moon = media.Movie("Over The Moon",
                            "Girl builds rocket to go to moon to prove her dead mothers story right",
                            "https://upload.wikimedia.org/wikipedia/en/d/dc/Over_the_Moon_%282020%29.png",
                            "https://www.youtube.com/watch?v=26DIABx44Tw")


spirited_away = media.Movie("Spirited Away",
                            "Chihiro gets spirited away and meets a demanding guest at her new job",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png",
                            "https://www.youtube.com/watch?v=fDUFP7EeXLE")


movies = [toy_story, avatar, howls_moving_castle, wish_dragon, over_the_moon, spirited_away]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movies.__doc__)
