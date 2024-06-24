Looking at the feature profiles from the transform_data_features, we can see that there may be a few errors. Namely, there are some extreme values. We need to establish some filters
* `trip_distance`: min>=1 and max<=1000
* `duration`: min>=1 and max<=60 