<div align="center" id="top"> 
  <img src="https://raw.githubusercontent.com/davifdepaula/logistic-regression-heart-disease/main/.github/app.gif" alt="Logistic Regression Heart Disease" />
</div>

<h1 align="center">Logistic Regression Heart Disease</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/davifdepaula/logistic-regression-heart-disease?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/davifdepaula/logistic-regression-heart-disease?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/davifdepaula/logistic-regression-heart-disease?color=56BEB8">
  <img alt="License" src="https://img.shields.io/github/license/davifdepaula/logistic-regression-heart-disease?color=56BEB8">
</p>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#card_index_dividers-data-processing">Data Processing</a> &#xa0; | &#xa0;
  <a href="#bar_chart-results">Results</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="https://github.com/davifdepaula" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Este projeto utiliza Regressão Logística para prever o risco de um paciente desenvolver doenças cardíacas nos próximos 10 anos. O objetivo principal é fornecer uma análise preditiva robusta com foco em interpretabilidade e alta taxa de detecção de pacientes em risco (Recall).

Os dados utilizados foram extraídos do dataset de Framingham, disponível no Kaggle:
[Logistic Regression for Heart Disease Prediction](https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression)

## :card_index_dividers: Data Processing ##

O pipeline de dados foi desenhado para tratar inconsistências e o desbalanceamento natural de dados clínicos:

* **Limpeza de Dados:** Remoção de 645 registros com valores ausentes (NaNs), garantindo a integridade estatística do treinamento.
* **Balanço de Classes:** * Classe Majoritária (0): 3.099 pacientes (Sem risco detectado).
    * Classe Minoritária (1): 557 pacientes (Com risco detectado).
* **Estratégia Baseline:** Aplicamos Undersampling na classe majoritária. Sem isso, o modelo teria um viés de falso otimismo, aprendendo que quase ninguém teria ataques cardíacos devido à enorme predominância da classe negativa. O balanceamento força o modelo a aprender as características críticas da classe minoritária.

## :bar_chart: Results & Model Selection ##

Durante o desenvolvimento, realizou-se uma análise comparativa entre o modelo Baseline (disponível na branch `main`) e uma versão experimental utilizando pesos balanceados e otimização de *threshold* via Curva ROC (disponível na branch `weight-balanced-threshold`).

### Desenvolvimento do Modelo Experimental

O pipeline da versão experimental foi desenhado para testar a generalização do modelo sob condições de penalização de erro:
* **Divisão de Dados:** Separação rigorosa em **Treino (75%)**, **Validação (12.5%)** e **Teste (12.5%)**.
* **Estratégia de Validação:** O conjunto de validação foi utilizado exclusivamente para testar diferentes limiares (*cutoffs*) e técnicas de balanceamento (`class_weight='balanced'`) antes da avaliação final.

### Comparativo de Performance (Test Set)

| Métrica | Modelo Baseline (Final) | Modelo Experimental | Impacto |
| :--- | :--- | :--- | :--- |
| **Recall (Sensibilidade)** | **71.31%** | 66.67% | **-4.64%** |
| **Precision** | **57.14%** | 32.86% | **-24.28%** |
| **Accuracy** | 62.00% | **74.40%** | +12.40% |

### Justificativa da Escolha

Optamos por consolidar o **Baseline** como o modelo principal pelos seguintes motivos:

1. **Priorização do Recall:** Em diagnósticos médicos, o custo de um falso negativo (não detectar o risco) é superior ao de um falso positivo. O Baseline identificou **71.31%** dos casos reais, superando a versão experimental.
2. **Viabilidade Clínica:** A precisão de **57.14%** do Baseline evita uma sobrecarga excessiva no sistema de saúde com alarmes falsos, mantendo um equilíbrio superior à versão experimental (32.86%).

## :rocket: Technologies ##

- Python / Pandas / Numpy
- Statsmodels / Scikit-learn
- Pickle (Serialização do Modelo)

## :checkered_flag: Starting ##

```bash
# Clone o projeto
$ git clone [https://github.com/davifdepaula/logistic-regression-heart-disease](https://github.com/davifdepaula/logistic-regression-heart-disease)

# Para visualizar o experimento de pesos balanceados:
$ git checkout weight-balanced-threshold

# Instale as dependências
$ pip install -r requirements.txt

# 1. Execute o treinamento (Baseline na main)
$ python src/train.py

# 2. Execute a análise de métricas
$ python src/test.py
```

Feito com :heart: por <a href="https://github.com/davifdepaula" target="_blank">Davi Ferreira</a>
&#xa0;

<p align="center">
  <a href="#top">Voltar para o topo!</a>
</p>


