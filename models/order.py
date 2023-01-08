from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import datetime


class Order(models.Model):
    _name = 'wedding.order'
    _description = 'Order Wedding Organizer'

    name = fields.Char(string='Kode Order', required=True)
    order_detail_panggung_ids = fields.One2many(comodel_name='wedding.order_detail_panggung', inverse_name='name',
                                                string='Order Detail Panggung', required=False)
    order_detail_kursi_tamu_ids = fields.One2many(comodel_name='wedding.order_detail_kursi_tamu', inverse_name='name',
                                                  string='Order Detail Panggung', required=False)
    total = fields.Integer(compute='_compute_total', string='Total Harga', store=True, required=False)
    tanggal_pesan = fields.Datetime(string='Tanggal Pemesanan', default=fields.Datetime.now(), required=True)
    tanggal_pengiriman = fields.Datetime(string='Tanggal Pengiriman',
                                         default=fields.Datetime.now() + datetime.timedelta(days=1), required=True)
    pemesan = fields.Many2one(comodel_name='res.partner', string='Pemesan', domain=[('is_pelanggan', '=', True)],
                              required=False)
    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', required=False)

    @api.depends('order_detail_panggung_ids', 'order_detail_kursi_tamu_ids')
    def _compute_total(self):
        for record in self:
            search_harga_panggung = sum(
                self.env['wedding.order_detail_panggung'].search([('name', '=', record.id)]).mapped('harga'))
            search_harga_kursi_tamu = sum(
                self.env['wedding.order_detail_kursi_tamu'].search([('name', '=', record.id)]).mapped('harga'))
            record.total = search_harga_panggung + search_harga_kursi_tamu

    def kembali_barang(self):
        pass


class OrderDetailPanggung(models.Model):
    _name = 'wedding.order_detail_panggung'
    _description = 'Order Detail Panggung'

    name = fields.Many2one(comodel_name='wedding.order', string='Order', required=False)
    panggung_id = fields.Many2one(comodel_name='wedding.panggung', string='Panggung', required=False)
    harga = fields.Integer(compute='_compute_harga', string='Harga', required=False)
    qty = fields.Integer(string='Quantity', required=False)
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan', required=False)

    @api.depends('panggung_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.panggung_id.harga

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['wedding.panggung'].search([('stok', '<', record.qty), ('id', '=', record.panggung_id.id)])
            if bahan:
                raise ValidationError('Stok %s tidak mencukupi' % record.panggung_id.name)

    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self, values):
        record = super(OrderDetailPanggung, self).create(values)
        if record.qty:
            self.env['wedding.panggung'].search([('id', '=', record.panggung_id.id)]).write(
                {'stok': record.panggung_id.stok - record.qty})
            return record


class OrderDetailKursiTamu(models.Model):
    _name = 'wedding.order_detail_kursi_tamu'
    _description = 'Order Detail Kursi Tamu'

    name = fields.Many2one(comodel_name='wedding.order', string='Order', required=False)
    kursi_tamu_id = fields.Many2one(comodel_name='wedding.kursi_tamu', string='Kursi Tamu', required=False)
    harga = fields.Integer(compute='_compute_harga', string='Harga', required=False)
    qty = fields.Integer(string='Quantity', required=False)
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan', required=False)

    @api.depends('kursi_tamu_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.kursi_tamu_id.harga

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['wedding.kursi_tamu'].search(
                [('stok', '<', record.qty), ('id', '=', record.kursi_tamu_id.id)])
            if bahan:
                raise ValidationError('Stok %s tidak mencukupi' % record.kursi_tamu_id.name)

    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self, values):
        # Add code here
        record = super(OrderDetailKursiTamu, self).create(values)
        if record.qty:
            self.env['wedding.kursi_tamu'].search([('id', '=', record.kursi_tamu_id.id)]).write(
                {'stok': record.kursi_tamu_id.stok - record.qty})
            return record
