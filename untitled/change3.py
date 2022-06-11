import numpy as np
import pandas as pd

txt = np.loadtxt("D:\entity_extractor_by_ner-master\data\example_datasets/traintxt2.txt",encoding='utf-8',dtype=str)
txtDF = pd.DataFrame(txt)
txtDF.to_csv("D:\entity_extractor_by_ner-master\data\example_datasets/finaltxt2.csv")