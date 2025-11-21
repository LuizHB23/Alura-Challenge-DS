from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import PCA

def pre_processo(df):

    # Prepara as colunas a serem modificadas
    X = df.columns
    X.remove('id')
    X.remove('bairro')

    # Aplica o VectorAssembler
    assembler = VectorAssembler(inputCols=X, outputCol='features')

    df_vetorizado = assembler.transform(df)
    df_vetorizado = df_vetorizado.select('features')

    # Aplica o StandardScaler
    scaler = StandardScaler(inputCol='features', outputCol='scaler_features')

    modelo_scaler = scaler.fit(df_vetorizado)
    df_scaler = modelo_scaler.transform(df_vetorizado)

    # Aplica o PCA
    pca = PCA(k=8, inputCol='scaler_features', outputCol='pca_features')

    modelo_pca = pca.fit(df_scaler)
    df_pca = modelo_pca.transform(df_scaler)

    df_final = df_pca.select('pca_features')
    df_final = df_final.withColumnRenamed('pca_features', 'features')

    # Constroí o modelo a partir de um Pipeline
    kmeans = KMeans(featuresCol='features', k=17, seed=390)

    pipeline = Pipeline(stages=[assembler, modelo_scaler, modelo_pca, kmeans])

    modelo_final = pipeline.fit(df)

    df_final_clusterizado = modelo_final.transform(df)

    return df_final_clusterizado
