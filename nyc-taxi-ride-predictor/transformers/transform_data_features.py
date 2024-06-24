import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    This aims to transform the dataframe into a simple dataframe with a few key columns

    * "PU_DO_LocationID": merged string of the pick up and drop off locations ["PULocationID" + "DOLocationID"]
    * "trip_distance": This stays the same
    * "duration": lpep_dropoff_datetime - lpep_pickup_datetime convert to minutes

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        pd.DataFrame
    """
    ChosenColumns = ['PU_DO_LocationID','trip_distance','duration']
    
    #Calculate duration
    df['duration'] = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']).dt.total_seconds().astype('float64').astype('float64') / 60
    
    #PU_DO_LocationID
    PU_DO_LocationIDs = []
    for i in range(df.shape[0]):
        PU = str(df.iloc[i]['PULocationID'])
        DO = str(df.iloc[i]['DOLocationID'])
        txt = f"{PU}_{DO}"
        PU_DO_LocationIDs.append(txt)
    df['PU_DO_LocationID'] = PU_DO_LocationIDs

    #Columns
    df_features = df[ChosenColumns]
    return df_features


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output.shape[1] == 3, 'The output should have 3 columns'
