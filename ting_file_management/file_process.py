from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    if instance.contains_file(path_file):
        return
    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data)


def remove(instance: Queue):
    if not len(instance):
        return print("Não há elementos")

    data = instance.dequeue()
    print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
