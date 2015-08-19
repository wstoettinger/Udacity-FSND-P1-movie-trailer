import webbrowser

# defining the Movie class
class Movie():
    # defining the constructor and assigning the variables
    def __init__ (self, title, storyline, poster_image, youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.wikipedia_url = ""
        self.director = ""
        # creating two empty lists here which can be extenden from outside the module/class
        self.producers = []
        self.actors = []

    # defining a function to open the youtube url in the browser
    def showTrailer(self):
        webbrowser.open(self.youtube_trailer)

