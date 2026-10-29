import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
df = pd.read_excel(sys.argv[1], header=1); Y='default payment next month'
df = df.rename(columns={'PAY_0':'PAY_1'})
static=['LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE']
def window(d, start):  # months start..start+4 relabelled as m1..m5 (m1 most recent)
    out = d[static].copy()
    for j in range(5):
        i = start + j
        out[f'S{j+1}'] = d[f'PAY_{i}']; out[f'B{j+1}'] = d[f'BILL_AMT{i}']; out[f'P{j+1}'] = d[f'PAY_AMT{i}']
    return out
tr_idx, te_idx = train_test_split(np.arange(len(df)), test_size=0.3, random_state=42, stratify=df[Y])
Xold = window(df, 2)           # Apr..Aug as inputs
Xnew = window(df, 1)           # May..Sep as inputs
yoct = df[Y].values
for thr in [1,2]:
    ysep = (df['PAY_1']>=thr).astype(int).values
    m = HistGradientBoostingClassifier(random_state=0, max_iter=300, learning_rate=0.05).fit(Xold.iloc[tr_idx], ysep[tr_idx])
    p = m.predict_proba(Xnew.iloc[te_idx])[:,1]
    print(f'proxy label Sep status>={thr}: base {ysep.mean():.3f}; AUC on true Oct default {roc_auc_score(yoct[te_idx], p):.4f}; top1000 defaulters {yoct[te_idx][np.argsort(-p)[:1000]].sum()}')
m = HistGradientBoostingClassifier(random_state=0, max_iter=300, learning_rate=0.05).fit(Xnew.iloc[tr_idx], yoct[tr_idx])
p = m.predict_proba(Xnew.iloc[te_idx])[:,1]
print(f'true label, same 5-month window: AUC {roc_auc_score(yoct[te_idx], p):.4f}; top1000 {yoct[te_idx][np.argsort(-p)[:1000]].sum()}')
print('agreement: Oct default rate among Sep status>=2', df.loc[df.PAY_1>=2, Y].mean().round(3), 'among Sep status<=0', df.loc[df.PAY_1<=0, Y].mean().round(3))
