import plistlib
import 

def find_duplicates(filename):
  
    """

    Find the duplicates in an Itunes playlist

    """
    plist = plistlib.readPlist(filename)
    songs = plist['Tracks']
    duplicates = []
    for key in songs:
        song = songs[key]
        if song['Duplicate']:
            duplicates.append(song)
    return duplicates

