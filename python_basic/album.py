def make_album(album_title, album_artist):
    album = {"Album Title": album_title.title(), "Album Artist": album_artist.title()}
    return album

print("This program will give you a database of album info. (Enter 'q' at "
"anytime to quit.)")
albums = []
while True:
    a_title = input("Enter album title: ")
    if a_title == 'q': break
    a_artist = input("Enter album artist: ")
    if a_artist == 'q': break
    a_album = make_album(a_title, a_artist)
    print(a_album)
    albums.append(a_album)

if albums:
    print(albums)