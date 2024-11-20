# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
      # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
    headers = rows[0]
    data = [
        {headers[i]: row[i] for i in range(len(headers))}
        for row in rows[1:]
    ]
    json_string = json.dumps(data, indent=4)
    ...  # TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json_file.write(json_string)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
