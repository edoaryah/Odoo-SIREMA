import base64
from odoo import models, fields, api
import xlrd

# import from csv
class ImportWizard(models.TransientModel):
    _name = 'import.wizard'

    file = fields.Binary(string='File')

    def import_data(self):
        file_data = base64.b64decode(self.file)
        workbook = xlrd.open_workbook(file_contents=file_data)
        sheet = workbook.sheet_by_index(0)

        for row in range(1, sheet.nrows):
            vals = {
                'name': sheet.cell(row, 0).value,
                'nim': sheet.cell(row, 1).value,
                'mk1': sheet.cell(row, 2).value,
                'mk2': sheet.cell(row, 3).value,
                'mk3': sheet.cell(row, 4).value,
                'mk4': sheet.cell(row, 5).value,
                'mk5': sheet.cell(row, 6).value,
                'mk6': sheet.cell(row, 6).value,
            }
            self.env['data.awal'].create(vals)

        self.env.invalidate_all()

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

class Mahasiswa(models.Model):
    _name = 'data.awal'
    _description = 'Data Mahasiswa'

    name = fields.Char(string='Nama', required=True)
    nim = fields.Char(string='NIM', required=True, index=True)
    mk1 = fields.Integer(string='Basis Data')
    mk2 = fields.Integer(string='Kecerdasan Bisnis')
    mk3 = fields.Integer(string='Jaringan Komputer')
    mk4 = fields.Integer(string='Pemrograman')
    mk5 = fields.Integer(string='IMK')
    mk6 = fields.Integer(string='Bahasa Inggris')

    @api.model
    def create(self, values):
        # Panggil create dari model ini
        record = super(Mahasiswa, self).create(values)

        # Cek apakah model 'mahasiswa.mahasiswa' sudah memiliki catatan dengan NIM yang sama
        existing_mahasiswa = self.env['mahasiswa.mahasiswa'].search([('nim', '=', values.get('nim'))])
        existing_mahasiswa2 = self.env['mahasiswa2.mahasiswa2'].search([('nim', '=', values.get('nim'))])
        existing_mahasiswa3 = self.env['mahasiswa3.mahasiswa3'].search([('nim', '=', values.get('nim'))])
        existing_mahasiswa4 = self.env['mahasiswa4.mahasiswa4'].search([('nim', '=', values.get('nim'))])
        existing_mahasiswa_rekomendasi = self.env['mahasiswa.rekomendasi'].search([('nim', '=', values.get('nim'))])

        if not existing_mahasiswa:
            # Buat catatan di model 'mahasiswa.mahasiswa' dengan nilai yang sama
            self.env['mahasiswa.mahasiswa'].create({
                'name': values.get('name'),
                'nim': values.get('nim'),
                'mk1': values.get('mk1'),
                'mk2': values.get('mk2'),
                'mk3': values.get('mk3'),
                'mk4': values.get('mk4'),
                'mk5': values.get('mk5'),
                'mk6': values.get('mk6'),
            })

        if not existing_mahasiswa2:
            # Buat catatan di model 'mahasiswa.mahasiswa' dengan nilai yang sama
            self.env['mahasiswa2.mahasiswa2'].create({
                'name': values.get('name'),
                'nim': values.get('nim'),
                'mk1': values.get('mk1'),
                'mk2': values.get('mk2'),
                'mk3': values.get('mk3'),
                'mk4': values.get('mk4'),
                'mk5': values.get('mk5'),
                'mk6': values.get('mk6'),
            })

        if not existing_mahasiswa3:
            # Buat catatan di model 'mahasiswa.mahasiswa' dengan nilai yang sama
            self.env['mahasiswa3.mahasiswa3'].create({
                'name': values.get('name'),
                'nim': values.get('nim'),
                'mk1': values.get('mk1'),
                'mk2': values.get('mk2'),
                'mk3': values.get('mk3'),
                'mk4': values.get('mk4'),
                'mk5': values.get('mk5'),
                'mk6': values.get('mk6'),
            })

        if not existing_mahasiswa4:
            # Buat catatan di model 'mahasiswa.mahasiswa' dengan nilai yang sama
            self.env['mahasiswa4.mahasiswa4'].create({
                'name': values.get('name'),
                'nim': values.get('nim'),
                'mk1': values.get('mk1'),
                'mk2': values.get('mk2'),
                'mk3': values.get('mk3'),
                'mk4': values.get('mk4'),
                'mk5': values.get('mk5'),
                'mk6': values.get('mk6'),
            })

        if not existing_mahasiswa_rekomendasi:
            # Buat catatan di model 'mahasiswa.mahasiswa' dengan nilai yang sama
            self.env['mahasiswa.rekomendasi'].create({
                'nim': values.get('nim'),
                'name': values.get('name')
            })

        return record