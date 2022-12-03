# Import the necessary libraries
import praw
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import statistics

# Connect to the Reddit API
reddit = praw.Reddit(client_id="your_client_id",
                     client_secret="your_client_secret",
                     user_agent="your_user_agent")

# Create a SentimentIntensityAnalyzer instance
analyzer = SentimentIntensityAnalyzer()

# Retrieve the posts from the subreddit
subreddit = reddit.subreddit("subreddit_name")
posts = subreddit.new(limit=100)

# Analyze the sentiment of each post
scores = []
for post in posts:
    # Use the analyzer.polarity_scores() method to get the sentiment scores for the post text
    scores.append(analyzer.polarity_scores(post.title + post.selftext))

# Calculate the average sentiment scores
positive_scores = [s["pos"] for s in scores]
negative_scores = [s["neg"] for s in scores]
neutral_scores = [s["neu"] for s in scores]
compound_scores = [s["compound"] for s in scores]

avg_positive = statistics.mean(positive_scores)
avg_negative = statistics.mean(negative_scores)
avg_neutral = statistics.mean(neutral_scores)
avg_compound = statistics.mean(compound_scores)

# Create the user interface using streamlit
st.title("Sentiment Analysis of r/subreddit_name")

# Create a sidebar with sliders for each sentiment category
st.sidebar.title("Sentiment Categories")

positive = st.sidebar.slider("Positive", 0.0, 1.0, avg_positive)
negative = st.sidebar.slider("Negative", 0.0, 1.0, avg_negative)
neutral = st.sidebar.slider("Neutral", 0.0, 1.0, avg_neutral)
compound = st.sidebar

