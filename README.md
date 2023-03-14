# surfs_up

## Overview
- The purpose of this analysis is to determine the sustainability of a year-round, surf and ice cream shop business, on Oahu, Hawaii, by observing the key differences in weather between June and December, along with providing recommendations for further analysis.

## Results
- Based on the Summary Statistics for June and December, 3 Key Differences between the two times of the year can be identified when observing the summary statistics from the tables below

![SurfsUp_Challenge_Screenshot_1](https://user-images.githubusercontent.com/120291854/225101719-e1a74c54-0f34-4058-91f7-f35b617e7011.png)
![SurfsUp_Challenge_Screenshot_2](https://user-images.githubusercontent.com/120291854/225101739-e280d82a-9823-4170-ae1f-439b3357bf27.png)

### 1. Lower number of observations for December
- The first difference we notice when evaluating the summary statistics is the differnnce in the count between June and December. The count represents the number of temperature observations recorded by the various stations on the island for that month. The count for June is 1700 while the count for December is only 1517.

### 2. Higher average and median temperatures in June 
- The tables above allow us to compare the temperatures, in Oahu, from June and December. One of the first statistics that stand out are the differences in the mean temperature values for June versus December. The average temperature in June is 74.9 °F, while the average temperature in December is only 71.0 °F. The median, represented by the 50% percentile value in the tables, is 75.0 °F for June and only 71.0 °F for December, indicating December has lower measures of central tendency than June.

### 3. Higher spread in the data for December
- The final major difference that stands out when observing the summary statistics for temperatures in June vs. December for the island of Oahu, is the difference in the spread of temperature values for the two months. For June, the standard deviation is 3.26 °F while the standard deviation in December is 3.75 °F. The Interquartile Range (IQR), determined by subtracting the 75th percentile value from the 25th percentile value, is 4.00 °F for the month of June and 5.00 °F for the month of December. 

## Summary
- In our analysis we were able to see how the temperature in Oahu varies during different times of the year by comparing temperature summary statistics for the months of June and December. Specifically, we were able to identify higher, but relatively similar temperatures in June over December. The lower measures of central tendency for December can be explained by the higher measures of spread between the values in December over June. This tells us that there are is a greater difference in temperature values between the two months on the lower end of the spectrum, and this is further supported by much lower minimum temperature value for December (56.0 °F) when compared to June's minimimum (64.0 °F). With temperature averages in the seventies for both months, a surfing and ice cream business on the island should be feasible year-round.

- One suggestion I would make to further corroborate our conclusion is to observe the difference in temperature between the various weather stations on the island. This could help us to find any weird outliers in the data that may skew our results due to a particular station. An additional query we could perform would be to obtain the number of days that a non-zero amount was recorded for precipitation on the island over a specific year. This query would give us the number of days that rainfall occurs to go along with the amount of precipitation recorded that we queried for earlier in the Module.
