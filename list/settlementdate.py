# -*- coding: utf-8 -*-
import datetime
import calendar


class PayoutSpecDays(object):
    __instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super(PayoutSpecDays, cls).__new__(cls, *args, **kwargs)
    #     return cls.__instance

    def __init__(self, spec_day=None, settlement_priority=None):
        self.__payout_spec_days = spec_day
        self.__payout_off = {}
        self.__payout_in_day_off = {}
        self.__payout_settlement_priority = settlement_priority
        self.__payout_time = {}

    @property
    def payout_spec_days(self):
        if self.__payout_spec_days is None:
            assert False, 'Necessary to load the data from the database (load_payout_spec_days method)'
        return self.__payout_spec_days

    @property
    def payout_settlement_priority(self):
        if self.__payout_settlement_priority is None:
            assert False, 'Necessary to load the data from the database (load_payout_settlement_priority method)'
        return self.__payout_settlement_priority

    def payout_off(self, pay_way):
        return self.__payout_off.setdefault(pay_way, [i['date'] for i in self.payout_spec_days if
                                                      i['pay_way'] == pay_way and not i['allow_payout']])

    def payout_in_day_off(self, pay_way):
        return self.__payout_in_day_off.setdefault(pay_way, [i['date'] for i in self.payout_spec_days if
                                                             i['pay_way'] == pay_way and i['allow_payout']])

    def payout_priorities(self, settlement_priority):
        return self.__payout_time.setdefault(
            settlement_priority,
            [i['settlement_hour'] for i in self.payout_settlement_priority if i['name'] == settlement_priority]
        )






def tofirstdayinisoweek(year, week):
    """

    :param year: Settlement year
    :param week: Settlement week
    :return: (datetime) First day of settlement week
    """
    ret = datetime.datetime.strptime('%04d-%02d-1' % (year, week), '%Y-%W-%w')
    if datetime.date(year, 1, 4).isoweekday() > 4:
        ret -= datetime.timedelta(days=7)
    return ret


