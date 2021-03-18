import datetime, time
from datetime import datetime
from datetime import timedelta


def get_delta_date_string(delta: int) -> str:
    """

    :param delta: 时间差
    :return: 距离当前delta天的时间
    """
    today_str = datetime.today().strftime('%Y%m%d')
    if delta < 0:
        delta = -delta
        return (datetime.strptime(today_str, '%Y%m%d') - \
                timedelta(days=delta)).strftime('%Y%m%d')
    else:
        return (datetime.strptime(today_str, '%Y%m%d') + \
                timedelta(days=delta)).strftime('%Y%m%d')


def event_time(event: str) -> str:
    """

    :param event: 事件
    :return: 事件对应时间
    """
    event_outtime = "{} start data:{}".format(event, time.strftime('%F %H:%M:%S'))
    return event_outtime
