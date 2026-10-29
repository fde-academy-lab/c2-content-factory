import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
df = pd.read_excel(sys.argv[1], header=1); Y='default payment next month'
bills=[f'BILL_AMT{i}' for i in range(1,7)]; pays=[f'PAY_AMT{i}' for i in range(1,7)]
inactive = (df[bills]==0).all(axis=1) & (df[pays]==0).all(axis=1)
print('inactive n', inactive.sum(), 'defaults among them', df.loc[inactive,Y].sum(), 'of', df[Y].sum())
X = df.drop(columns=['ID',Y]); y=df[Y].values; allc=list(X.columns)
lag1=[c for c in allc if c not in ('PAY_0','BILL_AMT1','PAY_AMT1')]
res=[]
for seed in range(5):
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.3,random_state=seed,stratify=y)
    p=HistGradientBoostingClassifier(random_state=0,max_iter=300,learning_rate=0.05).fit(Xtr[lag1],ytr).predict_proba(Xte[lag1])[:,1]
    key=Xte.PAY_2.values+np.random.default_rng(seed).random(len(yte))*0.01
    res.append((yte[np.argsort(-p)[:1000]].sum(), yte[np.argsort(-key)[:1000]].sum()))
r=np.array(res); print('lag1 model top1000 mean', r[:,0].mean(), 'rule by PAY_2 top1000 mean', r[:,1].mean())
# BILL vs LIMIT oddities
print('bill1 negative', (df.BILL_AMT1<0).sum(), 'bill1 > limit', (df.BILL_AMT1>df.LIMIT_BAL).sum())
print('Sept codes -2 or 0', df.PAY_0.isin([-2,0]).sum())
print('defaults count by SEX', df.groupby('SEX')[Y].agg(['size','sum','mean']).round(4).to_dict())
