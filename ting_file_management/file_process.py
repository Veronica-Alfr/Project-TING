from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file: str, instance: Queue) -> list:
    if instance.contains_file(path_file):
        return
    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data)


def remove(instance: Queue) -> list:
    if not len(instance):
        return print("Não há elementos")

    data = instance.dequeue()
    print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position: int):
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
