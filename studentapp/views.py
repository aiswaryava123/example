from django.shortcuts import render,HttpResponse,redirect
from .models import Student,User,Teacher
from django.contrib.auth import authenticate,logout,login



# Create your views here.
def home(request):
    return render(request,"home.html")

def studentregister(request):
    if request.method=="POST":
        FIRSTNAME=request.POST['firstname']
        LASTNAME=request.POST['lastname']
        EMAIL=request.POST['email']
        ADDRESS=request.POST['address']
        PHONENUMBER=request.POST['phonenumber']
        GUARDIAN=request.POST['guardian']
        USERNAME=request.POST['username']
        PASSWORD=request.POST['password']
        new_user=User.objects.create_user(first_name=FIRSTNAME,last_name=LASTNAME,
        email=EMAIL,username=USERNAME,password=PASSWORD,address=ADDRESS,phone_number=PHONENUMBER,usertype='student',is_active=False)
        new_user.save()
        x=Student.objects.create(student_id=new_user,guardian=GUARDIAN)
        x.save()
        return redirect("logins")
        # return HttpResponse("registration successfull")
    else:
     return render(request,'studentregister.html')
    
    
def teacherregister(request):
    if request.method=="POST":
        FIRSTNAME=request.POST['firstname']
        LASTNAME=request.POST['lastname']
        EMAIL=request.POST['email']
        ADDRESS=request.POST['address']
        PHONENUMBER=request.POST['phonenumber']
        SALARY=request.POST['salary']
        EXPERIENCE=request.POST['Experience']
        USERNAME=request.POST['username']
        PASSWORD=request.POST['password']
        new_user=User.objects.create_user(first_name=FIRSTNAME,last_name=LASTNAME,
        email=EMAIL,username=USERNAME,password=PASSWORD,address=ADDRESS,phone_number=PHONENUMBER,usertype='teacher',is_active=True,is_staff=True)
        new_user.save()
        cust=Teacher.objects.create(teacher_id=new_user,salary=SALARY,experience=EXPERIENCE)
        cust.save()

        return HttpResponse("registration successfull")
    else:
     return render(request,'teacherregister.html')
    
def logins(request):
   if request.method=="POST":
      USERNAME=request.POST['username']
      PASSWORD=request.POST['password']
      userpass=authenticate(request,username=USERNAME,password=PASSWORD)
      if userpass is not None and userpass.is_superuser==1:
         return redirect('adminhome')
      elif userpass is not None and userpass.is_staff==1:
         login(request,userpass)
         request.session['teach_id']=userpass.id
         return redirect("teacherhome")
      elif userpass is not None and userpass.is_active==1:
         login(request,userpass)
         request.session['stud_id']=userpass.id
         return redirect("studenthome")
      else:
         return HttpResponse("invalid login")
   else:
      return render(request,'logins.html')
def adminhome(request):
   return render(request,'admin.html')     

      
def teacherhome(request):
    return render(request,'teacherhome.html')

def studenthome(request):
    return render(request,'studenthome.html')

def adminhome(request):
    return render(request,"admin.html")


def view_student(request):
    y=Student.objects.all()
    return render(request,"viewstudent.html",{"data":y})

def view_teacher(request):
    y=Teacher.objects.all()
    return render(request,"viewteacher.html",{"data":y})

def delete(request,id):
    stud=Student.objects.get(id=id)
    user_id=stud.student_id.id
    stud.delete()
    user=User.objects.get(id=user_id)
    user.delete()
    return redirect(view_student)

def approve_student(request,id):
     stud=Student.objects.select_related('student_id').get(id=id)
     stud.student_id.is_active=True
     stud.student_id.save()
     return redirect('view_student')



def edit_student_profile(request):
    stud=request.session.get('stud_id')

    student=Student.objects.get(student_id_id=stud)
    user=User.objects.get(id=stud)


    return render(request,"edit_student_profile.html",{"view": student,"data":user})


def updatestudent(request,id):


    if request.method == "POST":
         stud=Student.objects.get(id=id)
         uid=stud.student_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         stud.guardian=request.POST["guardian"] 
         user.save()
         stud.save()

         return redirect(view_student)  #function name

def logouts(request):
    if "stud_id" in request.session:
        del request.session['stud_id']
    else:
        if "teach_id" in request.session:
            del request.session['teach_id']
            logout(request)
    return redirect("logins")

def view_teacher_student(request):
    y=Teacher.objects.all()
    return render(request,"view_teacher_student.html",{"data":y})

def tdelete(request,id):
    teach=Teacher.objects.get(id=id)
    user_id=teach.teacher_id.id
    teach.delete()
    User.objects.get(id=user_id).delete()
    return redirect("view_teacher")

def editteacher(request):
   teach=request.session.get('teach_id')

   teacher=Teacher.objects.get(teacher_id_id=teach)
   user=User.objects.get(id=teach)


   return render(request,"editteacher.html",{"view": teacher,"data":user})

def updateteacher(request,id):
    if request.method == "POST":
         teach=Teacher.objects.get(id=id)
         uid=teach.teacher_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         teach.salary=request.POST["salary"] 
         teach.experience=request.POST["experience"] 

         user.save()
         teach.save()

         return redirect(view_teacher) 

def view_student_teacher(request):
     x=Student.objects.all()
     return render(request,"View_student_teacher.html",{"view":x})

def logouts(request):
    if "stud_id" in request.session:
        del request.session['stud_id']
    else:
        if "teach_id" in request.session:
            del request.session['teach_id']
            logout(request)
    return redirect("logins")


def bootstrap(request):
    return render(request,"index.html")


def index(request):
    return render(request,"index.html")


