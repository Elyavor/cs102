from bottle import (
    route, run, template, request, redirect
)
import pickle
import string
from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier

@route('/index')
@route('/')
@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    label = request.query['label']
    id = request.query['id']
    s = session()
    needed_new = s.query(News).filter(News.id == id).first()
    needed_new.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    s = session()
    news = get_news('https://news.ycombinator.com/newest')
    for i in range(0, 10):
        item = News(title = news[i]['title'],
                    author = news[i]['author'],
                    url = news[i]['url'],
                    comments = news[i]['comments'],
                    points = news[i]['score'])
        s.add(item)
        s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    clf = NaiveBayesClassifier(1)
    s = session()
    training_set = s.query(News).filter(News.label != None).all()
    X_train = clear(training_set)
    y = [item.label for item in training_set]
 #   clf.fit(X_train, y)
 #   with open('classifier.pcl', 'wb') as f:
 #      pickle.dump(clf,f)
    with open('classifier.pcl', 'rb') as f:

        clf = pickle.load(f)
    rows = s.query(News).filter(News.label == None).all()
    X_test = []
    X_test = clear(rows)
    predictions = clf.predict(X_test)
    for i, item in enumerate(rows):
        item.label = predictions[i]
    rows.sort(key=lambda x: x.label)
    rows.reverse()
    return template('news_template', rows=rows)

def clear(data):
    titles = []
    translator = str.maketrans("","", string.punctuation)
    for item in data:
        titles.append(item.title)
    new_titles = []
    for title in titles:
        title = title.translate(translator)
        new_titles.append(title.lower().split())
    return new_titles


if __name__ == "__main__":
    run(host="localhost", port=8080)

