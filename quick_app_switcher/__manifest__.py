# -*- coding: utf-8 -*-

{
    "name": "Quick App Switcher",
    "version": "18.0.1.0.0",
    "category": "Productivity",
    "summary": "Switch Odoo apps instantly from compact navbar buttons",
    "description": """
Quick App Switcher adds compact, one-click application buttons directly to
the Odoo backend navbar.

Each user can configure their own shortcuts from Preferences. The switcher
respects Odoo menu access rights and displays only applications available to
the current user. It stays hidden on the Home / All Apps page.
    """,
    "author": "Mitchel Admin",
    "maintainer": "Mitchel Admin",
    "support": "erpmitchellodoo@gmail.com",
    "depends": ["web_enterprise"],
    "data": ["views/res_users_views.xml"],
    "assets": {
        "web.assets_backend": [
            "quick_app_switcher/static/src/js/quick_app_switcher.js",
            "quick_app_switcher/static/src/xml/quick_app_switcher.xml",
            "quick_app_switcher/static/src/scss/quick_app_switcher.scss",
        ],
    },
    "license": "LGPL-3",
    "images": ["static/description/banner.png"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
