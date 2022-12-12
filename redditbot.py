import praw

# Replace these values with your own Reddit credentials
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     password='YOUR_PASSWORD',
                     user_agent='YOUR_USER_AGENT',
                     username='YOUR_USERNAME')

# Replace this with the subreddit you want to monitor
subreddit = reddit.subreddit('learnpython')

# This is the message that the bot will post when it finds a new submission
response_message = 'Hi, I am a Reddit bot!'

# This is the main loop of the bot
for submission in subreddit.new(limit=10):
    # Check if the bot has already replied to this submission
    if not submission.saved:
        # Post the response message
        submission.reply(response_message)

        # Save the submission so we don't reply to it again
        submission.save()
