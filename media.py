class Movie():
    """
    Objects of the Movie class represent movies, with the following attributes:
    - movie title
    - url for poster image
    - url for trailer video
    """
    
    def __init__(self, movie_title, poster_image, trailer_video):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_video
