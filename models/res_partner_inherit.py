from odoo import fields, models, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_pegawai = fields.Boolean(
        string='Pegawai',
        required=False)
    is_pelanggan = fields.Boolean(
        string='Pelanggan',
        required=False)
