from user.models import User,Activity

import random
import datetime


def fake_activity():
	begin = datetime.date(2018,4,11)
	end = datetime.date(2019,4,11)
	for i in range((end - begin).days+1):
		a = Activity()
		a.user = User.objects.get(id=1)
		a.activity_date =  str(begin + datetime.timedelta(days=i))
		a.activity_level = random.choice(['#ebedf0', '#c6e48b', '#7bc96f','#239a3b','#196127'])
		a.save()
		print(i)

if __name__ == '__main__':
	fake_activity()