import csv
from bayes import  NaiveBayesClassifier

model = NaiveBayesClassifier(alpha=0.05)
def clean(s):
        translator = str.maketrans("", "", str.punctuation)
        return s.translate(translator)
X, y = [], []
with open("SMSSpamCollection") as f:
        data = list(csv.reader(f, delimiter="\t"))

for target, msg in data:
    X.append(msg)
    y.append(target)

X = [clean(x).lower() for x in X]
X_train, y_train, X_test, y_test = X[:3900], y[:3900], X[3900:], y[3900:]
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

