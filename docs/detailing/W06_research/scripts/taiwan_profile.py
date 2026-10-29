import sys, pandas as pd, numpy as np
p = sys.argv[1]
df = pd.read_excel(p, header=1)
print(df.shape); print(list(df.columns))
y = 'default payment next month'
print('base rate', df[y].mean(), df[y].sum())
print('missing total', int(df.isna().sum().sum()))
print('dup ID', df['ID'].duplicated().sum())
feat = [c for c in df.columns if c not in ('ID',)]
print('dup rows excl ID', df.duplicated(subset=feat).sum(), 'dup rows excl ID and target', df.duplicated(subset=[c for c in feat if c!=y]).sum())
d2 = df[df.duplicated(subset=[c for c in feat if c!=y], keep=False)]
print('rows in dup groups', len(d2), 'conflicting labels groups', d2.groupby([c for c in feat if c!=y])[y].nunique().gt(1).sum())
print('all-zero bill and pay rows', ((df[[f'BILL_AMT{i}' for i in range(1,7)]]==0).all(1) & (df[[f'PAY_AMT{i}' for i in range(1,7)]]==0).all(1)).sum())
for c in ['SEX','EDUCATION','MARRIAGE']:
    print(c, df[c].value_counts().sort_index().to_dict())
    print('  default rate by', df.groupby(c)[y].mean().round(4).to_dict())
for c in ['PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']:
    print(c, df[c].value_counts().sort_index().to_dict())
print('PAY_0 default rate', df.groupby('PAY_0')[y].agg(['mean','size']).round(3).to_string())
print('AGE', df.AGE.describe().round(1).to_dict())
print('LIMIT_BAL', df.LIMIT_BAL.describe().round(0).to_dict())
for i in range(1,7):
    b=df[f'BILL_AMT{i}']; pa=df[f'PAY_AMT{i}']
    print(f'BILL_AMT{i} neg', (b<0).sum(), 'zero', (b==0).sum(), 'max', b.max(), ' PAY_AMT zero', (pa==0).sum(), 'max', pa.max())
print('bill > limit (month1)', (df.BILL_AMT1>df.LIMIT_BAL).sum())
# column order check
print(df[[ 'PAY_0','PAY_2','BILL_AMT1','PAY_AMT1']].head())
