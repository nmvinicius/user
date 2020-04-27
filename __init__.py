VERSION = (0, 0, 1, 'FINAL', 0)
__version_info__ = VERSION
__version__ = '.'.join(map(str, VERSION[:3])) + ('-{}{}'.format(
    VERSION[3], VERSION[4] or '') if VERSION[3] != 'final' else '')
__author__ = 'Vinicius Nunes Martins'
__license__ = 'MIT'

__title__ = 'MyUser'

