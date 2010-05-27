from models import Patient

def handle_uploaded_file(f):
    first_line = True
    for line in f:
        # TODO: What will the first line normally be? Headers?
        if not first_line:
            split = line.split('\t') #TODO: can there be other separators?
            patient_id = split[0]
            all_patients = Patient.objects.all()
            for p in all_patients:
                if p.id == patient_id:
                    p.delete()
            #TODO: when the model changes this needs to too
            patient = Patient(id=patient_id, date=get_date(split[1]), 
                              std=get_date(split[2]), program=split[3],
                              age=split[4], sex=split[5], 
                              enroll_d=get_date(split[6]), f250v=split[7],
                              f250d=get_date(split[8]))
            patient.save()
        else:
            first_line = False

def get_date(date_string):
    if len(date_string) >0:
        date_string = date_string.strip('\"')
        day = date_string[0:2]
        month = get_month(date_string[2:5])
        if month == None:
            return None
        year = date_string[5:9]
        return year + "-" + month + "-" + day
    else:
        return None

def get_month(month_string):
    if month_string == 'jan':
        return '01'
    if month_string == 'feb':
        return '02'
    if month_string == 'mar':
        return '03'
    if month_string == 'apr':
        return '04'
    if month_string == 'may':
        return '05'
    if month_string == 'jun':
        return '06'
    if month_string == 'jul':
        return '07'
    if month_string == 'aug':
        return '08'
    if month_string == 'sep':
        return '09'
    if month_string == 'oct':
        return '10'
    if month_string == 'nov':
        return '11'
    if month_string == 'dec':
        return '12'
