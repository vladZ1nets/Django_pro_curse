import unittest
import datetime
import utils

class TestSchedule(unittest.TestCase):
    maxDiff = None
    def test_schedule_no_bookings(self):
         schedule_start = datetime.datetime(2024, 12, 25, 9, 0)
         schedule_end = datetime.datetime(2024, 12, 25, 14, 0)
         trainer_bookings = []
         search_window = 60
         results = utils.booking_time_discovery(schedule_start, schedule_end, trainer_bookings, search_window)
         expected = [
             datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15), datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
             datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15), datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
             datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
             datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
             datetime.datetime(2024, 12, 25, 13, 0)
                     ]
         self.assertListEqual(expected, results)

         search_window = 30
         expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15),
            datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15),
            datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15),
            datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15),
            datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 13, 15),
            datetime.datetime(2024, 12, 25, 13, 30)
        ]
         results = utils.booking_time_discovery(schedule_start, schedule_end, trainer_bookings, search_window)
         self.assertListEqual(expected, results)



    def test_schedule_one_booking(self):
        start_date = datetime.datetime(2024, 12, 25, 9, 0)
        end_date = datetime.datetime(2024, 12, 25, 14, 0)
        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0),),
        ]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0),
            datetime.datetime(2024, 12, 25, 11, 0),
            datetime.datetime(2024, 12, 25, 11, 15),
            datetime.datetime(2024, 12, 25, 11, 30),
            datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0),
            datetime.datetime(2024, 12, 25, 12, 15),
            datetime.datetime(2024, 12, 25, 12, 30),
            datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0)
        ]
        self.assertListEqual(expected, results)

        # Тест для пошуку вікон 30 хвилин
        search_window = 30
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15),
            datetime.datetime(2024, 12, 25, 9, 30),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15),
            datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15),
            datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 13, 15),
            datetime.datetime(2024, 12, 25, 13, 30)
        ]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

        # Тест для різних бронювань
        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0),),
        ]
        expected = [
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15),
            datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15),
            datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15),
            datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0)
        ]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

        # Тест для додаткового бронювання в другій частині дня
        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 14, 0),),
        ]
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15),
            datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15),
            datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15),
            datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0)
        ]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

    def test_schedule_two_bookings(self):
        start_date = datetime.datetime(2024, 12, 25, 9, 0)
        end_date = datetime.datetime(2024, 12, 25, 14, 0)
        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0),),
            (datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 13, 0),),
        ]

        expected = [datetime.datetime(2024, 12, 25, 9, 0),
                    datetime.datetime(2024, 12, 25, 11, 0),
                    datetime.datetime(2024, 12, 25, 13, 0),]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

        # дві броні з початку
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0),),
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0),),
        ]

        expected = [
             datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
             datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
             datetime.datetime(2024, 12, 25, 13, 0)]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

        # дві броні з кінця
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 14, 0),),
            (datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 13, 0),),
        ]

        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15),
            datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15),
            datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0)
        ]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

        # з двох кінців
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0),),
            (datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 14, 0),),
        ]

        expected = [
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15),
            datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15),
            datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0)
        ]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)

        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 14, 0),),
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0),),
        ]
        results = utils.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertListEqual(expected, results)