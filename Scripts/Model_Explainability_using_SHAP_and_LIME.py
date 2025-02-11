###  Model Explainability using SHAP and LIME
import shap
import lime.lime_tabular

# SHAP Explainability
explainer = shap.Explainer(log_reg, X_train)
shap_values = explainer(X_test)
shap.summary_plot(shap_values, X_test)



# LIME Explainability
explainer = lime.lime_tabular.LimeTabularExplainer(X_train.values, mode='classification')
exp = explainer.explain_instance(X_test.iloc[0].values, log_reg.predict_proba)
exp.show_in_notebook()
