class Movie():
    """This is a class to create movie objects
    Attributes:
        title (str):
        poster_image_url (str):
        trailer_youtube_url (str):
    Methods:
        TBA
    """
    def __init__(self, title=None, poster_image_url=None,
                 trailer_youtube_url=None):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
