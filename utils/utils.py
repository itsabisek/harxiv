"""
Utils file for misc utility classes and methods
"""
from __future__ import annotations
import json
import collections
from utils.constants import QUERY_CONFIG_FILE

class QueryParams(object):
    """
    Singleton class to parse the Query config json file
    """
    __instance = None
    query_params = {}
    search_query_options = {}
    search_query_boolean = {}

    def __new__(cls) -> QueryParams:
        if cls.__instance is None:
            cls.__instance = super(QueryParams, cls).__new__(cls)
        return cls.__instance

    def get_query_params(self) -> dict:
        if (
            not self.query_params or
            not self.search_query_options or
            not self.search_query_boolean
        ):
            with open(QUERY_CONFIG_FILE, "r", encoding="utf-8") as config:
                config_dict = json.loads(config.read())
                self.query_params = config_dict.get("query_params", {})
                self.search_query_options = config_dict.get("search_query_options", {})
                self.search_query_boolean = config_dict.get("search_query_boolean", {})

        return self.query_params

class Query:
    """
    Query object class
    """
    query_params = {}
    search_query_options = {}
    search_query_boolean = {}
    query_params = QueryParams()

    def __init__(self, **query_kwargs) -> None:
        self.query_params = self.query_params.get_query_params().copy()
        for param, val in query_kwargs.items():
            self.query_params[param] = val

    def get_string(self):
        """
        Get query object as a formatted query string starting with ?
        """
        return f'?{"&".join([f"{param}={val}" for param, val in self.query_params.items() if val is not None])}'

    @classmethod
    def get_available_params(cls) -> collections.abc.KeysView:
        """
        Get all the available params in the Query class
        """
        return cls.query_params.get_query_params().keys()

    @classmethod
    def make_query(cls, **query_kwargs) -> Query:
        """
        Returns a Query Object
        """
        return cls(**query_kwargs)
