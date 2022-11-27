from odoo import fields, models, api


class KursiPengantin(models.Model):
    _name = 'wedding.kursi_pengantin'
    _description = 'Daftar Kursi Pengantin Pelaminan'

    name = fields.Char(string='Nama Kursi Pengantin', required=True)
    deskripsi = fields.Char(string='Deskripsi Kursi Pengantin', required=False)
    harga = fields.Integer(string='Harga Sewa', required=False)
