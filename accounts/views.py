from django.shortcuts import render, redirect
from django.views import View
from  .models import Student, StudentLogin
from .forms import StudentLoginForm, StudentRegistrationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, random, time
from .utils import send_verification, generate_token

class LogInView(View):
    template = 'accounts/login.html'

    def get(self, request):
        form = StudentLoginForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = StudentLoginForm(request.POST)
        if form.is_valid():

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
                # status = send_verification(code, student.email)
                status = True
                if status:
                    request.session[f'{roll}'] = code
                    response = {
                        "success": True,
                        "msg": code
                    }
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


@csrf_exempt
def verify_email(request):
    data = json.loads(request.body)
    code_received = data.get('code')
    roll = data.get('roll')
    if not isinstance(roll, int):
        return JsonResponse({
            "success": False,
            "msg": "Verification code didn't match 1"
        })
    if not f'{roll}' in request.session.keys():
        return JsonResponse({
            "success": False,
            "msg": "hello"
        })

    code_sent = request.session.get(f'{roll}')

    if code_sent == code_received:
        token = generate_token()
        del request.session[f'{roll}']
        request.session[f'{roll}_token'] = token
        return JsonResponse({
            "success" : True,
            "token" : token
        })


    return JsonResponse({
            "success": False,
            "msg": "Verification code didn't match 2"
        })

@csrf_exempt
def register(request):
    data = json.loads(request.body)
    roll = data.get('roll')
    password = data.get('password')
    token_received = data.get('token')

    if roll is None or password is None or token_received is None:
        return JsonResponse({
            "success": False,
            "msg" : "Invalid request"
        })

    if password.find(' ') >= 0:
        return JsonResponse({
            "success": False,
            "msg": "Password must not contain spaces"
        })

    if len(password)<5 :
        return JsonResponse({
            "success": False,
            "msg": "Password must be at least 5 characters long"
        })

    if not isinstance(roll, int):
        return JsonResponse({
            "success": False,
            "msg": "Invalid roll number"
        })

    if not f'{roll}_token' in request.session.keys():
        return JsonResponse({
            "success": False,
            "msg" : "Unauthenticated request"
        })

    token_sent = request.session.get(f'{roll}_token')

    if not token_sent == token_received:
         return JsonResponse({
            "success": False,
            "msg" : "Unauthenticated request"
        })


    student = Student.objects.filter(roll=roll).first()

    if student:
        del request.session[f'{roll}_token']
        StudentLogin.objects.create(student=student,password=password)
        student.registered = True
        student.save()
        request.session['roll'] = roll

    return JsonResponse({
        "success": True,
        "student": student.roll
    })


def student_home(request):
    if 'roll' not in request.session:
        return render(request, 'accounts/login.html')

    roll = request.session.get('roll')
    student = Student.objects.filter(roll=roll).first()
    return render(request, 'accounts/student_home.html', {'student': student})

