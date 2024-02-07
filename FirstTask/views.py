from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def url(request):
    return render(request,'url.html')

def task(request):
    students = [
        {'name': 'Radha', 'roll_number': '123', 'grade': 'A'},
        {'name': 'Sumit', 'roll_number': '456', 'grade': 'B'},
        {'name': 'Raman', 'roll_number': '112', 'grade': 'A'},
        {'name': 'Rama', 'roll_number': '14', 'grade': 'C'},
        {'name': 'Sonal', 'roll_number': '234', 'grade': 'A'},
        {'name': 'Krishna', 'roll_number': '124', 'grade': 'B'},
    ]
    return render(request, 'task.html', {'students': students})