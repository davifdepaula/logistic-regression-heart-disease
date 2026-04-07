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

Este projeto utiliza Regressão Logística para prever o risco de um paciente desenvolver doenças cardíacas nos próximos 10 anos. O objetivo central é fornecer uma ferramenta de triagem que maximize a detecção de casos de risco, equilibrando a viabilidade com rigor estatístico.

Dados extraídos do dataset de Framingham (Kaggle):
[Logistic Regression for Heart Disease Prediction](https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression)

## :card_index_dividers: Data Processing ##

O pipeline foi desenhado para tratar o desbalanceamento natural de dados clínicos e garantir a generalização do modelo:

* **Limpeza:** Remoção de 645 registros com valores ausentes para evitar viés por imputação.
* **Divisão de Dados:** Separação em Treino (75%), Validação (12.5%) e Teste (12.5%).
* **Estratégia de Validação:** Utilizamos o conjunto de validação para testar diferentes limiares (*cutoffs*) e técnicas de balanceamento antes da avaliação final.

## :bar_chart: Results & Evolution ##

Durante o desenvolvimento, comparamos o modelo Baseline (disponível na branch main) com uma versão utilizando pesos balanceados e otimização de threshold via Curva ROC. 

### Comparativo de Métricas (Test Set)

| Métrica | Modelo Baseline (Escolhido) | Modelo Otimizado (ROC/Balanced) | Evolução |
| :--- | :--- | :--- | :--- |
| **Recall (Sensibilidade)** | 71.32% | 66.67% | -4.65% |
| **Precision** | 57.14% | 32.86% | -24.28% |
| **Accuracy** | 62.01% | 74.40% | +12.41% |

### Por que optamos por manter o Baseline?

Após a análise dos resultados, decidimos manter a configuração Baseline como o modelo final devido aos seguintes fatores:

1. **Maior Rede de Segurança:** O Baseline alcançou um Recall de 71.31%. No contexto de saúde pública, perder 4.6% a mais de pacientes em risco (como ocorreu na versão com a curva ROC e pesos balanceados) é um risco clínico que é necessário evitar.
2. **Confiabilidade do Diagnóstico:** A precisão do Baseline (57.14%) é significativamente superior. Uma precisão baixa demais (32%) geraria muitos alarmes falsos, causando ansiedade desnecessária nos pacientes e sobrecarga financeira ao sistema de saúde com exames confirmatórios.
3. **Eficiência do Trade-off:** O Baseline provou ser o ponto de operação mais equilibrado, garantindo que a maioria dos doentes seja identificada sem sacrificar a utilidade prática do modelo.

## :rocket: Technologies ##

- Python 3.10+
- Pandas / Numpy
- Scikit-learn
- Pickle

## :checkered_flag: Starting ##

```bash
# Clone o projeto
$ git clone [https://github.com/davifdepaula/logistic-regression-heart-disease](https://github.com/davifdepaula/logistic-regression-heart-disease)

# Instale as dependências
$ pip install -r requirements.txt

# 1. Execute o treinamento
# Processa dados e exporta o modelo (.pkl) e o threshold (.txt)
$ python src/train.py

# 2. Execute a análise de métricas
# Valida a performance no dataset de teste e gera o relatório final
$ python src/test.py
```

Feito com :heart: por <a href="https://github.com/davifdepaula" target="_blank">Davi Ferreira</a>
&#xa0;

<p align="center">
  <a href="#top">Voltar para o topo!</a>
</p>