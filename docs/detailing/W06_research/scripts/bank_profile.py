import sys, pandas as pd, numpy as np
from sklearn.metrics import roc_auc_score
df = pd.read_csv(sys.argv[1])
print(df.shape); print(list(df.columns))
y = (df.Attrition_Flag=='Attrited Customer').astype(int)
print(df.Attrition_Flag.value_counts().to_dict(), 'base', y.mean().round(4))
print('missing', df.isna().sum()[df.isna().sum()>0].to_dict())
print('dup CLIENTNUM', df.CLIENTNUM.duplicated().sum(), 'dup rows excl id', df.drop(columns='CLIENTNUM').duplicated().sum())
nb = [c for c in df.columns if c.startswith('Naive_Bayes')]
for c in nb:
    print(c, 'AUC', round(roc_auc_score(y, df[c]),5), 'mean', df[c].mean().round(4))
    print('  thresh0.5 acc', ((df[c]>0.5).astype(int)==y).mean().round(4))
print('NB cols sum to 1?', (df[nb].sum(1)-1).abs().max())
for c in df.select_dtypes('object').columns:
    if c!='Attrition_Flag':
        vc=df[c].value_counts().to_dict(); print(c, vc)
        print('   attr rate', df.groupby(c).apply(lambda g:(g.Attrition_Flag=="Attrited Customer").mean(), include_groups=False).round(3).to_dict())
num = df.select_dtypes('number').drop(columns=['CLIENTNUM']+nb)
for c in num.columns:
    print(f'{c:28s} min {num[c].min():>10} max {num[c].max():>10} mean {num[c].mean():>10.2f} AUC {roc_auc_score(y,num[c]):.3f}')
print('Months_on_book mode count', df.Months_on_book.value_counts().head(3).to_dict())
print('Avg_Open_To_Buy == Limit - Revolving?', (abs(df.Avg_Open_To_Buy-(df.Credit_Limit-df.Total_Revolving_Bal))<1).mean())
print('Avg_Utilization approx Revolving/Limit?', (abs(df.Avg_Utilization_Ratio-(df.Total_Revolving_Bal/df.Credit_Limit))<0.002).mean())
