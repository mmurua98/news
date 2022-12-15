import datetime
import requests

# Get data from this site, using the API KEY
URL = ('https://newsapi.org/v2/top-headlines?')
API_KEY = '6de43fab6f6d40c3b55dfaab6da93ff5'

#Get data by category
# def get_articles_by_category(category):
#     query_parameters = {
#         "category": category,
#         "sortBy": "top",
#         "country": "gb",
#         "apiKey": API_KEY
#     }
#     return get_articles(query_parameters)

#Get data articles or results
def get_articles(params):
    response = requests.get(URL, params=params)
    articles = response.json()['articles']

    global title, url, results, image, publishedAt
    results = []

    for article in articles:
        results.append(
            {
                "title": article["title"], 
                "url": article["url"],
                "image": article['urlToImage'],
                "publishedAt": datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y, %H:%M:%S")

            })

    for result in results:
       
        title = result['title']
        url = result['url']
        image = result['image']
        publishedAt = result['publishedAt']
        # publishedAt = datetime.datetime.strptime(result['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y, %H:%M:%S")
        # new_format = "%Y-%B-%d"
        # publishedAt.strftime(new_format)
        # print(result['title'])
        # print(result['url'])
        # print(image)
        # print('')
        #print(results)

#print(get_articles_by_category('technology'))

#Get trending articles
def get_trending_articles():
    query_parameters = {
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)

def get_business_articles():
    query_parameters = {
        "category": "business",
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)

def get_entertainment_articles():
    query_parameters = {
        "category": "entertainment",
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)

def get_general_articles():
    query_parameters = {
        "category": "general",
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)

def get_health_articles():
    query_parameters = {
        "category": "health",
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)

def get_science_articles():
    query_parameters = {
        "category": "science",
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)

def get_sports_articles():
    query_parameters = {
        "category": "sports",
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)


def get_technology_articles():
    query_parameters = {
        "category": "technology",
        "sortBy": "top",
        "country": "mx",
        "apiKey": API_KEY
    }
    return get_articles(query_parameters)


def getResults():
    return results
