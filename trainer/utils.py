import datetime
from datetime import timedelta
from booking.models import Booking
from trainer.models import TrainerSchedule, Service

# Заміна моделей джанго на прості класи для тестування
class TrainerSchedule:
    def __init__(self, trainer_id, datetime_start, datetime_end):
        self.trainer_id = trainer_id
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end

class Booking:
    def __init__(self, trainer_id, datetime_start, datetime_end):
        self.trainer_id = trainer_id
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end

class Service:
    def __init__(self, service_id, duration):
        self.service_id = service_id
        self.duration = duration

# Функція для визначення доступного часу для бронювання
def booking_time_discovery(trainer_id, service_id, date):
    # Отримуємо розклад тренера на задану дату
    trainer_schedule = [
        TrainerSchedule(trainer_id, datetime.datetime.combine(date, datetime.time(9, 0)), datetime.datetime.combine(date, datetime.time(12, 0))),
        TrainerSchedule(trainer_id, datetime.datetime.combine(date, datetime.time(13, 0)), datetime.datetime.combine(date, datetime.time(17, 0))),
    ]

    # Отримуємо існуючі бронювання тренера на задану дату
    trainer_bookings = [
        Booking(trainer_id, datetime.datetime.combine(date, datetime.time(10, 0)), datetime.datetime.combine(date, datetime.time(11, 0))),
        Booking(trainer_id, datetime.datetime.combine(date, datetime.time(15, 0)), datetime.datetime.combine(date, datetime.time(16, 0))),
    ]

    # Отримуємо інформацію про бажану послугу
    desired_service = Service(service_id, 60)  # Послуга тривалістю 60 хвилин
    search_window = desired_service.duration

    # Визначаємо початковий і кінцевий час для обчислень
    start_time = datetime.datetime.combine(date, datetime.time(0, 0))
    end_time = datetime.datetime.combine(date, datetime.time(23, 59))

    # Формуємо список всіх можливих часових слотів з кроком 15 хвилин
    all_time_slots = []
    current_time = start_time
    while current_time + timedelta(minutes=search_window) <= end_time:
        all_time_slots.append(current_time)
        current_time += timedelta(minutes=15)

    # Видаляємо зайняті слоти за розкладом тренера
    for schedule in trainer_schedule:
        schedule_start = schedule.datetime_start
        schedule_end = schedule.datetime_end
        all_time_slots = [slot for slot in all_time_slots if not (slot >= schedule_start and slot < schedule_end)]

    # Видаляємо заброньовані слоти
    for booking in trainer_bookings:
        booking_start = booking.datetime_start
        booking_end = booking.datetime_end
        all_time_slots = [slot for slot in all_time_slots if not (slot >= booking_start and slot < booking_end)]

    return all_time_slots

# Тестування функції
trainer_id = 1
service_id = 1
date = datetime.date(2024, 12, 25)  # Обрана дата

available_slots = booking_time_discovery(trainer_id, service_id, date)
print("Доступні часові слоти для бронювання:")
for slot in available_slots:
    print(slot.strftime("%Y-%m-%d %H:%M"))
