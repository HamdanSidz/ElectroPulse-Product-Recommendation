import pickle

check = 0
similarities = 0
dict_data = 0
org_name_product = 0


def main1():
    global check
    check += 1
    return check

def main():
    global check,similarities,dict_data,org_name_product

    if check == 1:
        dict_data = pickle.load(open("D:\\Django projects\\Product_Recommendation\\recommend\\dict_of_data","rb"))
        org_name_product = pickle.load(open("D:\\Django projects\\Product_Recommendation\\recommend\\original_name_product","rb"))
        similarities =  pickle.load(open("D:\\Django projects\\Product_Recommendation\\recommend\\similarities_file","rb"))
    
    return dict_data,org_name_product,similarities

    