def get_spent_calories(training_type: str, mean_speed: float, weight: float, duration: float):
    if training_type == "RUN":
        return (18 * mean_speed + 1.79) * weight / 1000 * duration * 60
    ...  # Все остальные формулы не описаны, вам их нужно будет реализовать в дочерних классах


def get_message(training_type: str, duration: float, distance, speed, calories) -> str:
    """Формирование строки информационного сообщения.

    training_type - имя класса тренировки
    duration - длительность тренировки в часах
    distance - дистанция в километрах, которую преодолел пользователь за время тренировки
    speed - средняя скорость в км/ч, с которой двигался пользователь
    calories - количество килокалорий, которое израсходовал пользователь за время тренировки
    """
    return (f'Тип тренировки: {training_type}; '
            f'Длительность: {duration:.3f} ч.; '
            f'Дистанция: {distance:.3f} км; '
            f'Ср. скорость: {speed:.3f} км/ч; '
            f'Потрачено ккал: {calories:.3f}.')


class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self, action: int, duration: float, weight: float) -> None:
        """Конструктор базового класса тренировки.

        action - количество совершённых действий
        duration - длительность тренировки в часах
        weight - вес спортсмена в килограммах
        """
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч"""
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
