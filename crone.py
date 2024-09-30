from crontab import CronTab


# каждые 3 часа, каждый день в 15:15, каждое вс в полночь
my_cron = CronTab(user='user')
job1 = my_cron.new(command='python decorate.py')
job1.hour.every(3)

job2 = my_cron.new(command='python decorate.py')
job2.hour.on(15.15)

job3 = my_cron.new(command='python decorate.py')
job3.hour.on(0)
job3.dow.on('SUN')
my_cron.write()