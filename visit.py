from enclosure import Enclosure


class Visit:
    def __init__(self, id: int, date: str, start_time: str, end_time: str, enclosures: list[Enclosure]):
        if len(enclosures) > 5:
            raise ValueError("A visit cannot include more than 5 enclosures.")

        self.visit_id = id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.enclosures = enclosures
