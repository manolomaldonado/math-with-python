sex=[]
yearonset=[]
SEX_INDEX=2
YRONSET_INDEX = 4
AGE_INDEX=3
with open("monica.csv","r") as f:
    next(f)
    years={}
    for line in f :
        values = line.strip("\n").split(",")
        sexo=values[SEX_INDEX].strip("\"")
        year=values[YRONSET_INDEX].strip("\"")
        edad=values[AGE_INDEX].strip("\"")
        data={}
        data={"sex":sexo,"age":edad}
        if not year in years:
            years[year]=[]
        else:
            years[year].append(data)

    average={}
    for year in years:
        total_m = 0
        total_f = 0
        ages_m = 0
        ages_f = 0
        for patient in years[year]:
            if patient['sex']=="m":
                total_m=total_m+1
                ages_m=ages_m+int(patient["age"])
            else:
                total_f=total_f+1
                ages_f=ages_f+int(patient["age"])

        average_ages_m=ages_m/total_m
        average_ages_f=ages_f/total_f

        average[year]={'edad_media_hombres': average_ages_m, 'edad_media_mujeres': average_ages_f}

    print average
