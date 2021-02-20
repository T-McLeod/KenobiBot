import requests
import json
import ast

headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAOqPMwEAAAAAd7QMdV%2FlXFY%2Fi73u6KZ3zCBrSyw%3DXZlLQc7jT0zaz7WB8l0KWj167oKgmqVM6qVrGSpul2AS9rKlVS',
}

location = 'TwitterIDs.txt'
file = open(location,"r+")
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

    if len(tweets)>0:
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
        tweets = getTweets(user)
        for tweet in tweets:
            final.append(tweet)
    return final

#print(getTweets(98047213))
#AAAAAAAAAAAAAAAAAAAAAOqPMwEAAAAAd7QMdV%2FlXFY%2Fi73u6KZ3zCBrSyw%3DXZlLQc7jT0zaz7WB8l0KWj167oKgmqVM6qVrGSpul2AS9rKlVS
