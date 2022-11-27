from odoo import fields, models, api


class Pengembalian(models.Model):
    _name = 'wedding.pengembalian'
    _description = 'Pengembalian Barang'

    name = fields.Many2one(comodel_name='wedding.order', string='Order')
    tanggal_pengembalian = fields.Date(string='Tanggal Pengembalian', default=fields.Date.today(), required=False)
    penyewa = fields.Char(compute='_compute_penyewa', string='Nama Penyewa', required=False)
    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan', required=False)

    @api.depends('name')
    def _compute_penyewa(self):
        for record in self:
            record.penyewa = self.env['wedding.order'].search([('id', '=', record.name.id)]).mapped('pemesan').name

    @api.depends('name')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.total

    @api.model
    def create(self, values):
        record = super(Pengembalian, self).create(values)
        if record.tanggal_pengembalian:
            self.env['wedding.order'].search([('id', '=', record.name.id)]).write(
                {'sudah_kembali': True})
            self.env['wedding.organizer_akunting'].create([{'kredit': record.tagihan, 'name': record.penyewa}])
            return record

    def unlink(self):
        for username in self:
            self.env['wedding.order'].search([('id', '=', username.name.id)]).write({'sudah_kembali': False})
        record = super(Pengembalian, self).unlink()
