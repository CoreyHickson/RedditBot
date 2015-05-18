"""	 
Corey Hickson
Bot to search for certain questions then notifty if they're posted
Reference: https://praw.readthedocs.org/en/v2.1.21/pages/writing_a_bot.html
"""

import time
import praw

r = praw.Reddit("PRAW related-question monitor by /u/Poruku v 1.0 "
		"Url: https://praw.readthedocs.org/en/latest/"
		"pages/writing_a_bot.html")
r.login()

already_done = []
prawWords = ['praw', 'reddit_api', 'mellort']

while True:
	subreddit = r.get_subreddit('learnpython')
	for submission in subreddit.get_hot(limit=10):
		op_text = submission.selftext.lower()
		has_praw = any(string in op_text for string in prawWords)
		# test if it contains a PRAW-related question
		if submission.id not in already_done and has_praw:
			msg = '[PRAW related thread](%s)' % submission.short_link
			r.send_message('Poruku', 'PRAW Thread', msg)
			already_done.append(submission.id)
		print "Checked and sleeping..."
		time.sleep(1800)
