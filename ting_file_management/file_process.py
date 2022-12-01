from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file: str, instance: Queue):
    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    if len(instance) > 0:
        for index in range(len(instance)):
            if instance.search(index)["nome_do_arquivo"] == path_file:
                return True
            return False

    instance.enqueue(data)

    return print(data, file=sys.stdout)


def remove(instance: Queue):
    if not len(instance):
        return print("Não há elementos")

    data = instance.dequeue()
    print(
        f"Arquivo {data['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout
        )


def file_metadata(instance: Queue, position: int):
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
