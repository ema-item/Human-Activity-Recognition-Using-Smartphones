# -*- coding: utf-8 -*-
"""Human Activity Recognition Using Smartphones.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13kpRNy__Pqo91IrgHdFf3wAxwpn68v3k

#EMAD AMANIFAR

Classification of dataset data "Classifying Human Activity Recognition Using Smartphones dataset using svm with 99% accuracy on test data!!!" Using svm with 99% accuracy on test data!!!
"""

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import numpy as np
import seaborn as sns

dataset = np.load('./UCI_HAR.npz')
x = dataset['x_train']
y = dataset['y_train']

print(f'The training set contains {x.shape[0]} samples, each with {x.shape[1]} features.')
print(f'There are {len(np.unique(y))} classes.')

# train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=5898)

# model
model = SVC(kernel='rbf', C=9.0, gamma='auto')
model.fit(x_train, y_train)

# predict
y_pred = model.predict(x_test)

# confusion matrix
cm = confusion_matrix(y_test,y_pred)
header = ["WALKING", "WALKING\nUPSTAIRS", "WALKING\nDOWNSTAIRS", "SITTING", "STANDING", "LAYING"]
sns.heatmap(cm,
            annot=True,
            fmt='g',
            xticklabels = header,
            yticklabels = header)

plt.title('Human Activity Recognition \n with Smartphones',fontsize=17)
plt.show()

# accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\n\n", f"Accuracy Score: {accuracy}")