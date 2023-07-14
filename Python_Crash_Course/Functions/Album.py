def make_album(artist_name: str, album_title: str, no_of_tracks= ""):
    """_summary_

    Args:
        artist_name (str): artist name
        album_title (str): Title of the album
        no_of_tracks (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """    
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