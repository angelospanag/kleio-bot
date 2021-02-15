# Kleio bot

https://twitter.com/KleioBot

A Twitter bot that:

* Aggregates the last 50 tweets of each political party currently in the Greek parliament using
  the [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
  

* Uses Natural Language Processing with the help of a [pre-trained model in the Greek language](https://spacy.io/models/el) to parse sentences, group words with similar
  roots ([lemmatisation](https://en.wikipedia.org/wiki/Lemmatisation)) and dismiss common words ([stop words](https://en.wikipedia.org/wiki/Stop_word))
  

* Creates and posts a word cloud image on its Twitter account for each political party using the above data. This process is not always perfect and you might occasionally notice some duplicated words, or some verbs being conjugated incorrectly. This is due to the language processing model being used, and it will hopefully be improved over time

I have named it Kleio Bot after the [muse Kleio](https://en.wikipedia.org/wiki/Clio) from the Greek mythology who was 'the proclaimer, glorifier and
celebrator of history, great deeds and accomplishments'.

It feels mundane to mention this, but for all intents and purposes this is a project just for fun and to explore the capabilities of technology when it interacts with a very rich and unique language such as Greek. This bot does not 'think' for itself, does not have political affiliations and does not take sides. It simply reproduces the data that it is given and presents it in a very specific and interesting way.
