import pandas as pd
import numpy as np
import joblib as jb
from sklearn.model_selection import train_test_split,RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,ExtraTreesClassifier,ExtraTreesRegressor
from sklearn.ensemble import AdaBoostClassifier,AdaBoostRegressor,GradientBoostingClassifier,GradientBoostingRegressor
from xgboost import XGBRegressor,XGBClassifier
from lightgbm import LGBMClassifier,LGBMRegressor
from catboost import CatBoostRegressor,CatBoostClassifier
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,f1_score,recall_score,accuracy_score,precision_score


df=pd.read_csv("creditcard_5000_project.csv")


numeric=[]
floatic=[]
cat=[]
for col in df.columns :
    if pd.api.types.is_numeric_dtype(df[col]):
        numeric.append(col)
    elif pd.api.types.is_float_dtype(df[col]):
        floatic.append(col)
    else:
        cat.append(col)


y=df["Class"]
y_reg=df["Amount"]
x=df.drop(columns=["Class","Amount"])

feature_state={}

for col in x.columns:
    feature_state[col]={
        "min":float(x[col].min()),
        "max":float(x[col].max()),
        "mean":float(x[col].mean())
    }

jb.dump(feature_state,"feature.pkl")    

# print(x.columns)

x_train,x_test,y1_train,y1_test,y_train,y_test=train_test_split(x,y,y_reg,train_size=0.8,random_state=22)


regressor={
    "random forest regressor":{
        "model":RandomForestRegressor(random_state=42),
        "params":{
        "n_estimators":[50,100],
        "max_depth":[5,10,15,None],
        "min_samples_split":[2,5,10],
        "min_samples_leaf":[1,2,4],
        "max_features":["sqrt", "log2"],
        
        }
    },
    "extra forest regressor":{
        "model":ExtraTreesRegressor(random_state=42),
        "params":{
        "n_estimators":[50,100],
        "max_depth":[5,10,15,None],
        "min_samples_split":[2,5,10],
        "min_samples_leaf":[1,2,4],
        "max_features":["sqrt", "log2"],
        
        }
    },
   
    "gradient boost regressor":{
        "model":GradientBoostingRegressor(),
        "params":{
    "n_estimators": [50,100],
    "learning_rate": [0.01, 0.1, 0.2],
    "max_depth": [3, 5, 7],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
        }
    },
    "Ada boost regressor":{
        "model":AdaBoostRegressor(),
        "params":{
            "n_estimators": [50, 100],
        "learning_rate": [0.01, 0.1, 1.0],
        "loss": ["linear", "square", "exponential"]
        }
    },
    "light boost regressor":{
        "model":LGBMRegressor(verbosity=-1,
    random_state=42),
        "params":{
            "n_estimators": [50,100],
            "learning_rate": [0.01, 0.1, 0.2],
            "max_depth": [3, 5, 7],
            "num_leaves": [31, 50, 100],
            "subsample": [0.8, 1.0]
        }
    },
    "cat boost regressor ":{
        "model":CatBoostRegressor(silent=True),
        "params":{
            "iterations": [50,100],
            "learning_rate": [0.01, 0.1, 0.2],
            "depth": [4, 6, 8, 10],
            "l2_leaf_reg": [1, 3, 5, 7]
        }
    },
}

reg_result=[]
best_regressor=[]
best_regression_model=None
best_reg_score=-999
best_reg_prediction=None
best_reg_model=None
best_reg_params=None
best_mae=None
best_mse=None
best_rmse=None
for name,info in regressor.items():
    best_model=info["model"]
    params=info["params"]
    search=RandomizedSearchCV(estimator=best_model,param_distributions=params,n_iter=2,cv=3,random_state=42,n_jobs=-1)
    search.fit(x_train,y_train)
    model=search.best_estimator_
    params=search.best_params_
    reg_prd=model.predict(x_test)
    reg_r2=r2_score(y_test,reg_prd)
    mae=mean_absolute_error(y_test,reg_prd)
    mse=mean_squared_error(y_test,reg_prd)
    rmse=np.sqrt(mse)
    reg_result.append({
        "model":name,
        "mae":round(mae,4),
        "mse":round(mse,4),
        "rmse":round(rmse,2),
        "r2":round(reg_r2,4),
        "parameter":params
    })
    if reg_r2>best_reg_score:
        best_reg_model=name
        best_reg_score=reg_r2
        best_reg_prediction=reg_prd
        best_reg_params=params
        best_mae=mae
        best_mse=mse
        best_rmse=rmse
        best_regression_model=model
