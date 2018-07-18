import media
from fresh_tomatoes import open_movies_page

# Let's define an empty list to keep the movies
movies = []

# Append the movies one by one
movies.append(media.Movie(title = "Wonder Park (2018)",
              poster_image_url = "https://goo.gl/uXzuFk",
              trailer_youtube_url = "https://www.youtube.com/watch?v=vYm7mYd0SgE"))
movies.append(media.Movie(title = "Bumblebee (2018)",
              poster_image_url = "https://goo.gl/H4mMG5",
              trailer_youtube_url = "https://www.youtube.com/watch?v=fAIX12F6958"))
movies.append(media.Movie(title = "Mission: Impossible - Fallout (2018)",
              poster_image_url = "https://goo.gl/jW8WSw",
              trailer_youtube_url = "https://www.youtube.com/watch?v=wb49-oV0F78"))
movies.append(media.Movie(title = "Ralph Breaks the Internet: Wreck-It Ralph 2 (2018)",
              poster_image_url = "https://goo.gl/DLWJEs",
              trailer_youtube_url = "https://www.youtube.com/watch?v=lX71_Jcm4po"))

# Render a web page and open it
open_movies_page(movies)
