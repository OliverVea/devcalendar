from devcalendar.models import Calendar
from devcalendar.storage import JsonCalendarProvider

def test__store_and_retrieve_calendar__calendar_stays_the_same(calendar: Calendar, json_provider: JsonCalendarProvider):
    json_provider.store_calendar(calendar)
    actual = json_provider.get_calendar()

    assert calendar == actual

def test__retrieve_real_calendar__does_not_fail():
    json_provider = JsonCalendarProvider('.data/calendar.json')
    calendar = json_provider.get_calendar()

    assert calendar