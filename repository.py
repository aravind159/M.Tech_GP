import csv
import datetime
from os import path
import time
class Repository:
    CSV_COL = ['battery_voltage', 'rpm', 'vehicle_speed', 'engine_runtime', 'engine_load', 'coolant_temperature']

    def __init__(self):
        self.__initialise_csv()

    def __initialise_csv(self):

        if not path.exists(f'obd_parameters_{datetime.datetime.now().strftime("%d_%b")}.csv'):
            with open(f'obd_parameters_{datetime.datetime.now().strftime("%d_%b")}.csv', 'a+') as csv_file:
                file_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                file_writer.writerow(['battery_voltage_in_volts', 'engine_speed_in_rpm', 'vehicle_speed_in_kmph',
                                      'engine_runtime_in_sec', 'engine_load_pct', 'coolant_temperature_in_deg_c'])

    def write_row(self, parameters: dict):
        row = []
        for parm in parameters.keys():
            row = row + [parameters[parm]]
        #row = [parameters[col] if col in parameters else None for col in self.CSV_COL]
        #time.sleep(0.4)
        if len(row) <6:
            return
        with open(f'obd_parameters_{datetime.datetime.now().strftime("%d_%b")}.csv', 'a+') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(row)
            csv_file.close()