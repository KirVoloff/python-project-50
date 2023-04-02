import json


def generate_diff(filepath1, filepath2):
    data1 = json.load(open(filepath1))
    data2 = json.load(open(filepath2))
    diff = find_diff(data1, data2)
    return format_diff(diff)


def find_diff(data1, data2):
    keys = sorted(set(list(data1.keys()) + list(data2.keys())))
    diff = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if value1 == value2:
            diff.append((' ', key, value1))
        elif key not in data2:
            diff.append(('-', key, value1))
        elif key not in data1:
            diff.append(('+', key, value2))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append((' ', key, find_diff(value1, value2)))
        else:
            diff.append(('-', key, value1))
            diff.append(('+', key, value2))
    return diff


def format_diff(diff, indent=2):
    lines = ['{']
    for sign, key, value in diff:
        if isinstance(value, list) or isinstance(value, dict):
            value = format_diff(value, indent + 2)
        else:
            value = json.dumps(value)
        lines.append('{indent}"{key}": {sign} {value}'.format(
            indent=' ' * indent, key=key, sign=sign, value=value))
    lines.append('}')
    return '\n'.join(lines)


if __name__ == '__main__':
    filepath1 = 'file1.json'
    filepath2 = 'file2.json'
    diff = generate_diff(filepath1, filepath2)
    print(diff)
