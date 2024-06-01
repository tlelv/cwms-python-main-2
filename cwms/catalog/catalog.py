from typing import Optional

import cwms.api as api
from cwms.types import JSON, Data


# TODO
# Add checks to see which args work
# Find out which arguments are essential
# Get catalogs function w response to server
# CONFIRM WHICH PARAMETERS ARE NECESSARY
#       Potentially make some parameters optional
#       How to connect to api and test. (Let computer run cwms imports)
#       What can i do to connect to server

#       Create checks for parameters (to see what is necessary)
#       GET RESPONSE FROM SERVER TO SEE HOW IT PARSES
#       Pass dictionary from timeseries file into catalog, so its not 1-to-1
#       Set dataset to timeseries. Set rest of args to dictionary
#       Catalog function has to return dataframe, make more concise
#       GET RESPONSE FROM SERVER
#       UPDATE FORMAT OF DATAFRAME
#       The filter are the args/parameters

def get_catalog(
        dataset: str,
        page: Optional[str] = None,
        page_size: Optional[int] = None,
        unit_system: Optional[str] = None,
        office_id: Optional[str] = None,
        like: Optional[str] = None,
        timeseries_category_like: Optional[str] = None,
        timeseries_group_like: Optional[str] = None,
        location_category_like: Optional[str] = None,
        location_group_like: Optional[str] = None,
        bounding_office_like: Optional[str] = None,
) -> Data:
    """Retrieves time series catalog

    Parameters
    ----------
        dataset: string
            The type of data in the list. Valid values for this field
            are:
                1. TIMESERIES
                2. LOCATIONS
        page: string
            The endpoint used to identify where the request is located.
        page_size: integer
            The entries per page returned. The default value is 500.
        unit_system: string
            The unit system desired in response. Valid values for this
            field are:
                1. SI
                2. EN
        office_id: string
            The owning office of the timeseries group.
        like: string
            The regex for matching against the id
        timeseries_category_like: string
            The regex for matching against the category id
        timeseries_group_like: string
            The regex for matching against the timeseries group id
        location_category_like: string
            The regex for matching against the location category id
        location_group_like: string
            The regex for matching against the location group id
        bounding_office_like: string
            The regex for matching against the location bounding office

    Returns
    -------
    response : dict
        The JSON response containing the time series catalog information.
    """

    endpoint = f"catalog/{dataset}"
    params = {"page": page,
              "page-size": page_size,
              "units": unit_system,
              "office": office_id,
              "like": like,
              "timeseries-category": timeseries_category_like,
              "timeseries-group": timeseries_group_like,
              "location-category": location_category_like,
              "location-group": location_group_like,
              "bounding-office": bounding_office_like,
              }

    response = api.get(endpoint=endpoint, params=params, api_version=1)
    return Data(response, selector="time-series-catalog")
