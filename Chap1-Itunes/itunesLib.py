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
    Duplicate_list=[]
    
    for song in Song_Stats.keys():
        if Song_Stats[song]>1:
            Duplicate_list.append((song[0],Song_Stats[song]))
    
    
    if len(Duplicate_list)>0:
        print(f'\n{len(Duplicate_list)} Duplicates were found:')
        for song in Duplicate_list:
            print(song[0])
        
    with open('Duplicates_Report.txt','w') as f:
        for song in Duplicate_list:
            f.write(song[0]+' : '+str(song[1])+'\n')

    return 1

def find_common_songs(filenames):
    """
    Finds shared songs across Itunes playlists.

    """
    playlists={}
    Song_info=[]
    for filename in filenames:
        plist = plistlib.readPlist(filename)
        songs = plist['Tracks']
        Song_info+=list([(songs[song]['Name'],songs[song]['Total Time'],filename) for song in songs.keys()])
    Match=[]
    Unique_songs=list(set(Song_info))
    for i in range(len(Unique_songs)):
        for j in range(i+1,len(Unique_songs)):
            if Unique_songs[i][0]==Unique_songs[j][0]: #and Unique_songs[i][1]==Unique_songs[j][1]:
                Match.append((Unique_songs[i][0],Unique_songs[i][2],Unique_songs[j][2]))
    if len(Match)>0:
        print(f'\n{len(Match)} Shared songs were found:')
        for hit in Match:
            print(hit[0]," : ",hit[1],' and ',hit[2])
    with open('Shared_Songs_Report.txt','w') as f:
        for hit in Match:
            f.write(hit[0]+' : '+hit[1]+' and '+hit[2]+'\n')
    return 1





find_duplicates(playlist)
find_common_songs(['Running.xml','Kurdish.xml','EDM Hits.xml'])
