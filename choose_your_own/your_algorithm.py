#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
clf = KNeighborsClassifier(n_neighbors=18)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "Accuracy: ", (accuracy_score(labels_test, pred))
clf2 = RandomForestClassifier()
clf2.fit(features_train, labels_train)
pred2 = clf2.predict(features_test)
print "Accuracy: ", (accuracy_score(labels_test, pred2))
clf3 = AdaBoostClassifier(n_estimators=100)
clf3.fit(features_train, labels_train)
pred3 = clf3.predict(features_test)
print "Accuracy: ", (accuracy_score(labels_test, pred3))





try:
    prettyPicture(clf, features_test, labels_test)
    plt.show()
    prettyPicture(clf2, features_test, labels_test)
    plt.show()
    prettyPicture(clf3, features_test, labels_test)
    plt.show()

except NameError:
    pass
