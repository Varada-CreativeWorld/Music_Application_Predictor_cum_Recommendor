# Music-Application : Predictor cum Recommender

This is a Music Application that predicts the genre of the uploaded song and recommends song based on content based recommendation engine. To classify songs, KNN algorithm has been used and it is trained on GTZAN dataset consisting of 1000 audio tracks each 30 seconds long. It contains 10 genres, each represented by 100 tracks. The tracks are all 22050Hz Mono 16-bit audio files in .wav format. The accuracy received using above algorithm is 70%.

For recommendation engine, content based recommendation algorithm is used, it works with the data that the user provides explicitly by generating their own public or private playlists. As the user provides more inputs or takes actions on the recommendations, the engine becomes more and more accurate.

Video Link of the Project : https://drive.google.com/file/d/1-uVA4zbA2BNlHerXz6zQp-wSRrWVlqNB/view?usp=sharing

# Technologies Used:

React + Redux
Flask
Python
Spotipy Library and Spotify API

# Major Functionalities of the Project:
• The system logs in user using Spotify API and receives Spotify Authentication Token in ‘user-read-private’ scope.

• The is allowed to upload wav extension file and the features extracted from the uploaded song to send to Genre Prediction Model.

• The classified song type is shown to the user.

• The user can play, search, and download songs through the application.

• The user is suggested to create public or private playlist so that the recommendation engine can work smoothly.

• These user created playlist is processed using Content Based Recommendation Engine and top 40 songs are recommended to the user.

# Limitations of the Project
• The application cannot predict songs of multiple genre combinations accurately.

• The recommendation engine is trained on a dataset which consists of limited number of songs and might not include popular songs.

• GTZAN dataset itself consist of some limitations hence developers needs to find other reliable datasets for genre prediction.

• The system is not efficient for visually challenged individuals. • Private mode and Public mode is not incorporated to switch recommendation engine.

# References
https://data-flair.training/blogs/python-project-music-genre-classification/
https://medium.com/excited-developers/file-upload-with-react-flask-e115e6f2bf99
https://levelup.gitconnected.com/how-to-create-a-spotify-music-search-app-in-react-1d71c8007e45
https://www.youtube.com/watch?v=tooddaC14q4&t=1167s
