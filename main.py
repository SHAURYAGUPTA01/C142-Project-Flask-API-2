from flask import jsonify,Flask,request
from storage import all_articles, liked_articles, disliked_articles
from demographic import output
from content import get_recommendations

app = Flask(__name__)

@app.route("/popular-articles")
def popular_articles() :
    a_data = []
    for i in output :
        ad = {
           "title": i[12]
        }
        a_data.append(ad)
    return jsonify({
        "data" : a_data,
        "status" : "success"
    }),200
    
@app.route("/recommended-articles")
def recommended_articles() :
    all_recommended = []
    for i in liked_articles :
        output = get_recommendations(i[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    a_data = []
    for i in all_recommended:
        ad = {
           "title": i[12]
        }
        a_data.append(ad)
    return jsonify({
        "data" : a_data,
        "status" : "success"
    }),200

if __name__ == "__main__":
    app.run(debug = True)