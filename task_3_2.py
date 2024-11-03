# TODO Напишите функцию find_common_participants


def find_common_participants(first_group, second_group, separator=","):
    common_participants = []

    first_group_list = first_group.split(separator)
    second_group_list = second_group.split(separator)

    for participant in first_group_list:
        if participant in second_group_list:
            common_participants.append(participant)

    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group, "|")
print(common)