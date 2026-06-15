from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_no_faktur_pajak = fields.Char(string='No Faktur Pajak')
