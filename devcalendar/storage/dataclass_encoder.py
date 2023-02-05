import dataclasses
import json
import datetime

class DataclassEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        elif isinstance(o, datetime.date):
            return str(o)
        return super().default(o)
