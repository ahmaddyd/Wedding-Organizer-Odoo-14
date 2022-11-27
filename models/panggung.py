from odoo import fields, models, api


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Panggung Pelaminan'

    name = fields.Char(string='Nama Panggung', required=True)
    pelaminan_id = fields.Many2one(comodel_name='wedding.pelaminan', string='Tipe Pelaminan', required=True)
    kursi_pengantin_id = fields.Many2one(comodel_name='wedding.kursi_pengantin', string='Kursi Pengantin',
                                         required=False)
    accesories = fields.Char(string='Aksesoris Pelaminan', required=True)
    bunga = fields.Selection(string='Tipe Bunga', required=True,
                             selection=[('bunga mati', 'Bunga Mati'), ('bunga hidup', 'Bunga Hidup')])
    harga = fields.Integer(compute='_compute_harga', string='Harga Sewa', required=True)
    stok = fields.Integer(string='Stok Paket Panggung', required=False)
    deskripsi_pelaminan = fields.Char(compute='_compute_deskripsi_pelaminan', string='Deskripsi Pelaminan',
                                      required=False)
    deskripsi_kursi = fields.Char(compute='_compute_deskripsi_kursi', string='Deskripsi Kursi', required=False)

    @api.depends('pelaminan_id', 'kursi_pengantin_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan_id.harga + record.kursi_pengantin_id.harga

    @api.depends('pelaminan_id')
    def _compute_deskripsi_pelaminan(self):
        for record in self:
            record.deskripsi_pelaminan = record.pelaminan_id.deskripsi

    @api.depends('kursi_pengantin_id')
    def _compute_deskripsi_kursi(self):
        for record in self:
            record.deskripsi_kursi = record.kursi_pengantin_id.deskripsi
