## Classification predicts the a category the data belongs to.
eg: Spam Detection, Churn Prediction, Sentiment Analysis,Dog Breed Detection.

## Regression predicts a numerical value based on previous observed data.
eg: House Price Prediction, Stock Price Prediction, Height-Weight Prediction.

## Classification
Classification is a technique for determining class the dependent belongs to based on the one or more independent variables.
                    
    Classification is used for predicting discrete responses.
 ![CLASSIFICATION](https://cdn-images-1.medium.com/max/800/1*QXttMMjauSK-XJ04AJBYsg.png)
### Applications of Classification are: speech recognition, handwriting recognition, biometric identification, document classification etc.
Classifiers can be:

### Binary classifiers: 
#### Classification with only 2 distinct classes or with 2 possible outcomes
example: Male and Female
example: classification of spam email and non spam email
example: classification of author of book
example: positive and negative sentiment

#### Multi-Class classifiers: Classification with more than two distinct classes.
example: classification of types of soil
example: classification of types of crops
example: classification of mood/feelings in songs/music
#### 1). Naive Bayes (Classifier):
Naive Bayes is a probabilistic classifier inspired by the Bayes theorem. Under a simple assumption which is the attributes are conditionally independent.

![fig. Naive Bayes Theorm](https://cdn-images-1.medium.com/max/800/0*U3LlC4m7PO5sqq9Q.png)

fig. Naive Bayes Theorm.      
         
The classification is conducted by deriving the maximum posterior which is the maximal P(Ci|X) with the above assumption applying to Bayes theorem. This assumption greatly reduces the computational cost by only counting the class distribution. Even though the assumption is not valid in most cases since the attributes are dependent, surprisingly Naive Bayes has able to perform impressively.
Naive Bayes is a very simple algorithm to implement and good results have obtained in most cases. It can be easily scalable to larger datasets since it takes linear time, rather than by expensive iterative approximation as used for many other types of classifiers.
Naive Bayes can suffer from a problem called the zero probability problem. When the conditional probability is zero for a particular attribute, it fails to give a valid prediction. This needs to be fixed explicitly using a Laplacian estimator.
###### Advantages:
This algorithm requires a small amount of training data to estimate the necessary parameters. Naive Bayes classifiers are extremely fast compared to more sophisticated methods.
###### Disadvantages: 
Naive Bayes is is known to be a bad estimator.
###### Steps for Implementation:

    Initialise the classifier to be used.
    Train the classifier: All classifiers in scikit-learn uses a fit(X, y) method to fit the model(training) for the given train data X and train label y.
    Predict the target: Given an non-label observation X, the predict(X) returns the predicted label y.
    Evaluate the classifier model

#### 2). Support Vector Machine:
Support vector machine is a representation of the training data as points in space separated into categories by a clear gap that is as wide as possible. New examples are then mapped into that same space and predicted to belong to a category based on which side of the gap they fall.
###### Advantages:
Effective in high dimensional spaces and uses a subset of training points in the decision function so it is also memory efficient.
###### Disadvantages: 
The algorithm does not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation.

![SVM](https://cdn-images-1.medium.com/max/800/0*G9Ql7oiZQV49tPN4.png)

fig. SVM

###### Description of diagram:
Examples of hyperplanes
H1 is not a good hyperplane as it doesn’t separate the classes
H2 does but only with small margin
H3 separates them with maximum margin (distance)
(https://en.wikipedia.org/wiki/Support_vector_machine)
###### Parameters of SVM
There are three main parameters which we could play with when constructing a SVM classifier:

    Type of kernel
    Gamma value
    C value

#### 3). K-NEAREST NEIGHBOUR (KNN):
kNN classfied an object by a majority vote of the object’s neighbours, in the space of input parameter. The object is assigned to the class which is most common among its k (an integer specified by human) nearest neighbour.
It is a non-parametric, lazy algorithm. It’s non-parametric since it does not make any assumption on data distribution (the data does not have to be normallly distributed). It is lazy since it does not really learn any model and make generalization of the data (It does not train some parameters of some function where input X gives output y).
So strictly speaking, this is not really a learning algorithm. It simply classfies objects based on feature similarity (feature = input variables).

![KNN](https://cdn-images-1.medium.com/max/800/0*2m7ZxmT2VVyBSiqk.png)

fig. classifying new example depending on Training instance distance

Classification is computed from a simple majority vote of the k nearest neighbours of each point.
###### Advantages:
This algorithm is simple to implement, robust to noisy training data, and effective if training data is large.
###### Disadvantages: 
Need to determine the value of K and the computation cost is high as it needs to computer the distance of each instance to all the training samples.

#### 4). Decision Tree
Given a data of attributes together with its classes, a decision tree produces a sequence of rules that can be used to classify the data.
Decision Tree, as it name says, makes decision with tree-like model. It splits the sample into two or more homogeneous sets (leaves) based on the most significant differentiators in your input variables. To choose a differentiator (predictor), the algorithm considers all features and does a binary split on them (for categorical data, split by cat; for continuous, pick a cut-off threshold). It will then choose the one with the least cost (i.e. highest accuracy), and repeats recursively, until it successfully splits the data in all leaves (or reaches the maximum depth).

![DT](https://cdn-images-1.medium.com/max/800/0*g2wMHxXJFZOSS8As.png)

fig. Tree like representation of datain Decision tree

###### Advantages:
Decision Tree is simple to understand and visualise, requires little data preparation, and can handle both numerical and categorical data.

###### Disadvantages:
Decision tree can create complex trees that do not generalise well, and decision trees can be unstable because small variations in the data might result in a completely different tree being generated.

#### 5). Random Forest
Random forest is an ensemble model that grows multiple tree and classify objects based on the “votes” of all the trees. i.e. An object is assigned to a class that has most votes from all the trees. By doing so, the problem with high bias (overfitting) could be alleviated.( — from Kaggle).

![Random Forest](https://cdn-images-1.medium.com/max/800/1*i0o8mjFfCn-uD79-F1Cqkw.png)

fig. Random forest

Random forest classifier is a meta-estimator that fits a number of decision trees on various sub-samples of datasets and uses average to improve the predictive accuracy of the model and controls over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement.

###### Pros of RF:

    It could handle large data set with high dimensionality, output Importance of Variable, useful to explore the data
    Could handle missing data while maintaining accuracy

###### Cons of RF:

    Could be a black box, users have little control on what the model does

###### Advantages:
Reduction in over-fitting and random forest classifier is more accurate than decision trees in most cases.

###### Disadvantages:
Slow real time prediction, difficult to implement, and complex algorithm.         

