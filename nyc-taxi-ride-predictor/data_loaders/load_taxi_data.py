import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    This will download taxi data from the site (https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

    The structure of the web address
    https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi-colour}_tripdata_{year}-{month}.parquet

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    years = kwargs['years']
    months = kwargs['months']
    taxi_colour = kwargs['taxi_colour']
    #url_address = https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi-colour}_tripdata_{year}-{month}.parquet
    for i, yr in enumerate(years):
        for j, mnth in enumerate(months):
            for k,colour in enumerate(taxi_colour):
                url_address = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{colour}_tripdata_{yr}-{mnth}.parquet"
                if (i==0) and (j==0) and (k==0):
                    df = pd.read_parquet(url_address)
                else:
                    df = pd.concat([df, pd.read_parquet(url_address)])
    return df


@test
def test_output(output, *args) -> None:
    """
    One simple unit test to seem if the number of columns is 20
    """
    assert output.shape[1]==20, 'There are an incorrect number of columns'
