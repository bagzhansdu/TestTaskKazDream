from django.db import models

class Lesson(models.Model):
	title = models.CharField(u'Название', max_length=255)
	class Meta:
		verbose_name=u'Урок'
		verbose_name_plural=u'Уроки'
	def __str__(self):
		return self.title

class Student(models.Model):
	first_name = models.CharField(u'Имя', max_length=255)
	last_name = models.CharField(u'Фамилия', max_length=255)
	lesson = models.ManyToManyField(Lesson)
	def __str__(self):
		return self.first_name



class Teacher(models.Model):
	first_name = models.CharField(u'Имя', max_length=255)
	last_name = models.CharField(u'Фамилия', max_length=255)
	lesson = models.OneToOneField(Lesson, on_delete = models.CASCADE, primary_key=True)

	def __str__(self):
		return self.first_name
