import json
import os
from datetime import datetime
from Python.RecordedDrivingDataMerger.converters.DictionaryConverter import dictionary_to_json, dictionary_to_csv
from Python.RecordedDrivingDataMerger.data_readers.GPXDataReader import transform_gpx_to_dictionary
from Python.RecordedDrivingDataMerger.data_readers.LabelsDataReader import transform_labels_to_dictionary
from Python.RecordedDrivingDataMerger.models.SensorRepository import SensorRepository
from Python.RecordedDrivingDataMerger.data_readers.VCDSDataReader import transform_vcds_to_dictionary


def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def generate_current_sensor_labels(sensor_labels_directory_path, sensor_labels_file_name, sensor_repository):
    current_sensors = []
    if os.path.exists(sensor_labels_directory_path + "/" + sensor_labels_file_name):
        with open(sensor_labels_directory_path + "/" + sensor_labels_file_name) as sensor_labels_file:
            sensor_labels = json.load(sensor_labels_file)
    else:
        print(f"The file {sensor_labels_directory_path + "/" + sensor_labels_file_name} does not exist.")
        sensor_labels = []

    for timestamp, data_list in sensor_repository.get_sensor_data().items():
        for sensor_entry in data_list:
            sensor_name = sensor_entry.get_sensor_name()
            if sensor_name not in sensor_labels:
                sensor_labels.append(sensor_name)
            if sensor_name not in current_sensors:
                current_sensors.append(sensor_name)

    if "ComfortabilityLabel" not in sensor_labels:
        sensor_labels.append("ComfortabilityLabel")

    if "ComfortabilityLabel" not in current_sensors:
        current_sensors.append("ComfortabilityLabel")

    with open(sensor_labels_directory_path + "/" + sensor_labels_file_name, 'w') as file:
        json.dump(sensor_labels, file, indent=4)
    return current_sensors


def older_main():
    # Not used anymore, at the beginning, this application allowed the user to choose which step of the data merging to execute.
    # Now, the application executes all steps in sequence.
    # This function is kept for reference.
    config = load_config("configurations/application_config.json")
    csv_output_data_directory_path = config["csv_output_data_directory_path"]
    json_output_data_directory_path = config["json_output_data_directory_path"]
    vcds_input_data_directory_path = config["vcds_input_data_directory_path"]
    input_data_file_name = config["vcds_input_data_file_name"]
    gps_input_data_directory_path = config["gps_input_data_directory_path"]
    gps_input_data_file_name = config["gps_input_data_file_name"]
    sensor_labels_directory_path = config["sensor_labels_directory_path"]
    sensor_labels_file_name = config["sensor_labels_file_name"]
    labels_directory_path = config["labels_directory_path"]
    labels_file_name = config["labels_file_name"]
    if sensor_labels_file_name.lower() == "same":
        sensor_labels_file_name = input_data_file_name
    vcds_months_list = config["vcds_months_list"]

    vcds_data_dictionary = {}
    gps_data_dictionary = {}
    generated_current_sensor_labels = None
    while True:
        print_main_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            vcds_data_dictionary = transform_vcds_to_dictionary(vcds_input_data_directory_path, input_data_file_name,
                                                                vcds_months_list)
        elif choice == "2":
            print_all_configurations(config)
        elif choice == "3":
            if len(vcds_data_dictionary) == 0:
                print("\nPlease read the VCDS data first\n")
                continue
            if len(gps_data_dictionary) == 0:
                print("\nPlease read the GPS data first\n")
                continue
            generated_current_sensor_labels = generate_current_sensor_labels(sensor_labels_directory_path,
                                                                             sensor_labels_file_name,
                                                                             vcds_data_dictionary, gps_data_dictionary)
            print("\nSensor labels generated\n")
        elif choice == "4":
            if len(vcds_data_dictionary) == 0:
                print("\nPlease read the data first\n")
                continue
            if not os.path.exists(json_output_data_directory_path):
                os.makedirs(json_output_data_directory_path)
            dictionary_to_json(vcds_data_dictionary, json_output_data_directory_path, input_data_file_name)
        elif choice == "5":
            if len(vcds_data_dictionary) == 0:
                print("\nPlease read the data first\n")
                continue
            if not os.path.exists(csv_output_data_directory_path):
                os.makedirs(csv_output_data_directory_path)
            if not generated_current_sensor_labels or len(generated_current_sensor_labels) == 0:
                print("\nPlease generate the sensor labels first\n")
                continue
            dictionary_to_csv(vcds_data_dictionary, csv_output_data_directory_path, input_data_file_name,
                              generated_current_sensor_labels)
        elif choice == "6":
            if generated_current_sensor_labels is None:
                print("\nPlease generate the sensor labels first\n")
                continue
            print("\nCurrently not implemented\n")
        elif choice == "7":
            if generated_current_sensor_labels is None:
                print("\nPlease generate the sensor labels first\n")
                continue
            if len(vcds_data_dictionary) == 0:
                print("\nPlease read the data first\n")
                continue
            plot_all_vcds_data(vcds_data_dictionary, generated_current_sensor_labels)
        elif choice == "8":
            if len(vcds_data_dictionary) == 0:
                print("\nPlease read the data first\n")
                continue
            longitudinal_sensor_label = "Slip control system sensor-Longitude Acceleration Sensor"
            lateral_sensor_label = "Slip control system sensor-Lateral acceleration sensor 1"
            plot_longitudinal_and_lateral_acceleration(vcds_data_dictionary, longitudinal_sensor_label,
                                                       lateral_sensor_label)
        elif choice == "9":
            vcds_data_dictionary = transform_vcds_to_dictionary(vcds_input_data_directory_path, input_data_file_name,
                                                                vcds_months_list)
            sorted_timestamps = sorted(vcds_data_dictionary.keys())
            starting_timestamp = datetime.strptime(sorted_timestamps[1], "%Y-%m-%d %H:%M:%S.%f")
            ending_timestamp = datetime.strptime(sorted_timestamps[-1], "%Y-%m-%d %H:%M:%S.%f")
            gps_data_dictionary = transform_gps_to_dictionary(gps_input_data_directory_path, gps_input_data_file_name,
                                                              starting_timestamp, ending_timestamp)
            generated_current_sensor_labels = generate_current_sensor_labels(sensor_labels_directory_path,
                                                                             sensor_labels_file_name,
                                                                             vcds_data_dictionary, gps_data_dictionary)
            all_data_dictionary = concatenate_two_dictionaries_based_on_timestamps(vcds_data_dictionary,
                                                                                   gps_data_dictionary)
            dictionary_to_json(all_data_dictionary, json_output_data_directory_path, input_data_file_name)
            dictionary_to_csv(all_data_dictionary, csv_output_data_directory_path, input_data_file_name,
                              generated_current_sensor_labels)
        elif choice == "10":
            vcds_data_dictionary = transform_vcds_to_dictionary(vcds_input_data_directory_path, input_data_file_name,
                                                                vcds_months_list)
            sorted_timestamps = sorted(vcds_data_dictionary.keys())
            starting_timestamp = datetime.strptime(sorted_timestamps[1], "%Y-%m-%d %H:%M:%S.%f")
            ending_timestamp = datetime.strptime(sorted_timestamps[-1], "%Y-%m-%d %H:%M:%S.%f")
            gps_data_dictionary = transform_gpx_to_dictionary(gps_input_data_directory_path, gps_input_data_file_name,
                                                              starting_timestamp, ending_timestamp)
            labels_dictionary = transform_labels_to_dictionary(labels_directory_path, labels_file_name,
                                                               starting_timestamp, ending_timestamp)
            generated_current_sensor_labels = generate_current_sensor_labels(sensor_labels_directory_path,
                                                                             sensor_labels_file_name,
                                                                             vcds_data_dictionary, gps_data_dictionary)
            all_data_dictionary = concatenate_three_dictionaries_based_on_timestamps(vcds_data_dictionary,
                                                                                     gps_data_dictionary,
                                                                                     labels_dictionary)
            dictionary_to_json(all_data_dictionary, json_output_data_directory_path, input_data_file_name)
            dictionary_to_csv(all_data_dictionary, csv_output_data_directory_path, input_data_file_name,
                              generated_current_sensor_labels)
        elif choice == "11":
            if len(vcds_data_dictionary) == 0:
                print("\nPlease read the data first\n")
                continue
            sorted_timestamps = sorted(vcds_data_dictionary.keys())
            starting_timestamp = datetime.strptime(sorted_timestamps[1], "%Y-%m-%d %H:%M:%S.%f")
            ending_timestamp = datetime.strptime(sorted_timestamps[-1], "%Y-%m-%d %H:%M:%S.%f")
            gps_data_dictionary = transform_gps_to_dictionary(gps_input_data_directory_path, gps_input_data_file_name,
                                                              starting_timestamp, ending_timestamp)
        elif choice == "12":
            break
        else:
            print("\nInvalid choice\n")


