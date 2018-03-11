"""Hello World - Machine Learning Recipes #1
Google Developers
"""
from sklearn import tree

"""Features, ie. training data for the machine to learn from.
Weight | Texture = Label
140g | Smooth = Apple
130g | Smooth = Apple
150g | Bumpy = Orange
17-g | Bumpy = Orange

The more training data we have, the better the classifier we can code.
Scikit-learn uses real-valued features
A classifier is at its root a box of rules, a learning algorithm is the procedure that creates the rules. It does that by finding patterns in the training data.
"""
#input to our classifier
# features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
#outputs of our classifier
# labels = ["apple", "apple", "orange", "orange"]
labels = [0, 0, 1, 1]

#Decision Tree Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#using the classifer, predict what fruit this is based on it's weight and texture:
print (clf.predict([[150, 0]]))