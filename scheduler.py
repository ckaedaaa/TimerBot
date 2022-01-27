from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import pytz



utc = pytz.utc

sch = AsyncIOScheduler(timezone = utc)
sch.start()

def scheduleDM(user, message, seconds_delay):
	run_date = datetime.datetime.now(tz = utc) + datetime.timedelta(seconds = seconds_delay)
	sch.add_job(user.send, 'date', run_date = run_date, args = [message])