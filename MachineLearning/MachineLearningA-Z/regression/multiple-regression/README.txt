####Assumption of Linear Regression

  1.Linearity
  2.HomoScedasticity
  3.Multivariate Normality
  4.Independence of Error
  5.Lack of Multicollinearity

####5 Methods of building model
  1. All-in
  2. Backward Elimination
  3. Forward Selection
  4. Bidirectional Elimination
  5. Score Comparision

number 2,3,4 is Stepwise Regression

1. All-in:
   Method Where you include all variable
   Criteria to do it:
    1. You have prior knowledge in other word you know what you are doing
    2. You have to or there is no other choice
    3. Preparing for backward elimination
    
2. Backward Elimination
   There is several step in backeward Elimination
   1. Select significant level to stay in model
   2. Fit the full model with all posible predictor
   3. Consider Predictor with Highest P-Value
   4. Remove predictor
   5. Fit the model without this variable
   
   After step 5 go back to step 3

  FIN: Your Fit Model
  
3. Forward Selection
  There is several Step in Forward Selection:
  1. Select significant level to stay in model
  2. Fil all simpel linear regression model y~Xn select the one with lowest P-Value
  3. Keep this variable and fit all posible model with one extra predictor added to the one you already have
  4. Consider the predictor with the lowest P-Value. if P < SL, go to step 3, otherwise go to FIN
  
  
4. Bidirectional Elimination(combination between forward and backward)
   There is several step in Bidirectiona Elimination:
   1. Select significant level to enter and to stay in model
   2. Perform next step of forward selection (new variable must have: P< SLENTER to Enter)
   3. Perform all of step backward elimination (new variable must have: P <SLSTAY to stay)
   after step 3 go back to step 2 if necessary
   4. No new variable can enter and no old variable can exit
   
   
All Posible model:
  There is several step in all possible model:
  1. select criterion of goodness of fit
  2. Construct all posible Regression model 2n-1 total combination
  3. Selecr the on with best criterion
 
