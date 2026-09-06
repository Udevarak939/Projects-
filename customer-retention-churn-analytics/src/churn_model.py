import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

FEATURES=['sessions_30d','orders_90d','avg_order_value','days_since_last_activity','support_tickets']

def train(df):
    X=df[FEATURES].fillna(0); y=df['churned']
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
    model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000))
    model.fit(Xtr,ytr)
    return model, roc_auc_score(yte,model.predict_proba(Xte)[:,1])

def score_customers(model,df):
    out=df.copy(); out['churn_probability']=model.predict_proba(out[FEATURES].fillna(0))[:,1]
    out['priority']=out.churn_probability * out.avg_order_value
    return out.sort_values('priority',ascending=False)
