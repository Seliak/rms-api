from odoo import models, fields
from odoo.exceptions import UserError
import re
import requests
import logging

_logger = logging.getLogger(__name__)

class ScholarSearch(models.TransientModel):
    _name = 'scholar.search'
    _description = 'Scholar Search'

    author_name = fields.Char(string='Author Name', required=True)

    def search_articles(self):
        """
        The function `search_articles` searches for articles by a specific
        author using the Google Scholar API and stores the results in a
        custom model in Odoo.
        """
        self.ensure_one()  # Ensure that the method is called on a single record

        API_KEY = 'c7bd80de63adb5373d1b55270f09560c537db52afc92833dd70332249b3d3c1d'
        params = {
            'engine': 'google_scholar',
            'q': self.author_name,
            'api_key': API_KEY
        }

        try:
            response = requests.get('https://serpapi.com/search', params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            results = response.json()
            for result in results.get('organic_results', []):
                self.env['scholar.article'].create({
                    'title': result['title'],
                    'snippet': result['snippet'],
                    'link': result['link'],
                    'author': self.author_name
                })
        except requests.exceptions.RequestException as e:
            _logger.error(f"Error while fetching articles: {e}")
            raise UserError(f"Error while fetching articles: {e}")

        return True
