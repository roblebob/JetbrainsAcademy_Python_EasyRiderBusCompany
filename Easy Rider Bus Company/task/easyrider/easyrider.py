# Write your code here
import json
import re

pattern = re.compile(r'^\b[A-Z].*\b(Road|Avenue|Boulevard|Street)\b$')

json_as_str = input()
data_list = json.loads(json_as_str)
data_type_checks = {
    'bus_id': lambda x: isinstance(x, int) and x in [128, 256, 512, 1024],
    'stop_id': lambda x: isinstance(x, int),
    'stop_name': lambda x: isinstance(x, str) and pattern.search(x) is not None,
    'next_stop': lambda x: isinstance(x, int),
    'stop_type': lambda x: x in ['S', 'O', 'F', ""],
    'a_time': lambda x: isinstance(x, str) and re.match(r"^([01]\d|2[0-4]):[0-5]\d$", x) is not None
}
error_counter = {k: 0 for k in ['stop_name', 'stop_type', 'a_time']}

for data in data_list:
    for key, value in data.items():
        if key in error_counter.keys() and not data_type_checks[key](value):
            error_counter[key] += 1

result = f"""Type and required field validation: {sum(error_counter.values())} errors
stop_name: {error_counter['stop_name']}
stop_type: {error_counter['stop_type']}
a_time: {error_counter['a_time']}
"""

print(result)
