#!/bin/python3

# Import libraries needed.
import re
import sys
import requests
from bs4 import BeautifulSoup as bs

# Create a class for printed text options.
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Define URL pattern to match using regular expressions.
url_pattern = re.compile('https?:\/\/(www\.washingtonpost.com\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')

# Define getnews function.
def getnews(news_url):
   # Use GET to get html.
   r = requests.get(news_url)
   # Create if conditional to check if status code was succesful or not.
   if r.status_code != 200:
      if r.status_code == 301 or 307 or 308:
         print('News could not be reached [3xx Error - Redirection]. Check if server moved URLs.')
         sys.exit()
      elif r.status_code == 400 or 401 or 403 or 404 or 408:
         print('News could not be reached [4xx Error - Client Error]. Check if internet is plugged in.')
         sys.exit()
      elif r.status_code == 500 or 501 or 502 or 503 or 504:
         print('News could not be reached [5xx Error - Server Error]. Check if server is alive.')
         sys.exit()
      else:
         print('An error occured getting the news data.')
         sys.exit()
   # Cook some soup (clean the html we extracted).
   soup = bs(r.content, 'html.parser')
   # Start defining variables we are going to use and print later.
   article_title = soup.title.string
   div_headline = soup.find(attrs={"data-qa": "headline-text"})
   headline = div_headline.text
   div_publishtime = soup.find('span', class_='gray-dark display-date')
   publishtime = div_publishtime.text
   div_paragraphs = soup.find_all('p', class_='font-copy font--article-body gray-darkest ma-0 pb-md')
   body = ''
   for paragraph in div_paragraphs:
      body += "\n\n" + paragraph.text
   # Print relevant information with text styling and good formatting.
   print('\n\n' + color.BOLD + article_title + color.END)
   print('Published: ' + publishtime + '\n\n')
   print(color.BOLD + color.RED + headline + color.END)
   print(body)

# Define main function to call as program runs.
def main():
   # Take url as argument using the sys library.
   news_url = str(sys.argv[1])
   # Create if conditional to check if the url matches the pattern we made earlier with regex.
   if url_pattern.match(news_url):
      getnews(news_url)
   else:
      print('Invalid URL for The Washington Post. Check your URL and try again.')
      sys.exit()

# When run, run main function.
if __name__ == "__main__":
    main()
