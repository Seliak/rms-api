from odoo import models, fields

class ScholarArticle(models.Model):
    _name = 'scholar.article'
    _description = 'Google Scholar Article'

    title = fields.Char(string='Title', required=True)
    snippet = fields.Text(string='Snippet')
    link = fields.Char(string='Link')
    author = fields.Char(string='Author')
