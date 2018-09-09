import praw
import time
import os
from selenium import webdriver
from WebDriver import browse

# code below allows the bot to go onto the reddit account and post and stuff
def bot_login():
	reddit = praw.Reddit(client_id = 'TNt3weN6P0aZPQ',
					client_secret = #secret id,
					user_agent = '<console:reddit_bot:0.0.1 (by /u/OPTC_Unit_Bot)>',
					username = #username,
					password = #password)
	return reddit

#takes in my reddit account and a list of id's that is has replied to
def reply(reddit, comments_replied_to):
	#phrase needed to active the bot
	phrase = '!unit '
	
	#loops through all the comments in the subreddit 'test'
	for comment in reddit.subreddit('OnePieceTC').comments():
		# checks to see if '!units' has been said in a comment 
		#and makes sure that it hasn't already replied to that comment
		if phrase in comment.body and comment.id not in comments_replied_to:
			
			#sees what comes after !unit and searches it in the optcDB
			unit = comment.body.replace(phrase, '')
			
			unit = unit.replace(' ', "%20")
			
			result = 'http://optc-db.github.io/characters/#/search/' + unit
			
			#searches the u=unit in the DB and checks if there are results
			numberOfEntries = browse(result)
			
			if("0 to 0 of 0") in numberOfEntries:
				errorMessage = "No such unit with the name " + unit + " exists. Try searching a different name"
				comment.reply(errorMessage)
				
			else:
				comment.reply(result)
			
			#adds the comment id to the list
			comments_replied_to.append(comment.id)
			
			# opens the file and adds in the new id
			with open ("comments_replied_to.txt", "a") as file:
				file.write(comment.id + "\n")
			
	#sleep for 10 seconds
	time.sleep(10)

# saves each id from each comment to a text file
def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as file:
			comments_replied_to = file.read()
			comments_replied_to = comments_replied_to.split("\n")
		
	return comments_replied_to
	

def main():
	reddit = bot_login()
	comments_replied_to = get_saved_comments()
	while True:
		reply(reddit, comments_replied_to)

if __name__ == '__main__':
	main()

