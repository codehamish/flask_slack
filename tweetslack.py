
 # Write a program to post on twitter and slack. 

#import twitter slack and dotenv libraries
import os
from TwitterAPI import TwitterAPI

from flask import Flask, request, Response

from slackclient import SlackClient

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
 
 # assign keys

consumer_key =os.environ["CONSUMER_KEY"]
consumer_secret =os.environ["CONSUMER_SECRET"]
access_token_key =os.environ["ACCESS_TOKEN_KEY"]
access_token_secret =os.environ["ACCESS_TOKEN_SECRET"]

 # function to post message on twitter and slack

def twitter_slack(message):
	api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
 # input message
	tweet_slack = message
 # post message on slack
	slack_token = os.environ["SLACK_API_TOKEN"]
	sc = SlackClient(slack_token)
	sc.api_call(
	"chat.postMessage",
	channel="general",
	text=tweet_slack
	)
 # post message on twitter
	r = api.request('statuses/update', {'status': tweet_slack})	
	return("{} has been sent to Slack and Twitter.".format(tweet_slack))
	
