import requests
from bs4 import BeautifulSoup

response_html = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

my_soup = BeautifulSoup(response_html, "html.parser")

all_movies = my_soup.find_all(name="h3", class_="title")
all_movies.reverse()
for movie in all_movies:
    current_movie = movie.getText()
    with open('./all_movies.txt', mode="a", encoding="utf-8") as movies_data:
        movies_data.write(current_movie + "\n")
