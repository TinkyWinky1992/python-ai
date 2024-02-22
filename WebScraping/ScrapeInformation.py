import nltk
import praw

from Settings import RedditSettings
from rake_nltk import Rake

# nltk.download('punkt')
# nltk.download('stopwords')

# Authenticate with Reddit API
config = RedditSettings.get_config()
reddit = praw.Reddit(client_id=config["id"],
                     client_secret=config["secret"],
                     user_agent=config["agent"])


def detect_subjects(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    for rating, keyword in r.get_ranked_phrases_with_scores():
        if rating > 3:
            print(rating, keyword)


def doctor_subjects_data():
    target_subreddit = "AskDocs"

    num_submissions = 10
    data = []

    for submission in reddit.subreddit(target_subreddit).new(limit=num_submissions):

        subject = submission.title
        comments = []
        for comment in submission.comments:
            comments.append(comment.body)

        data.append({"subject": subject, "comments": comments})
    print(data)


def doctor_commadns_data():
    target_subreddit = "AskDocs"

    subreddit = reddit.subreddit(target_subreddit)
    submission = subreddit.submission(id="SUBMISSION_ID")
    comments = submission.comments.list()

    for comment in comments:
        if "keyword1" in comment.body or "keyword2" in comment.body:
            print(comment.body)


