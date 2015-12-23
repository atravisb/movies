import media
import fresh_tomatoes

# instantiate movie objects
matrix = media.Movie("The Matrix",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

amelie = media.Movie("Amelie",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=6Q537310azE")

never_let_me_go = media.Movie("Never Let Me Go",
                              "https://upload.wikimedia.org/wikipedia/en/a/a1/Neverletmegoposterquad.jpg",
                              "https://www.youtube.com/watch?v=sXiRZhDEo8A")

# create a list of movie objects
movies = [matrix, amelie, never_let_me_go]

# build HTML page and render in browser
fresh_tomatoes.open_movies_page(movies)

