# The Recommended Group 2021
This is the group project of the Recommender Systems course of Maastricht University.

lenskit and gensim packages are required to be able to run every code.

The dataset used with the models: https://drive.google.com/file/d/1SVCdY2bt_6I5dfsYRCqRNnvW6xCRFTHW/view?usp=sharing

For Model 1, if you run the whole code you will see that we trained content based model for each user and form a dataframe called "full_predictions"
We switched between the Rating M1 and Rating M2 by manually editing the code.
At the end of the script, you will see an ExpGenerator. If you set the privacy parameter to False you will see Repairing Inconsistency Explanations.
Model 1 takes aroun 15 minutes to complete running.

Model 2, has to be run on Google Colab because a state-of-the-art NCF model is implemented from scratch using keras. You can also train it on your machine if you want to however, you need to remove the cell where google mounting is done. Model 2 needs aroung 15 mins to complete running. 

For Model 3, you need the gensim package to run the model. The explanation generations are at the end of the code.
