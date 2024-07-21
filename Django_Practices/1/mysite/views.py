from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render


class Person(object):
    def __init__(self, name, gretting) -> None:
        self.name=name 
        self.gretting=gretting

def Gretting(request): #First view 
    return HttpResponse('<h1>Hello world</h1>')

def CurrentDate(request):#Second view
    GetTime = datetime.now()
    ans = f'''
            <h2> Current date:{GetTime}</h2>
            '''
    return HttpResponse(ans)

def GetMyAgeAt(request,age,year):
    currentAge = age
    period = year-2024
    FutureAge = currentAge+period
    ans = f'''
            <p>In the year {year} you'll have {FutureAge}</p>
            '''
    return HttpResponse(ans)

def Gretting_Pt2(request):
    My_Html = open('C:/Users/Paul Manriquez/Desktop/Django/Django_Practices/1/mysite/templates/greting.html')

    Read_Html = Template(My_Html.read())#Get the document stored in the variable
    My_Html.close()

    now = datetime.now()
    Person1 = Person('Paul','Welcome!')
    ctx = Context({
        'name': Person1.name,
        'message': Person1.gretting,
        'Time':now,
        'FullName':['Paul','Alfredo','Manriquez','Chavez'],
        'Profesor':1
    })

    document = Read_Html.render(ctx)
    return HttpResponse(document)



def Gretting_Pt3(request):  
    
    #Load Template
    Load_Template = loader.get_template('greting.html')

    now = datetime.now()
    Person1 = Person('Paul','Welcome!')
    My_Dic = {
        'name': Person1.name,
        'message': Person1.gretting,
        'Time':now,
        'FullName':['Paul','Alfredo','Manriquez','Chavez'],
        'Profesor':0
    }

    Template = Load_Template.render(My_Dic)

    return HttpResponse(Template)


def Gretting_Pt4(request):  
    
    now = datetime.now()
    Person1 = Person('Paul','Welcome!')
    My_Dic = {
        'name': Person1.name,
        'message': Person1.gretting,
        'Time':now,
        'FullName':['Paul','Alfredo','Manriquez','Chavez'],
        'Profesor':0
    }

    return render(request,'greting.html',My_Dic)


def child1_page(request):

    MyDic={
        'name':'Paul'
    }

    return render(request,'child1.html',MyDic)




