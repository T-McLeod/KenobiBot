import requests
import json
import ast
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("TWITTER_API_KEY")

headers = {
    'Authorization': 'Bearer ' + key,
}

location = 'TwitterIDs.txt'
file = open(location, "r+")
ID = ast.literal_eval(file.read())
file.close()


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def getTweets(userID):
    lastMessage = ID[str(userID)]
    link = "https://api.twitter.com/2/users/{user}/tweets"
    params = (
    ('since_id', lastMessage),
    )
    response = requests.get(link.format(user=userID), headers=headers, params=params)
    try:
        tweets = response.json()['data']
    except:
        return []

    if len(tweets) > 0:
        ID[str(userID)] = tweets[0]['id']
        file = open(location, "w+")
        file.write(json.dumps(ID))
        file.close()
        
        final = []
        for tweet in tweets:
            final.append(tweet['id'])
        return final
    

def getTwitter(users):
    final = []
    for user in users:
        try:
            tweets = getTweets(user)
        except:
            pass
        for tweet in tweets:
            final.append(tweet)
    return final

