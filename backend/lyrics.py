from dotenv import load_dotenv
import os
import requests
import lyricsgenius




def get_lyrics(artist,track):
    load_dotenv()
    api_key = os.environ.get("CLIENT_TOKEN_GEN")
    

    LyricsGenius = lyricsgenius.Genius(api_key)
    song = LyricsGenius.search_song(artist, track)
    lyrics = song.lyrics
   

#     lyric = """
# Searching for "Noah Kahan" by Stick Season
# Done.

# Verse 1
# As you promised me that I was more than all the miles combined
# You must've had yourself a change of heart like halfway through the drive
# Because your voice trailed off exactly as you passed my exit sign
# Kept on drivin' straight and left our future to the right
# Now I am stuck between my anger and the blame that I can't face
# And memories are somethin' even smoking weed does not replace
# And I am terrified of weather 'cause I see you when it rains
# Doc told me to travel, but there's Covid on the planes

# Chorus
# And I love Vermont, but it's the season of the sticks
# And I saw your mom, she forgot that I existed
# And it's half my fault, but I just like to play the victim
# I'll drink alcohol 'til my friends come home for Christmas
# And I'll dream each night of some version of you
# That I might not have, but I did not lose
# Now you're tire tracks and one pair of shoes
# And I'm split in half, but that'll have to do

# Verse 2
# So I thought that if I piled something good on all my bad
# That I could cancel out the darkness I inherited from Dad
# No, I am no longer funny 'cause I miss the way you laugh
# You once called me "forever," now you still can't call me back

# Chorus
# And I love Vermont, but it's the season of the sticks
# And I saw your mom, she forgot that I existed
# And it's half my fault, but I just like to play the victim
# I'll drink alcohol 'til my friends come home for Christmas
# And I'll dream each night of some version of you
# That I might not have, but I did not lose
# Now you're tire tracks and one pair of shoes
# And I'm split in half, but that'll have to do

# Bridge
# Oh, that'll have to do
# My other half was you
# I hope this pain's just passin' through
# But I doubt it

# Chorus
# And I love Vermont, but it's the season of the sticks
# And I saw your mom, she forgot that I existed
# And it's half my fault, but I just like to play the victim
# I'll drink alcohol 'til my friends come home for Christmas
# And I'll dream each night of some version of you
# That I might not have, but I did not lose
# Now you're tire tracks and one pair of shoes
# And I'm split in half, but that'll have to do
# Have to do
# """
    return lyrics



