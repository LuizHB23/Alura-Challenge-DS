from Recomendacao import calcula_proximos
from Pre_processo import pre_processo
from pyspark.sql import SparkSession

# Inicializar o Spark
spark = SparkSession.builder.appName("ProcessamentoParquet").getOrCreate()

# Caminho do arquivo PARQUET
parquet_path = "/home/luizh/Python/1Challenge/Data Science/Alura-Challenge-DS/Dataset/dataset_ml_parquet"

# Carregar o arquivo JSON em um DataFrame
df = spark.read.parquet(parquet_path)

# Pré processa o DataFrame
df_clusterizado = pre_processo(df)

# Escolhe o imóvel para calcular os mais próximos e define a quantidade de imóveis próximos
id_imovel = '24f784d6-7603-48d5-a74c-f2b4a9638fe6'
numero_proximos = 20

imovel = df_clusterizado.select('*').where(df_clusterizado['id'] == id_imovel)

array_proximos = calcula_proximos(imovel, df_clusterizado, numero_proximos)

# Para uma melhor visualização retiraremos as seguintes colunas
df = df.drop(*['Zona Norte', 'Zona Oeste', 'Zona Sul', 'Zona Central', 'Portão eletrônico', 'Salão de festas'])

df.filter(df['id'].isin(array_proximos)).show()



# Para escolher qual imóvel quiser

