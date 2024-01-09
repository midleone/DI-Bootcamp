import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the HTML content of the chosen website
url = "https://github.com/topics"
response = requests.get(url)

# Print the status code of the response
print("Status Code:", response.status_code)

if response.status_code == 200:
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Identify and extract information (titles and descriptions)
    topic_titles = [title.text.strip() for title in soup.select('h3.f3 a')]
    topic_descriptions = [desc.text.strip() for desc in soup.select('.f5')]

    # Print the length and content of each extracted list
    print("\nLength of topic_titles:", len(topic_titles))
    print("Content of topic_titles:", topic_titles[:5])
    print("\nLength of topic_descriptions:", len(topic_descriptions))
    print("Content of topic_descriptions:", topic_descriptions[:5])

    # Create a Python dictionary to structure the extracted data
    data_dict = {'Title': topic_titles, 'Description': topic_descriptions}

    # Convert the dictionary into a pandas DataFrame
    df = pd.DataFrame(data_dict)

    # Print the DataFrame to confirm its structure and contents
    print("\nDataFrame structure and contents:\n", df.head())

    # Save the data into a .csv file
    df.to_csv('github_topics.csv', index=False)
    print("\nData has been saved to 'github_topics.csv'")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
