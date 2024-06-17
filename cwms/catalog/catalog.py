from typing import Optional, Dict

import cwms.api as api
from cwms.types import Data


# TODO
#       1. Run CWMS
#           - Potentially get data/response from server
#       Extra:
#           - See format of resulting dataframe or json
#           - Setup Pre-commit/pre-commit hooks (in docs/read-me)
#           - Setup pycharm to pre-format before
#               - black (plugin) and isort on save
#               - Flake8 (linter)

def function_test():
    print("Hello World")


def get_catalog(dataset: str, params: Dict[str, Optional[str]]) -> Data:
    """Retrieves filters for the catalog

        Parameters
            ----------
            dataset: string
                The type of data in the list. Valid values for this field
                are:
                    1. TIMESERIES
                    2. LOCATIONS
            params: dict
                A dictionary containing the following keys:
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
                    office: string
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
                The JSON response containing the time series catalog.
        """

    # CHECKS
    if dataset is None:
        raise ValueError("Cannot retrieve a time series for a catalog without a dataset")

    endpoint = f"catalog/{dataset}"

    # creates the dataframe from the timeseries data
    response = api.get(endpoint=endpoint, params=params, api_version=1)
    return Data(response, selector="time-series-catalog")


'''

def get_catalog(
        dataset: str,
        office_id: str,
        page: Optional[str] = None,
        page_size: Optional[int] = None,
        unit_system: Optional[str] = None,
        like: Optional[str] = None,
        timeseries_category_like: Optional[str] = None,
        timeseries_group_like: Optional[str] = None,
        location_category_like: Optional[str] = None,
        location_group_like: Optional[str] = None,
        bounding_office_like: Optional[str] = None,
) -> Data:
    """Retrieves filters for the catalog

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
            The JSON response containing the time series catalog.
        """
    
    # CHECKS
    if dataset is None:
        raise ValueError("Cannot retrieve a time series for a catalog without a dataset")
    if office_id is None:
        raise ValueError("Retrieve timeseries catalog requires an office")
    
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
    
    # creates the dataframe from the timeseries data (TESTING STOPS HERE DUE TO CERTIFICATE ISSUE)
    response = api.get(endpoint=endpoint, params=params, api_version=1)
    return Data(response, selector="time-series-catalog")
'''
