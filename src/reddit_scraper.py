import praw
from src.secrets import PRAW_TOKEN_SECRET, PRAW_TOKEN_ID

def get_words_from_reddit():
    words = []
    reddit = praw.Reddit(client_id=PRAW_TOKEN_ID, client_secret=PRAW_TOKEN_SECRET, user_agent="TaifuWiddies")

    for submission in reddit.subreddit('onebag').top(time_filter="all"):
        is_valid_post = submission.is_self and submission.link_flair_text is not None and "Packing" in submission.link_flair_text
        if is_valid_post:
            words.append(submission.selftext)
    return words

print(get_words_from_reddit())