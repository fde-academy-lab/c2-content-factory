import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score, average_precision_score
f = pd.read_parquet(sys.argv[1]); f['Class']=f.Class.astype(int)
tr = f[f.Time<86400]; te = f[f.Time>=86400]
cols = [c for c in f.columns if c not in ('Class','Time')]
yt = te.Class.values; amt = te.Amount.values
models = {
 'LR': make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)),
 'HGB lr0.05 l2=1': HistGradientBoostingClassifier(random_state=0, learning_rate=0.05, max_iter=300, l2_regularization=1.0, early_stopping=False),
 'RF 200': RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=0, min_samples_leaf=1),
}
for nm, m in models.items():
    m.fit(tr[cols], tr.Class); p = m.predict_proba(te[cols])[:,1]
    out = f'{nm}: AUC {roc_auc_score(yt,p):.4f} AP {average_precision_score(yt,p):.4f}'
    for k in [100,200,500]:
        idx=np.argsort(-p)[:k]; out += f' | top{k} {yt[idx].sum()} frauds amt {amt[idx][yt[idx]==1].sum():.0f}'
    idx=np.argsort(-(p*amt))[:200]; out += f' | top200 by p*amt {yt[idx].sum()} amt {amt[idx][yt[idx]==1].sum():.0f}'
    print(out, '| total day2 fraud amt', round(amt[yt==1].sum()))
