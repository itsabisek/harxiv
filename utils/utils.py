"""
Utils file for misc utility classes and methods
"""
from __future__ import annotations
import collections
class Query:
    """
    Query object class
    """
    search_query:str = None
    id_list:str = None
    start:int = 0
    max_results:int = 10
    sortBy = None
    sortOrder = None

    def __init__(self, **query_kwargs) -> None:
        for param, val in query_kwargs.items():
            self.__dict__[param] = val

    def get_string(self):
        """
        Get query object as a formatted query string starting with ?
        """
        return f'?{"&".join([f"{param}={val}" for param, val in self.__dict__.items() if val is not None])}'

    @classmethod
    def get_available_params(cls) -> collections.abc.KeysView:
        """
        Get all the available params in the Query class
        """
        return cls.__dict__.keys()

    @classmethod
    def make_query(cls, **query_kwargs) -> Query:
        """
        Returns a Query Object
        """
        return cls(**query_kwargs)
