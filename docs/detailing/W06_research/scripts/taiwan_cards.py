import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss
df = pd.read_excel(sys.argv[1], header=1)
Y='default payment next month'
y = df[Y].values
bills=[f'BILL_AMT{i}' for i in range(1,7)]; pays=[f'PAY_AMT{i}' for i in range(1,7)]
stat=['PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']
inactive = (df[bills]==0).all(axis=1) & (df[pays]==0).all(axis=1)
print('inactive accounts', inactive.sum(), 'default rate', df.loc[inactive,Y].mean().round(3))
allm2 = (df[stat]==-2).all(axis=1)
print('PAY all -2', allm2.sum(), 'default rate', df.loc[allm2,Y].mean().round(3))
for code in [-2,-1,0]:
    m = df.PAY_0==code
    print(f'PAY_0={code}: n {m.sum()}, BILL_AMT1==0 share {(df.loc[m,"BILL_AMT1"]==0).mean():.3f}, BILL_AMT1 median {df.loc[m,"BILL_AMT1"].median():.0f}, PAY_AMT1==0 share {(df.loc[m,"PAY_AMT1"]==0).mean():.3f}')
X = df.drop(columns=['ID',Y])
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
Xtr2, Xva, ytr2, yva = train_test_split(Xtr, ytr, test_size=0.25, random_state=42, stratify=ytr)
print('split sizes', len(Xtr2), len(Xva), len(Xte), 'test base', yte.mean().round(4))
def lr(cols, cw=None):
    return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight=cw)).fit(Xtr[cols], ytr)
def hgb(cols):
    return HistGradientBoostingClassifier(random_state=0, max_iter=300, learning_rate=0.05).fit(Xtr[cols], ytr)
allc = list(X.columns)
m_lr = lr(allc); p_lr = m_lr.predict_proba(Xte[allc])[:,1]
m_hg = hgb(allc); p_hg = m_hg.predict_proba(Xte[allc])[:,1]
print(f'AUC LR {roc_auc_score(yte,p_lr):.4f} AP {average_precision_score(yte,p_lr):.4f} | HGB AUC {roc_auc_score(yte,p_hg):.4f} AP {average_precision_score(yte,p_hg):.4f}')
rule = (Xte.PAY_0>=1).astype(int).values
rule2 = (Xte.PAY_0>=2).astype(int).values
for nm,r in [('PAY_0>=1',rule),('PAY_0>=2',rule2)]:
    tp=((r==1)&(yte==1)).sum(); fp=((r==1)&(yte==0)).sum(); fn=((r==0)&(yte==1)).sum()
    print(f'rule {nm}: flagged {r.mean():.3f} precision {tp/(tp+fp):.3f} recall {tp/(tp+fn):.3f}')
acc_null = 1-yte.mean(); print('accuracy of predict-no-default', round(acc_null,4), 'HGB acc@0.5', ((p_hg>=0.5)==yte).mean().round(4), 'LR acc@0.5', ((p_lr>=0.5)==yte).mean().round(4))
# CARD cost ratio
def cost(p, t, c_fn, c_fp):
    f = p>=t; return ((~f)&(yte==1)).sum()*c_fn + (f&(yte==0)).sum()*c_fp, f.mean()
pva = m_hg.predict_proba(Xva)[:,1]  # note: in-sample-ish since trained on Xtr incl va; refit on tr2 for threshold
m_hg2 = HistGradientBoostingClassifier(random_state=0, max_iter=300, learning_rate=0.05).fit(Xtr2, ytr2)
pva = m_hg2.predict_proba(Xva)[:,1]; pte2 = m_hg2.predict_proba(Xte)[:,1]
for ratio in [20,5]:
    ts = np.linspace(0.01,0.9,179)
    cva = [((pva<t)&(yva==1)).sum()*ratio + ((pva>=t)&(yva==0)).sum() for t in ts]
    tbest = ts[int(np.argmin(cva))]
    for nm,t in [('0.5',0.5),('theory 1/(1+r)',1/(1+ratio)),('val-tuned',tbest)]:
        c,fl = cost(pte2,t,ratio,1)
        print(f'ratio {ratio}:1 threshold {nm}={t:.3f}: cost units per 1000 customers {1000*c/len(yte):.0f}, share flagged {fl:.3f}')
    print(f'   flag nobody: {1000*yte.sum()*ratio/len(yte):.0f}; flag everybody: {1000*(yte==0).sum()/len(yte):.0f}')
