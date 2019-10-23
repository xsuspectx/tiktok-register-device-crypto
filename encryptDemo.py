import requests
import json
import base64
import string
import random
import time

# THIS IS ONLY A SMALL DEMO ON HOW OUR API CAN BE USED. FULL DETAILS HIDDEN FOR PUBLIC.


apiEndpoint = "http://HIDDEN/encrypt"
apiKey = "INVALID"

# This is the body tiktok Expects.
# For this public script, it's not disclosed. Customers of course get the FULL details needed for TikTok

openudid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

tData = {
    "magic_tag":"ss_app_log",
    "many_more": "fields",
    "are": "needed"
    }


payload = {
    "apikey": apiKey,
    "encrypt": base64.b64encode(bytes(json.dumps(tData,separators=(',', ':')), 'utf-8'))
}
try:
    # Send a POST request to our API
    # API returns JSON. the "status" key is either "success" if everything worked, or "error" if there was an error
    # If status is success, the key "data" holds the base64 encoded string you need to send to TikTok to register your device!
    r = requests.post(apiEndpoint,json=payload)

    data = r.json()

    if data["status"] == "success":
        #the base64 encoded body
        cryptedBody = data["data"]

        #you are now able to send this to tiktok to register your device
        ts = str(time.time())
        tsMilli = str(int(round(time.time() * 1000)))
        endpoint = "/service/2/device_register/other_url_parts_hidden"
        headers = {"content-type":"hidden",
                    "User-Agent": "hidden"}
        rd = requests.post("http://applog.musical.ly" + endpoint,headers=headers,data=base64.b64decode(cryptedBody))
        print(rd.json())

        

    else:
        print(data["reason"])
    

except Exception as e:
    print(e)
