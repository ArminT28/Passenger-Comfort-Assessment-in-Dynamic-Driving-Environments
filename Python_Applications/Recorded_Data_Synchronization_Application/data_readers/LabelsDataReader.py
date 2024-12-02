import csv
from Python.RecordedDrivingDataMerger.models.SensorEntry import SensorEntry


def transform_labels_to_dictionary(labels_directory_path, labels_file_name,starting_timestamp, ending_timestamp, sensor_repository):
    file_path = labels_directory_path + "/" + labels_file_name
    starting_timestamp = starting_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
    ending_timestamp = ending_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")

    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            timestamp = row[0]
            if starting_timestamp <= timestamp <= ending_timestamp:
                label = row[1]

                label_entry = SensorEntry(timestamp, 'ComfortabilityLabel', label)

                sensor_repository.add_sensor_data(label_entry)
