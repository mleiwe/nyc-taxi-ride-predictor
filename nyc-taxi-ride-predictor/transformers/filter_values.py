if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    dur_min = 0
    dur_max = 60
    dist_min = 0
    dist_max = 1000
    
    idx = ((df['duration']>dur_min) & (df['duration']<=dur_max)) & ((df['trip_distance']>dist_min) & (df['trip_distance']<=dist_max))
    df_filt = df[idx]
    print("Original")
    print(df.describe())
    print("Filtered")
    print(df_filt.describe())
    return df_filt


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
