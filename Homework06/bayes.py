from math import log

class NaiveBayesClassifier:

    def __init__(self, alpha):
        self.alpha = alpha
        self.p_s = {}
        self.all_classes = set()

    def fit(self, X, y):
        """ Fit Naive Bayes classifier according to X, y. """
        self.all_classes = set(y)
        classes_and_titles = {}
        for item in self.all_classes:
           classes_and_titles[item] = []
        for i in range(len(y)):
            classes_and_titles[y[i]].extend(X[i])
        unique_words = set()
        for i in range(len(X)):
            unique_words.update(set(X[i]))
        for word in unique_words:
            self.p_s[word] = {}
            for a_class in self.all_classes:
                self.p_s[word][a_class] = classes_and_titles[a_class].count(word)
 
    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        predictions = []
        for title in X:
            title_porba = {}
            for word in title:
                if word in self.p_s:
                    for a_class in self.all_classes:
                        if a_class in title_porba.keys():
                            title_porba[a_class] += log((self.p_s[word][a_class] + self.alpha) / (sum(list(self.p_s[word].values())) + (self.alpha * len(self.p_s))))
                        else:
                            title_porba[a_class] = log((self.p_s[word][a_class] + self.alpha) / (sum(list(self.p_s[word].values())) + (self.alpha * len(self.p_s))))
            max_key = None
            max_value = float('-inf')
            for key, value in title_porba.items():
                if value > max_value:
                    max_value = value
                    max_key = key
            predictions.append(max_key)
        return predictions



    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        predictions = self.predict(X_test)
        good_matches = 0
        for i in range(len(y_test)):
            if predictions[i] == y_test[i]:
                good_matches += 1
        return good_matches / len(y_test)

