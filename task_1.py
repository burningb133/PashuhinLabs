numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

missing_element_index = numbers.index(None)

numbers[missing_element_index] = 0

avr_sum = sum(numbers) / len(numbers)

numbers[missing_element_index] = avr_sum

print("Измененный список:", numbers)
