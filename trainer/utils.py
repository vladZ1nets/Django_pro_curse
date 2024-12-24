import datetime
from datetime import timedelta
from booking.models import Booking
from trainer.models import TrainerSchedule, Service

def booking_time_discovery(trainer_id, service_id, date):
    trainer_schedule = TrainerSchedule.objects.filter(trainer_id=trainer_id, datetime_start__date=date)
    trainer_bookings = Booking.objects.filter(trainer_id=trainer_id, datetime_start__date=date)
    desired_service = Service.objects.get(pk=service_id)
    search_window = desired_service.duration

    start_time = datetime.datetime.combine(date, datetime.time(0, 0))
    end_time = datetime.datetime.combine(date, datetime.time(23, 59))

    all_time_slots = []
    current_time = start_time
    while current_time + timedelta(minutes=search_window) <= end_time:
        all_time_slots.append(current_time)
        current_time += timedelta(minutes=15)

    for schedule in trainer_schedule:
        schedule_start = schedule.datetime_start
        schedule_end = schedule.datetime_end
        all_time_slots = [slot for slot in all_time_slots if not (slot >= schedule_start and slot < schedule_end)]

    for booking in trainer_bookings:
        booking_start = booking.datetime_start
        booking_end = booking.datetime_end
        all_time_slots = [slot for slot in all_time_slots if not (slot >= booking_start and slot < booking_end)]

    return all_time_slots
