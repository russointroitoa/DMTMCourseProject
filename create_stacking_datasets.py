import pandas as pd
import numpy as np
from algorithms.Model_LightGBM import LightGBM
from algorithms.Model_CatBoost import CatBoost
from algorithms.Model_Linear_Regression import LinearRegressionClass

import sys
sys.path.append('../')

from main import main

categorical_features = ['cluster', 'sku', 'pack', 'brand'],
drop_cols = ['scope', 'Date', 'real_target', 'pack', 'size (GM)', 'cluster']

train_params = {
    'useTest':False,
    'useScope':False,
    'save':True,
    'completeCV':True,
    'dataAugm':True,
    'rand_noise':False,
    'categorical_features':['cluster', 'sku', 'pack', 'brand'],
    'drop_cols':['scope', 'Date', 'real_target', 'pack', 'size (GM)', 'cluster'],
}

train_params_cluster = train_params.copy()
train_params_cluster['cluster'] = [1,2,3]

test_params = {
    'useTest':True,
    'useScope':True,
    'save':True,
    'completeCV':False,
    'dataAugm':False,
    'rand_noise': False,
    'categorical_features':['cluster', 'sku', 'pack', 'brand'],
    'drop_cols':['scope', 'Date', 'real_target', 'pack', 'size (GM)', 'cluster'],
}

test_params_cluster = test_params.copy()
test_params_cluster['cluster'] = [1,2]

# Create Prediction on both Train and Test


# LightGBM Standard
lgb_model_params = {'max_depth': 15, 'learning_rate': 0.07617385187267685, 'n_estimators': 950, 'num_leaves': 24}

train_params['name'] = 'lgb_std'
test_params['name'] = 'lgb_std'

lgb_train_params = train_params.copy()
lgb_train_params['drop_cols'] = ['scope', 'Date',
                                 'real_target', 'pack',
                                 'size (GM)','cluster',
                                 'week_of_the_year',
                                 'month','brand']

lgb_test_params = test_params.copy()
lgb_test_params['drop_cols'] = ['scope', 'Date',
                                'real_target', 'pack',
                                'size (GM)', 'cluster',
                                'week_of_the_year',
                                'month','brand']

main(model=LightGBM(**lgb_model_params),**lgb_train_params)
main(model=LightGBM(**lgb_model_params),**lgb_test_params)

# LightGBM Cluster
train_params_cluster['name'] = 'lgb_cls'
test_params_cluster['name'] = 'lgb_cls'

lgb_train_params_cluster = train_params_cluster.copy()
lgb_train_params_cluster['drop_cols'] = ['scope', 'Date', 'real_target', 'pack', 'size (GM)',
                                 'cluster','week_of_the_year','month','brand']

lgb_test_params_cluster = test_params_cluster.copy()
lgb_test_params_cluster['drop_cols'] = ['scope', 'Date', 'real_target', 'pack', 'size (GM)',
                                 'cluster','week_of_the_year','month','brand']

main(model = LightGBM(**lgb_model_params), **lgb_train_params_cluster)
main(model=LightGBM(**lgb_model_params),**lgb_test_params_cluster)



# Catboost Standard
model = CatBoost()

train_params['name'] = 'cat_std'
test_params['name'] = 'cat_std'

main(model=CatBoost(), **train_params)
main(model=CatBoost(),**test_params)


# Catboost Cluster

train_params_cluster['name'] = 'cat_cls'
test_params_cluster['name'] = 'cat_cls'

main(model=CatBoost(), **train_params_cluster)
main(model=CatBoost(),**test_params_cluster)


# Linear Regression per sku
train_params['name'] = 'linear_reg'
test_params['name'] = 'linear_reg'

drop_cols = train_params['drop_cols'].copy()
drop_cols = drop_cols + ['pack', 'brand']

train_params['drop_cols'] = drop_cols
test_params['drop_cols'] = drop_cols

train_params['rand_noise'] = True
test_params['rand_noise'] = True

main(model=LinearRegressionClass(), **train_params)
main(model=LinearRegressionClass(), **test_params)
