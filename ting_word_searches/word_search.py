from ting_file_management.queue import Queue


def exist_content(i, line, content):
    if content:
        return {"linha": i + 1, "conteudo": line}
    return {"linha": i + 1}


def exists_word(word: str, instance: Queue, content: bool = False) -> list:
    data = []

    for index in range(len(instance)):
        file = instance.search(index)

        occurrences = [
            exist_content(i, line, content)
            for i, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]

        item = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": occurrences,
        }

        if occurrences:
            data.append(item)

    return data


def search_by_word(word: str, instance: Queue) -> list:
    return exists_word(word, instance, True)
