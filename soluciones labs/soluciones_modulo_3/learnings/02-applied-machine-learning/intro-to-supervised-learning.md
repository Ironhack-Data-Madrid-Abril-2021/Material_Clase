![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Introduction to Supervised Learning

## Lesson Goals

In this lesson you will learn the concepts and procedures of Supervised Machine Learning:

* The meaning of Supervision in Machine Learning.
* Criteria for determining the suitability of a Supervised Machine Learning approach.
* The software applications required in Supervised Machine Learning.
* The process model of Supervised Machine Learning.
* Lazy Machine Learning.

So let's get started...


## Introduction
In the same ways that persons can learn from past experience, Machine Learning systems can also learn from the experience of past cases, expressed as a dataset. If this past experience contained in a dataset contains cases (aka problem instances) with their correct solutions, the Machine Learning algorithms can learn to connect problem descriptions to their corresponding solutions, and we are then in a scenario known as "Supervised Learning". In this scenario there is always a supervisor, or teaching signal, that provides the correct solution. There are other forms of Machine Learning where this supervisor, or teaching signal, is not available, for instance in Unsupervised Learning. We will cover the topic of Supervised Learning in a later lesson. For now, it is sufficient to know the difference between Supervised and Unsupervised Machine Learning.
Regarding what is a well formed Supervised Learning problem, we have to look for two ingredients:
1. the problem descriptions expressed as problem instances (a list of attribute-value pairs).
2. The corresponding solutions expressed as the value of the target attribute.

Let's see some examples in the following section.

## Problems suitable for Supervised Learning
Problems where experience is available as a set of solved cases are suitable for Supervised Machine Learning. For instance, consider the following three:
1. Medical diagnosing. Health systems contain databases with the historical eHRs (electronic Health Records) of millions of patients suffering and not suffering from diabetes. In this problem, each patient would be a problem instance described by a set of attributes: age, gender, height, weight, known past diseases, genetic risks, values obtained from blood tests, symptoms, ... And the solution corresponding to this problem instance is encoded as the value of a binary target attribute indicating "positive" or "negative" depending on whether at this moment the patient suffers from diabetes. Using this dataset as a training set, we can train a Supervised Machine Learning model, to learn from the historical database how to diagnose diabetes, and use this model to diagnose new patients.
2. Credit Risk Assignment. Credit card companies have huge historical databases of customers who have used credit cards in the past, and have (or have not) paid their credit card debt on time. In this problem, every credit card customer is a problem instance, described by attributes such as: age, gender, average account balance, area of residence, occupation, purchase history, .... And the solution corresponding to this problem instance is stored in the target attribute as either "low risk", "medium risk" or "high risk" (based on the repayment history found for the client in the historical database). A training set can be obtained from the historical database, and used to train a Supervised Machine Learning model, so that it learns how to associate customers with levels of risk. After this Machine Learning model is trained, we can use it to assess the risk of providing credit to new customers.
3. News Recommendation. Newspaper websites provide users with the electronic version of the daily newspapers. They usually want to maximize the time spent by each user on the website, and they want to provide relevant and interesting content to its registered users. Every registered user has a particular reading history, formed by the topics of the news he has read, where he has clicked, and how much type was spent reading each article (or watching each video). Newspaper websites store this information in huge historical databases that reflect the insterests and preferences of its registered users. A Supervised Machine Learning model can be learned for each registered user, to predict how interesting an article is for this registered user. In this problem, an article is represented as a problem instance described as a set of attributes such as: topic of article, keywords of article, opinion targets in the article, sentiments about opinion targets, subscription fee of registered user, average subscription duration of readers of the article, average time readers of the article spent on website, average time readers of the article spent on each section of website, keywords of other articles read, ... And the solution corresponding to this problem instance is either "interesting" or "not interesting" for a particular registered user (depending on the time spent, if any, reading the article). A training set can be obtained from the historical database for each registered user. Using these training sets, models specific to concrete users can be learned using Supervised Machine Learning. These models can be used to recommend new articles to registered users, thus improving the benefit obtained from the time spent on the website.

## The Process Model
In Supervised Machine Learning you follow this procedure:
1. Determine suitability of Supervised Machine Learning solution depending on the possibility of building a dataset with problem instances and their corresponding solutions.
2. Build the dataset.
3. Split the dataset in disjoint training and test sets. Alternatetively you can do cross-validation here.
4. Train using a Supervised Machine Learning algorithm.
5. Test and obtain quality metrics.
6. If quality metrics are satisfactory, deploy the model. Otherwise design new experiment and iterate.

![Supervised ML Process Model](../../../static/images/supervised-ml-process-model-shrunk.png)

Usually, the first time you follow this procedure the results are not optimal, and you have to change something (i.e. design a new experiment) and iterate. These are ideas you can use to design a new Machine Learning experiment:
1. Use additional data.
2. Remove useless attributes that are misleading the Machine Learning algorithm.
3. Add additional relevant attributes.
4. Use a different Machine Learning algorithm.


## Trainer
Every Supervised Machine Learning system has a trainer software application. The trainer takes as input the training set and configuration parameters, executes the chosen Machine Learning algorithm on the training set, regulated by the configuration parameters, and outputs the Machine Learning model learned from the training set. We will see practical examples of how to do this with Scikit-learn in the next lesson.

## Decision Maker
The Decision Maker is a software application used to put to work the model learned by the trainer. The Decision Maker receives as input the Machine Learning model, possibly some configuration parameters, and a problem instance. It then feeds the problem instance to the Machine Learning model, and outputs the estimation provided by the model for that particular problem instance. The Decision Maker can be understood as a wrapper software around the model used to deploy the model to a production environment. 
In our next lesson, we will present practical examples of how to query the model learned by the Trainer.


## Lazy Supervised Machine Learning
So far we have covered Machine Learning paradigms that build a model prior to executing the Decision Maker. There is one kind of Supervised Machine Learning that is lazy, in the sense that it does not build a model in advance, and performs all necessary computations at the time of the query. One example of lazy Supervised Machine Learning is the K Nearest Neighbor algorithm (aka KNN). Let's explain how the lazy approach works in KNN with an example. For this purpose we will use the medical diagnosing problem domain presented in this section. Suppose we have a historical database of eHRs with 10 million patients on it, and a new patient needs to be diagnosed about having or not having diabetes. We set K=100 and execute the KNN algorithm:
1. the KNN algorithm looks for the K=100 pre-existing patients most similar to the new patient (aka the nearest neighbors).
2. KNN computes the most frequent diabetes diagnose among the nearest neighbors.
3. KNN outputs the most frequent diagnose among the nearest neighbors as the diagnose for the new patient.
Note that step one cannot be executed until query time, so no model is computed in advance.

## Lab
Now its your turn to practice putting the concepts you learned in this lesson to work:
1. Find a real problem domain, different from those presented in this lesson, where Supervised Learning can be used.
2. Explain how you would obtain the data: the source, and the extraction procedure.
3. Explain the problem instance representation.
4. Define the target attribute and provide the values of its domain.
5. Explain how to deploy the Machine Learning model to production to solve real world problems.
6. Explain how to evaluate the Decision Maker.




## Summary

In preparation for the next lesson, in this chapter you have learned about the basic concepts and procedures of Supervised Machine Learning. In our next lesson, we will provide examples of how to implement these ideas in Python using Scikit-learn. You now have a concrete criterion to determine whether a problem is suitable for Supervised Machine Learning or not. You have learned about the Trainer and the Decision Maker and the role they play in the Supervised Machine Learning process. So now you have all the background required to start the implementation of Supervised Machine Learning systems. Let's see how to do it in our next chapter!

