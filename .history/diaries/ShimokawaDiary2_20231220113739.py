from diaries.AbstractDiary import AbstractDiary


class Diaryshimokawa(AbstractDiary):

    def get_date(self):
        return "2021-12-01"

    def get_summary(self):
        return "線形代数わかんない"

    def get_author(self):
        return "Sample"
