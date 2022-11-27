from odoo import fields, models, api


class Akunting(models.Model):
    _name = 'wedding.organizer_akunting'
    _description = 'Akunting'
    _order = 'id asc'

    name = fields.Char(string='Nama', required=True)
    id_akunting = fields.Char(string='Kode Akunting')
    tanggal = fields.Datetime(string='Tanggal', default=fields.Datetime.now(), required=False)
    debet = fields.Integer(string='Debet', required=False)
    kredit = fields.Integer(string='Kredit', required=False)
    saldo = fields.Float(compute='_compute_saldo', string='Saldo')

    @api.depends('debet', 'kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id', '<', record.id)], limit=1, order='tanggal desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debet
