# -*- coding: utf-8 -*-
{
    "name": "Account payment: Select accounts",
    "summary": "Allow user to select the account where journal item will be recorded",
    "version": "15.0.1.0.0",
    "development_status": "Beta",
    "category": "Invoicing Management",
    "author": "Bashier Elbashier",
    "maintainers": ["Bashier Elbashier"],
    "application": False,
    "installable": True,
    "depends": [
        "account",
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        "data/data.xml",
        "views/account_payment_view.xml"
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
