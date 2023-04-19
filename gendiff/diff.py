import json


def generate_diff(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_data = json.load(file1)
        file2_data = json.load(file2)

    diff = {}
    all_keys = set(file1_data.keys()) | set(file2_data.keys())

    for key in sorted(all_keys):
        if key not in file1_data:
            diff["+ {0}".format(key)] = file2_data[key]
        elif key not in file2_data:
            diff["- {0}".format(key)] = file1_data[key]
        elif file1_data[key] != file2_data[key]:
            diff["- {0}".format(key)] = file1_data[key]
            diff["+ {0}".format(key)] = file2_data[key]
        else:
            diff["  {0}".format(key)] = file1_data[key]

    diff_lines = ["{0}: {1}".format(key, value) for key, value in diff.items()]
    return '\n'.join(diff_lines)
