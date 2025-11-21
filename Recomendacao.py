import numpy as np

def __vetores_cluster__(df, numero_cluster):
    cluster = df.filter(df['prediction'] == numero_cluster).select('id', 'pca_features')

    partes_cluster = cluster.collect()

    vetores_cluster = []
    for row in partes_cluster:
        vetores_cluster.append((row['id'], row['pca_features']))

    return vetores_cluster

def calcula_proximos(imovel, df, quantidade_proximos):
    numero_cluster = imovel.select('prediction').first()[0]

    cluster_utilizado = __vetores_cluster__(df, numero_cluster)

    id_imovel = imovel.select('id').first()[0]
    vetor_imovel = imovel.select('pca_features').first()[0]

    distancias = []

    for i in range(len(cluster_utilizado)):
        id, vetor = cluster_utilizado[i]

        if id != id_imovel:
           distancias.append((id, np.linalg.norm(vetor - vetor_imovel)))

    distancias = sorted(distancias, key=lambda x: x[1])
    
    distancias_proximos = []
    for i in range(quantidade_proximos):
        ids, valor = distancias[i]
        distancias_proximos.append(ids) 

    return distancias_proximos