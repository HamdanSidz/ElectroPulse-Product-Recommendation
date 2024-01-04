from django.shortcuts import render
import pandas as pd  
from .helper import main,main1
from nltk.stem.porter import PorterStemmer

# Create your views here.



# logic for fetching stored dataframe and developed model
dict_data = 0
org_name_product = 0
similarities = 0
df = 0
ps = PorterStemmer()

if main1() == 1:
    dict_data,org_name_product,similarities = main()
    #print(similarities)
else:
    dict_data,org_name_product,similarities = main()
    #print(similarities)


def similar_word_fix(val):
    arr = []
    for i in val.split():
        arr.append(ps.stem(i))
    
    return " ".join(arr)


def recommend(product_name):
    global similarities,dict_data,df
    df = pd.DataFrame(dict_data)

    product_name = similar_word_fix(product_name)
    product_name = product_name.lower()
    #print("@@@@@@@@@@@@@@@@@@@@@@",product_name)
    index_no_product = df[df['name'] == product_name].index[0]
    #print("@@@@@@@@@@@@@@@@@@@@@@",index_no_product)
    distances = similarities[index_no_product]
    rec_prod_captured = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
    #print(rec_prod_captured)
    
    return rec_prod_captured





# server logic starts heres
def fun_home(request):
    return render(request,"recommend/home.html")


def fun_aboutus(request):
    return render(request,"recommend/about.html")


def fun_recommender(request):
    global similarities,dict_data,org_name_product

    product_list = []
    each_product_dict = {}

    if request.method == "POST":
        selected_value = request.POST.get('mySelect')
        #print("@@@@@@@@@@@@@@@@@@@@@@",selected_value)

        if selected_value == "Open this select menu to choose":
            return render(request,"recommend/rec.html",{"message":"Please select an appropriate item"})

        rec_prod_captured = recommend(selected_value)

        for i in rec_prod_captured:
            #print(df.iloc[i[0]]["name"])
            #print(df.iloc[i[0]]["image"])
            #print(df.iloc[i[0]]["ratings"])
            #print(df.iloc[i[0]]["no_of_ratings"])
            #print(df.iloc[i[0]]["link"])
            each_product_dict["name"] = df.iloc[i[0]]["name"]
            each_product_dict["image"] = df.iloc[i[0]]["image"]
            each_product_dict["ratings"] = df.iloc[i[0]]["ratings"]
            each_product_dict["no_of_ratings"] = df.iloc[i[0]]["no_of_ratings"]
            each_product_dict["link"] = df.iloc[i[0]]["link"]

            product_list.append(each_product_dict)
            each_product_dict = {}

        return render(request,"recommend/rec.html",{"product_list":product_list})

    else:
        return render(request,"recommend/rec.html",{"data_list":org_name_product})

    
    
