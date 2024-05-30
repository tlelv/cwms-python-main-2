from typing import Optional

import cwms.api as api
from cwms.types import JSON, Data


# TODO
# - Create Categories folder & File                                         *DONE*
# - Fork Repo locally                                                       *DONE*
# - Create call to get function
#   - Call catalog function (dictionary) and return a data frame
# - Add function into time series file (to call JSON from API get).

# NOTES:
# Params are timeseries from get time series
# Add checks to see which args work
# Find out which arguments are essential
# Get catalogs function w response to server


# CONFIRM WHICH PARAMETERS ARE NECESSARY
#       Potentially make some parameters optional
#       How to connect to api and test. (Let computer run cwms imports)
#       What can i do to connect to server

#       Create catalog test file
#       Reinstall cwms to test (getting started)
#       Create checks for parameters (to see what is necessary)
#       GET RESPONSE FROM SERVER TO SEE HOW IT PARSES
#       Pass dictionary from timeseries file into catalog, so its not 1-to-1
#       Set dataset to timeseries. Set rest of args to dictionary
#       Catalog function has to return dataframe, make more concise

def get_timeseries_catalog(
        dataset: str,
        page: Optional[str] = None,
        page_size: Optional[int] = None,
        unit_system: Optional[str] = None,
        office_id: Optional[str] = None,
        like: Optional[str] = None,
        timeseries_category_id: Optional[str] = None,
        timeseries_group_id: Optional[str] = None,
        location_category_id: Optional[str] = None,
        location_group_id: Optional[str] = None,
        bounding_office_id: Optional[str] = None,
) -> Data:
    """Retrieves time series catalog (FIX ME ONCE PARAMETERS HAVE BEEN CONFIRMED)

        Parameters
            ----------
                group_id: string
                    Timeseries group whose data is to be included in the response.
                category_id: string
                    The category id that contains the timeseries group.
                office_id: string
                    The owning office of the timeseries group.

            Returns
            -------
            response : dict
                The JSON response containing the time series catalog information.
        """

    # INCLUDE CONNECTION FROM CATEGORIES CLASS HERE
    # Include time series, follow swger page
    endpoint = f"catalog/{dataset}"
    params = {"page": page,
              "page-size": page_size,
              "units": unit_system,
              "office": office_id,
              "like": like,
              "timeseries-category": timeseries_category_id,
              "timeseries-group": timeseries_group_id,
              "location-category": location_category_id,
              "location-group": location_group_id,
              "bounding-office": bounding_office_id,
              }

    response = api.get(endpoint=endpoint, params=params, api_version=1)
    return Data(response, selector="time-series-catalog")
