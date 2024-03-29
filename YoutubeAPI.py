import requests
import json
import requests
import ast
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("YOUTUBE_API_KEY")

location = 'YoutubeIDs.txt'
file = open(location,"r+")
ID = ast.literal_eval(file.read())
file.close()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def getVideo(channel):
    link = 'https://www.googleapis.com/youtube/v3/channels?id={channelID}&key={APIkey}&part=contentDetails'
    response = requests.get(link.format(channelID = channel, APIkey = key)).json()
    uploadID = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    link = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId={upload}&key={API}&part=contentDetails&maxResults=1'
    response = requests.get(link.format(upload = uploadID, API = key)).json()
    try:
        video = response['items'][0]['contentDetails']
    except:
        print(response)
    try:
        if(ID[channel] == video['videoPublishedAt']):
            return None
    except:
        None
    ID[channel] = video['videoPublishedAt']
    file = open(location, "w+")
    file.write(json.dumps(ID))
    file.close()
    return video['videoId']

def getYoutube(users):
    final = []
    try:
        for user in users:
            video = getVideo(user)
            if video!=None:
                final.append(video)
    except:
        pass
    return final

#AIzaSyC8S-L4JatFTKJLOP6sKRdgTjKmkkbbr5w
