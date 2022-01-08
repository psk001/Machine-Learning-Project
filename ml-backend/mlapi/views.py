import pickle
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author
from .serializers import AuthorSerializer

# Create your views here.


class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
       
        return Response({"authors": serializer.data})


def home (request):
    return render(request, 'index.html')




def getPredictions(pclass, sex, age, sibsp, parch, fare):
    model = pickle.load(open("mlapi/titanic_survival_model.sav", "rb"))
    sc = pickle.load(open("mlapi/scaler.sav", "rb"))
    prediction = model.predict(sc.transform([[pclass, sex, age, sibsp, parch, fare, 20, 0, 0, 0, 2, 0, 0, 8]]))
    
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"

def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    #embmarked = int(request.GET['embarked'])
 

    result = getPredictions(pclass, sex, age, sibsp, parch, fare)

    return render(request, 'result.html', {'result':result})
