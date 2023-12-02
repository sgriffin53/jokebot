import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='ID_HERE', \
                     client_secret='SECRET_HERE', \
                     user_agent='jokebot', \
                     username='USERNAME_HERE', \
                     password='PASSWORD_HERE')
file = open("jokes.txt","w")
subreddit = reddit.subreddit('jokes')
for submission in reddit.subreddit('jokes').hot(limit=1000):
    title = str(submission.title.encode('utf-8').strip())
    body = submission.selftext.encode('utf-8').strip().splitlines()
    numlines = len(body)
    if numlines == 1:
        body[0] = str(body[0])
        print(title)
        print(body[0])
        if (len(body[0]) < 400): file.write(title + "|" + body[0] + "\n")
file.close()
file = open("jokesdone.txt","w")
file.write("done")
file.close()
