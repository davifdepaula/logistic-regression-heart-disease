<div align="center" id="top"> 
  <img src="https://raw.githubusercontent.com/davifdepaula/logistic-regression-heart-disease/main/.github/app.gif" alt="Logistic Regression Heart Disease" />

  &#xa0;
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
  <a href="#num-data-processing">Data Processing</a> &#xa0; | &#xa0;
  <a href="#bar_chart-results">Results</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="https://github.com/davifdepaula" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Este projeto utiliza Regressão Logística para prever o risco de um paciente desenvolver doenças cardíacas nos próximos 10 anos. O objetivo principal é fornecer uma análise preditiva robusta com foco em interpretabilidade e alta taxa de detecção de pacientes em risco.

Os dados utilizados foram extraídos do dataset de Framingham, disponível publicamente no Kaggle:
[Logistic Regression for Heart Disease Prediction](https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression)

## :num-data-processing: Data Processing ##

O pipeline de dados foi desenhado para tratar inconsistências e o desbalanceamento natural de dados clínicos:

* Limpeza de Dados: Iniciamos com 4.238 registros. Foram removidos 645 valores ausentes (NaNs), garantindo que o modelo não fosse treinado com informações incompletas.
* Balanço de Classes: 
    * Classe Majoritária (0): 3.099 pacientes (Sem risco detectado de desenvolver ataque cardiaco daqui a 10 anos).
    * Classe Minoritária (1): 557 pacientes (Com risco de ataque cardíaco daqui a 10 anos).
* Estratégia: Aplicamos Undersampling na classe majoritária. Sem isso, o modelo teria um viés de falso otimismo, aprendendo que quase ninguém teria ataques cardíacos devido à enorme predominância da classe negativa. O balanceamento força o modelo a aprender as características críticas da classe minoritária.

## :bar_chart-results: Results ##

As métricas obtidas no conjunto de teste demonstram a eficácia do modelo, especialmente na métrica mais sensível ao contexto médico:

| Métrica | Valor |
| :--- | :--- |
| Recall | 71.31% |
| Accuracy | 62.00% |
| Precision | 57.14% |

> Em saúde pública, o Recall é a métrica de sucesso. É mais seguro para o sistema de saúde realizar exames preventivos em um falso positivo (Precisão baixa) do que dar alta para um paciente que corre risco real de vida (Recall baixo).

## :rocket: Technologies ##

As seguintes ferramentas foram utilizadas neste projeto:

- Python
- Pandas
- Statsmodels
- Scikit-learn
- Pickle

## :white_check_mark: Requirements ##

Antes de começar, você precisa ter o Git e o Python 3.10+ instalados.

## :checkered_flag: Starting ##

```bash
# Clone o projeto
$ git clone [https://github.com/davifdepaula/logistic-regression-heart-disease](https://github.com/davifdepaula/logistic-regression-heart-disease)

# Instale as dependências
$ pip install -r requirements.txt

# 1. Execute o treinamento
# Este comando processa os dados brutos, aplica a limpeza/balanceamento,
# treina o modelo (.pkl) e exporta os datasets de treino (train_dataset.csv)
# e de teste (test_dataset.csv) para a pasta src/data/.
$ python src/train.py

# 2. Execute a análise de métricas
# Este comando carrega o modelo salvo e o dataset de teste para validar
# a performance e gerar o relatório final (metrics_report.txt).
$ python src/test.py