from Album import make_album
import string
print("Hi Dear welcome to your album maker")
while True:
    print("\nFeed us with the information of your album\n(Don't forget to enter 'q' to quit at anytime!)\n")
    artist_name = input("Tell us the artist's name: ")
    if artist_name == "q":
        break
    album_title = input("What's the album's title: ")
    if album_title == "q":
        break
    no_of_tracks = input("Number of tracks: (This is optional enter 's' to skip): ")
    if no_of_tracks == "s":
        no_of_tracks = ""
    elif no_of_tracks not in string.digits:
        no_of_tracks = ""
    album = make_album(artist_name.lower(),album_title.lower(),no_of_tracks.lower())
    print(album)