"""
|00002dd9-cc74-4809-b5a5-850adf0e7526|
|0009ca94-2b37-4381-b8b8-773ce0f92444|
|000e3d28-e3e5-4110-b488-69154931140e|
|000fb707-6cad-496d-8cb7-d8046cb5ef37|
|001b6db0-e88d-4eba-84e5-0ef94b091a64|
|002db67e-52cc-4807-ad36-7fc809fb90c2|
|002dc4e0-f1a5-4add-9c1c-3f43904645da|
|0030dd84-f657-41f3-8b86-0f2a72e0fb55|
|003213bb-ec21-4ad9-b918-3d51f6300a0c|
|0032884c-aa5f-4558-b9eb-1d37892e466f|
|00348cd1-923a-4dbd-b113-b31c7b877bec|
|0034df72-124a-4383-a89f-a019850a2ba0|
|0036114a-4a0f-4926-ad98-864f4474fb22|
|00370d62-f774-405f-9412-c50cde27a177|
|00396d9d-2d0e-4b54-b3a3-58aec00459b6|
|003cb63c-a666-458a-b605-13616ae32c78|
|0040f5a7-6c6a-40ed-94e6-2e4accbbc1b4|
|00529a9d-d876-4dc5-bb13-847513de1879|
|00584813-33b4-477b-a7cc-80777593a9ba|
|005b5441-16b2-483b-b177-c15a4bc9e70e|
|005c608c-5afc-459d-8d94-d42fb1eec510|
|007a7c27-bb0b-4b60-9d14-527010304296|
|0084766a-2c37-4802-896a-27c26779a590|
|0088ef55-9e24-402c-b3bc-dd9fe31a4816|
|008f5865-d5f4-4087-8af2-ed81b9120959|
|00923806-e94a-44e1-b043-22260856c048|
|0092be3c-1736-42ac-b098-76e410b41da9|
|0092f04d-ee0a-4965-818a-ee2e58bba23e|
|00a24367-5bf0-4b79-a587-2326526fbac8|
|00a5991a-9aee-405d-90c9-84b64a385968|
|00aa1c1e-758e-45f5-8ab4-2ee904a15d44|
|00aa9e39-9224-4d24-8e47-8a0213bc0282|
|00abd716-4d6b-4575-a126-bf21dfb27c7e|
|00b61c4e-bfc0-4708-b3e1-edf860d01768|
|00bde691-6e81-462a-b091-d4279100b4e3|
|00be125f-6bc7-4ed5-8b4f-17aa15d471fa|
|00cc6ebd-d268-4cc4-9a96-8eaa2b362446|
|00cd6c5d-592d-4294-8cc9-a9c537d4de81|
|00d01937-9bca-45a5-8080-b6df516686db|
|00d2956a-a053-42b9-bb0d-15eff24ac49d|
|00eb8693-5de8-4578-a10c-c75855956727|
|00edc0a5-4d9d-4420-b382-3dae14eaa869|
|00f07937-c074-47e3-a4f1-09fa16dcadf8|
|00f21fe7-ae20-4b37-83f8-89ace74b7631|
|00f2fc1a-ca61-48d2-bbc3-a3f35f005048|
|00fafb28-3930-4b68-b3b1-ba7a3d83fc52|
|00fc267c-9956-4766-bc44-34f353045655|
|00fcb5fb-c01b-44b2-a76f-00a086dc5d52|
|00ff8cc4-306e-48a3-a29c-23c4dd3c7710|
|0102d472-2c51-4529-92c5-959b171a12d9|
|01064d20-7e1f-4e94-90ef-ad53d0f5f61d|
|010cc24b-6cc5-4b84-b4a7-2159683992ae|
|011c65c8-d56d-4a91-98c6-64c0f4c04df9|
|011cd0f0-0856-451f-8161-b33e3b2fe587|
|01228c26-3a13-4800-9790-6c92728e5a02|
|01229c2f-45ef-4b76-bab4-2ab37dd8f9a3|
|0123b5ed-e6b5-4dec-8d02-1fc6c1b4d3f5|
|01259581-b96b-4ce2-a184-f8b5947cd9b9|
|012e17ec-df9a-42a2-b7a1-97e5680a0413|
|012ec525-c891-40f7-92c7-e7bbae52ab82|
|012ecfb6-c710-4126-9315-471e424385ed|
|012f6a6f-a576-4cec-9534-0a0cae5b9355|
|013027d3-92a5-488a-b2e3-f4da3b06d26d|
|0132b86a-e0f9-4ab0-9907-0e30c7ace2b3|
|0133f9b4-926a-4bd3-94b5-5cc04428c764|
|0134b627-7f25-4fe5-b6ad-4cc8c1ff0602|
|0140dd2f-0f9b-4ccb-8f02-f77c6a46b69a|
|01429b39-66ab-4130-8065-65cdd83d6967|
|0148c5de-0b01-45bd-97bc-56ac109922ae|
|015395b7-e80c-46bd-a811-69b4abd47a14|
|0157d169-18cc-4c9e-8f57-9abe81e8f58a|
|015c98f7-50b3-40e6-acc1-b508428d3b10|
|01606b94-61f5-44d6-8088-420378f3a01c|
|01643d2f-1fbb-429b-93d9-b0672d145b54|
|01680d26-2560-47d8-bd4a-73198f564010|
|016aa5e1-aa7b-42fc-8096-670c527afa6e|
|017447b1-e1f2-4d43-a606-8e9df845b9bf|
|01762566-ec21-4d0d-a4ff-9d00ad732b6f|
|0177193b-144e-4d3b-bcfd-c371311d40af|
|01791924-4d51-4e5d-8738-f6663514d421|
|017a16ba-d6d7-41f4-bd3d-a48852e045fa|
|017cf41e-3127-4f78-b618-22fa7765b7c6|
|04248072-5d66-4713-857b-33b2ac922b2a|
|042d23e6-0f8f-44ce-8b8c-3bf3be2fce5c|
|0431970a-8532-4833-888c-079f2eaf9f22|
|04332cf9-21a4-4546-8d6e-e93b7bf488df|
|04370c71-9100-4e20-b5f1-d7312404d141|
|04376c42-3c52-45c3-9443-0e490bbd2503|
|0439ef23-5cbf-4a2d-991c-5c717c5fefb8|
|043e8b3c-9188-432c-8acf-73711bc1c6f8|
|0441bfe6-dd9f-419d-97a2-23e5d045ae64|
|0445299b-6f2b-43b7-9e01-bf02e1850e0c|
|045f59b4-5a0a-4e2e-be2b-ebc9911fe3fd|
|04602f49-c0f2-407d-88a7-578ce6bf85df|
|04604490-2ec8-4f87-b4a5-c052a5211a38|
|0461e284-c42a-4645-a601-03201370204e|
|04677ac3-362f-4029-ad33-811e5cd24d68|
|0467b11d-b2ed-4022-9133-f9465645899e|
|046880e3-fdf6-420f-aa22-18190117a559|
|046a277e-9549-47eb-84c7-06975ecc7d70|
|046ac18c-d3e6-452c-800c-c2f97ace5245|
|046bc8f5-59b3-4e6c-830c-9fad21db0e9d|
|046f2f30-65fb-431c-ba33-2f320a2a5e91|
"""