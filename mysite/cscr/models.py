# coding:utf-8
from django.db import models
from django.utils import timezone
import urllib

# Create your models here.

class Bulletin(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	img_url=models.CharField(max_length=225,blank=True)
	photo280_400=models.ImageField(upload_to = 'static/cscr/img/',blank=True)
	photo280_400_2=models.ImageField(upload_to = 'static/cscr/img/',blank=True)
	photo450_300=models.ImageField(upload_to = 'static/cscr/img/',blank=True)
	video_url=models.CharField(max_length=500,blank=True)
	video_url=models.CharField(max_length=500,blank=True)
	'''置頂'''

	top_choices=(
			('t', u'置頂'),
			('g', u'一般')
		)

	class Meta:
		# 定义显示的名字
		verbose_name = '最新消息'
		verbose_name_plural = '最新消息'

	top = models.CharField(verbose_name=u'置頂', max_length=1, choices=top_choices, default='g')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def picture_upload(self):
		"""Store image locally if we have a URL"""
		if self.img_url and not self.photo280_400:
			result = urllib.urlretrieve(self.img_url)
			self.photo.save(os.path.basename(self.img_url),File(open(result[0])))
			self.save()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return 'Proposal for: %s' % self.title

class Project(models.Model):
	project_name = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	url=models.CharField(max_length=300,blank=False)
	img_url=models.CharField(max_length=225,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def picture_upload(self):
		"""Store image locally if we have a URL"""
		if self.img_url and not self.img_photo:
			result = urllib.urlretrieve(self.img_url)
			self.photo.save(os.path.basename(self.img_url),File(open(result[0])))
			self.save()

	def __str__(self):
		return self.project_name

	def __unicode__(self):
		return 'Proposal for: %s' % self.project_name

class Achievement(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	img_url=models.CharField(max_length=225,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)
	video_url=models.CharField(max_length=500,blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def picture_upload(self):
		"""Store image locally if we have a URL"""
		if self.img_url and not self.img_photo:
			result = urllib.urlretrieve(self.img_url)
			self.photo.save(os.path.basename(self.img_url),File(open(result[0])))
			self.save()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return 'Proposal for: %s' % self.title

class Publication(models.Model):
	title=models.TextField(max_length=200,blank=False)
	published_date=models.CharField(max_length=20,blank=True)
	book_type=models.CharField(max_length=500,blank=True)
	author=models.CharField(max_length=100,blank=True)
	img_url=models.CharField(max_length=225,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def picture_upload(self):
		"""Store image locally if we have a URL"""
		if self.img_url and not self.img_photo:
			result = urllib.urlretrieve(self.img_url)
			self.photo.save(os.path.basename(self.img_url),File(open(result[0])))
			self.save()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return 'Proposal for: %s' % self.title

class Journal(models.Model):
	title=models.CharField(max_length=200,blank=True)
	published_date=models.CharField(max_length=20,blank=True)
	book_type=models.CharField(max_length=500,blank=True)
	author=models.CharField(max_length=100,blank=True)
	img_url=models.CharField(max_length=225,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def picture_upload(self):
		"""Store image locally if we have a URL"""
		if self.img_url and not self.img_photo:
			result = urllib.urlretrieve(self.img_url)
			self.photo.save(os.path.basename(self.img_url),File(open(result[0])))
			self.save()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return 'Proposal for: %s' % self.title

class Database(models.Model):
	name = models.CharField(max_length=200)
	text = models.TextField()
	url=models.CharField(max_length=300,blank=False)
	img_url=models.CharField(max_length=225,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def picture_upload(self):
		"""Store image locally if we have a URL"""
		if self.img_url and not self.img_photo:
			result = urllib.urlretrieve(self.img_url)
			self.photo.save(os.path.basename(self.img_url),File(open(result[0])))
			self.save()

	def __str__(self):
		return self.name

	def __unicode__(self):
		return 'Proposal for: %s' % self.name

class People(models.Model):
	job_title=models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	name_url=models.CharField(max_length=500,blank=True)
	specialty=models.CharField(max_length=100,blank=True)
	text=models.TextField(blank=True)
	publications_list=models.CharField(max_length=500,blank=True)
	publications_url=models.CharField(max_length=500,blank=True)
	mail=models.CharField(max_length=300,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return 'Proposal for: %s' % self.name

class People_Researcher(models.Model):
	job_title=models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	name_url=models.CharField(max_length=500,blank=True)
	specialty=models.CharField(max_length=100,blank=True)
	text=models.TextField(blank=True)
	publications_list=models.CharField(max_length=500,blank=True)
	publications_url=models.CharField(max_length=500,blank=True)
	mail=models.CharField(max_length=300,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return 'Proposal for: %s' % self.name

class People_Administrator(models.Model):
	job_title=models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	name_url=models.CharField(max_length=500,blank=True)
	specialty=models.CharField(max_length=100,blank=True)
	text=models.TextField(blank=True)
	publications_list=models.CharField(max_length=500,blank=True)
	publications_url=models.CharField(max_length=500,blank=True)
	mail=models.CharField(max_length=300,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return 'Proposal for: %s' % self.name

class People_Committee(models.Model):
	job_title=models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	name_url=models.CharField(max_length=500,blank=True)
	specialty=models.CharField(max_length=100,blank=True)
	text=models.TextField(blank=True)
	publications_list=models.CharField(max_length=500,blank=True)
	publications_url=models.CharField(max_length=500,blank=True)
	mail=models.CharField(max_length=300,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return 'Proposal for: %s' % self.name

class People_Scholar(models.Model):
	job_title=models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	name_url=models.CharField(max_length=500,blank=True)
	specialty=models.CharField(max_length=100,blank=True)
	text=models.TextField(blank=True)
	publications_list=models.CharField(max_length=500,blank=True)
	publications_url=models.CharField(max_length=500,blank=True)
	mail=models.CharField(max_length=300,blank=True)
	img_photo=models.ImageField(upload_to = 'static/cscr/img/',blank=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return 'Proposal for: %s' % self.name






