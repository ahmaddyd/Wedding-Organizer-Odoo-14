import json

from odoo import http
from odoo.http import request


class KursiTamuController(http.Controller):

    @http.route(['/kursi_tamu'], type="http", auth="public", website=True, method=['GET'],
                csrf=False)
    def getkursitamu(self, **kwargs):
        kursi = request.env['wedding.kursi_tamu'].search([])
        value = [{"nama_kursi": k.name,
                  "tipe_bahan": k.tipe,
                  "stok_tersedia": k.stok,
                  "harga_sewa": k.harga} for k in kursi]
        return json.dumps(value)
