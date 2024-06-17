#  Copyright (c) 2024
#  United States Army Corps of Engineers - Hydrologic Engineering Center (USACE/HEC)
#  All Rights Reserved.  USACE PROPRIETARY/CONFIDENTIAL.
#  Source may not be released without written approval from HEC
import json
from datetime import datetime

import pytest
import pytz

import cwms.api
from tests._test_utils import read_resource_file
import cwms.catalog.catalog as ct

_MOCK_ROOT = "https://mockwebserver.cwms.gov"
_CATALOG_JSON = read_resource_file("catalog.json")


@pytest.fixture(autouse=True)
def init_session():
    cwms.api.init_session(api_root=_MOCK_ROOT)

def test_get_catalog(requests_mock):
    requests_mock.get(

        #JUST FIX THIS MOCK ROOT
        f"{_MOCK_ROOT}"
        "/timeseries/binary?office=SPK&name=TEST.Binary.Inst.1Hour.0.MockTest&"
        "begin=2024-02-12T00%3A00%3A00-08%3A00&"
        "end=2020-02-12T02%3A00%3A00-08%3A00",
        json=_CATALOG_JSON,
    )

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

    data = ct.get_timeseries_catalog(dataset,
                                     office_id,
                                     page,
                                     page_size,
                                     unit_system,
                                     like,
                                     timeseries_category_like,
                                     timeseries_group_like,
                                     location_category_like,
                                     location_group_like,
                                     bounding_office_like)
    assert data.json == _CATALOG_JSON

def run_catalog_examples():
    print("------Running through catalog examples-------")

    # GIVEN DATA for DATASET
    location = """
        {
          "name": "TEST",
          "latitude": 0,
          "longitude": 0,
          "active": true,
          "public-name": "CWMS TESTING",
          "long-name": "CWMS TESTING",
          "description": "CWMS TESTING",
          "timezone-name": "America/Los_Angeles",
          "location-kind": "PROJECT",
          "nation": "US",
          "state-initial": "NV",
          "county-name": "Clark",
          "nearest-city": "Las Vegas, NV",
          "horizontal-datum": "NAD83",
          "vertical-datum": "NGVD29",
          "elevation": 320.04,
          "bounding-office-id": "SPK",
          "office-id": "SPK"
        }
        """
    headers = {"Content-Type": constants.HEADER_JSON_V1}
    print("Storing location TEST")
    ct_api.get_session().post(
        "locations", params=None, headers=headers, data=location
    )
    catalog_dict = json.loads(
        """
        {
              "dataset": location,
              "page": "",
              "page-size": "500",
              "units": "SI",
              "office": "SPK",
              "like": "",
              "timeseries-category": "",
              "timeseries-group": "",
              "location-category": "",
              "location-group": "",
              "bounding-office": "",
        }
        """
    )
    print(f"Storing catalog params {catalog_dict['dataset']}")
    ct.get_timeseries_catalog(catalog_dict, office_id=None)
    date_string = "1900-01-01T06:00:00"
    office_id = "SPK"
    effective_date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
    print('dataset')

    # TEST EACH FUNCTION (INSERT PARAMETER CHECKS)

    # time_series = level_api.retrieve_level_as_timeseries_json(
    #    level_id, office_id, "m", interval="1Hour"
    #)
    #print(time_series)


if __name__ == "__main__":
    ct.function_test()
    run_catalog_examples()
