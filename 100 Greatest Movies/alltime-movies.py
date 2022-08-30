from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
all_time_movies = response.text

soup = BeautifulSoup(all_time_movies, "lxml")
movies = soup.findAll(name="h3", class_="title")
title_list = [movie.get_text() for movie in movies]
title_list.reverse()

with open("greatest_movies.txt", "a") as g_movies:
  for title in title_list:
    g_movies.write(f"\n{title}")
