import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "nu3zxh"
deviceType = "SAMSUNG"
deviceId = "123456"
authMethod = "token"
authToken = "99121499"

# Initialize GPIO

def myCommandCallback(cmd):
        if cmd.data:
                print("Time to take medicine")#for commands
       
try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)#create client
        #.............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()#connect client to platform

while True:
        
        
        data = { '8:00 ' : 'Olmat' , '9:30 ' : 'Metxl' , '11:15 ': 'Aspirin' , '12:00 ': 'Metformin' }
        #print (data)
        def myOnPublishCallback():
            print ('8:00  : Olmat' , '9:30  : Metxl' , '11:15 : Aspirin', '12:00 : Metformin' )
        success = deviceCli.publishEvent("DHT11", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
