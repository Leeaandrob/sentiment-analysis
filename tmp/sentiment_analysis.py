import nltk
from twython import Twython
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def return_trainer():
    data = open('training.txt')
    data = data.readlines()
    return [d.split('\t') for d in data]


def bagOfWords(tweets):
    wordsList = []
    for (words, sentiment) in tweets:
        wordsList.extend(words)
        return wordsList


def wordFeatures(wordList):
    wordList = nltk.FreqDist(wordList)
    wordFeatures = wordList.keys()
    return wordFeatures


def getFeatures(doc):
    docWords = set(doc)
    feat = {}
    for word in wordFeatures:
        feat['contains(%s)' % word] = (word in docWords)
        return feat


tweets = [(d[1], 'positive') if d[0] == '1' else (d[1], 'negative')
          for d in return_trainer()]

positiveTweets = [data for data in tweets if data[1] == 'positive']
negativeTweets = [data for data in tweets if data[1] == 'negative']


tweets = []
for (words, sentiment) in positiveTweets + negativeTweets:
    words_filtered = [e.lower() for e in nltk.word_tokenize(words) if len(
        e) >= 3]
    tweets.append((words_filtered, sentiment))

for t in tweets:
    print(t)

wordFeatures = wordFeatures(bagOfWords(tweets))


data_trainer = return_trainer()

training_set = nltk.classify.apply_features(getFeatures, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

print(classifier.show_most_informative_features(32))


ConsumerKey = "6TO19L8LlJouqnztJ6hZkCgsA"
ConsumerSecret = "gK5dcQFlgS1lLTMPdhsqh046v48VfGYIpWqENwEhwLaFEpX0Pv"
AccessToken = "257611954-EBfaOkObL04YTCB2NEC39C5GzhyTIGMGcF1TNXul"
AccessTokenSecret = "YrvPzGj97TsLR9XRUp5ESbP3KxlMfezHVnmex5RNZb3y6"


twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)

queryText = "#VemPraRuaBrasil"
result = twitter.search(q=queryText)


for status in result["statuses"]:
    print("Tweet: {0} \n Sentiment: {1} \n".format(
        status["text"], classifier.classify(getFeatures(
            status["text"].split()))))


for status in result["statuses"]:
    blob = TextBlob(status['text'], analyzer=NaiveBayesAnalyzer())
    print("Tweet: {0} \n Sentiment: {1} \n".format(status['text'],
                                                   blob.sentiment))
