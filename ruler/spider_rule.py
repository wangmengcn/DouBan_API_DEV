#-*- coding: UTF-8 -*- 

def get_rule(category):
	sleep=0
	count=0
	tag=''
	
	if category in ['movie','book','music']:
		if category == 'movie':
			sleep=2
			count=20
			tag='subjects'
		elif category =='book':
			sleep=5
			count=100
			tag='subjects'
		else :
			sleep=5
			count=100
			tag='musics'
	else:
		print "没有此类别的查询"
	rules=[sleep,count,tag]
	return rules