# CARD capacity
n = len(yte)
for k in [500, 1000, 2000]:
    for nm,p in [('HGB',p_hg),('LR',p_lr)]:
        idx = np.argsort(-p)[:k]; tp = yte[idx].sum()
        print(f'capacity top {k} of {n} ({k/n:.1%}) {nm}: defaulters reached {tp} precision {tp/k:.3f} recall {tp/yte.sum():.3f}')
    # rule ranking: sort by PAY_0 then random tie-break
    rng=np.random.default_rng(0); key = Xte.PAY_0.values + rng.random(n)*0.01
    idx=np.argsort(-key)[:k]; tp=yte[idx].sum(); print(f'   rule-sort by PAY_0: {tp} precision {tp/k:.3f}')
    print(f'   random: expected {k*yte.mean():.0f}')
# CARD exposure
bill = np.clip(Xte.BILL_AMT1.values,0,None)
for k in [1000]:
    for nm,score in [('p only',p_hg),('p x bill',p_hg*bill)]:
        idx=np.argsort(-score)[:k]
        print(f'exposure top {k} by {nm}: defaulters {yte[idx].sum()}, defaulted bill captured NT$ {bill[idx][yte[idx]==1].sum()/1e6:.1f}M of {bill[yte==1].sum()/1e6:.1f}M ({bill[idx][yte[idx]==1].sum()/bill[yte==1].sum():.1%})')
# CARD reasons: LR vs HGB, and a 6-feature scorecard
sc = ['PAY_0','PAY_2','LIMIT_BAL','PAY_AMT1','PAY_AMT2','BILL_AMT1']
m_sc = lr(sc); p_sc = m_sc.predict_proba(Xte[sc])[:,1]
print(f'scorecard LR 6 features AUC {roc_auc_score(yte,p_sc):.4f}; LR all {roc_auc_score(yte,p_lr):.4f}; HGB all {roc_auc_score(yte,p_hg):.4f}')
# LR with PAY codes one-hot (categorical) -> better LR
cat = stat+['EDUCATION','MARRIAGE','SEX']
num = [c for c in allc if c not in cat]
ct = ColumnTransformer([('c',OneHotEncoder(handle_unknown='ignore'),cat),('n',StandardScaler(),num)])
m_lrc = make_pipeline(ct, LogisticRegression(max_iter=3000)).fit(Xtr, ytr); p_lrc=m_lrc.predict_proba(Xte)[:,1]
print(f'LR with status codes one-hot AUC {roc_auc_score(yte,p_lrc):.4f}')
# CARD sensitive
sens = ['SEX','MARRIAGE','AGE','EDUCATION']
nos = [c for c in allc if c not in sens]
m_ns = hgb(nos); p_ns = m_ns.predict_proba(Xte[nos])[:,1]
print(f'HGB without SEX,MARRIAGE,AGE,EDUCATION AUC {roc_auc_score(yte,p_ns):.4f} vs {roc_auc_score(yte,p_hg):.4f}')
k=1000
for nm,p in [('with',p_hg),('without',p_ns)]:
    idx=np.argsort(-p)[:k]; fl=np.zeros(n,bool); fl[idx]=True
    s=Xte.SEX.values
    print(f'  {nm} sensitive: share of men flagged {fl[s==1].mean():.3f}, women {fl[s==2].mean():.3f}; actual default men {yte[s==1].mean():.3f} women {yte[s==2].mean():.3f}; defaulters reached {yte[idx].sum()}')
# CARD data lag
lag1 = [c for c in allc if c not in ('PAY_0','BILL_AMT1','PAY_AMT1')]
lag2 = [c for c in lag1 if c not in ('PAY_2','BILL_AMT2','PAY_AMT2')]
for nm,cols in [('lag1',lag1),('lag2',lag2)]:
    m=hgb(cols); p=m.predict_proba(Xte[cols])[:,1]; idx=np.argsort(-p)[:1000]
    print(f'data lag {nm}: HGB AUC {roc_auc_score(yte,p):.4f}, AP {average_precision_score(yte,p):.4f}, top1000 defaulters {yte[idx].sum()}')
# CARD calibration with class_weight balanced
m_bal = lr(allc, cw='balanced'); p_bal = m_bal.predict_proba(Xte[allc])[:,1]
print(f'mean p: LR {p_lr.mean():.3f}, LR balanced {p_bal.mean():.3f}, true {yte.mean():.3f}; Brier LR {brier_score_loss(yte,p_lr):.4f} bal {brier_score_loss(yte,p_bal):.4f}')
t=1/21
for nm,p in [('LR',p_lr),('LR balanced',p_bal)]:
    c,fl=cost(p,t,20,1); print(f'  threshold 1/21 on {nm}: flagged {fl:.3f}, cost/1000 {1000*c/n:.0f}')
# duplicates effect
feat=[c for c in allc]
d = df.duplicated(subset=feat, keep=False)
print('rows sharing identical features', d.sum())
