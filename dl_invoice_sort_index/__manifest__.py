# __manifest__.py
{
    'name': 'DL Invoice Sort Index',
    'version': '15.0.1.0.0',
    'summary': 'Ensures invoices are ordered correctly by sequential number (SAFT-AO compliant).',
    'description': """
🔢 DL Invoice Sort Index

This module improves the sorting of invoices in Odoo by using the sequential invoice number instead of the default string-based sorting.

✨ Features
- Fixes incorrect ordering (e.g., INV2024/10 before INV2024/2).
- Adds a numeric index field `name_sort_index`.
- Ensures invoices are listed and exported in proper sequential order.

📑 SAFT-AO Compliance
Proper invoice sequencing is mandatory for SAFT validation in Angola. With this module, your invoices are exported in the correct order, ensuring compliance.
    """,
    'author': 'DIGITALUB ANGOLA, LDA',
    'website': 'https://digitalub.ao',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
    'price': 12.0,
    'currency': 'USD',
}