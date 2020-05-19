from django.shortcuts import render, redirect
from django.views import View
from  .models import Student
from .forms import StudentLoginForm, StudentRegistrationForm
from django.contrib import messages


class LogInView(View):
    template = 'accounts/login.html'

    def get(self, request):
        form = StudentLoginForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            print(f'{form.cleaned_data}')

            return redirect('home')

        return render(request, self.template, {'form': form})


class RegisterView(View):
    template = 'accounts/register.html'

    def get(self, request):
        form = StudentRegistrationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            roll = form.cleaned_data.get('roll')
            student = Student.objects.get(roll=roll)
            if student is None:
                print('Your roll number is not in database. Contact your department')
                messages.error(request, 'Your roll number is not in database. Contact your department')
                return render(request, self.template, {'form': form})

            else:
                if student.registered:
                    messages.info(request, 'You are already registered')
                    return render(request, self.template, {'form': form})
                else:
                    instance = form.save(commit=False)
                    student.registered = True
                    student.save()
                    instance.student = student
                    instance.save()
                    messages.success(request, 'Successfully registered')
                    return redirect('home')

        return render(request, self.template, {'form': form})
