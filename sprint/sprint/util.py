def total_seconds(timedelta):
	return (timedelta.microseconds + (timedelta.seconds + timedelta.days * 24 * 3600) * 10 ** 6) / 10 ** 6
