modelos = ['Random Forest', 'XGBoost', 'SVM']
scores = [0.85, 0.92, 0.78]

for modelo, acuracia in zip(modelos, scores):
    print(f"O modelo {modelo} teve acurácia de {acuracia}")