from user.models import User,Activity,Article

import random
import datetime

LEVEL = ['#ebedf0', '#c6e48b', '#7bc96f','#239a3b','#196127']

def fake_activity():
	begin = datetime.date(2019,4,9)
	end = datetime.datetime.today()
	for i in range(365):
		date = begin + datetime.timedelta(days=i)
		user = User.objects.get(id=1)

		try:
			a = Activity.objects.get(activity_date=date,user=user)
		except:
			a = Activity()
			a.user = user
			a.activity_date = date 

		# c = Article.objects.filter(user=a.user).filter(creat_time=a.activity_date).count()
		# if c > 3:
		# 	c = 4
		a.activity_level = random.choice(LEVEL)
		a.save()
		print(i)

if __name__ == '__main__':
	fake_activity()