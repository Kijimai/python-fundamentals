import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response_html = response.text

my_soup = BeautifulSoup(response_html, "html.parser")

article_tags = my_soup.find_all(name="span", class_="titleline")
article_links  = []

for tag in article_tags:
  current_tag = tag.find("a").get("href")
  article_links.append(current_tag)

all_upvotes = [int(score.getText().split()[0]) for score in my_soup.find_all(name="span", class_='score')]

# get the title and link of the news story with the highest upvote count

# print(len(article_tags), len(article_links), len(all_upvotes))
most_upvote_idx = all_upvotes.index(max(all_upvotes))
most_voted_article_tag = article_links[most_upvote_idx]
most_voted_article_title = article_tags[most_upvote_idx].getText()
print(most_voted_article_tag, most_voted_article_title)