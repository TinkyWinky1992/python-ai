import praw
from Settings import RedditSettings

# Authenticate with Reddit API (replace placeholders with your actual credentials)
config = RedditSettings.get_config()
reddit = praw.Reddit(client_id=config["id"],
                     client_secret=config["secret"],
                     user_agent=config["agent"])


def casual_conversation():
    # Specify the subreddit you want to scrape
    subreddit_name = "CasualConversation"
    subreddit = reddit.subreddit(subreddit_name)

    # Stream all comments from the subreddit
    for comment in subreddit.stream.comments():
        print(comment.body)


casual_conversation()
