import csv
import json


def dictionary_to_csv(dictionary, csv_output_directory_name, output_file_name, current_sensor_labels):
    timestamps_to_remove = ['0001-01-01 00:00:00.000000']

    for timestamp_to_remove in timestamps_to_remove:
        del dictionary[timestamp_to_remove]

    with open(csv_output_directory_name + "/CSV-" + output_file_name, 'w', newline='\n') as csvfile:
        unique_fieldnames = ['timestamp', 'marker'] + list(current_sensor_labels)
        writer = csv.DictWriter(csvfile, fieldnames=unique_fieldnames)

        writer.writeheader()
        current_row_data = {}
        for timestamp, data_list in dictionary.items():
            current_row_data['timestamp'] = timestamp
            current_row_data['marker'] = 0
            for entry in data_list:
                if entry.get_marker() > current_row_data['marker']:
                    current_row_data['marker'] = entry.get_marker()
                sensor_key = entry.get_sensor_name()
                current_row_data[sensor_key] = entry.get_sensor_value()
                all_sensor_are_available = True
                for current_sensor_label in current_sensor_labels:
                    if current_sensor_label not in current_row_data.keys():
                        all_sensor_are_available = False
                if all_sensor_are_available:
                    writer.writerow(current_row_data)
                print(timestamp + ":" + str(all_sensor_are_available))


def dictionary_to_json(dictionary, output_directory_name, output_file_name):
    str_timestamp_dictionary = {}
    for timestamp, data_list in dictionary.items():
        print(type(timestamp))
    with open(output_directory_name + "/JSON-" + output_file_name, 'w') as json_file:
        json.dump(str_timestamp_dictionary, json_file, indent=4)


def concatenate_three_dictionaries_based_on_timestamps(vcds_data_dictionary, gps_data_dictionary, labels_dictionary):
    concatenated_dictionary = {}
    for timestamp, data_list in vcds_data_dictionary.items():
        if timestamp in concatenated_dictionary.keys():
            for entry in data_list:
                concatenated_dictionary[timestamp].append(entry)
        else:
            concatenated_dictionary[timestamp] = data_list

    for timestamp, data_list in gps_data_dictionary.items():
        if timestamp in concatenated_dictionary.keys():
            for entry in data_list:
                concatenated_dictionary[timestamp].append(entry)
        else:
            concatenated_dictionary[timestamp] = data_list

    for timestamp, label_entry in labels_dictionary.items():
        concatenated_dictionary[timestamp] = [label_entry]

    sorted_dictionary = dict(sorted(concatenated_dictionary.items()))

    return sorted_dictionary
