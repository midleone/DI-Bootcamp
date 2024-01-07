# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
#
# url = "https://www.imdb.com/chart/top/"
# response = requests.get(url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html5lib')
#     movie_list = soup.select('td.titleColumn')
#
#     movies = []
#
#     for movie in movie_list:
#         title = movie.find('a').get_text()
#         year = movie.find('span').get_text()[1:-1]
#         rating = movie.find('strong').get_text()
#         link = "https://www.imdb.com" + movie.find('a')['href']
#
#         movie_details = {
#             'Title': title,
#             'Year': year,
#             'Rating': rating,
#             'Link': link
#         }
#         movies.append(movie_details)
#
#     for movie in movies:
#         print(f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}, Link: {movie['Link']}")
#
#     df = pd.DataFrame(movies)
#     df.to_csv('imdb_top_movies.csv', index=False)
#     print("\nData has been saved to 'imdb_top_movies.csv'")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
