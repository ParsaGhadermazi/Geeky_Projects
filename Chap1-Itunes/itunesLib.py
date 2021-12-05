import plistlib
import collections
playlist='Running.xml'
def find_duplicates(filename):
  
    """

    Find the duplicates in an Itunes playlist

    """
    plist = plistlib.readPlist(filename)
    songs = plist['Tracks']
    Song_info=[(songs[song]['Name'],songs[song]['Total Time']) for song in songs.keys()]
    Song_Stats=collections.Counter(Song_info)
    for song in Song_Stats.keys():
        if Song_Stats[song]>1:
            print(song)
    return 1

find_duplicates(playlist)