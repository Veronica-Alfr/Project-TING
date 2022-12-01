import sys


def txt_importer(path_file):
    if path_file.endswith('.txt'):
        try:
            with open(path_file) as file:
                return file.read().split('\n')
        except FileNotFoundError:
            print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
    else:
        print('Formato inválido', file=sys.stderr)
