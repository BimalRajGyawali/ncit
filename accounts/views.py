from django.shortcuts import render, redirect
from django.views import View
from  .models import Student
from .forms import StudentLoginForm, StudentRegistrationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random
from .utils import send_verification

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


@csrf_exempt
def collect_roll(request):
    roll = json.loads(request.body).get("roll")
    if isinstance(roll, int):
        student = Student.objects.filter(roll=roll).first()
        if student is None:
            response = {
                "success": False,
                "msg": f"Roll {roll} not found"
            }
        else:
            if student.registered:
                response = {
                    "success": False,
                    "msg": f"Roll {roll} is already registered"
                }
            elif student.email is None:
                response = {
                    "success": False,
                    "msg": f"No email is registered for {roll}. Contact your department"
                }

            else:
                code = random.randint(100000, 999999)
                status = send_verification(code, 'gyawalijj5@gmail.com')
                if status:
                    request.session[roll] = code
                    response = {
                        "success": True,
                        "msg": code
                    }
                    print(request.session.get(roll))
                else:
                    response = {
                        "success": False,
                        "msg": "Error in sending mail"
                    }


        return JsonResponse(response)

    return JsonResponse({
        "success": False,
        "msg": f"{roll} is invalid roll"
    })
