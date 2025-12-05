from django.urls import path
from studentapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('teacherregister',views.teacherregister,name='teacherregister'),
    path('view_student',views.view_student,name='view_student'),
    path('view_teacher',views.view_teacher,name='view_teacher'),

    path('adminhome',views.adminhome,name='adminhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('logins',views.logins,name='logins'),
    path("delete/<int:id>",views.delete,name='delete'),
    path("approve_student/<int:id>",views.approve_student,name='approve_student'),

    path("approve_student/<int:id>",views.approve_student,name='approve_student'),
    path("edit_student_profile",views.edit_student_profile,name="edit_student_profile"),
    path("updatestudent/<int:id>",views.updatestudent,name="updatestudent"),
    path("updatestudent/<int:id>",views.updatestudent,name="updatestudent"),


    path('view_teacher_student',views.view_teacher_student,name='view_teacher_student'),
    path("tdelete/<int:id>",views.tdelete,name='tdelete'),
    path("editteacher",views.editteacher,name="editteacher"),
    path("updateteacher/<int:id>",views.updateteacher,name="updateteacher"),
    path("view_student_teacher",views.view_student_teacher,name="view_student_teacher"),
    path("logouts",views.logouts,name="logouts"),

    path("bootstrap",views.bootstrap,name="bootstrap"),
    path("",views.index,name="index"),




 










    
]