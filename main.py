import streamlit as st
import pandas as pd
from typing import List  # Add import statement for List type


def get_profanity_scores(tweets: List[str], slurs: List[str]) -> List[int]:
    """
    Returns a list of profanity scores for each tweet in the given list.
    Each profanity score is the number of times a racial slur appears in the tweet.

    Parameters:
    tweets (List[str]): the list of tweets to count the racial slurs in
    slurs (List[str]): the list of racial slurs to count in the tweets

    Returns:
    List[int]: a list of profanity scores, one for each tweet in the list
    """
    profanity_scores = []
    for tweet in tweets:
        profanity_count = 0
        for slur in slurs:
            profanity_count += tweet.count(slur)
        profanity_scores.append(profanity_count)
    return profanity_scores


def main():
    st.title("Profanity Counter")

    # Use st.file_uploader to allow the user to select a CSV file
    tweet_file = st.file_uploader("Select a CSV file containing tweets", type="csv")
    slurs = st.text_input("Slurs (comma-separated):")

    if tweet_file and slurs:  # If tweet file and slurs are not empty
        slurs = slurs.split(",")  # Split slurs by comma
        # Read the CSV file using pandas and extract the "tweet" column
        df = pd.read_csv(tweet_file)
        tweets = df["tweet"].tolist()

        # Count the profanity in the tweets
        profanity_scores = get_profanity_scores(tweets, slurs)

        # Display the profanity scores in a table
        st.write("Profanity Scores:")
        st.write(profanity_scores)


if __name__=="__main__":
    main()
