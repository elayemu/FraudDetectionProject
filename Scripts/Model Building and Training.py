###  Model Building and Training
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# Prepare data
X = fraud_data.drop(columns=['class'])
y = fraud_data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression Model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred))

git add .
git commit -m "Trained and evaluated Logistic Regression model"
git push

### Task 3: Model Explainability using SHAP and LIME
import shap
import lime.lime_tabular

# SHAP Explainability
explainer = shap.Explainer(log_reg, X_train)
shap_values = explainer(X_test)
shap.summary_plot(shap_values, X_test)

git add .
git commit -m "Implemented SHAP explainability for Logistic Regression"
git push

# LIME Explainability
explainer = lime.lime_tabular.LimeTabularExplainer(X_train.values, mode='classification')
exp = explainer.explain_instance(X_test.iloc[0].values, log_reg.predict_proba)
exp.show_in_notebook()
