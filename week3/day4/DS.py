import requests
import psycopg2
from random import sample

db_credentials = psycopg2.connect(
    dbname = 'exday3',
    user= 'postgres',
    password ='142321',
    host ='localhost',
    port ='5432'
)

api_url = 'https://restcountries.com/v3.1/all'

num_countries = 10

def fetch_random_countries():
    response = requests.get(api_url)
    countries_data = response.json()
    return sample(countries_data, num_countries)

def write_countries_to_database(countries):
    conn = None
    cur = None

    try:
        conn = psycopg2.connect(**db_credentials)
        cur = conn.cursor()

        for country in countries:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', 'N/A')
            flag = country.get('flags', {}).get('png', 'N/A')
            subregion = country.get('subregion', 'N/A')
            population = country.get('population', 0)

            cur.execute(
                f"INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)",
                (name, capital, flag, subregion, population)
            )

        conn.commit()
        print(f"{num_countries} countries added to the database successfully.")
    except Exception as e:
        print(f"Error writing to the database: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    random_countries = fetch_random_countries()
    write_countries_to_database(random_countries)