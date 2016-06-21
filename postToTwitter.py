import apiKey
import getRandomPic

# Pull in twitter API thingies

token = apiKey.token
token_key = apiKey.token_key
con_secret = apiKey.con_secret
con_secret_key = apiKey.con_secret_key


# Pull in Username and image ink
unplashUsername = getRandomPic.userName
unplashPicURL = getRandomPic.link_URL
unsplashFilename = getRandomPic.fileName

# format a tweet to yourself, because your that way
tweet = '@endodino, I changed your background. photographer credit: ' + unplashUsername + ' link: ' + unplashPicURL

# get the twitters

from twitter import *

t = Twitter(
auth=OAuth(token, token_key, con_secret, con_secret_key))

# Update your status
t.statuses.update(status=tweet)


