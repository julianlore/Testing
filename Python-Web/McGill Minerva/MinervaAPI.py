import requests

def transcript(s):
    url = "https://horizon.mcgill.ca/pban1/bzsktran.P_Display_Form"
    payload = {
        'user_type' : 'S',
        'tran_type' : 'V'
    }
    r = s.get(transcript, params=payload)
    # Write the response to a file (for testing)
    with open("test.html", mode="wb") as localfile:
        localfile.write(r.content)
