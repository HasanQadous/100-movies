from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

movies = []
for y in soup.find_all(name="h3", class_="title"):
    movies.append(y.get_text())

movies_list = movies[::-1]

for movie in movies_list:
    with open("./movies.txt", mode="a", encoding="utf8") as file:
        file.write(f"{movie}\n")