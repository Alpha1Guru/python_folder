def make_album(artist_name, album_title,no_of_tracks= ""):
    music_album = {"artist": artist_name,
                    "album title": album_title,}
    if no_of_tracks:
        music_album["Number of tracks"] = int(no_of_tracks)
    return music_album
# franklin = make_album("franklin","my world need you")
# print(franklin)
# Hope = make_album("hope","you make my heart")
# print(Hope)
# jay_jay = make_album("jay jay","songs of revivals",no_of_tracks="6")
# print(jay_jay)