from Python.RecordedDrivingDataMerger.models import SensorEntry


class SensorRepository:
    def __init__(self, sensor_data: SensorEntry = None):
        if sensor_data is None:
            sensor_data = {}
        self.sensor_data = sensor_data

    def get_sensor_data(self):
        return self.sensor_data

    def get_sensor_data_by_timestamp(self, timestamp):
        return self.sensor_data[timestamp]

    def add_sensor_data(self, sensor_data):
        if sensor_data.timestamp not in self.sensor_data:
            self.sensor_data[sensor_data.timestamp] = []

        self.sensor_data[sensor_data.timestamp].append(sensor_data)

    def sort_sensor_data(self):
        for timestamp, data_list in self.sensor_data.items():
            self.sensor_data[timestamp] = sorted(data_list, key=lambda x: x.get_sensor_name())

        self.sensor_data = dict(sorted(self.sensor_data.items()))

    def remove_sensor_data(self, sensor_data):
        if sensor_data.timestamp in self.sensor_data:
            self.sensor_data[sensor_data.timestamp].remove(sensor_data)

    def remove_sensor_data_by_timestamp(self, timestamp):
        del self.sensor_data[timestamp]

    def __str__(self):
        return f"SensorRepository({self.sensor_data})"

    def __repr__(self):
        return str(self)

    def keys(self):
        return self.sensor_data.keys()
