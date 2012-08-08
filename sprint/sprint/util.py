import datetime
from django.utils.timezone import utc, make_aware

def total_seconds(timedelta):
	return (timedelta.microseconds + (timedelta.seconds + timedelta.days * 24 * 3600) * 10 ** 6) / 10 ** 6

def now():
    return datetime.datetime.utcnow().replace(tzinfo=utc)
