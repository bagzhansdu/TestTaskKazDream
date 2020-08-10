from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson, Student, Teacher


def home(request):
	lessons = Lesson.objects.all()
	context = {
	'lessons':lessons
	}
	return render(request, 'base/index.html', context)
def more(request, **kwargs):
	lesson = Lesson.objects.filter(id=kwargs.pop('lesson_pk')).get()
	students = lesson.student_set.all()
	context = {
	'lesson':lesson,
	'students':students
	}

	return render(request, 'base/lesson_more.html', context)
