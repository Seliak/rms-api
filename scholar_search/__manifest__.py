{
    'author': 'Francisco José S.E. (PeGon)',
    'license': 'AGPL-3',
    'name': 'Scholar Search',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Search and store Google Scholar articles by author',
    'description': """Module to search and store Google Scholar articles
    by author using SerpApi.""",
    'depends': ['base'],
    'data': [
        'views/scholar_article_view.xml',
        'views/scholar_search_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
