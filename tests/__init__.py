import cwms
from datetime import datetime, timedelta

end = datetime.now()
begin = end - timedelta(days = 10)
data = cwms.get_timeseries(tsId='Some.Fully.Qualified.Ts.Id',office_id='SVT' , begin = begin, end = end)

#a cwms data object will be provided this object containes both the JSON as well
#as the values converted into a dataframe

#display the dataframe

df = data.df
print(df)