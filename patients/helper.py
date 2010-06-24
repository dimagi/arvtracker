from datetime import datetime, timedelta
from models import Patient

def handle_uploaded_file(f):
    file_name = f.name
    file_size = f.size
    result = 'Success' 
    first_line = True
    all_patients = Patient.objects.all()
    for line in f:
        # The first line of the file will always be headers
        if not first_line:
            # The data will always be separated by tabs
            split = line.split('\t') 
            if len(split) == 14:
                patient_id = split[0]
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
                              startgprg=trim(split[13]))
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
    
def trim(input):
    trimmed = input.strip('\"\r\n')
    return trimmed

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

def get_starting_by_stakeholder(request):
    weeks = get_weeks(request)
    months = get_months(request)
    counts = {'moh': weeks.copy(), 'ftf': weeks.copy(), 'mjap': weeks.copy(),
              'total': weeks.copy()}
    sum_counts(counts, weeks)
    
    return get_stakeholder_url(counts, weeks, months)

def get_percentage_initiations(request):
    url = ''
    weeks = get_weeks(request)
    return url

def sum_counts(counts, weeks):
    patients = Patient.objects.all()
    for patient in patients:
        startdate = patient.startdt
        program = patient.startgprg
        if startdate and program != '':
            for week in weeks.keys():
                next_week = week + timedelta(7)
                if startdate >= week and startdate < next_week:
                    counts[program][week] += 1
                    counts['total'][week] += 1

def get_stakeholder_url(counts, weeks, months):
    keys = weeks.keys()
    keys.sort()
    max_number = get_max(counts)
    url = "http://chart.apis.google.com/chart?"
    url += "chtt=Weekly+Number+of+Patients|Starting+ART+by+Stakeholder&"
    url += "chs=1000x200&" # chart size
    url += "chbh=20,0,0&" #TODO: tweak this smaller
    data = "chd=t:"
    legend = "&chdl="
    for program in counts.keys():
        if program != "total":
            legend += program + "|"
            weeks_counts = counts[program]
            for key in keys:
                data += str(weeks_counts[key]) + ","
            data = data.strip(',')
            data += "|"
    data = data.strip('|')
    legend = legend.strip('|')
    url += legend + "&"
    data += "&"
    url += data
    url += "chds=0,"
    url += str(max_number)
    url += "&chxr=1,0,"
    url += str(max_number)
    url += "&cht=bvs&" # vertical bar graph, stacked
    url += "chco=4D89F9,C6D9FD,0000FF&" # series colors
    url += "chxt=x,y&" # show x and y axes
    xaxis = "chxl=0:|"
    i = 0
    for key in keys: #TODO: or could loop by month but spacing is tricky
        if i == 0:
            xaxis += str(key) #TODO: try leaving out every couple of these
            i += 1
        elif i == 1: i += 1
        elif i == 2: i += 1
        elif i == 3: i = 0
        xaxis += "|"
    xaxis = xaxis.strip('|')
    url += xaxis
    #url += "&chxp=0,0,80" #TODO: base this on number of months and size of graph
    return url

def get_max(counts):
    largest_number = 0
    for count in counts['total'].values():
        if count > largest_number:
            largest_number = count
    max = 10
    while max < largest_number:
        max += 10
    return max

def get_months(request):
    months = []
    start_year = ''
    start_month = ''
    end_year = ''
    end_month = ''
    if request:
        for item in request.POST.items():
            if item[0] == 'start_year':
                start_year = int(item[1])
            if item[0] == 'start_month':
                start_month = int(item[1])
            if item[0] == 'end_year':
                end_year = int(item[1])
            if item[0] == 'end_month':
                end_month = int(item[1])
    first_date = datetime(start_year, start_month, 01).date()
    last_date = datetime(end_year, end_month, 01).date()
    while first_date <= last_date:
        months.append(first_date)
        nextmonth = first_date.month + 1
        year = first_date.year
        if nextmonth == 13:
            nextmonth = 1
            year += 1
        first_date = datetime(year, nextmonth, 01).date()
    return months
                
def get_weeks(request):
    # TODO: make sure the end date is later than the start date
    weeks = {}
    start_year = ''
    start_month = ''
    end_year = ''
    end_month = ''
    if request:
        for item in request.POST.items():
            if item[0] == 'start_year':
                start_year = int(item[1])
            if item[0] == 'start_month':
                start_month = int(item[1])
            if item[0] == 'end_year':
                end_year = int(item[1])
            if item[0] == 'end_month':
                end_month = int(item[1])
    #try making the first and last date and increment to find all those in between
    first_date = datetime(start_year, start_month, 01).date()
    nextmonth = end_month + 1
    if nextmonth == 13:
        nextmonth = 1
        end_year += 1
    last_date = datetime(end_year, nextmonth, 01).date()
    current = first_date
    while current < last_date:
        weeks[current] = 0
        current += timedelta(7)
    return weeks