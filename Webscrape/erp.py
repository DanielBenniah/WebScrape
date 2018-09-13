import requests
import re
from bs4 import BeautifulSoup as soup
import ctypes  # An included library with Python install.

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

try:
  credentials = open("credentials.txt", "r")
except:
  Mbox("Error", "File not found: credentials.txt", 1)
  exit()

login_details = []

for line in credentials:
  login_details.append(line)

fileName = "Claim Status.csv"
try:
  output_file = open(fileName, "w")
except:
  Mbox("Error", "Unable to write to file erp.csv. Please close the file if it is open", 1)
  output_file.close()
  exit()

output_file.write("Claim Amount, Status\n")

url = 'http://erp.merce.co/erp'
login = 'http://erp.merce.co/erp/AuthOwnerServlet'
claims_page = 'http://erp.merce.co/erp/ShowClaimServlet?action=home'

auth = {'username': login_details[0].replace("\n", ""), 
        'password': login_details[1].replace("\n", ""),
        'login':'Login'
        }

with requests.session() as session:
  
  try:
    response = session.post(login, data = auth)
  except:
    print ("Invalid login")
    raw_input("Press Enter to exit")
    exit()

  soupText = soup(response.text, 'html.parser')

  invalid_logins = soupText.findAll("span")
  for span in invalid_logins:
    if (span.text.find("Invalid") != -1):
      Mbox("Error", "Invalid Login", 1)
      exit()

  print ("Login successful")
  response = session.get(claims_page)

  soupText = soup(response.text, 'html.parser')
  
  table = soupText.table
  
  spans = table.findAll("span", {"id":re.compile("^claim_state")})
  
  tds = table.findAll("td", {"align":"right"})

  print ("Data found")
  
  span_list = []
  
  tds_list = []
  
  for span in spans:
    span_list.append(span.text)
    
  for td in tds:
    if (is_number(td.text)):
      tds_list.append(td.text)
    
  for i in range(len(span_list)):
    try:
      output_file.write (str(tds_list[i]) + "," + str(span_list[i]) + "\n")
    except:
      Mbox("Error", "Unable to write to file erp.txt. Please close the file if it is open", 1)
      print ("Unable to write to erp.txt")
      raw_input("Press Enter to exit")
      #output_file.close()
      exit()

  Mbox("Success", "Please open erp.csv to view status.\nIf you have more ideas, please mail them to\ndanielbenniah@gmail.com", 1)
  input("Press Enter to exit")
  output_file.close()