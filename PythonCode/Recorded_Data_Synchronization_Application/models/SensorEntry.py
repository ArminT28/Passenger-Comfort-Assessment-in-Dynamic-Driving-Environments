class SensorEntry:
    def __init__(self, timestamp, sensor_name, sensor_value, marker=0):
        self.timestamp:str = timestamp
        self.sensor_name = sensor_name
        self.sensor_value = sensor_value
        self.marker = marker
        
    def get_timestamp(self):
        return self.timestamp
    
    def get_sensor_name(self):
        return self.sensor_name
    
    def get_sensor_value(self):
        return self.sensor_value
    
    def get_marker(self):
        return self.marker

    def __str__(self):
        return f"SensorEntry({self.timestamp}, {self.sensor_name}, {self.sensor_value}, {self.marker})"
    
    def __repr__(self):
        return str(self)