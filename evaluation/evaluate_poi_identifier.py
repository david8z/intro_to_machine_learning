#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split( features, labels, test_size = 0.3, random_state = 42)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
clf = DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
aux = clf.predict(features_test) 
print "Accurcay: ", accuracy_score(labels_test, aux)
print "Precision: ", precision_score(labels_test, aux)
print "Recall: ", recall_score(labels_test, aux)
res = 0 
for t, f in zip(labels_test,aux):
	if t == 1 and f == 1:
		res += 1
print res

res = 0
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
for p, t in zip(predictions, true_labels):
	if p == 0 and  t == 1:
		res += 1
print res