def main():
    config = load_config("configurations/application_config.json")
    csv_output_data_directory_path = config["csv_output_data_directory_path"]
    json_output_data_directory_path = config["json_output_data_directory_path"]
    vcds_input_data_directory_path = config["vcds_input_data_directory_path"]
    input_data_file_name = config["vcds_input_data_file_name"]
    gps_input_data_directory_path = config["gps_input_data_directory_path"]
    gps_input_data_file_name = config["gps_input_data_file_name"]
    sensor_labels_directory_path = config["sensor_labels_directory_path"]
    sensor_labels_file_name = config["sensor_labels_file_name"]
    labels_directory_path = config["labels_directory_path"]
    labels_file_name = config["labels_file_name"]
    if sensor_labels_file_name.lower() == "same":
        sensor_labels_file_name = input_data_file_name
    vcds_months_list = config["vcds_months_list"]

    sensor_repository = SensorRepository()
    transform_vcds_to_dictionary(vcds_input_data_directory_path, input_data_file_name,
                                 vcds_months_list, sensor_repository)
    sensor_repository.sort_sensor_data()
    sorted_timestamps = sorted(sensor_repository.keys())
    starting_timestamp = datetime.strptime(sorted_timestamps[1], "%Y-%m-%d %H:%M:%S.%f")
    ending_timestamp = datetime.strptime(sorted_timestamps[-1], "%Y-%m-%d %H:%M:%S.%f")
    transform_gpx_to_dictionary(gps_input_data_directory_path, gps_input_data_file_name,
                                starting_timestamp, ending_timestamp, sensor_repository)
    transform_labels_to_dictionary(labels_directory_path, labels_file_name,
                                   starting_timestamp, ending_timestamp, sensor_repository)
    generated_current_sensor_labels = generate_current_sensor_labels(sensor_labels_directory_path,sensor_labels_file_name,sensor_repository)
    sensor_repository.sort_sensor_data()
    dictionary_to_json(sensor_repository.get_sensor_data(), json_output_data_directory_path, input_data_file_name)
    dictionary_to_csv(sensor_repository.get_sensor_data(), csv_output_data_directory_path, input_data_file_name,
                      generated_current_sensor_labels)


if __name__ == "__main__":
    main()
