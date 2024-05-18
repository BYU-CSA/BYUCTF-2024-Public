import praw
import nltk
from nltk.tokenize import word_tokenize

# Initialize PRAW with your Reddit API credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT"
)

# Function to scrape comments from a subreddit and collect words into a word list
def scrape_comments(subreddit_name, limit=20):
    word_list = []
    subreddit = reddit.subreddit(subreddit_name)

    # Iterate over hot submissions and collect comments
    for submission in subreddit.hot(limit=limit):
        submission.comments.replace_more(limit=0)  # Replace 'MoreComments' objects
        for comment in submission.comments.list():
            # Tokenize the comment into words
            words = word_tokenize(comment.body)
            # Add words to the word list
            word_list.extend(words)

    return word_list

# Scrape comments from both subreddits
conservative_words = scrape_comments("conservative")
liberal_words = scrape_comments("liberal")

# Save the word lists to files
with open("conservative_words.txt", "w") as f:
    f.write("\n".join(conservative_words))

with open("liberal_words.txt", "w") as f:
    f.write("\n".join(liberal_words))

print("Word lists saved successfully.")
