import media
import fresh_tomatoes

# creating the movie objects
mSteveJobs = media.Movie("Steve Jobs", "Awesome Movie about Steve Jobs", "http://www.patentlyapple.com/.a/6a0120a5580826970c01b8d115b9de970c-800wi", "https://www.youtube.com/watch?v=aEr6K1bwIVs")
mAntMan = media.Movie("Marvel Ant-Man", "latest marvel movie", "http://t3.gstatic.com/images?q=tbn:ANd9GcRvTs_PtoegY0eToOxODXT12cfV-AipOD6GftFO0ze7wbociMNB", "https://www.youtube.com/watch?v=pWdKf3MneyI")

# adding further details to the steve jobs movie (beyond minimum specification)
mSteveJobs.director = "Danny Boyle"
mSteveJobs.producers.extend(["Danny Boyle", "Guymon Casady", "Christian Colson", "Mark Gordon", "Scott Rudin"])
mSteveJobs.actors.extend(["Michael Fassbender", "Kate Winslet", "Seth Rogen", "Jeff Daniels"])

# and further details to ant man
mAntMan.director = "Peyton Reed"
mAntMan.producers.extend(["Kevin Feige"])
mAntMan.actors.extend(["Paul Rudd", "Evangeline Lilly", "Corey Stoll", "Bobby Cannavale", "Michael Pena", "Tip \"T.I.\" Harris", "Anthony Mackie", "Wood Harris", "Judy Greer", "David Dastmalchian", "Michael Douglas"])

# creating a movies list
movies = [mSteveJobs, mAntMan]

# generating and opening the movies html page
fresh_tomatoes.open_movies_page(movies)
