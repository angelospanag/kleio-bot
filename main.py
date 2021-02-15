import os
import pathlib
import re
from datetime import datetime

import matplotlib.pyplot as plt
import spacy
import tweepy
from dotenv import load_dotenv
from wordcloud import WordCloud

load_dotenv()

consumer_key: str = os.getenv('CONSUMER_KEY')
consumer_secret: str = os.getenv('CONSUMER_SECRET')
access_token: str = os.getenv('ACCESS_TOKEN')
access_token_secret: str = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Twitter account of political parties in Greece
# In ascending order based on the number of parliament seats held after the 2019 Greek legislative election
# https://en.wikipedia.org/wiki/2019_Greek_legislative_election
twitter_accounts: list[str] = ['mera25_gr', 'ellinikilisi', 'gt_kke', 'kinimallagis', 'syriza_gr', 'neademokratia']

# Load Greek NLP model
nlp = spacy.load('el_core_news_md')

# Record timestamp when the script starts to run
timestamp = datetime.now()


def generate_account_word_cloud(twitter_account: str, number_of_tweets: int) -> None:
    tweets = api.user_timeline(screen_name=twitter_account,
                               count=number_of_tweets,
                               tweet_mode='extended')
    all_tokens = []
    for tweet in tweets:
        # Text might be a retweet, try to parse it first as such
        try:
            full_text = tweet.retweeted_status.full_text
        except AttributeError:
            full_text = tweet.full_text
        full_text = re.sub(r'(https://t.co\/[^\s]+|&amp|&gt)', '',
                           full_text, flags=re.MULTILINE)
        doc = nlp(full_text)
        new_tokens = [
            token.lemma_ for token in doc if not token.is_stop]
        if len(new_tokens) > 2:
            if '@' in new_tokens[1]:
                del new_tokens[1]
        if len(new_tokens) > 1:
            if '@' in new_tokens[0] or new_tokens[0] == 'rt':
                del new_tokens[0]

        all_tokens += new_tokens
    tokens_str = ' '.join(all_tokens)
    word_cloud = WordCloud(width=800, max_font_size=80,
                           height=400).generate(tokens_str)
    plt.figure(figsize=(20, 10))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    title: str = f'Word cloud for account @{twitter_account} using its last {number_of_tweets} tweets\ngenerated on {timestamp.strftime("%Y-%m-%d %H:%M")} UTC'
    plt.title(f'{title} by @KleioBot', fontdict={'size': 30})
    image_path = pathlib.Path(pathlib.Path.cwd() / 'images' /
                              f'{twitter_account}_{timestamp.strftime("%Y_%m_%d_%H_%M")}.png')
    plt.savefig(image_path)

    api.update_with_media(image_path, title)


if __name__ == '__main__':
    for account in twitter_accounts:
        generate_account_word_cloud(
            twitter_account=account, number_of_tweets=50)
