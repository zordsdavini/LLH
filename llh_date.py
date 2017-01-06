"""
Init: 2017-01-06 11:10 by Zordsdavini
"""

from datetime import date

class LLHDate(object):

    """Docstring for LLHDate. """

    gdate = None
    gdate_ordered = None
    start_data = date(1987, 12, 22)
    start_data_ordered = start_data.toordinal()

    def __init__(self, gdate=None):
        """TODO: to be defined1. """
        if not gdate:
            gdate = date.today()
        self.gdate = gdate
        self.gdate_ordered = gdate.toordinal()

    def get(self):
        """Gautė pargoldīta data
        :returns: string

        """
        diff = self.gdate_ordered - self.start_data_ordered
        i = 0
        while diff > 0:
            minus = 354
            if self._is_ousis(i):
                minus = 384

            if diff < minus:
                # self._count_day(diff)
                break

            diff -= minus
            i += 1

        return i

    def _is_ousis(self, year_number):
        """Sotikrintė a metā tor ůsė mienesi

        :year_number: int
        :returns: bool

        """
        tskl = [
            (2, 7, False, 0),    # 3/4
            (6, 7, False, 0),      # 3/4 arba 3/4-4/3
            (1, 8, True, 345),      # kas 8, 345 nȧsisded
        ]
        sk = [0, 0, 0]

        ousis = False
        for k, t in enumerate(tskl):
            if year_number % int(t[1]) == int(t[0]) or int(t[0]) == int(t[1]) and year_number % int(t[0]) == 0:
                # Sotikrintė a nȧrēk nȧpridietė
                # if (t[2]):
                #     sk[k] += 1
                #     if sk[k] >= t[3]:
                #         sk[k] = 0
                #         break

                ousis = True

        return ousis


a = LLHDate()
print('30.%i' % a.get())
