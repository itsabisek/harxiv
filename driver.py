"""
Driver code to test working of all modules
"""
from crawler.crawler import Crawler
crawler = Crawler(search_query="electron")
crawler.make_request()
