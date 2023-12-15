from odoo import models, fields, api

class MahasiswaRekomendasi(models.Model):
    _name = 'mahasiswa.rekomendasi'
    _description = 'Rekomendasi Mahasiswa'

    name = fields.Char(string='Nama Mahasiswa', compute='_compute_nama', store=True)
    nim = fields.Char(string='NIM', required=True, index=True)
    nilai_topsis_mahasiswa1 = fields.Float(string='Topsis Data Analyst', compute='_compute_nilai_topsis_mahasiswa1', store=True, digits=(6, 3))
    nilai_topsis_mahasiswa2 = fields.Float(string='Topsis Software Engineer', compute='_compute_nilai_topsis_mahasiswa2', store=True, digits=(6, 3))
    nilai_topsis_mahasiswa3 = fields.Float(string='Topsis Jaringan', compute='_compute_nilai_topsis_mahasiswa3', store=True, digits=(6, 3))
    nilai_topsis_mahasiswa4 = fields.Float(string='Topsis UI/UX', compute='_compute_nilai_topsis_mahasiswa4', store=True, digits=(6, 3))
    rekomendasi = fields.Char(string='Rekomendasi', compute='_compute_rekomendasi')

    # def action_report_mahasiswa_rekomendasi(self):
    #     # Logika untuk mempersiapkan data
    #     data = {
    #         'model': 'mahasiswa.rekomendasi',
    #         'form': self.read()[0]
    #     }
    #
    #     # Mengeksekusi tindakan laporan
    #     return self.env.ref('sirema_ahp.report_mahasiswa_rekomendasi').report_action(self, data=data)

    @api.depends('nim')
    def _compute_nama(self):
        for record in self:
            mahasiswa = self.env['data.awal'].search([('nim', '=', record.nim)], limit=1)
            record.name = mahasiswa.name if mahasiswa else ''

    @api.depends('nim')
    def _compute_nilai_topsis_mahasiswa1(self):
        for record in self:
            mahasiswa1 = self.env['mahasiswa.mahasiswa'].search([('nim', '=', record.nim)])
            record.nilai_topsis_mahasiswa1 = mahasiswa1.nilai_topsis if mahasiswa1 else 0.0

    @api.depends('nim')
    def _compute_nilai_topsis_mahasiswa2(self):
        for record in self:
            mahasiswa2 = self.env['mahasiswa2.mahasiswa2'].search([('nim', '=', record.nim)])
            record.nilai_topsis_mahasiswa2 = mahasiswa2.nilai_topsis if mahasiswa2 else 0.0

    @api.depends('nim')
    def _compute_nilai_topsis_mahasiswa3(self):
        for record in self:
            mahasiswa3 = self.env['mahasiswa3.mahasiswa3'].search([('nim', '=', record.nim)])
            record.nilai_topsis_mahasiswa3 = mahasiswa3.nilai_topsis if mahasiswa3 else 0.0

    @api.depends('nim')
    def _compute_nilai_topsis_mahasiswa4(self):
        for record in self:
            mahasiswa4 = self.env['mahasiswa4.mahasiswa4'].search([('nim', '=', record.nim)])
            record.nilai_topsis_mahasiswa4 = mahasiswa4.nilai_topsis if mahasiswa4 else 0.0

    @api.depends('nilai_topsis_mahasiswa1', 'nilai_topsis_mahasiswa2', 'nilai_topsis_mahasiswa3',
                 'nilai_topsis_mahasiswa4')
    def _compute_rekomendasi(self):
        for record in self:
            max_nilai = max(record.nilai_topsis_mahasiswa1, record.nilai_topsis_mahasiswa2,
                            record.nilai_topsis_mahasiswa3, record.nilai_topsis_mahasiswa4)
            if max_nilai == record.nilai_topsis_mahasiswa1:
                record.rekomendasi = 'Data Analyst'
            elif max_nilai == record.nilai_topsis_mahasiswa2:
                record.rekomendasi = 'Software Engineer'
            elif max_nilai == record.nilai_topsis_mahasiswa3:
                record.rekomendasi = 'Jaringan'
            elif max_nilai == record.nilai_topsis_mahasiswa4:
                record.rekomendasi = 'UI/UX'
            else:
                record.rekomendasi = 'Belum Ada Rekomendasi'