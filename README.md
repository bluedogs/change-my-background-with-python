# Change My Background with Python

This is a small app to put in my crontab to go to [Unsplash](https://unsplash.com/developers) grab a random picture, download it, set it as my desktop background, and post a tweet about it.

Check out [@endo_img](https://twitter.com/endo_img) on twitter to see the recent pictures.

## Needed:

I have all the files in one directory, and setup cron to run 'changeBackground.py'.

Unsplash API app and key. 
	- https://unsplash.com/developers
	- You just need READ type rights on your app as it doesn't POST (YET)

Twitter API keys and tokens
	- rights to POST an update user timeline

Written for Python 2.7 on OSX 10.11

Have a better way? 
Want to make a change? 

fork it, update it, push it. hit me up on twitter [@endodino.](https://twitter.com/endodino)

## TO DO:
 - Add 'likes' to Unsplash pics
	- requires Unsplash Oauth
	- Once a picture is set as my background, give it a like

 - Code clean up
    - collapse to one file


