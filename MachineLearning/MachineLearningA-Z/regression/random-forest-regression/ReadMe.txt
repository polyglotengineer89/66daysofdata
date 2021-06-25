Step By Step Random Forest

Step 1:
 - Pick at Random K data point from the training set

Step 2:
 - Build Desicion Tree associated to this K data point

Step 3:
 - Choose the number of Ntree of tree you want to build repeat step 1 & 2
 
Step 4:
 - For new data point, make each one of your Ntrees predict the value of Y to for data point in question, and assign new data point the averange accross all of data predicted Y value