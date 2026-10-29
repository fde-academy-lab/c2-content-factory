import sys, pandas as pd, numpy as np
df = pd.read_csv(sys.argv[1], low_memory=False, dtype=str)
print(df.shape)
y = (df.action_taken=='3').astype(int)
print('action_taken', df.action_taken.value_counts().to_dict(), 'denial rate', y.mean().round(4))
print('loan_purpose', df.loan_purpose.value_counts().to_dict())
for c in ['interest_rate','rate_spread','total_loan_costs','origination_charges','denial_reason-1','debt_to_income_ratio','income','loan_to_value_ratio','property_value','applicant_age','derived_sex','derived_race','applicant_credit_score_type']:
    s = df[c]
    na = s.isna() | s.isin(['NA'])
    print(f'{c}: missing/NA overall {na.mean():.3f}; among denied {na[y==1].mean():.3f}; among originated {na[y==0].mean():.3f}; Exempt {(s=="Exempt").sum()}; top {s.value_counts().head(8).to_dict()}')
print('denial reasons', df.loc[y==1,'denial_reason-1'].value_counts().to_dict())
print('denial rate by derived_race', df.groupby('derived_race').apply(lambda g:(g.action_taken=="3").mean(), include_groups=False).round(3).to_dict())
print('n by derived_race', df.derived_race.value_counts().to_dict())
print('denial rate by derived_sex', df.groupby('derived_sex').apply(lambda g:(g.action_taken=="3").mean(), include_groups=False).round(3).to_dict())
print('dup rows', df.duplicated().sum())
