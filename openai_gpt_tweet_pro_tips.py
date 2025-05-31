import tweepy
import os
from openai import OpenAI

# Set the environment variables
consumer_key            = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret         = os.environ['TWITTER_CONSUMER_SECRET']
access_token_key        = os.environ['TWITTER_ACCESS_TOKEN_KEY']
access_token_secret     = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Initialize OpenAI client (modern API v1.0+)
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
model                   = 'gpt-3.5-turbo'

MAX_TOKENS              = 60


prompt        = "Pro Python programming tip:"
messages      =[{"role": "system",    "content": "You are a helpful assistant who is professional python develeper with advance knowledge of python programming"},
                {"role":   "user",    "content": prompt}]


# This code generates a Python tip using OpenAI's modern client API
def generate_python_tip(prompt=prompt, max_tokens=MAX_TOKENS):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.9,
        max_tokens=max_tokens,
        messages=messages
    )

    tip = response.choices[0].message.content.strip()
    
    # Ensure the message is within Twitter's character limit
    #tip = (tip[:277] + '...') if len(tip) > 280 else tip

    return tip

# Post a tweet to your twitter account using modern tweepy API
def post_tweet(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret, message=generate_python_tip()):
    # Create tweepy client (v2 API)
    client_v2 = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token_key,
        access_token_secret=access_token_secret
    )
    
    # Post tweet using v2 API
    response = client_v2.create_tweet(text=message)
    return response


response = post_tweet()
print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
