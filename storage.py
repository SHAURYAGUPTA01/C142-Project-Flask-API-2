from flask import jsonify,request,Flask
import csv

app = Flask(__name__)

all_articles = []
with open("articles.csv" , encoding = "utf-8") as f:
    r  = csv.reader(f)
    data = list(r)
    all_articles = data[1:]
    
like = []
dislike = []

@app.route('/get-article')
def get_article():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })

@app.route('/like-article' ,methods = ["POST"] )
def liked_articles():
    global all_articles
    m = all_articles[0]
    all_articles = all_articles[1:]
    like.append(m)
    return jsonify({"status" : "success"}),200

@app.route('/dislike-articles', methods = ["POST"])
def disliked_articles():
    global all_articles
    m = all_articles[0]
    all_articles = all_articles[1:]
    dislike.append(m)
    return jsonify({"status" : "success"}),200

if __name__ == "__main__":
    app.run(debug = True)