import datetime

from devcalendar.models import Calendar, CalendarEntry


def read_date_string(date_string: str) -> datetime.date:
    return datetime.date.fromisoformat(date_string)


class CalendarDecoder:
    @staticmethod
    def decode(data: dict) -> Calendar:
        data['start'] = read_date_string(data['start'])
        data['end'] = read_date_string(data['end'])

        for i in range(len(data['entries'])):
            data['entries'][i] = CalendarDecoder.decode_entry(
                data['entries'][i])

        return Calendar(**data)

    @staticmethod
    def decode_entry(data: dict) -> CalendarEntry:
        data['start'] = read_date_string(data['start'])
        data['end'] = read_date_string(data['end'])

        return CalendarEntry(**data)
