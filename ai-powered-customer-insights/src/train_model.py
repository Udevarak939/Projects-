import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,roc_auc_score
import joblib

df=pd.read_csv('data/customers.csv'); X=df.drop(columns=['customer_id','churn']); y=df.churn
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
m=GradientBoostingClassifier(random_state=42).fit(Xtr,ytr); p=m.predict_proba(Xte)[:,1]
print('ROC-AUC:',round(roc_auc_score(yte,p),3)); print(classification_report(yte,m.predict(Xte)))
joblib.dump(m,'model.joblib')
