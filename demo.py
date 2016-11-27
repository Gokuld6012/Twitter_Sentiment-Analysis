from sys import argv
import tweepy
from textblob import TextBlob

name, topic = argv

polarity_count = 0.0
tweetcount = 0


consumer_key = '' #Your Consumer Key
consumer_secret = '' #Your Consumer Secret

access_token = ''  #Your Access Token
access_token_secret= '' #Your Access Token Secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(topic)

for tweet in public_tweets:
    print(tweet.text)
    tweetcount += 1
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
    polarity_count = analysis.sentiment.polarity + polarity_count 
    print("")

#print "The Polarity Count and total tweet is %f and %d"%(polarity_count,tweetcount)
print "The Mean value of the reaction is",polarity_count/tweetcount   #The Overall Polarity of the above tweets

if (polarity_count/tweetcount) > 0.5 :
    print "Twitter is reacting highly positively"
elif (polarity_count/tweetcount) > 0.0 and (polarity_count/tweetcount) < 0.5 :
    print "Twitter is reacting positively"
elif (polarity_count/tweetcount) < 0.0 and (polarity_count/tweetcount) > -0.5 :
    print "Twitter is reacting negatively"
else:
    print "Twitter is reacting highly negatively"