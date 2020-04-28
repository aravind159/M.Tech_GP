import time
import obd
from obd_cloud_storage import CloudStorage
from raw_can_messages import rpm_raw_canned
from repository import Repository
class OBDAnalyzer:
    def __init__(self):
        self.connection = obd.Async(baudrate=38400, fast=False)
        self.cloud_storage = CloudStorage()
        self.repository = Repository()
        self.starter_count = 0
        self.parameters = {'battery_voltage': None, 'rpm': None, "vehicle_speed": None, "engine_runtime": None, "engine_load": None,
                           "coolant_temperature": None}

    def update_voltage(self, voltage_response):
        self.parameters['battery_voltage'] = voltage_response.__str__().split(" ")[0]

    def update_rpm(self, rpm_response):
        self.parameters['rpm'] = rpm_response.__str__().split(" ")[0]

    def update_speed(self, speed_response):
        self.parameters['vehicle_speed'] = speed_response.__str__().split(" ")[0]

    def update_run_time(self, run_time_response):
        self.parameters['engine_runtime'] = run_time_response.__str__().split(" ")[0]

    def update_engine_load(self, engine_load_response):
        self.parameters['engine_load'] = engine_load_response.__str__().split(" ")[0]

    def update_coolant_temp(self, coolant_temp_response):
        self.parameters['coolant_temperature'] = coolant_temp_response.__str__().split(" ")[0]

    # def update_something(self, somethingresponse):
    #     self.parameters['something val'] = somethingresponse.__str__().split(" ")[0]

    def start_monitoring(self):
        #self.connection.start()
        self.connection.watch(obd.commands.ELM_VOLTAGE, callback=self.update_voltage)
        self.connection.watch(obd.commands.RPM, callback=self.update_rpm)
        self.connection.watch(obd.commands.SPEED, callback=self.update_speed)
        self.connection.watch(obd.commands.RUN_TIME, callback=self.update_run_time)
        self.connection.watch(obd.commands.ENGINE_LOAD, callback=self.update_engine_load)
        self.connection.watch(obd.commands.COOLANT_TEMP, callback=self.update_coolant_temp)
        # self.connection.watch(obd.commands., callback=self.update_something)
        self.connection.start()
        time.sleep(0.3)


    def __store(self):
        print(self.parameters)
        #self.cloud_storage.send_data(self.parameters)
        self.repository.write_row(self.parameters)
        self.cloud_storage.send_data(self.parameters)

    #def __starter_monitor(self):
     #  if self.parameters['rpm'] > 0:
      #        self.starter_count += 1

    #def __check(self):
     #   if self.parameters['rpm']:
      #      return True
       # return False

    def main_start(self):
        self.start_monitoring()
        while True:
           # self.__starter_monitor()
            #rpm_raw_canned()
            #if self.__check():
                self.__store()
                #time.sleep(1)
            

if __name__ == '__main__':
    obd_analyzer = OBDAnalyzer()
    obd_analyzer.main_start()
    obd_analyzer.start_monitoring()
    while True:
        obd_analyzer.__store()
        #time.sleep(4)
