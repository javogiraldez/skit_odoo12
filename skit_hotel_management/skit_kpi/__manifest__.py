# -*- coding: utf-8 -*-

{
    "name": "Key Performance Indicator",
    "version": "12.0.1.1.0",
    "author": "Srikesh Infotech",
    "website": "http://www.srikeshinfotech.com",
    "license": "AGPL-3",
    "category": "Report",
    "depends": [
        'base_external_dbsource', 'point_of_sale',
    ],
    "qweb": ['static/src/xml/pos.xml'],
    "data": [
        'security/ir.model.access.csv',
        'security/kpi_security.xml',
        'views/kpi_category.xml',
        'views/kpi_history.xml',
        'views/kpi_threshold_range.xml',
        'views/kpi_threshold.xml',
        'views/kpi.xml',
        'views/menu.xml',
        'views/kpi_templates.xml',
        'data/kpi.xml',
    ],
    "images": [
        "images/kpi_definition.png",
        "images/kpi_computation.png",
        "images/kpi_threshold.png",
        "images/kpi_range.png",
    ],
    'installable': True,
}
