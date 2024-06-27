from typing import Tuple, List, Dict
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse._csr import csr_matrix

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def dict_vectoriser(data, *args, **kwargs) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    The aim here is to create the dictionary vectoriser for the pick up and drop off location IDs

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df_train = data['taxi_train_test_split'][0]
    df_test = data['taxi_train_test_split'][1]

    #Extract the target variable
    y_train = df_train['duration']
    y_test = df_test['duration']
    
    #Dictionary Vectoriser for Categorical features
    dv = DictVectorizer()
    X_train = dv.fit_transform(df_train.drop(columns=['duration']).to_dict(orient='records'))
    X_test = dv.transform(df_test.drop(columns=['duration']).to_dict(orient='records'))

    return X_train, y_train, X_test, y_test, dv


@test
def test_output(output, *args) -> Tuple[csr_matrix, pd.Series, csr_matrix, pd.Series, DictVectorizer]:
    """
    Template code for testing the output of the block.
    """

    assert output is not None, 'The output is undefined'
