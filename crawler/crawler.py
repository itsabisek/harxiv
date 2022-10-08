"""
Crawler file
"""
import requests
from utils.logger_utils import bootstrap_logger
from utils.utils import Query

logger = bootstrap_logger(__name__, "crawler.log")

class Crawler:
    """
    The crawler class
    """

    API_URL = "https://export.arxiv.org/api/query"

    def __init__(self, **query_kwargs) -> None:
        self.query_obj = self.get_query_obj(**query_kwargs)

    def get_query_obj(self, **query_kwargs) -> Query:
        """
        Uses Query class to return a query object
        """
        for param in query_kwargs:
            if param not in Query.get_available_params():
                raise ValueError(f"Invalid query parameter {param} passed!")

        return Query.make_query(**query_kwargs)

    def build_session(self) -> requests.Session:
        """
        Create a request session
        """
        __session = requests.Session()
        return __session

    def get_url(self) -> str:
        """
        Form and return the final url
        """
        return f'{self.API_URL}{self.query_obj.get_string()}'

    def push_resp_for_parsing(self, resp) -> None:
        """
        Push the response to the parsing queue
        """
        logger.info("Got Response\n\n\n\n %s", len(resp.text))
        #TODO: Put push to celery/redis here

    def make_request(self):
        """
        Make the request to the API
        """
        __url = self.get_url()
        with self.build_session() as s:
            resp = s.get(__url)
            self.push_resp_for_parsing(resp)
