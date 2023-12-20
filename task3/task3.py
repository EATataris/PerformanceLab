import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def update_values(tests_data, values_data):
    for test in tests_data:
        if isinstance(test, dict):
            test_id = test.get('id', None)
            if test_id is not None:
                test_id = int(test_id)
                test_result = next((value['value'] for value in values_data if value.get('id') == test_id), '')
                test['value'] = test_result

            if 'values' in test:
                update_values(test['values'], values_data)


def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    tests_data = read_json("task3/tests.json")
    values_data = read_json("task3/values.json")

    update_values(tests_data, values_data)

    write_json(tests_data, "task3/report.json")
