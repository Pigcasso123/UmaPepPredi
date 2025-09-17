import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


df=pd.read_csv('umami_features.csv')
X=df[['logP','TPSA','charge','molecular_weight','CTERM','NTERM','N_TERM','vina_energy']].values
y=df['umami_intensity'].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=123)
model=RandomForestRegressor()
model.fit(X_train,y_train)
print(f"R²: {model.score(X_test, y_test):.2f}")