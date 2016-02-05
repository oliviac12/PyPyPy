from bs4 import BeautifulSoup
import urllib2
import re # Regular expressions
from time import sleep # To prevent overwhelming the server between connections
from collections import Counter # Keep track of our term counts
#from nltk.corpus import stopwords # Filter out stopwords, such as 'the', 'or', 'and'
#import pandas as pd

#The website you want to scrape
website = "https://www.yelp.com/careers/job-openings/e733f9c7-a970-4075-a403-d99fdc55675b?description=Data-Scientist-New-Grad_College-Engineering-Product_San-Francisco-CA&lever-source=indeed"
site = urllib2.urlopen(website).read() # Connect to the job posting
    
    #except: 
    #    return   # Need this in case the website isn't there anymore or some other weird connection problem 


soup_obj = BeautifulSoup(site) # Get the html from the site

for script in soup_obj(["script", "style"]):
	script.extract()
	 # Remove these two elements from the BS4 object
text = soup_obj.get_text().encode('utf-8')# Get the text from this
#This gets all the plain text in this page excluding html syntax 


#plain text -> bring into lines using splitlines(but it comes quotations) -> get rid of quoration using line.strip() 

lines = (line.strip() for line in text.splitlines()) 
#MAYBE JUST THIS!!!!
# for line in text.splitlines():
# 	if line:
# 		print(line.strip())
	

chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # break multi-headlines into a line each (OLIVIA THINKS THIS LINE IS UNNECESSARY)

def chunk_space(chunk):
	chunk_out = chunk + ' '# Need to fix spacing issue
	return chunk_out
    
text= ''.join(chunk_space(chunk) for chunk in lines if chunk) # Get rid of all blank lines and ends of line
# print(text)



    # # Now clean out all of the unicode junk (this line works great!!!)

    # try:
    #     text = text.decode('unicode_escape').encode('ascii', 'ignore') # Need this as some websites aren't formatted
    # except:                                                            # in a way that this works, can occasionally throw
    #     return                                                         # an exception

text = re.sub("[^a-zA-Z.+3]"," ", text)  # Now get rid of any terms that aren't words (include 3 for d3.js)
                                                # Also include + for C++ #WHY? BUT IT'S OKAY 


text = text.lower().split()  # Go to lower case and split them apart GOOD LINE, BUT rfamiliar is R and familar
#maybe dont lower case it, and find the words start with lower case, and upper case show later in the word to detect this kind of problem


    # stop_words = set(stopwords.words("english")) # Filter out any stop words
    # text = [w for w in text if not w in stop_words]



    # text = list(set(text)) # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed
    #                         # or not on the website)