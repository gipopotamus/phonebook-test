import os
from typing import List
from phonebook_entry import PhonebookEntry


class Phonebook:
    def __init__(self, filename: str):
        """
        Создает объект Phonebook для управления записями в телефонном справочнике.
        :param filename: Имя файла для сохранения данных.
        """
        self.filename = filename
        self.entries: List[PhonebookEntry] = []
        self.load_entries()

    def load_entries(self) -> None:
        """
        Загружает записи из файла.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(';')
                    entry = PhonebookEntry(*data)
                    self.entries.append(entry)

    def save_entries(self) -> None:
        """
        Сохраняет записи в файл.
        """
        with open(self.filename, 'w') as file:
            for entry in self.entries:
                file.write(f"{entry.last_name};{entry.first_name};{entry.middle_name};{entry.organization};"
                           f"{entry.work_phone};{entry.personal_phone}\n")

    def add_entry(self, entry: PhonebookEntry) -> None:
        """
        Добавляет новую запись в справочник.
        :param entry: Объект PhonebookEntry с данными контакта.
        """
        self.entries.append(entry)
        self.save_entries()
        self.load_entries()

    def edit_entry(self, index: int, new_entry: PhonebookEntry) -> None
        """
           Редактирует запись в справочнике.
           :param index: Индекс записи для редактирования.
           :param new_entry: Объект PhonebookEntry с новыми данными контакта.
        """
        self.entries[index] = new_entry
        self.save_entries()

    def search_entries(self, query: str) -> List[PhonebookEntry]:
        """
            Выполняет поиск записей в справочнике по заданному запросу.

            :param query: Запрос для поиска.
            :return: Список записей, соответствующих запросу.
        """
        results = []
        for entry in self.entries:
            if (query.lower() in entry.last_name.lower() or
                query.lower() in entry.first_name.lower() or
                query.lower() in entry.middle_name.lower() or
                query.lower() in entry.organization.lower() or
                query in entry.work_phone or
                query in entry.personal_phone):
                results.append(entry)
        return results

    def display_entries(self) -> None:
        """
        Выводит на экран все записи в справочнике.
        """
        for idx, entry in enumerate(self.entries, start=1):
            print(f"{idx}. {entry.last_name} {entry.first_name} {entry.middle_name} ({entry.organization})")
            print(f"   Work Phone: {entry.work_phone}")
            print(f"   Personal Phone: {entry.personal_phone}")
            print()