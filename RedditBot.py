# based off of Reddit user /u/Scotty_the_Hamster and praw documentation
import praw
import time

r = praw.Reddit(user_agent = "Reactions gifs by /u/Poruku.")
print "[!] Logging in..."
r.login()

words_to_match = ["hello"]
cache = []

def run_bot():
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit=25)
	
	for comment in comments:
		comment_text = comment.body.lower()
		is_match = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and is_match:
			comment.reply("[Hola!](http://www.reactiongifs.com/r/dora.gif)")
			cache.append(comment.id)
			print "Match found: %s" % comment.body

while True:
	run_bot()
	time.sleep(10)
