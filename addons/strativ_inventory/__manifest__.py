# -*- coding: utf-8 -*-
{
    "name": "Strativ Inventory",
    "summary": """
        Inventory management app for Strativ""",
    "description": """
        This app is designed to streamline inventory management for Strativ.
        It provides a centralized platform for tracking, organizing,
        and managing assets, ensuring efficient operations and accurate record-keeping
    """,
    "author": "Strativ",
    "website": "https://www.strativ.se",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Inventory/Inventory",
    "version": "16.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        'security/ir.model.access.csv',
        'views/items_views.xml',
        'views/items_menus.xml',
        'views/item_category_views.xml',
        'views/item_tag_views.xml',
    ],
    # only loaded in demonstration mode
    "demo": [],
    'installable': True,
    'application': True,
}
