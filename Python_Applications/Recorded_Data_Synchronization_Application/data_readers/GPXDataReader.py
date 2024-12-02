import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from Python.RecordedDrivingDataMerger.models.SensorEntry import SensorEntry


def compute_timestamp(timestamp):
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    date_obj = datetime.strptime(timestamp, date_format)
    date_obj += timedelta(hours=3)

    if date_obj.hour >= 24:
        date_obj -= timedelta(hours=24)
        date_obj += timedelta(days=1)

    timestamp = date_obj.strftime("%Y-%m-%d %H:%M:%S.%f")

    return timestamp


def transform_gpx_to_dictionary(data_input_directory_name, data_input_file_name, starting_timestamp, ending_timestamp, sensor_repository):
    tree = ET.parse(data_input_directory_name + "/" + data_input_file_name)
    root = tree.getroot()
    starting_timestamp = starting_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
    ending_timestamp = ending_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
    for trackpoint in root.iter('{http://www.topografix.com/GPX/1/1}trkpt'):
        timestamp = compute_timestamp(trackpoint.find('{http://www.topografix.com/GPX/1/1}time').text)
        if starting_timestamp <= timestamp <= ending_timestamp:
            longitude = float(trackpoint.get('lon'))
            longitude_sensor_entry = SensorEntry(timestamp,'Longitude',longitude)
            sensor_repository.add_sensor_data(longitude_sensor_entry)
            latitude = float(trackpoint.get('lat'))
            latitude_sensor_entry = SensorEntry(timestamp, 'Latitude', latitude)
            sensor_repository.add_sensor_data(latitude_sensor_entry)
            elevation = float(trackpoint.find('{http://www.topografix.com/GPX/1/1}ele').text)
            elevation_sensor_entry = SensorEntry(timestamp,'Elevation',elevation)
            sensor_repository.add_sensor_data(elevation_sensor_entry)
            try:
                heart_rate = int(trackpoint.find('.//{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}hr').text)
                heart_rate_sensor_entry = SensorEntry(timestamp,'Heart Rate',heart_rate)
                sensor_repository.add_sensor_data(heart_rate_sensor_entry)
            except AttributeError:
                print('No heart rate data for trackpoint at timestamp: ' + timestamp)
