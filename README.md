# Kleio bot

https://twitter.com/KleioBot

A Twitter bot that:

* Aggregates the last 50 tweets of each political party currently in the Greek parliament using
  the [Twitter API](https://developer.twitter.com/en/docs/twitter-api)


* Uses Natural Language Processing with the help of
  a [pre-trained model in the Greek language](https://spacy.io/models/el) to parse sentences, group words with similar
  roots ([lemmatisation](https://en.wikipedia.org/wiki/Lemmatisation)) and dismiss common
  words ([stop words](https://en.wikipedia.org/wiki/Stop_word))


* Creates and posts a word cloud image on its Twitter account for each political party using the above data. This
  process is not always perfect and you might occasionally notice some duplicated words, or some verbs being conjugated
  incorrectly. This is due to the language processing model being used, and it will hopefully be improved over time

I have named it Kleio Bot after the [muse Kleio](https://en.wikipedia.org/wiki/Clio) from the Greek mythology who was '
the proclaimer, glorifier and celebrator of history, great deeds and accomplishments'.

It feels mundane to mention this, but for all intents and purposes this is a project just for fun and to explore the
capabilities of technology when it interacts with a very rich and unique language such as Greek. This bot does not '
think' for itself, does not have political affiliations and does not take sides. It simply reproduces the data that it
is given and presents it in a very specific and interesting way.

## Prerequisites

* [Python 3.9.*](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/docs/#installation)

### Ubuntu (using `apt`)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
sudo apt install python3-pip python3-dev
```

### MacOS (using `brew`)

```bash
brew install python@3.9 poetry
```

### Windows

Use the above links to download the appropriate executables and install them.

## Installation

### Install dependencies

```bash
poetry install
```

### Activate virtual environment shell

```bash
poetry shell
```

### Create a Twitter app and generate the necessary credentials

In order for this bot to make use of the Twitter API, you must first create an app and generate the necessary consumer
keys and access tokens. Refer to the Twitter
API [documentation](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide) on how to do that.

### Environment variables

Create a `.env` file in the root of the project and add the consumer keys and access tokens generated for your app:

```dotenv
CONSUMER_KEY=...
CONSUMER_SECRET=...
ACCESS_TOKEN=...
ACCESS_TOKEN_SECRET=...
```

## Running the bot manually

***Warning!*** Running this application will actually post word clouds to the Twitter account you have linked using the
environment variables above. To avoid this and just see the generated pictures, comment out the following line:

```python
api.update_with_media(image_path, title)
```

***TODO*** - I might make this adjustable using an environment variable

```bash
python main.py
```

## Running the bot periodically

I am currently using [cron](https://man7.org/linux/man-pages/man5/crontab.5.html) to schedule the bot to run every day
at 9:00 AM UTC (which translates to 11:00 AM Greece time). You can easily experiment using the same process.

You can edit your `cron` schedule with:

```dotenv
crontab -e
```

Assuming the project resides in a home folder of a user `your_user` with Python and `poetry` installed on the same box,
then you can schedule it with adding to your crontab a line like the following:

```
0 9 * * * cd /home/your_user/kleio-bot && /home/your_user/.local/bin/poetry run python main.py
```

Refer to [cron](https://man7.org/linux/man-pages/man5/crontab.5.html) documentation about the necessary syntax to use.
