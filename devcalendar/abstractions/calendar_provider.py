from abc import ABC, abstractmethod

from devcalendar.models import Calendar
from devcalendar.validation import validate_calendar

class CalendarProvider(ABC):
    @abstractmethod
    def internal_get_calendar(self) -> Calendar:
        pass

    def get_calendar(self) -> Calendar:
        calendar = self.internal_get_calendar()
        validate_calendar(calendar)
        return calendar

    @abstractmethod
    def internal_store_calendar(self, calendar: Calendar):
        pass

    def store_calendar(self, calendar: Calendar):
        validate_calendar(calendar)
        self.internal_store_calendar(calendar)
