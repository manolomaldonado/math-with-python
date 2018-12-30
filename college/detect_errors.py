HOSP_INDEX=12
errors = 0
stream = ''
with open("monica.csv","r") as f:
    next(f)
    years={}
    for line in f :
        values = line.strip("\n").split(",")
        hosp=values[HOSP_INDEX].strip("\"")
        if hosp != "y" and hosp != "n" :
            print line
            errors = errors+1
    print errors


with open("monica.csv","r") as f:
    for line in f :
        values = line.strip("\n").split(",")
        hosp=values[HOSP_INDEX].strip("\"")
        if hosp != "y" and hosp != "n" :
            values[HOSP_INDEX] = "\"y\"" #Suponiendo que sea y
            line = ','.join(values)+"\n"
        stream = stream+line


    print stream