# Need to change for recursive state
def set_payoutdate(startdate, settlement_period, settlement_type='daily', pay_way='bank_account', spec_day=None,
                   spec_settlement=None, settlement_priority='common'):
    """
    Function to set settlement date
    :param startdate: Transaction create date
    :type startdate date
    :type settlement_period: int
    :param settlement_type: Type of settlement, daily-month-week
    :type settlement_type: str
    :param pay_way: Payout settlement type, bank_account, bank_account_psbank
    :type pay_way: str
    :param spec_day:
    :type spec_day:
    :param spec_settlement:
    :type spec_settlement:
    :param settlement_priority Payout settlement priority, common, priority
    :type settlement_priority: str
    :return payoutdate
    :rtype: date
    """

    payout_spec_days = PayoutSpecDays(spec_day, spec_settlement)

    payout_off_days = payout_spec_days.payout_off(pay_way)
    payout_in_day_off = payout_spec_days.payout_in_day_off(pay_way)
    payout_time = payout_spec_days.payout_priorities(settlement_priority)[0]
    day_of_payout = startdate
    if settlement_type == 'daily':
        while settlement_period > 0:
            day_of_payout += datetime.timedelta(days=1)
            if day_of_payout.date() in payout_in_day_off or \
                    (day_of_payout.isoweekday() < 6 and day_of_payout.date() not in payout_off_days):
                settlement_period -= 1
        if day_of_payout.date() < datetime.datetime.today().date():
            today = datetime.datetime.today()
            return set_payoutdate(
                today, 1, settlement_type=settlement_type, pay_way=pay_way, spec_day=spec_day,
                spec_settlement=spec_settlement
            )
        date_today = datetime.datetime.today()
        next_day = date_today + datetime.timedelta(days=1)
        if settlement_priority == 'urgent' and (
                next_day.isoweekday() == 6 or next_day.date() in payout_off_days)\
                and next_day.date() not in payout_in_day_off and day_of_payout.time() < datetime.time(14, 00, 00):
            day_of_payout = date_today
        else:
            payout_time = payout_spec_days.payout_priorities('priority')[0]
    elif settlement_type == 'half_month':
        to_pay = False
        year = startdate.year
        month = startdate.month
        day_of_payout = datetime.datetime(year, month, 16, 1, 00, 00)
        if startdate.date() > datetime.date(year, month, 15):
            day_of_payout = datetime.datetime(year, month, calendar.mdays[startdate.month], 1, 00, 00) \
                            + datetime.timedelta(days=1)
        while to_pay is False:
            if day_of_payout.isoweekday() >= 6 or day_of_payout.date() in payout_off_days:
                day_of_payout += datetime.timedelta(days=1)
            else:
                to_pay = True
    elif settlement_type == 'normal_day':
        while settlement_period > 0:
            day_of_payout += datetime.timedelta(days=1)
            settlement_period -= 1
            if (day_of_payout.date() not in payout_in_day_off) and \
                    (day_of_payout.isoweekday() >= 6 or day_of_payout.date() in payout_off_days) and \
                    settlement_period == 0:
                settlement_period += 1
        if day_of_payout.date() < datetime.datetime.today().date():
            today = datetime.datetime.today()
            return set_payoutdate(
                today, 1, settlement_type=settlement_type, pay_way=pay_way, spec_day=spec_day,
                spec_settlement=spec_settlement
            )
    elif settlement_type == 'deposite_day':
        while settlement_period > 0:
            day_of_payout += datetime.timedelta(days=1)
            settlement_period -= 1
            if (day_of_payout.date() not in payout_in_day_off) and \
                    (day_of_payout.isoweekday() >= 6 or day_of_payout.date() in payout_off_days) and \
                    settlement_period == 0:
                settlement_period += 1
    elif settlement_type == 'month':
        settlement_period = 1
        month = day_of_payout.month - 1 + settlement_period
        year = day_of_payout.year + month / 12
        month = month % 12 + 1
        day = min(1, calendar.monthrange(year, month)[1])
        day_of_payout = datetime.date(year, month, day)
        day_of_payout = datetime.datetime.combine(day_of_payout, datetime.time(23, 51, 00))
        allow_payout = False
        while allow_payout is False:
            if (day_of_payout not in payout_in_day_off) and \
                    (day_of_payout.isoweekday() > 5 or day_of_payout in payout_off_days):
                day_of_payout += datetime.timedelta(days=1)
            else:
                allow_payout = True
    elif settlement_type == 'twice_week':
        current_weekday = day_of_payout.isoweekday()
        if 2 <= current_weekday < 5:
            day_of_payout = day_of_payout - datetime.timedelta(days=day_of_payout.weekday()) + \
                            datetime.timedelta(days=4)
        else:
            next_week = day_of_payout
            if current_weekday != 1:
                next_week = day_of_payout + datetime.timedelta(weeks=1)

            year = next_week.year
            day_of_payout = tofirstdayinisoweek(year, next_week.isocalendar()[1])
            if day_of_payout.isoweekday() == 1 or str(day_of_payout.date()) in payout_off_days:
                day_of_payout += datetime.timedelta(days=1)
        day_of_payout = datetime.datetime.combine(day_of_payout, datetime.time(23, 50, 00))

    elif settlement_type == 'every_friday':
        next_week = day_of_payout + datetime.timedelta(weeks=1)
        next_week = datetime.datetime.combine(next_week, datetime.time(1, 00, 00))
        year = next_week.year
        day_of_payout = tofirstdayinisoweek(year, next_week.isocalendar()[1])
        allow_payout = False

        while allow_payout is False:
            if day_of_payout.isoweekday() != 5 and day_of_payout.isoweekday() >= 6:
                day_of_payout -= datetime.timedelta(days=1)
                day_of_payout = datetime.datetime.combine(day_of_payout, datetime.time(1, 00, 00))
            elif day_of_payout.isoweekday() != 5 and day_of_payout.isoweekday() <= 4:
                day_of_payout += datetime.timedelta(days=1)
                day_of_payout = datetime.datetime.combine(day_of_payout, datetime.time(1, 00, 00))
            else:
                allow_payout = True
    elif settlement_type == 'week':
        next_week = day_of_payout + datetime.timedelta(weeks=1)
        next_week = datetime.datetime.combine(next_week, datetime.time(23, 49, 00))
        year = next_week.year
        day_of_payout = tofirstdayinisoweek(year, next_week.isocalendar()[1])
        allow_payout = False
        while allow_payout is False:
            if day_of_payout.isoweekday() == 1 or day_of_payout.isoweekday() > 5 \
                    or str(day_of_payout.date()) in payout_off_days:
                day_of_payout += datetime.timedelta(days=1)
                day_of_payout = datetime.datetime.combine(day_of_payout, datetime.time(23, 00, 00))
            else:
                allow_payout = True
    elif settlement_type == 'report':
        while settlement_period > 0:
            settlement_period -= 1
            if (day_of_payout.date() not in payout_in_day_off) and \
                    (day_of_payout.isoweekday() >= 6 or day_of_payout.date() in payout_off_days) and \
                    settlement_period == 0:
                settlement_period += 1
                day_of_payout += datetime.timedelta(days=1)
    elif settlement_type == 'report_liqpay':
        while settlement_period > 0:
            settlement_period -= 1
            day_of_payout += datetime.timedelta(days=1)
    else:
        while settlement_period > 0:
            day_of_payout += datetime.timedelta(days=1)
            if day_of_payout.isoweekday() < 6 and str(day_of_payout.date()) not in payout_off_days:
                settlement_period -= 1
        if day_of_payout.date() < datetime.datetime.today().date():
            today = datetime.datetime.today()
            return set_payoutdate(
                today, 1, settlement_type=settlement_type, pay_way=pay_way, spec_day=spec_day,
                spec_settlement=spec_settlement
            )

    return datetime.datetime.combine(day_of_payout, payout_time)





