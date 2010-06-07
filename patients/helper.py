from models import Patient

def handle_uploaded_file(f):
    result = 'Success' 
    first_line = True
    for line in f:
        # The first line of the file will always be headers
        if not first_line:
            # The data will always be separated by tabs
            split = line.split('\t') 
            if len(split) == 14:
                patient_id = split[0]
                all_patients = Patient.objects.all()
                for p in all_patients:
                    if p.id == patient_id:
                        p.delete()
                patient = Patient(id=patient_id, height=get_value(split[1]), 
                              egplandt=get_date(split[2]), 
                              egpregdt=get_date(split[3]),
                              egstage4dt=get_date(split[4]), 
                              egcd4dt=get_date(split[5]), 
                              egcd4v=get_value(split[6]), 
                              edate=get_date(split[7]),
                              egweight=get_value(split[8]), 
                              enroldt=get_date(split[9]),
                              lastdt=get_date(split[10]), 
                              returndt=get_date(split[11]),
                              startdt=get_date(split[12]), 
                              startgprg=split[13])
                #TODO: there will be one more field coming
                patient.save()
            else:
                result = 'At least one line of the file did not have the correct number of entries and was not added'
        else:
            first_line = False
    return result
      
def get_value(input):
    # for integers and decimals handles empty string case by returning none
    if input == '':
        return None
    else:
        return input

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
