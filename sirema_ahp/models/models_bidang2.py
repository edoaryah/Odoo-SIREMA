import base64
from odoo import models, fields, api
import xlrd

class Mahasiswa2(models.Model):
    _name = 'mahasiswa2.mahasiswa2'
    _description = 'Data Mahasiswa'

    name = fields.Char(string='Nama', required=True)
    nim = fields.Char(string='NIM', required=True, index=True)
    mk1 = fields.Integer(string='Basis Data')
    mk2 = fields.Integer(string='Kecerdasan Bisnis')
    mk3 = fields.Integer(string='Jaringan Komputer')
    mk4 = fields.Integer(string='Pemrograman')
    mk5 = fields.Integer(string='IMK')
    mk6 = fields.Integer(string='Bahasa Inggris')

    nilai_topsis = fields.Float(compute="_perhitungan_spk", store=True, digits=(6, 3))

    @api.depends('mk1', 'mk2', 'mk3', 'mk4', 'mk5', 'mk6')
    def _perhitungan_spk(self):
        for record in self:
            mahasiswa_data = self.env['mahasiswa2.mahasiswa2'].search([])

            alternatif = [mhs.name for mhs in mahasiswa_data]

            alternatifkriteria = [[mhs.mk1, mhs.mk2, mhs.mk3, mhs.mk4, mhs.mk5, mhs.mk6] for mhs in mahasiswa_data]

            kriteria = ["Basis Data", "Kecerdasan Bisnis", "Jaringan Komputer", "Pemrograman", "IMK", "Bahasa Inggris"]

            costbenefit = ["benefit", "benefit", "benefit", "benefit", "benefit", "benefit"]

            perbandingankriteria = [
                [1, 2, 1, 1, 0.333, 2],
                [0.5, 1, 0.5, 0.5, 0.2, 1],
                [1, 2, 1, 1, 0.333, 2],
                [1, 2, 1, 1, 0.333, 5],
                [3, 5, 3, 3, 1, 5],
                [0.5, 1, 0.5, 0.2, 0.2, 1],
            ]

            totalkolom = [sum(x) for x in zip(*perbandingankriteria)]

            normalisasi = [[perbandingankriteria[i][j] / totalkolom[j] for j in range(len(kriteria))] for i in range(len(perbandingankriteria))]

            bobotprioritas = [sum(normalisasi[i]) / len(kriteria) for i in range(len(normalisasi))]

            pembagi = [sum(alternatifkriteria[j][i] ** 2 for j in range(len(alternatif))) ** 0.5 for i in range(len(kriteria))]

            normalisasi_topsis = [[alternatifkriteria[i][j] / pembagi[j] for j in range(len(kriteria))] for i in range(len(alternatif))]

            terbobot = [[normalisasi_topsis[i][j] * bobotprioritas[j] for j in range(len(kriteria))] for i in range(len(alternatif))]

            aplus = [min(terbobot[j][i] for j in range(len(alternatif))) if costbenefit[i] == 'cost' else max(terbobot[j][i] for j in range(len(alternatif))) for i in range(len(kriteria))]

            amin = [max(terbobot[j][i] for j in range(len(alternatif))) if costbenefit[i] == 'cost' else min(terbobot[j][i] for j in range(len(alternatif))) for i in range(len(kriteria))]

            dplus = [(sum((aplus[j] - terbobot[i][j]) ** 2 for j in range(len(kriteria)))) ** 0.5 for i in range(len(alternatif))]

            dmin = [(sum((terbobot[i][j] - amin[j]) ** 2 for j in range(len(kriteria)))) ** 0.5 for i in range(len(alternatif))]

            hasil = [dmin[i] / (dmin[i] + dplus[i]) for i in range(len(alternatif))]

            # Assuming each record has a unique Mahasiswa assigned
            record.nilai_topsis = float(hasil[alternatif.index(record.name)])
