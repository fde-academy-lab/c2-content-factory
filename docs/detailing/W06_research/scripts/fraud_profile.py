import sys, pandas as pd, numpy as np
df = pd.read_parquet(sys.argv[1])
print(df.shape); print(list(df.columns)); print(df.dtypes.value_counts().to_dict())
y = df['Class'].astype(int)
print('frauds', y.sum(), 'base', round(y.mean()*100,4), '%')
print('missing', int(df.isna().sum().sum()))
print('dup rows (all cols)', df.duplicated().sum(), 'dup rows excl Time', df.drop(columns='Time').duplicated().sum())
dd = df[df.duplicated(keep=False)]
print('frauds among duplicated rows', dd.Class.astype(int).sum())
print('Time range', df.Time.min(), df.Time.max(), 'hours', df.Time.max()/3600)
print('Amount', df.Amount.describe().round(2).to_dict())
print('Amount==0', (df.Amount==0).sum(), 'frauds with Amount 0', ((df.Amount==0)&(y==1)).sum())
print('fraud Amount', df.Amount[y==1].describe().round(2).to_dict())
print('total fraud amount', df.Amount[y==1].sum().round(2), 'total amount', df.Amount.sum().round(0))
day = (df.Time>=86400).astype(int)
print('day1/day2 rows', day.value_counts().to_dict(), 'fraud rate by day', y.groupby(day).mean().round(5).to_dict())
hr = (df.Time//3600)%24
print('fraud rate by hour of clock', y.groupby(hr).mean().mul(100).round(3).to_dict())