if __name__ == '__main__':
    spec_days = [{'date': datetime.date(2019, 1, 14), 'pay_way': u'cash', 'allow_payout': True, 'id': 97}, {'date': datetime.date(2019, 1, 15), 'pay_way': u'card', 'allow_payout': True, 'id': 98}, {'date': datetime.date(2019, 1, 17), 'pay_way': u'direct', 'allow_payout': True, 'id': 99}, {'date': datetime.date(2019, 1, 18), 'pay_way': u'cash', 'allow_payout': False, 'id': 100}, {'date': datetime.date(2019, 1, 19), 'pay_way': u'cash', 'allow_payout': True, 'id': 101}, {'date': datetime.date(2019, 1, 21), 'pay_way': u'cash', 'allow_payout': True, 'id': 102}, {'date': datetime.date(2016, 1, 4), 'pay_way': u'bank_account', 'allow_payout': False, 'id': 6}, {'date': datetime.date(2019, 1, 23), 'pay_way': u'direct', 'allow_payout': True, 'id': 103}, {'date': datetime.date(2016, 1, 8), 'pay_way': u'bank_account', 'allow_payout': False, 'id': 10}, {'date': datetime.date(2016, 3, 12), 'pay_way': u'bank_account', 'allow_payout': True, 'id': 11}, {'date': datetime.date(2016, 3, 8), 'pay_way': u'bank_account', 'allow_payout': False, 'id': 12}, {'date': datetime.date(2019, 1, 24), 'pay_way': u'cash', 'allow_payout': True, 'id': 104}, {'date': datetime.date(2019, 1, 25), 'pay_way': u'cash', 'allow_payout': True, 'id': 105}, {'date': datetime.date(2019, 1, 27), 'pay_way': u'direct', 'allow_payout': True, 'id': 106}, {'date': datetime.date(2018, 12, 31), 'pay_way': u'cash', 'allow_payout': False, 'id': 111}, {'date': datetime.date(2019, 2, 1), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 112}, {'date': datetime.date(2019, 2, 28), 'pay_way': u'direct', 'allow_payout': True, 'id': 113}, {'date': datetime.date(2019, 2, 14), 'pay_way': u'unknown', 'allow_payout': False, 'id': 114}, {'date': datetime.date(2019, 3, 1), 'pay_way': u'unknown', 'allow_payout': False, 'id': 115}, {'date': datetime.date(2018, 5, 9), 'pay_way': u'bank_account', 'allow_payout': False, 'id': 8}, {'date': datetime.date(2018, 9, 1), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 30}, {'date': datetime.date(2018, 6, 1), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 31}, {'date': datetime.date(2018, 9, 3), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 32}, {'date': datetime.date(2018, 9, 2), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 33}, {'date': datetime.date(2020, 10, 13), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 116}, {'date': datetime.date(2018, 8, 31), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 35}, {'date': datetime.date(2018, 8, 30), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 36}, {'date': datetime.date(2018, 8, 29), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 37}, {'date': datetime.date(2018, 8, 28), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 38}, {'date': datetime.date(2018, 8, 27), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 39}, {'date': datetime.date(2018, 8, 26), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 40}, {'date': datetime.date(2018, 8, 17), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 41}, {'date': datetime.date(2018, 8, 24), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 42}, {'date': datetime.date(2018, 8, 23), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 43}, {'date': datetime.date(2018, 8, 22), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 44}, {'date': datetime.date(2018, 8, 21), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 45}, {'date': datetime.date(2018, 8, 20), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 46}, {'date': datetime.date(2018, 8, 19), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 47}, {'date': datetime.date(2018, 8, 18), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 48}, {'date': datetime.date(2018, 8, 16), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 50}, {'date': datetime.date(2018, 8, 15), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 51}, {'date': datetime.date(2018, 8, 14), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 52}, {'date': datetime.date(2018, 8, 13), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 53}, {'date': datetime.date(2018, 8, 12), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 54}, {'date': datetime.date(2018, 8, 11), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 55}, {'date': datetime.date(2018, 8, 10), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 56}, {'date': datetime.date(2018, 8, 9), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 57}, {'date': datetime.date(2018, 8, 8), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 58}, {'date': datetime.date(2018, 9, 7), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 59}, {'date': datetime.date(2018, 7, 1), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 60}, {'date': datetime.date(2018, 7, 29), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 61}, {'date': datetime.date(2018, 7, 31), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 62}, {'date': datetime.date(2018, 7, 30), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 63}, {'date': datetime.date(2018, 7, 28), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 66}, {'date': datetime.date(2018, 7, 27), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 67}, {'date': datetime.date(2018, 7, 26), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 68}, {'date': datetime.date(2018, 7, 25), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 69}, {'date': datetime.date(2018, 7, 24), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 70}, {'date': datetime.date(2018, 7, 23), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 71}, {'date': datetime.date(2018, 7, 22), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 72}, {'date': datetime.date(2018, 7, 21), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 73}, {'date': datetime.date(2018, 7, 20), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 74}, {'date': datetime.date(2018, 7, 19), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 75}, {'date': datetime.date(2018, 7, 18), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 76}, {'date': datetime.date(2018, 7, 17), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 77}, {'date': datetime.date(2018, 7, 16), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 78}, {'date': datetime.date(2018, 7, 15), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 79}, {'date': datetime.date(2018, 7, 14), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 80}, {'date': datetime.date(2018, 7, 13), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 81}, {'date': datetime.date(2018, 7, 12), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 82}, {'date': datetime.date(2018, 7, 11), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 83}, {'date': datetime.date(2018, 7, 10), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 84}, {'date': datetime.date(2018, 7, 9), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 85}, {'date': datetime.date(2018, 7, 8), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 86}, {'date': datetime.date(2018, 7, 7), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 87}, {'date': datetime.date(2018, 7, 6), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 88}, {'date': datetime.date(2018, 7, 4), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 89}, {'date': datetime.date(2018, 7, 3), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 90}, {'date': datetime.date(2018, 7, 2), 'pay_way': u'qiwi', 'allow_payout': False, 'id': 91}, {'date': datetime.date(2018, 9, 12), 'pay_way': u'paytechnik', 'allow_payout': False, 'id': 94}, {'date': datetime.date(2018, 9, 26), 'pay_way': u'webmoney', 'allow_payout': True, 'id': 95}]
    settlement_priority = [{'settlement_hour': datetime.time(14, 0), 'name': u'common'}, {'settlement_hour': datetime.time(8, 0), 'name': u'priority'}, {'settlement_hour': datetime.time(14, 30), 'name': u'urgent'}]


    payoutdate = set_payoutdate(datetime.datetime.today(), 1                         , 'daily'                   , pay_way='bank_account',   spec_day=spec_days, spec_settlement=settlement_priority, settlement_priority='urgent')
    print("*HTML* payoutdate:  %s" % payoutdate)

    # payouttime = set_payoutdate(mr.trantimeend           , merchant.settlement_period, merchant.settlement_schema, pay_way=merchant.pay_way, spec_day=spec_days, spec_settlement=settlement_priority)

