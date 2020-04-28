import datetime
import thingspeak

'''
Usage:
    install => pip install thingspeak

    Usage Example:
        pass parameter dict to store parameters for each 15 sec
        parameters = {'battery_voltage': 40, 'vehicle_speed': 50, 'engine_load': 50, 'coolant_temperature': 70,
                      'rpm': 80, 'engine_runtime': 38}
        cloud_storage = CloudStorage()
        cloud_storage.send_data(parameters)
'''


class CloudStorage:
    def __init__(self):
        #self.channel = thingspeak.Channel(id=978849, api_key="QKLLG1O7HCUKWV66")
        self.channel = thingspeak.Channel(id=980414, api_key="B1E91134TN7P6PJM")

    def send_data(self, parameters):
        try:
            response = self.channel.update({
                1: parameters['battery_voltage'],
                2: parameters['vehicle_speed'],
                3: parameters['engine_load'],
                4: parameters['coolant_temperature'],
                5: parameters['rpm'],
                6: parameters['engine_runtime'],
                7: datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            })
            print(response)
        except Exception as e:
            print(e)
