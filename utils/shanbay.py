import requests
import re
import json
import pickle
import time
	

# s = requests.Session()

# def login(username ,password):
# 	'''下载 word_type 的单词数据，存放到对应文件里'''
# 	data = {"username":username,"password": password}
# 	# 登陆shanbay网
# 	response = s.put('https://www.shanbay.com/api/v1/account/login/web/',data=data,verify=False)
# 	print(response.status_code)
# 	if response.status_code == 200:
# 		return True
# 	else:
# 		return False

def download_words(username ,password,word_type = 'today'):
	'''下载 word_type 的单词数据，存放到对应文件里'''
	data = {"username":username,"password": password}

	# 登陆shanbay网
	s = requests.Session()
	response = s.put('https://www.shanbay.com/api/v1/account/login/web/',data=data,verify=False)

	response = s.get('https://www.shanbay.com/api/v1/bdc/library/%s/?page=1' % word_type,verify=False)

	response_dict = json.loads(response.text)
	ipp = response_dict['data']['ipp']
	total = response_dict['data']['total']

	total_page = total//ipp
	#print(total_page)

	
	objects = []
	for page in range(1,total_page+1):
		print('[LOG...PAGE:%d / %d]'%(page,total_page))
		response = s.get('https://www.shanbay.com/api/v1/bdc/library/%s/?page=%s'% (word_type , page),verify=False)
		# print('https://www.shanbay.com/api/v1/bdc/library/master/?page=%s'% page)
		response_dict = json.loads(response.text)
		objects += response_dict['data']['objects']

	with open('%s.data'% word_type,'wb') as f:	
		pickle.dump(objects,f)


def bdc(number = 7,islast=False):
	'''作弊背单词'''
	username = "SingleSinger"
	password = r"lxr100%lovexs"
	data = {"username":username,"password": password}

	# 登陆shanbay网
	s = requests.Session()
	response = s.put('https://www.shanbay.com/api/v1/account/login/web/',data=data,verify=False)
	
	stamp = ''.join(str(time.time()).split('.'))[0:13]
	url = 'https://www.shanbay.com/api/v1/bdc/review/?len=%d&update_type=fresh&_=%s' % (number,stamp)
	rep = s.get(url,verify=False)
	js = json.loads(rep.text)
	ds = js['data']['reviews']

	contents = [d['content'] for d in ds]
	content_ids = [d['content_id'] for d in ds]
	ids = [d['id'] for d in ds]

	print(contents)

	content_id_str = ','.join(str(content_id) for content_id in content_ids)
	# print(content_id_str)
	# 获取单词内容
	stamp = ''.join(str(time.time()).split('.'))[0:13]
	url2='https://www.shanbay.com/api/v1/bdc/vocabulary/?version=2&ids=%s&_=%s' % (content_id_str,stamp)
	rep = s.get(url2,verify=False)
	js = json.loads(rep.text)
	ds = js['data']

	# # 获取例子内容
	# url3 = 'https://www.shanbay.com/api/v1/bdc/example/?ids=3845698,3845701,3834100,3834103,3838225,3838222,3858235,3858238,3861622,24352,24353,24354,71209,71210,71211,234506,37452,37453,37454,230011,53766,53767,47172,47173,47174,3854368,3854371,33032,245375,33031,40688,40689,40690&_=1540909984048'
	# rep = s.get(url3,verify=False)
	# 七个一组复习 
	url4='https://www.shanbay.com/api/v1/bdc/review/' #put	
	# 提交复习结果
	if not islast:
		ids_str = ','.join(str(_) for _ in ids)
		data = {"ids":ids_str,
				"results":"2,2,2,2,2,2,2",
				"seconds":"0,3,1,2,2,2,2"}

		rep = s.put(url4,data=data,verify=False)
	else:
		rep = s.get(url4,verify=False)
	print(rep.text)

def bdc_all(number = 300):
	'''背完今天所有单词'''
	i = number//7+1
	while(i>0):
		if i==1:
			bdc(islast=True)
		else:
			bdc()
		time.sleep(1)
		i-=1
	return True
	
def get_quote(date = '2018-10-30'):
	url = 'https://rest.shanbay.com/api/v2/quote/quotes/%s/'% date
	response = requests.get(url,verify=False)
	quotes_dict = json.loads(response.text)
	return( quotes_dict['data']['content'],quotes_dict['data']['translation'],quotes_dict['data']['author'])

def check_in():
	'''签到Failed'''
	username = "SingleSinger"
	password = r"lxr100%lovexs"
	data = {"username":username,"password": password}

	# 登陆shanbay网
	s = requests.Session()
	response = s.put('https://www.shanbay.com/api/v1/account/login/web/',data=data,verify=False)
	
	note = {'note':'TEST'}
	url = 'https://apiv3.shanbay.com/uc/checkin/log'
	rep = s.options(url,verify=False)
	rep = s.put(url,data = note,verify=False)
	print(rep)

if __name__ == '__main__':

	# from idate import daterange

	# with open("quotes2017.txt",'a',encoding='utf8') as f: 
	# 	for date in daterange('2017-02-01','2017-12-31'):
	# 		d = get_quote(date)
	# 		f.write(d[0]+'\t')
	# 		f.write(d[1]+'\t')
	# 		f.write(d[2]+'\n')
	
	import datetime
	print(datetime.datetime.today().strftime('%Y-%m-%d'))