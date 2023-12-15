# -*- coding: utf-8 -*-
{
    'name': "SIREMA",

    'summary': """
        Sistem Rekomendasi Magang
        Jurusan Teknologi Informasi
        Politeknik Negeri Malang""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kelompok 3 SIB 3E",
    'website': "https://www.sirema.com",
    'sequence': -100,
    'category': 'Education',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views_menuitem.xml',
        'views/views_all.xml',
        'views/template.xml',
        'reports/report.xml',
        'reports/mahasiswa_card.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
