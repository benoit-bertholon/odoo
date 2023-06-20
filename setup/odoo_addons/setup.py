from os.path import join, dirname

import setuptools

setuptools.setup(
    classifier=['Private :: Do Not Upload'], # avoid accidental upload to pypi
    name='odoo-addons',
    version='15.0+20230202',
    setup_requires=['setuptools-odoo'],
    odoo_addons={
        'depends_override': {
            'test_performance': None,
        },
#        'external_dependencies_override': {
#            'python': {
#                'usb.core': 'pip',
#                'evdev': 'pip',
#                'ldap': 'pip',
#            },
#        },
#        'odoo_version_override': '%s.%s' % version_info[:2],
        'odoo_version_override': '15.0',
    },
)

