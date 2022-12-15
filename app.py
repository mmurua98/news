from flask import Flask, render_template, request
import news

app = Flask(__name__)

@app.route("/")
def home():
    news.get_trending_articles()
    trendingNews = news.getResults()
    #print(trendingNews)
    return render_template('index.html', results=trendingNews)

# @app.route("/category",  methods=['POST', 'GET'])
# def search():
#     #category = request.form['category']

#     if request.method == 'POST':
#         #Get data from JAVASCRIPT via JSON
#         data = request.get_json(force=True)
#         category = data['category']
#         news.get_articles_by_category(category)

#         # print(data)
#         #news_title = news.getTitle()
#         # news_url = news.getUrl()

#         #Variable to get all articles and use it in a FOR LOOP
#         category_results = news.getResults()

#         print(category_results)
#         return 'ok'

@app.route("/category/business",  methods=['POST', 'GET'])
def business():
    news.get_business_articles()
    #Variable to get all articles and use it in a FOR LOOP
    business_results = news.getResults()

    return render_template('index.html', results=business_results)

@app.route("/category/entertainment",  methods=['POST', 'GET'])
def entertainment():
    news.get_entertainment_articles()
    #Variable to get all articles and use it in a FOR LOOP
    entertainment_results = news.getResults()

    return render_template('index.html', results=entertainment_results)

@app.route("/category/general",  methods=['POST', 'GET'])
def general():
    news.get_general_articles()
    #Variable to get all articles and use it in a FOR LOOP
    general_results = news.getResults()

    return render_template('index.html', results=general_results)

@app.route("/category/health",  methods=['POST', 'GET'])
def health():
    news.get_health_articles()
    #Variable to get all articles and use it in a FOR LOOP
    health_results = news.getResults()

    return render_template('index.html', results=health_results)

@app.route("/category/science",  methods=['POST', 'GET'])
def science():
    news.get_science_articles()
    #Variable to get all articles and use it in a FOR LOOP
    science_results = news.getResults()

    return render_template('index.html', results=science_results)

@app.route("/category/sports",  methods=['POST', 'GET'])
def sports():
    news.get_sports_articles()
    #Variable to get all articles and use it in a FOR LOOP
    sports_results = news.getResults()

    return render_template('index.html', results=sports_results)

@app.route("/category/technology",  methods=['POST', 'GET'])
def technology():
    news.get_technology_articles()
    #Variable to get all articles and use it in a FOR LOOP
    technology_results = news.getResults()

    return render_template('index.html', results=technology_results)

if __name__ == "__main__":
    app.run()