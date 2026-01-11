from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sentiment Analysis Function
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    my_result = {
        "sentiment": sentiment_score,
        "subjectivity": subjectivity_score
    }
    return my_result

# Cosine Similarity Function
def calc_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity_zone = cosine_similarity(vectors)
    return round(similarity_zone[0][1], 3)
