# By Vehicom
# For assistance or to repot errors contact me at elvisxiag06@gmail.com or Vehicom#6109 on discord

# Most of this is repurposed code from my Bad Apple/Rick Roll to google sheets video

# To get creds.json
# go to https://console.cloud.google.com/projectselector2/apis/credentials?authuser=1&supportedpurview=project
# Create a new project
# Go to library on the left navbar
# Enable the Sheets API
# Go to Credentials
# Click on your project
# Click create credentials on the top
# Create a service account
# Click on service accounts on the left
# click the three dots next to your service account
# Manage Keys > Add Key > Create new JSON Key >
# A JSON file should be automatically downloaded
# Copy and paste the contents into creds.json

from CreateRequest import create_request
import cv2
import gspread
from skimage import io

URL = input("Google Sheet URL: ")
ROWS = int(input("ROWS: "))
COLS = int(input("COLUMNS: "))
IMG = input("Image Link: ")

image = io.imread(IMG)

gc = gspread.service_account('./creds.json')
wsh = gc.open_by_url(URL)

body = create_request(ROWS, COLS, image)
wsh.batch_update(body)