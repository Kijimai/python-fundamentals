from bs4 import BeautifulSoup
import requests as rq

chosen_year = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

print(type(chosen_year), chosen_year)

response_html = rq.get(
    f"https://www.billboard.com/charts/hot-100/{chosen_year}/").text

billboard_soup = BeautifulSoup(response_html, "html.parser")

# Choose only the titles of the songs that are inside a ul, li and a h3 element
all_songs_html = billboard_soup.select("ul li h3#title-of-a-story.c-title")

all_songs = [song.getText().strip() for song in all_songs_html]

print(all_songs)
