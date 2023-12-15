from odoo import models, fields, api

class PerhitunganSPK(models.Model):
        _name = 'perhitungan.spk'
        _description = 'Perhitungan SPK Mahasiswa'

        mahasiswa_id = fields.Many2one('mahasiswa.mahasiswa', string='Mahasiswa', required=True)
        nilai_topsis = fields.Float(string='Nilai TOPSIS', compute='_compute_nilai_topsis', store=True)

        @api.depends('mahasiswa_id')
        def _compute_nilai_topsis(self):

            alternatif = []
            alternatifkriteria = []

            for record in self:
                mahasiswa = record.mahasiswa_id  # Ambil data mahasiswa dari field relasi

                if not mahasiswa:
                    record.nilai_topsis = 0.0  # Nilai default jika data mahasiswa tidak ditemukan
                    continue

                alternatif.append(mahasiswa.name)
                alternatifkriteria.append([mahasiswa.mk1, mahasiswa.mk2, mahasiswa.mk3, mahasiswa.mk4, mahasiswa.mk5])

                kriteria = ["C1", "C2", "C3", "C4", "C5"]
                costbenefit = ["benefit", "benefit", "benefit", "benefit", "benefit"]
                perbandingankriteria = [
                    [1, 1, 3, 1, 3],
                    [1, 1, 2, 1, 1],
                    [0.3333, 0.5, 1, 1, 2],
                    [1, 1, 1, 1, 3],
                    [0.3333, 1, 0.5, 0.3333, 1],
                ]

                totalkolom = []
                for i in range(len(kriteria)):
                    totalkolom.append(0)
                    for j in range(len(perbandingankriteria)):
                        totalkolom[i] = totalkolom[i] + perbandingankriteria[j][i]

                normalisasi = []
                for i in range(len(perbandingankriteria)):
                    normalisasi.append([])
                    for j in range(len(kriteria)):
                        normalisasi[i].append(0)
                        normalisasi[i][j] = perbandingankriteria[i][j] / totalkolom[j]

                bobotprioritas = []
                for i in range(len(normalisasi)):
                    bobotprioritas.append(sum(normalisasi[i]) / len(kriteria))

                pembagi = []
                for i in range(len(kriteria)):
                    pembagi.append(0)
                    for j in range(len(alternatif)):
                        pembagi[i] = pembagi[i] + (alternatifkriteria[j][i] * alternatifkriteria[j][i])
                    pembagi[i] = pembagi[i] ** (1 / 2.0)

                normalisasi_topsis = []
                for i in range(len(alternatif)):
                    normalisasi_topsis.append([])
                    for j in range(len(kriteria)):
                        normalisasi_topsis[i].append(0)
                        normalisasi_topsis[i][j] = alternatifkriteria[i][j] / pembagi[j]

                terbobot = []
                for i in range(len(alternatif)):
                    terbobot.append([])
                    for j in range(len(kriteria)):
                        terbobot[i].append(0)
                        terbobot[i][j] = normalisasi_topsis[i][j] * bobotprioritas[j]

                aplus = []
                for i in range(len(kriteria)):
                    aplus.append(0)
                    if costbenefit[i] == 'cost':
                        for j in range(len(alternatif)):
                            if j == 0:
                                aplus[i] = terbobot[j][i]
                            else:
                                if aplus[i] > terbobot[j][i]:
                                    aplus[i] = terbobot[j][i]
                    else:  # costbenefit[i] == 'benefit':
                        for j in range(len(alternatif)):
                            if j == 0:
                                aplus[i] = terbobot[j][i]
                            else:
                                if aplus[i] < terbobot[j][i]:
                                    aplus[i] = terbobot[j][i]

                amin = []
                for i in range(len(kriteria)):
                    amin.append(0)
                    if costbenefit[i] == 'cost':
                        for j in range(len(alternatif)):
                            if j == 0:
                                amin[i] = terbobot[j][i]
                            else:
                                if amin[i] < terbobot[j][i]:
                                    amin[i] = terbobot[j][i]
                    else:  # costbenefit[i] == 'benefit':
                        for j in range(len(alternatif)):
                            if j == 0:
                                amin[i] = terbobot[j][i]
                            else:
                                if amin[i] > terbobot[j][i]:
                                    amin[i] = terbobot[j][i]

                dplus = []
                for i in range(len(alternatif)):
                    dplus.append(0)
                    for j in range(len(kriteria)):
                        dplus[i] = dplus[i] + ((aplus[j] - terbobot[i][j]) * (aplus[j] - terbobot[i][j]))
                    dplus[i] = dplus[i] ** (1 / 2.0)

                dmin = []
                for i in range(len(alternatif)):
                    dmin.append(0)
                    for j in range(len(kriteria)):
                        dmin[i] = dmin[i] + ((terbobot[i][j] - amin[j]) * (terbobot[i][j] - amin[j]))
                    dmin[i] = dmin[i] ** (1 / 2.0)

                hasil = []
                for i in range(len(alternatif)):
                    hasil.append(0)
                    for j in range(len(kriteria)):
                        hasil[i] = dmin[i] / (dmin[i] + dplus[i])

                # Simpan nilai TOPSIS ke dalam record
                record.nilai_topsis = hasil