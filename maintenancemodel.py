import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

np.random.seed(42)
num_samples = 1000

sensor_data = np.random.rand(num_samples, 5)  # 5 sensors

failure_labels = np.random.randint(0, 2, num_samples)  # Binary labels (0: No failure, 1: Failure)

df = pd.DataFrame(data=np.hstack((sensor_data, failure_labels.reshape(-1, 1))),
                  columns=[f'Sensor_{i}' for i in range(1, 6)] + ['Equipment_Failure'])

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df['Equipment_Failure'], test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print('\nConfusion Matrix:')
print(confusion_matrix(y_test, y_pred))
print('\nClassification Report:')
print(classification_report(y_test, y_pred))
