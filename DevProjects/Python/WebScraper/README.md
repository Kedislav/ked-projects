# DevProjects - Washington Post News Scraper

This is an open source project taken from [DevProjects](http://www.codementor.io/projects). It scrapes a Washington Post URL and prints the news to your terminal. You can find the project requirements here: [Web scraper to get news article content](https://www.codementor.io/projects/tool/web-scraper-to-get-news-article-content-atx32d46qe). Built with Python3, using the parsing library [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

The difficulties I encountered while working on this project were as follows:
1. Reading the BeautifulSoup docs and not understanding any of it.
2. Requests was fairly easy, but getting the text from the html in a formatted way was hard and did not work at all at first.
3. Re-learning html elements, classes and etc.
4. Separating the different variables such as title, heading, date and body.

After sorting those out, the rest was figuring out how to build the program and enabling fail-checks. The name of the program in the screenshot will be different because I had submitted it with that name to DevProjects.

## Screenshot
<img src=https://i.imgur.com/ijK1rEw.png/>

## Installation
You will need Python installed in your system. You can install it from a terminal using your preferred package manager, or by following the instructions on [the official Python downloads page](https://www.python.org/downloads/). Download the repository .zip file or use the `git clone <this_repository's_link>`. Inside the repository directory install the required dependencies. Just run the following command in a terminal:
```bash
>  pip3 install -r requirements.txt
```

## How to use
Run this command in a terminal inside the repository's directory:
```bash
> python3 scrape_washingtonpost.py <news_url>
```

Example:
```bash
> python3 scrape_washingtonpost.py https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/
```
