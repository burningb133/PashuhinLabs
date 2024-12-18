# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Weather:
    def __init__(self, temperature: float, wind_speed: float, humidity: float):
        """
        :param temperature: Температура в градусах цельсия
        :param wind_speed: Скорость ветра в м/с
        :param humidity: Влажность в %
        """
        if wind_speed < 0:
            raise ValueError("Скорость ветра не может быть отрицательной.")
        if not (0 <= humidity <= 100):
            raise ValueError("Влажность должна быть в диапазоне от 0 до 100.")

        self.temperature = temperature
        self.wind_speed = wind_speed
        self.humidity = humidity

    def feels_like_temperature(self) -> float:
        """
        Ощущаемая температура

        :return: Ощущаемая температура
        """
        ...

    def is_stormy(self) -> bool:
        """
        Определить, есть ли шторм

        :return: True, если скорость ветра больше 20 м/с, иначе False.
        """
        ...



class Mortgage:
    def __init__(self, cost: float, interest_rate: float, area: float):
        """
        :param cost: Стоимость жилья в рублях
        :param interest_rate: Процентная ставка
        :param area: Площадь жилья в квадратных метрах
        """
        if cost <= 0:
            raise ValueError("Стоимость жилья должна быть больше 0р.")
        if not (0 <= interest_rate <= 100):
            raise ValueError("Процентная ставка должна быть в диапазоне от 0 до 100.")
        if area <= 0:
            raise ValueError("Площадь жилья должна быть больше 0 квм.")

        self.cost = cost
        self.interest_rate = interest_rate
        self.area = area

    def monthly_payment(self, month: int) -> float:
        """
        Рассчитать ежемесячный платеж

        :param month: Срок ипотеки в месяцах
        :return: Ежемесячный платеж в рублях.

        Пример:
        >>> mortgage = Mortgage(5000000, 10, 60)
        >>> mortgage.monthly_payment(20)  # doctest: +ELLIPSIS
        ...
        """
        if month <= 0:
            raise ValueError("Срок ипотеки должен быть больше 0.")
        ...

    def cost_per_square_meter(self) -> float:
        """
        Рассчитать стоимость за квадратный метр.

        :return: Стоимость за 1 квм.

        Пример:
        >>> mortgage = Mortgage(5000000, 10, 60)
        >>> mortgage.cost_per_square_meter()  # doctest: +ELLIPSIS
        ...
        """
        ...


class MuseumAttendance:
    def __init__(self, month: str, visitors: int, revenue: float):
        """
        :param month: Название месяца (например, "Январь")
        :param visitors: Количество посетителей за месяц (должно быть >= 0)
        :param revenue: Доход за месяц в рублях (должен быть >= 0)
        """
        if visitors < 0:
            raise ValueError("Количество посетителей не может быть отрицательным.")
        if revenue < 0:
            raise ValueError("Доход не может быть отрицательным.")

        self.month = month
        self.visitors = visitors
        self.revenue = revenue

    def revenue_per_visitor(self) -> float:
        """
        Рассчитать доход на одного посетителя.

        :return: Доход на посетителя.

        Пример:
        >>> museum = MuseumAttendance("Январь", 1000, 500000)
        >>> museum.revenue_per_visitor()
        ...
        """
        ...

    def is_peak_month(self, threshold: int) -> bool:
        """
        Проверить, является ли месяц пиковым по количеству прибыли.

        :param threshold: Пороговое значение для пикового месяца.
        :return: True, если прибыль больше, чем threshold, иначе False.

        Пример:
        >>> museum = MuseumAttendance("Январь", 1000, 500000)
        >>> museum.is_peak_month(900)
        True
        """
        return self.revenue > threshold





if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
