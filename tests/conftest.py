import tempfile

from datetime import date, timedelta
from pathlib import Path

import pytest

from devcalendar.models import Calendar, CalendarEntry
from devcalendar.storage import JsonCalendarProvider

@pytest.fixture
def calendar():
    start = date(2022, 11, 17)
    end = date(2022, 12, 3)
    entries = [
        CalendarEntry('entry 1', start, []),
        CalendarEntry('entry 2', end, ['tag A']),
        CalendarEntry('entry 3', start, ['tag B'], end),
        CalendarEntry('entry 4', start + timedelta(days=1), ['tag A', 'tag B']),
    ]

    return Calendar(start, end, entries)


@pytest.fixture
def json_provider():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / 'calendar.json'
        provider = JsonCalendarProvider(file_path)
        yield provider
