from odoo import http

class ScholarSearchController(http.Controller):

    @http.route('/scholar/search', type='json', auth='user')
    def search_articles(self, **kwargs):
        author_name = kwargs.get('author_name')
        if author_name:
            request.env['scholar.search'].search_articles(author_name)
        return {'status': 'success'}
