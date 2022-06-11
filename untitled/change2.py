import pandas as pd

lizi = pd.read_csv('D:\entity_extractor_by_ner-master\data\example_datasets/traintxt.csv')

for i in range(lizi.shape[0]):
    if i % 2 == 0:
        lizi = lizi.drop([i], axis=0)

lizi.to_csv('D:\entity_extractor_by_ner-master\data\example_datasets/traintxt2.csv', encoding='utf-8', index=0)
