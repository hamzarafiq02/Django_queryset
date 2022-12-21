from django.shortcuts import render
from .models import Student
# Create your views here.


def home(request):
    student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=90)

    # student_data = Student.objects.exlude(marks=90)

    # student_data = Student.objects.order_by('id')

    # student_data = Student.objects.order_by('id').reverce()

    # student_data = Student.objects.value('name', 'city')

    # student_data = Student.objects.filter(id=1).delete()

    # student_data = Student.objects.create(id='1', name='test', roll_no='16', city='lahore', marks='40', pass_date='2022-12-15')

    # student_data = Student.objects.filter(id='2').update()

    return render(request, 'core/home.html', {'students': student_data})
