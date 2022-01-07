from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
import phonenumbers
codes = dict([(value, key) for key, value in COUNTRY_CODE_TO_REGION_CODE.items()])
#function to get the country code
def recode(code):
    for i in codes.keys():
        if code in i:
            return i
#fucntion to check on the string fname and lname
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)