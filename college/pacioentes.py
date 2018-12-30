datos_pacientes=[]
pacientes= []
atributos = ("outcome","sex","age","yronset","premi","smstatus","diabetes","highbp","hichol","angina","stroke","hosp")

with open("monica.csv","r") as f:
    next(f)
    for line in f :
        values = line.strip("\n").split(",")
        paciente_values = []
        pacientes.append(values[0].strip("\""))
        paciente_values = values[1:len(values)]
        dict1={}
        dict1=zip(atributos,paciente_values)

        datos_pacientes.append(dict1)


    dict2=dict(zip(pacientes,datos_pacientes))

print("The values of the patient number 5270 is",list(dict2['5270']))#6048 y 6367 casualmente tienen los mismos datos y me los esta escupiendo si uso de key id en el dic1
print("The values of the patient number 3341 is",list(dict2['3341']))
