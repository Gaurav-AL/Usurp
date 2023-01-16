from django.shortcuts import render
from .init_db import curr,conn
from google.oauth2 import service_account
import time
from googleapiclient.discovery import build





# Create your views here.
def index(request):
    return render(request,'index.html')
    

def sheets(request):
    # api data
    
    SHEET_SERVICE_ACCOUNT_FILE = 'keys.json'
    SHEET_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    # filling in credentials
    sheet_credentials = None
    sheet_credentials = service_account.Credentials.from_service_account_file(SHEET_SERVICE_ACCOUNT_FILE,scopes = SHEET_SCOPES)
    
    # spreadsheet ID
    SPREAD_SHEET_ID = '18leWt2SzR_QqBmb3u208nJ0eaAsBiZNy3XtXtMtBKIc'
    
    # call the sheet API
    service = build('sheets','v4',credentials = sheet_credentials)
    sheet = service.spreadsheets()
    
    result = sheet.values().get(spreadsheetId = SPREAD_SHEET_ID,range = "sheet1!A2:E37").execute()
    rows = result.get('values',[])
    print(rows)
    for row in rows:
        try:
            serial_id,name,age,college,roll_number = row[0],row[1],row[2],row[3],row[4]
            curr.execute('INSERT INTO login(login_id,name,age,college,roll_no)' 
                    'VALUES(%s,%s,%s,%s,%s)',(serial_id,name,age,college,roll_number))
            conn.commit()
        except Exception as err:
            print(err)
                   
    return render(request,'sheets.html')

def calender(request):
    # Defining Scopes
    CAL_SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    # Service keys
    CAL_SERVICE_ACCOUNT_FILE = 'cal_keys.json'
    # getting credentials
    cal_credentials = None
    cal_credentials = service_account.Credentials.from_service_account_file(CAL_SERVICE_ACCOUNT_FILE,scopes = CAL_SCOPES)
    services = build('calendar', 'v3', credentials=cal_credentials)
    
    
    cal_result = services.calendars().get(calendarId='primary').execute()
    for i in range(len(cal_result)):
        try:
            summary, kind , timezone = cal_result['summary'], cal_result['kind'],cal_result['timeZone']
            curr.execute('INSERT INTO calendar(kind,summary,timezone) VALUES (%s,%s,%s)',(kind,summary,timezone))
            conn.commit()
        except Exception as err:
            print(err)
    return render(request,'calender.html')
    
