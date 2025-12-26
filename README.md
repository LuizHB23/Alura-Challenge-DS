# 🏠 Alura Challenge: Ciência de Dados Aplicada ao Mercado Imobiliário

Este repositório contém a resolução do Challenge de Data Science da Alura. O objetivo principal foi atuar como um Cientista de Dados na "InsightPlaces", uma imobiliária que busca expandir seus negócios através da análise de dados e modelos de Machine Learning utilizando **PySpark**.

---

## 📅 Estrutura do Desafio (Semanas 1 a 4)

O projeto foi dividido em quatro semanas intensivas, cobrindo todo o ciclo de vida de um projeto de dados em ambiente de Big Data.

### **Semana 1: ETL e Exploração com Spark**
* **Objetivo:** Processamento inicial de uma base bruta em JSON com múltiplos níveis de aninhamento.
* **Ações:**
    * Exploração de dados brutos e normalização de colunas.
    * Tratamento de campos nulos e inconsistentes.
    * Transformação e salvamento dos dados em formatos otimizados (**Parquet** e **CSV**) para garantir performance nas etapas seguintes.

### **Semana 2: Regressão e Previsão de Preços**
* **Objetivo:** Criar um modelo capaz de prever os valores de venda dos imóveis.
* **Ações:**
    * Seleção de variáveis relevantes (Feature Selection).
    * Preparação de dados com `VectorAssembler`.
    * Treinamento e comparação de modelos de regressão (Linear Regression, Decision Tree Regressor, Random Forest Regressor e GBT Regressor).
    * **Resultados:** O modelo GBT (Gradient-boosted tree) obteve o melhor desempenho com **R² de 0.87**.

### **Semanas 3 e 4: Sistema de Recomendação**
* **Objetivo:** Recomendar imóveis semelhantes para usuários com base nas características de interesse.
* **Ações:**
    * Clusterização de imóveis utilizando o algoritmo **K-Means**.
    * Pré-processamento avançado com `StandardScaler` (normalização) e `PCA` (redução de dimensionalidade).
    * Implementação de uma função de recomendação baseada na **Distância Euclidiana** entre os vetores dos imóveis dentro de um mesmo cluster.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem Principal:** Python
* **Processamento de Big Data:** Apache Spark (PySpark)
* **Machine Learning:** Spark MLlib
* **Matemática/Estatística:** NumPy, Pandas
* **Formatos de Armazenamento:** Parquet, JSON, CSV

---

## 📂 Organização dos Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| `Challenge_DS_Semana_1.ipynb` | Extração, limpeza e transformação inicial dos dados. |
| `Challenge_DS_Semana_2.ipynb` | Modelagem de regressão para previsão de preços. |
| `Challenge_DS_Semana_3_e_4.ipynb` | Desenvolvimento do motor de recomendação. |
| `main.py` | Script principal para execução das recomendações. |
| `Pre_processo.py` | Pipeline de preparação de dados (Assembler, Scaler, PCA, KMeans). |
| `Recomendacao.py` | Lógica de cálculo de similaridade e busca de vizinhos próximos. |

---

## 🚀 Como Executar o Motor de Recomendação

1. Certifique-se de ter o **Spark** instalado e configurado em seu ambiente.
2. No arquivo `main.py`, defina o `id_imovel` que deseja usar como referência.
3. Execute o script:
   ```bash
   python main.py