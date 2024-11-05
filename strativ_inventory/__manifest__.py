{
    "name": "Strativ Inventory",
    "summary": """
        Inventory management app for Strativ
    """,
    "description": """
        This app is designed to streamline inventory management for Strativ.
        It provides a centralized platform for tracking, organizing,
        and managing assets, ensuring efficient operations and accurate record-keeping
    """,
    "author": "Strativ",
    "website": "https://www.strativ.se",
    "category": "Inventory/Inventory",
    "version": "16.0.1.0.0",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'views/strativ_inventory_item.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'strativ_inventory/static/src/css/custom_style.css',
        ],
    },
    "demo": [],
}
