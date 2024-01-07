#EX1

# from bs4 import BeautifulSoup
#
# html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Sports World</title>
#     <style>
#         body { font-family: Arial, sans-serif; }
#         header, nav, section, article, footer { margin: 20px; padding: 15px; }
#         nav { background-color: #333; }
#         nav a { color: white; padding: 14px 20px; text-decoration: none; display: inline-block; }
#         nav a:hover { background-color: #ddd; color: black; }
#         .video { text-align: center; margin: 20px 0; }
#     </style>
# </head>
# <body>
#
#     <header>
#         <h1>Welcome to Sports World</h1>
#         <p>Your one-stop destination for the latest sports news and videos.</p>
#     </header>
#
#     <nav>
#         <a href="#football">Football</a>
#         <a href="#basketball">Basketball</a>
#         <a href="#tennis">Tennis</a>
#     </nav>
#
#     <section id="football">
#         <h2>Football</h2>
#         <article>
#             <h3>Latest Football News</h3>
#             <p>Read about the latest football matches and player news.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/football-video-id" frameborder="0" allowfullscreen>
#                 </iframe>
#             </div>
#         </article>
#     </section>
#
#     <section id="basketball">
#         <h2>Basketball</h2>
#         <article>
#             <h3>NBA Highlights</h3>
#             <p>Watch highlights from the latest NBA games.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/basketball-video-id" frameborder="0" allowfullscreen>
#                 </iframe>
#             </div>
#         </article>
#     </section>
#
#     <section id="tennis">
#         <h2>Tennis</h2>
#         <article>
#             <h3>Grand Slam Updates</h3>
#             <p>Get the latest updates from the world of Grand Slam tennis.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/tennis-video-id" frameborder="0" allowfullscreen></iframe>
#             </div>
#         </article>
#     </section>
#
#     <footer>
#         <form action="mailto:contact@sportsworld.com" method="post" enctype="text/plain">
#             <label for="name">Name:</label><br>
#             <input type="text" id="name" name="name"><br>
#             <label for="email">Email:</label><br>
#             <input type="email" id="email" name="email"><br>
#             <label for="message">Message:</label><br>
#             <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
#             <input type="submit" value="Send">
#         </form>
#     </footer>
#
# </body>
# </html>
# """
#
# soup = BeautifulSoup(html_content, 'html.parser')
#
# title = soup.title.text
# print("Title:", title)
#
# paragraphs = soup.find_all('p')
# print("\nParagraphs:")
# for paragraph in paragraphs:
#     print(paragraph.text)
#
# links = soup.find_all('a', href=True)
# print("\nLinks:")
# for link in links:
#     print(link['href'])

#EX2

# import requests
# from bs4 import BeautifulSoup
#
# url = "https://en.wikipedia.org/robots.txt"
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     print("Robots.txt for en.wikipedia.org:\n")
#     print(soup.get_text())
# else:
#     print(f"Failed to retrieve robots.txt. Status code: {response.status_code}")

#EX3

# import requests
# from bs4 import BeautifulSoup
#
# url = "https://en.wikipedia.org/wiki/Main_Page"
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
#
#     if header_tags:
#         print("Header tags on the Main Page:")
#         for header_tag in header_tags:
#             print(header_tag.text.strip())
#     else:
#         print("No header tags found on the Main Page.")
# else:
#     print(f"Failed to retrieve the Main Page. Status code: {response.status_code}")

#EX4
#
# import requests
# from bs4 import BeautifulSoup
#
# def has_title(url):
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         title_tag = soup.title
#         if title_tag:
#             print("Title found:", title_tag.text.strip())
#             return True
#         else:
#             print("No title tag found on the page.")
#             return False
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")
#         return False



#EX5

# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
#
# def get_us_cert_security_alerts(url):
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         security_alerts_section = soup.find('section', {'id': 'block-system-main'})
#
#         if security_alerts_section:
#             alert_items = security_alerts_section.find_all('div', {'class': 'views-row'})
#
#             current_year = datetime.now().year
#
#             alerts_in_current_year = sum(1 for item in alert_items if str(current_year) in item.text)
#
#             print(f"Number of security alerts issued by US-CERT in {current_year}: {alerts_in_current_year}")
#         else:
#             print("Security alerts section not found on the page.")
#     else:
#         print(f"Failed to retrieve the US-CERT alerts page. Status code: {response.status_code}")
#
# us_cert_url = "https://www.us-cert.gov/ncas/alerts"
#
# get_us_cert_security_alerts(us_cert_url)

# EX6

# import random
# from imdb import IMDb
#
# def get_top_10_movies():
#     ia = IMDb()
#
#     top_250 = ia.get_top250_movies()
#
#     random_movies = random.sample(top_250, min(10, len(top_250)))
#
#     for movie in random_movies:
#         ia.update(movie, info=['title', 'year', 'plot'])
#
#         print(f"Title: {movie['title']}")
#         print(f"Year: {movie['year']}")
#         print(f"Summary: {movie['plot'][0] if 'plot' in movie.keys() else 'N/A'}")
#         print("\n" + "-"*50 + "\n")
#
# if __name__ == "__main__":
#     get_top_10_movies()
