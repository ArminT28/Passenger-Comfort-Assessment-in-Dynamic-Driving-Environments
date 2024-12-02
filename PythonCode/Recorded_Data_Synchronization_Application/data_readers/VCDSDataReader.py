from datetime import datetime
from Python.RecordedDrivingDataMerger.models.SensorEntry import SensorEntry


def convert_timestamp(initial_datetime, timestamp):
    total_seconds = float(timestamp)

    hours = int(total_seconds // 3600)
    total_seconds %= 3600

    minutes = int(total_seconds // 60)
    total_seconds %= 60

    seconds = int(total_seconds)
    milliseconds = int((total_seconds - seconds) * 1000)

    offset_timestamp = {
        'hour': hours,
        'minute': minutes,
        'second': seconds,
        'millisecond': milliseconds
    }

    if offset_timestamp['hour'] >= 24:
        raise (ValueError('Invalid offset hour timestamp'))

    if offset_timestamp['minute'] >= 60:
        raise (ValueError('Invalid offset min timestamp'))

    if offset_timestamp['second'] >= 60:
        raise (ValueError('Invalid offset secs timestamp'))

    computed_timestamp = {
        'hour': initial_datetime['hour'] + offset_timestamp['hour'],
        'minute': initial_datetime['minute'] + offset_timestamp['minute'],
        'second': initial_datetime['second'] + offset_timestamp['second'],
        'millisecond': initial_datetime['millisecond'] + offset_timestamp['millisecond'],
        'year': initial_datetime['year'],
        'month': initial_datetime['month'],
        'day': initial_datetime['day']
    }

    if computed_timestamp['millisecond'] >= 1000:
        computed_timestamp['second'] += computed_timestamp['millisecond'] // 1000
        computed_timestamp['millisecond'] %= 1000

    if computed_timestamp['second'] >= 60:
        computed_timestamp['minute'] += computed_timestamp['second'] // 60
        computed_timestamp['second'] %= 60

    if computed_timestamp['minute'] >= 60:
        computed_timestamp['hour'] += computed_timestamp['minute'] // 60
        computed_timestamp['minute'] %= 60

    if computed_timestamp['hour'] >= 24:
        computed_timestamp['day'] += 1
        computed_timestamp['hour'] %= 24

    return computed_timestamp


def transform_vcds_to_dictionary(data_input_directory_name, data_input_file_name, vcds_months_list,sensor_repository):
    with open(data_input_directory_name + "/" + data_input_file_name, mode='r', newline='') as file:
        header = file.readline().strip()
        day = int(header.split(",")[1])
        month = header.split(",")[2]
        for single_month in vcds_months_list:
            if single_month == month:
                month = vcds_months_list.index(single_month) + 1
                if month < 10:
                    month = "0" + str(month)
                break
        year = int(header.split(",")[3])
        time = header.split(",")[4].split("-")[0]
        hour = int(time.split(":")[0])
        minutes = int(time.split(":")[1])
        seconds = int(time.split(":")[2])
        miliseconds = int(time.split(":")[3])
        computed_datetime = {'year': year, 'month': month, 'day': day, 'hour': hour, 'minute': minutes,
                             'second': seconds,
                             'millisecond': miliseconds}
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        data_matrix = []
        for row in file:
            single_row = row.strip().split(",")
            data_matrix.append(single_row)

        data_dictionary = {}

        header_row = data_matrix[0]

        current_marker = 0
        for row in data_matrix[1:]:
            if row[0] != "" and current_marker < int(row[0]):
                current_marker = int(row[0])

            for i in range(1, len(row) - 1, 2):
                if row[i + 1] != "":
                    if row[i] == "":
                        timestamp = datetime(year=1, month=1, day=1, hour=00, minute=00, microsecond=0)
                    else:
                        dictionary_timestamp = convert_timestamp(computed_datetime, row[i])
                        formatted_timestamp = (f'{dictionary_timestamp['year']}-{dictionary_timestamp['month']}-'
                                               f'{dictionary_timestamp['day']} '
                                               f'{dictionary_timestamp['hour']}:{dictionary_timestamp['minute']}:'
                                               f'{dictionary_timestamp['second']}.{dictionary_timestamp['millisecond']}')
                        timestamp = datetime.strptime(str(formatted_timestamp), "%Y-%m-%d %H:%M:%S.%f")
                    if timestamp in data_dictionary and data_dictionary[timestamp]:
                        data_dictionary[timestamp].append(
                            {"value": row[i + 1], "sensor": header_row[i + 1], "marker": current_marker})
                    else:
                        data_dictionary[timestamp] = [
                            {"value": row[i + 1], "sensor": header_row[i + 1], "marker": current_marker}]

        string_data = {}

        for timestamp, data in data_dictionary.items():
            if type(timestamp) is not str:
                new_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
                string_data[new_timestamp] = data
            else:
                string_data[timestamp] = data

        for timestamp,data in string_data.items():
            for single_data in data:
                single_data_sensor_entry = SensorEntry(timestamp,single_data['sensor'],single_data['value'],single_data['marker'],)
                sensor_repository.add_sensor_data(single_data_sensor_entry)
