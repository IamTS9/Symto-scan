from django.shortcuts import render
from mainapp.models import Contact_info

from joblib import load

covid_model = load('./models/covid.joblib')
kidney_model=load('./models/Kidney.joblib')
heart_disease_model=load('./models/heart_disease.joblib')
diabetes_model=load('./models/Diabetes.joblib')
breast_cancer_model=load('./models/breast_cancer.joblib')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']
        ins = Contact_info(name= name, email= email, Query= query)
        ins.save()
    return render(request, 'contact.html')

def covid(request):
    return render(request, 'covid.html')

def heart(request):
    return render(request, 'heart_disease.html')

def diabetes(request):
    return render(request, 'diabetes.html')

def Breast_cancer(request):
    return render(request, 'cancer.html')

def diabetes_result(request):
    disease = ''
    if request.method=='POST':
        gender = request.POST['gender']
        age = int(request.POST['age'])/100
        hypertension = request.POST['hypertension']
        heart_disease = request.POST['heart_disease']
        smoking = request.POST['smoking']
        current=0
        ever=0
        former=0
        never=0
        noinfo=0
        if smoking==1:
            current=1
        elif smoking==2:
            former=1
        elif smoking==0:
            never=1
        bmi = request.POST['bmi']
        hba = request.POST['hba']
        glucose = request.POST['glucose']
        features=[gender,age,hypertension, heart_disease,bmi, hba, glucose, current, ever, former, never, noinfo]
        y_pred = diabetes_model.predict([features])[0]
        diabetes_prob=diabetes_model.predict_proba([features])[0]
        if y_pred==0:
            result_diabetes="You have Diabetes"
            prob = round(diabetes_prob[0]*100, 2)
            if prob>80:
                disease="We advice you to consult a doctor and get yourself checked immediately"
        
        else:
            result_diabetes="You don't have Diabetes"
            prob = round(diabetes_prob[1]*100, 2)
            if prob>80:
                disease="Congratulations! You're safe and healthy"

        return render(request, 'result.html',{'result':result_diabetes, 'probability': prob, 'disea':disease})

def heart_result(request):
    disease = ''
    if request.method=='POST':
        age = request.POST['age']
        age=int(age)/100
        gender=request.POST['Gender']
        chestpain = request.POST['chestpain']
        Blood_Pressure = request.POST['Blood-Pressure']
        cholesterol = request.POST['cholesterol']
        heart_rate = request.POST['heart-rate']
        angina = request.POST['angina']
        st = request.POST['st']
        thal = request.POST['thal']
        vessels = request.POST['vessels']
        array=[age, gender,chestpain, Blood_Pressure, cholesterol,0,0, heart_rate, angina, st,0, vessels,thal]
        y_pred = heart_disease_model.predict([array])[0]
        heart_prob = heart_disease_model.predict_proba([array])[0]
        if y_pred==0:
            result_heart="You don't have Heart Disease"
            prob = round(heart_prob[0]*100, 2)
            if prob>80:
                disease="Congratulations! You're safe and healthy"        
        else:
            result_heart="You have Heart Disease"
            prob = round(heart_prob[1]*100, 2)
            if prob>80:
                disease="We advice you to consult a doctor and get yourself checked immediately"

        return render(request, 'result.html',{'result':result_heart, 'probability': prob, 'disea': disease})

def cancer_result(request):
    disease = ''
    if request.method=='POST':
        texture_mean = request.POST['texture_mean']
        cell_compactness = request.POST['cell_compactness']
        worst_cell_texture_rate = request.POST['worst_cell_texture_rate']
        worst_cell_area_rate = request.POST['worst_cell_area_rate']
        worst_cell_smooth_rate=request.POST['worst_cell_smooth_rate']
        worst_cell_concavity = request.POST['worst_cell_concavity']
        worst_concave_points = request.POST['worst_concave_points']
        mean_cell_area_rate = request.POST['mean_cell_area_rate']
        predictors = [0,texture_mean,0, 0, 0, 0,0,0,0,0,0,0,0,mean_cell_area_rate,0, cell_compactness,0,0,0,0,0,0, worst_cell_texture_rate,0, worst_cell_area_rate, worst_cell_smooth_rate,0, worst_cell_concavity, worst_concave_points,0]
        y_pred = breast_cancer_model.predict([predictors])[0]
        cancer_prob = breast_cancer_model.predict_proba([predictors])[0]
        if y_pred == 0:
            result_cancer="You don't have Breast Cancer"
            prob=round(cancer_prob[0]*100, 2)
            if prob>80:
                disease="Congratulations! You're safe and healthy"        
        else:
            result_cancer = "You have Breast-Cancer"
            prob = round(cancer_prob[1]*100, 2)
            if prob>80:
                disease="We advice you to consult a doctor and get yourself checked immediately"

        return render(request, 'result.html',{'result': result_cancer, "probability": prob, 'disea':disease})

def covid_result(request):
    disease = ''
    if request.method=='POST':
        Gender = request.POST['Gender']
        age = request.POST['age']
        age = int(age)/100
        fever = request.POST['fever']
        cough = request.POST['cough']
        runnynose = request.POST['runnynose']
        musclesore = request.POST['musclesore']
        Pneumonia = request.POST['Pneumonia']
        Diarrhea = request.POST['Diarrhea']
        Lung = request.POST['Lung']
        travel = request.POST['travel']
        features =[Gender, age, fever, cough, runnynose, musclesore, Pneumonia, Diarrhea, Lung, travel,0]
        y_pred = covid_model.predict([features])[0]
        covid_prob=covid_model.predict_proba([features])[0]
        if y_pred == 0:
            result_covid = "You don't have Covid-19 disease"
            prob = round(covid_prob[0]*100, 2)
            if prob>80:
                disease="Congratulations! You're safe and healthy"
        else:   
            result_covid = "You have Covid-19 disease"
            prob = round(covid_prob[1]*100, 2)
            if prob>80:
                disease="We advice you to consult a doctor and get yourself checked immediately"

        return render(request, 'result.html', {'result' : result_covid, 'probability':prob, 'disea':disease})