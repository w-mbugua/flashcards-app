from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def add(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST.get('answer',False)
        old_num_1 = request.POST.get('old_num_1',False)
        old_num_2 = request.POST.get('old_num_2',False)

        if not answer:
            return render(request,'divide.html', {
                'my_answer' : "You didn't entered any answer",
                'num_1' : num_1,
                'num_2' : num_2,
                'color' : 'warning',
                })

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct ! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect ! " + old_num_1 + " + " + old_num_2 + " is  " + str(correct_answer) + ", not " + answer
            color = "danger"

        return render(request,'add.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1' : num_1,
            'num_2' : num_2,
            'color' : color,
            })

    return render(request,'add.html',{
        'num_1' : num_1,
        'num_2' : num_2,
        })

def subtract(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST.get('answer',False)
        old_num_1 = request.POST.get('old_num_1',False)
        old_num_2 = request.POST.get('old_num_2',False)

        if not answer:
            return render(request,'divide.html', {
                'my_answer' : "You didn't entered any answer",
                'num_1' : num_1,
                'num_2' : num_2,
                'color' : 'warning',
                })

        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct ! " + old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect ! " + old_num_1 + " - " + old_num_2 + " is  " + str(correct_answer) + ", not " + answer
            color = "danger"

        return render(request,'subtract.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1' : num_1,
            'num_2' : num_2,
            'color' : color,
            })

    return render(request,'subtract.html',{
        'num_1' : num_1,
        'num_2' : num_2,
        })

def multiply(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST.get('answer',False)
        old_num_1 = request.POST.get('old_num_1',False)
        old_num_2 = request.POST.get('old_num_2',False)

        if not answer:
            return render(request,'divide.html', {
                'my_answer' : "You didn't entered any answer",
                'num_1' : num_1,
                'num_2' : num_2,
                'color' : 'warning',
                })

        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct ! " + old_num_1 + " * " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect ! " + old_num_1 + " * " + old_num_2 + " is  " + str(correct_answer) + ", not " + answer
            color = "danger"

        return render(request,'multiply.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1' : num_1,
            'num_2' : num_2,
            'color' : color,
            })

    return render(request,'multiply.html',{
        'num_1' : num_1,
        'num_2' : num_2,
        })

def divide(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(1,10)

    if request.method == "POST":
        answer = request.POST.get('answer',False)
        old_num_1 = request.POST.get('old_num_1',False)
        old_num_2 = request.POST.get('old_num_2',False)

        if not answer:
            return render(request,'divide.html', {
                'my_answer' : "You didn't entered any answer",
                'num_1' : num_1,
                'num_2' : num_2,
                'color' : 'warning',
                })

        correct_answer = int(old_num_1) / int(old_num_2)
        answer = round(float(answer),2)
        correct_answer = round(correct_answer,2)
        if answer == correct_answer:
            my_answer = "Correct ! " + old_num_1 + " / " + old_num_2 + " = " + str(answer)
            color = "success"
        else:
            my_answer = "Incorrect ! " + old_num_1 + " / " + old_num_2 + " is  " + str(correct_answer) + ", not " + str(answer)
            color = "danger"

        return render(request,'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1' : num_1,
            'num_2' : num_2,
            'color' : color,
            })

    return render(request,'divide.html',{
        'num_1' : num_1,
        'num_2' : num_2,
        })