best_regressor.append({
        "model":best_reg_model,
        "mae":round(best_mae,4),
        "mse":round(best_mse,4),
        "rmse":round(best_rmse,4),
        "r2":best_reg_score
    })  


resutl_df=pd.DataFrame(reg_result)  
print(resutl_df)
best_regressor_df=pd.DataFrame(best_regressor)
print(f"\n\n{best_regressor_df}")



classifier={
    "random forest classifier":{
        "models":RandomForestClassifier(random_state=42),
        "parames":{
        "n_estimators":[50,100],
        "max_depth":[5,10,15,None],
        "min_samples_split":[2,5,10],
        "min_samples_leaf":[1,2,4],
        "max_features":["sqrt", "log2"],
        
        }
    },
    "extra forest classifier":{
        "models":ExtraTreesClassifier(random_state=42),
        "parames":{
        "n_estimators":[50,100],
        "max_depth":[5,10,15,None],
        "min_samples_split":[2,5,10],
        "min_samples_leaf":[1,2,4],
        "max_features":["sqrt", "log2"],
        
        }
    },
   
    "gradient boost classifier":{
        "models":GradientBoostingClassifier(random_state=42),
        "parames":{
    "n_estimators": [50,100],
    "learning_rate": [0.01, 0.1, 0.2],
    "max_depth": [3, 5, 7],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
        }
    },
    "Ada boost classifier":{
        "models":AdaBoostClassifier(random_state=42),
        "parames":{
            "n_estimators": [50, 100],
        "learning_rate": [0.01, 0.1, 1.0],
        }
    },
    "light boost classifier":{
        "models":LGBMClassifier(verbosity=-1,
    random_state=42),
        "parames":{
            "n_estimators": [50,100],
            "learning_rate": [0.01, 0.1, 0.2],
            "max_depth": [3, 5, 7],
            "num_leaves": [31, 50, 100],
            "subsample": [0.8, 1.0]
        }
    },
    "cat boost classifier ":{
        "models":CatBoostClassifier(silent=True),
        "parames":{
            "iterations": [50,100],
            "learning_rate": [0.01, 0.1, 0.2],
            "depth": [4, 6, 8, 10],
            "l2_leaf_reg": [1, 3, 5, 7]
        }
    },
}


cla_result=[]
best_clasifier=[]
best_classify_model=None
best_cla_score=-999
best_cla_prediction=None
best_cla_model=None
best_cla_params=None
best_accuracy=None
best_precision=None
best_recall=None
for key,value in classifier.items():
    best_model=value["models"]
    parames=value["parames"]
    find=RandomizedSearchCV(estimator=best_model,param_distributions=parames,n_iter=2,cv=3,random_state=42,n_jobs=-1)
    find.fit(x_train,y1_train)
    models=find.best_estimator_
    best_parames=find.best_params_
    cla_prd=models.predict(x_test)
    acu=accuracy_score(y1_test,cla_prd)
    f1=f1_score(y1_test,cla_prd)
    prc=precision_score(y1_test,cla_prd)
    rll=recall_score(y1_test,cla_prd)
    cla_result.append({
        "model":key,
        "score":round(acu,3),
        "precision":round(prc,3),
        "recall":round(rll,3),
        "f1":round(f1,3)
    })
    if f1 >best_cla_score:
        best_cla_score=f1
        best_cla_prediction=cla_prd
        best_cla_model=key
        best_cla_params=best_parames
        best_accuracy=acu
        best_precision=prc
        best_recall=rll
        best_classify_model=models
best_clasifier.append({
        "model":best_cla_model,
        "prediction":best_cla_prediction[:4],
        "score":best_cla_score,
        "precision":best_precision,
        "recall":best_recall,
        "accuracy":best_accuracy
    })    

cla_result_df=pd.DataFrame(cla_result)
best_cla_df=pd.DataFrame(best_clasifier)    
print(f"\n\n{cla_result_df}")
print(f"\n\n{best_cla_df}")

jb.dump(best_classify_model,"best_classifier.pkl")
jb.dump(best_regression_model,"best_regressor.pkl")
 
cla_result_df.to_csv("classification_rsult.csv",index=False) 
best_cla_df.to_csv("best_classification_rslt.csv",index=False)
resutl_df.to_csv("regression_result.csv",index=False)
best_regressor_df.to_csv("best_regressor.csv",index=False)

