{
    'name': 'Naska Account Faktur Pajak',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Menambahkan field x_no_faktur_pajak pada account.move',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
