from odoo import models, fields, api


class ClearDataWizard(models.TransientModel):
    _name = 'clear_data_wizard'
    _description = 'Clear Data Wizard'

    confirmation_text = fields.Text(string='Confirmation', default='')

    def clear_data(self):
        # Lakukan operasi penghapusan data dari model-model yang Anda inginkan
        self.env['data.awal'].sudo().search([]).unlink()
        self.env['mahasiswa.mahasiswa'].sudo().search([]).unlink()
        self.env['mahasiswa2.mahasiswa2'].sudo().search([]).unlink()
        self.env['mahasiswa3.mahasiswa3'].sudo().search([]).unlink()
        self.env['mahasiswa4.mahasiswa4'].sudo().search([]).unlink()
        self.env['mahasiswa.rekomendasi'].sudo().search([]).unlink()

        # Atau gunakan pendekatan lain sesuai dengan kebutuhan Anda

        # Bersihkan teks konfirmasi
        self.confirmation_text = "Data cleared successfully!"
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'clear_data_wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('sirema_ahp.clear_data_wizard_view_form').id,
            'target': 'new',
            'res_id': self.id,
        }