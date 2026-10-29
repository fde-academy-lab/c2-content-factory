import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score
hm, ulb, bc = sys.argv[1], sys.argv[2], sys.argv[3]
# HMDA
df = pd.read_csv(hm, low_memory=False, dtype=str)
y = (df.action_taken=='3').astype(int).values
leak = (df.interest_rate.isna() | df.interest_rate.isin(['NA','Exempt'])).astype(int).values
print('HMDA AUC of interest_rate-missing flag alone', round(roc_auc_score(y, leak),4))
def num(s):
    return pd.to_numeric(s, errors='coerce')
dti_map = {'<20%':15,'20%-<30%':25,'30%-<36%':33,'50%-60%':55,'>60%':65}
dti = df.debt_to_income_ratio.map(lambda v: dti_map.get(v, v)); dti = num(dti.astype(str).str.rstrip('%'))
age_map={'<25':22,'25-34':30,'35-44':40,'45-54':50,'55-64':60,'65-74':70,'>74':78}
X = pd.DataFrame({'loan_amount':num(df.loan_amount),'income':num(df.income),'ltv':num(df.loan_to_value_ratio),
    'property_value':num(df.property_value),'dti':dti,'loan_term':num(df.loan_term),
    'loan_purpose':num(df.loan_purpose),'loan_type':num(df.loan_type),'lien':num(df.lien_status),'occupancy':num(df.occupancy_type),
    'credit_score_type':num(df.applicant_credit_score_type)})
X_leak = X.assign(interest_rate=num(df.interest_rate), origination_charges=num(df.origination_charges))
cv = StratifiedKFold(5, shuffle=True, random_state=0)
for nm, XX in [('application fields only', X), ('plus interest_rate and origination_charges', X_leak)]:
    s = cross_val_score(HistGradientBoostingClassifier(random_state=0), XX, y, cv=cv, scoring='roc_auc')
    print(f'HMDA HGB {nm}: CV AUC {s.mean():.4f}')
print('HMDA DTI raw values with no % sign', df.debt_to_income_ratio.str.fullmatch(r'\d+').sum(), 'with %', df.debt_to_income_ratio.str.fullmatch(r'\d+%').sum())
print('HMDA credit_score_type 1111 (exempt) rows', (df.applicant_credit_score_type=='1111').sum(), 'age 8888', (df.applicant_age=='8888').sum(), 'denial_reason-1 1111', (df['denial_reason-1']=='1111').sum())
print('HMDA denied with denial_reason-1==10 (not applicable)', ((y==1)&(df['denial_reason-1']=='10')).sum(), 'originated with reason !=10', ((y==0)&(df['denial_reason-1']!='10')).sum())
# ULB
f = pd.read_parquet(ulb); f['Class']=f.Class.astype(int)
tr = f[f.Time<86400]; te = f[f.Time>=86400]
cols = [c for c in f.columns if c not in ('Class','Time')]
m = HistGradientBoostingClassifier(random_state=0, max_iter=200).fit(tr[cols], tr.Class)
p = m.predict_proba(te[cols])[:,1]; yt = te.Class.values
print(f'ULB time split: train day1 n {len(tr)} frauds {tr.Class.sum()}, test day2 n {len(te)} frauds {yt.sum()}; AUC {roc_auc_score(yt,p):.4f} AP {average_precision_score(yt,p):.4f}')
print(f'ULB accuracy of all-genuine on day2 {1-yt.mean():.5f}')
amt = te.Amount.values
for k in [100, 200, 500]:
    idx=np.argsort(-p)[:k]
    print(f'ULB review top {k} alerts on day2: frauds caught {yt[idx].sum()} of {yt.sum()}, fraud amount caught EUR {amt[idx][yt[idx]==1].sum():.0f} of {amt[yt==1].sum():.0f}')
for k in [200]:
    idx=np.argsort(-(p*amt))[:k]
    print(f'ULB review top {k} by p x amount: frauds caught {yt[idx].sum()}, amount caught {amt[idx][yt[idx]==1].sum():.0f}')
# random split comparison
Xtr,Xte,ytr,yte = train_test_split(f[cols], f.Class, test_size=te.shape[0]/len(f), random_state=0, stratify=f.Class)
m2 = HistGradientBoostingClassifier(random_state=0, max_iter=200).fit(Xtr,ytr); p2=m2.predict_proba(Xte)[:,1]
print(f'ULB random split AUC {roc_auc_score(yte,p2):.4f} AP {average_precision_score(yte,p2):.4f}')
# BankChurners
b = pd.read_csv(bc); yb=(b.Attrition_Flag=='Attrited Customer').astype(int).values
nb=[c for c in b.columns if c.startswith('Naive')]
Xb = b.drop(columns=['CLIENTNUM','Attrition_Flag']+nb)
for c in Xb.select_dtypes(exclude='number').columns: Xb[c]=Xb[c].astype('category').cat.codes
s = cross_val_score(HistGradientBoostingClassifier(random_state=0), Xb, yb, cv=cv, scoring='roc_auc'); print(f'BankChurners HGB without NB columns CV AUC {s.mean():.4f}')
act=['Total_Trans_Ct','Total_Trans_Amt','Total_Ct_Chng_Q4_Q1','Total_Amt_Chng_Q4_Q1','Total_Revolving_Bal','Avg_Utilization_Ratio','Avg_Open_To_Buy']
s = cross_val_score(HistGradientBoostingClassifier(random_state=0), Xb.drop(columns=act), yb, cv=cv, scoring='roc_auc'); print(f'BankChurners HGB without 12-month activity columns CV AUC {s.mean():.4f}')
