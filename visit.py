class Visit:
    def __init__(self, visit_id, date, start_time, end_time, enclosures):
        if len(enclosures) > 5:
            raise ValueError("A visit cannot include more than 5 enclosures.")
        self.visit_id = visit_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.enclosures = enclosures
