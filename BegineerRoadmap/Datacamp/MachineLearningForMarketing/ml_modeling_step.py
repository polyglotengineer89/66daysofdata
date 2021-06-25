# Split X and Y into training and testing datasets
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.25)

# Ensure training dataset has only 75% of original X data
print(train_X.shape[0] / X.shape[0])

# Ensure testing dataset has only 25% of original X data
print(test_X.shape[0] / X.shape[0])

#Fit desicion Tree

# Initialize the model with max_depth set at 5
mytree = tree.DecisionTreeClassifier(max_depth = 5)

# Fit the model on the training data
treemodel = mytree.fit(train_X, train_Y)

# Predict values on the testing data
pred_Y = treemodel.predict(test_X)

# Measure model performance on testing data
accuracy_score(test_Y, pred_Y)


# Initialize the Decision Tree
clf = tree.DecisionTreeClassifier(max_depth = 7, 
               criterion = 'gini', 
               splitter  = 'best')

# Fit the model to the training data
clf = clf.fit(train_X, train_Y)

# Predict the values on test dataset
pred_Y = clf.predict(test_X)

# Print accuracy values
print("Training accuracy: ", np.round(clf.score(train_X, train_Y), 3)) 
print("Test accuracy: ", np.round(accuracy_score(test_Y, pred_Y), 3))