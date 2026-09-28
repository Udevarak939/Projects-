import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score,classification_report

df=pd.read_csv('data/raw/bank-full.csv',sep=';'); y=(df.y=='yes').astype(int); X=df.drop(columns='y'); cat=X.select_dtypes(include='object').columns
pre=ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),cat)],remainder='passthrough')
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
model=Pipeline([('prep',pre),('clf',GradientBoostingClassifier(random_state=42))]).fit(Xtr,ytr); p=model.predict_proba(Xte)[:,1]
print('ROC-AUC:',round(roc_auc_score(yte,p),3)); print(classification_report(yte,(p>=.5).astype(int)))
