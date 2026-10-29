import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score
df = pd.read_excel(sys.argv[1], header=1); Y='default payment next month'
X = df.drop(columns=['ID',Y]); y=df[Y].values; allc=list(X.columns)
stat=['PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']; cat=stat+['EDUCATION','MARRIAGE','SEX']; num=[c for c in allc if c not in cat]
sens=['SEX','MARRIAGE','AGE','EDUCATION']; nos=[c for c in allc if c not in sens]
lag1=[c for c in allc if c not in ('PAY_0','BILL_AMT1','PAY_AMT1')]
rows=[]
for seed in range(5):
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.3,random_state=seed,stratify=y)
    r={}
    p=HistGradientBoostingClassifier(random_state=0,max_iter=300,learning_rate=0.05).fit(Xtr,ytr).predict_proba(Xte)[:,1]
    r['hgb']=roc_auc_score(yte,p)
    idx=np.argsort(-p)[:1000]; r['hgb_top1000']=yte[idx].sum()
    idx=np.argsort(-p)[:2000]; r['hgb_top2000']=yte[idx].sum()
    key=Xte.PAY_0.values+np.random.default_rng(seed).random(len(yte))*0.01
    r['rule_top1000']=yte[np.argsort(-key)[:1000]].sum(); r['rule_top2000']=yte[np.argsort(-key)[:2000]].sum()
    r['lr_raw']=roc_auc_score(yte, make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000)).fit(Xtr,ytr).predict_proba(Xte)[:,1])
    ct=ColumnTransformer([('c',OneHotEncoder(handle_unknown='ignore'),cat),('n',StandardScaler(),num)])
    r['lr_onehot']=roc_auc_score(yte, make_pipeline(ct,LogisticRegression(max_iter=3000)).fit(Xtr,ytr).predict_proba(Xte)[:,1])
    r['hgb_nosens']=roc_auc_score(yte,HistGradientBoostingClassifier(random_state=0,max_iter=300,learning_rate=0.05).fit(Xtr[nos],ytr).predict_proba(Xte[nos])[:,1])
    r['hgb_lag1']=roc_auc_score(yte,HistGradientBoostingClassifier(random_state=0,max_iter=300,learning_rate=0.05).fit(Xtr[lag1],ytr).predict_proba(Xte[lag1])[:,1])
    rows.append(r)
R=pd.DataFrame(rows); print(R.round(4).to_string()); print('mean'); print(R.mean().round(4).to_string()); print('std'); print(R.std().round(4).to_string())
