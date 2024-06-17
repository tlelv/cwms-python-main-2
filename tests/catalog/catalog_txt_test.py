import cwms.timeseries.timeseries as ts
import cwms.catalog.catalog as ct

# ts.get_timeseries_catalog("MVP")

ct.function_test()

dataset = "TIMESERIES"
office_id = "SPK"
page = None
page_size = 500
unit_system = "SI"
like = None
timeseries_category_like = None
timeseries_group_like = None
location_category_like = None
location_group_like = None
bounding_office_like = None

ts.get_timeseries_catalog(office_id,
                          page,
                          page_size,
                          unit_system,
                          like,
                          timeseries_category_like,
                          timeseries_group_like,
                          location_category_like,
                          location_group_like,
                          bounding_office_like)
