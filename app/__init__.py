from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__,static_folder='static', template_folder='templates')

import users, cmdb, monitor, cost, statistics, code_release


sched = BackgroundScheduler()
sched.add_job(monitor.mongoback_info_auto_refresh_getip, 'cron', hour='10', minute='10')
sched.add_job(monitor.backupServer_monitor_cron, 'cron', hour='10', minute='20')
sched.start()