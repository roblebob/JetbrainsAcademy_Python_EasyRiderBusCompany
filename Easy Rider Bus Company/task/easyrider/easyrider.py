# Write your code here
import json
import re

json_as_str = input()
data_list = json.loads(json_as_str)
data_type_checks = {
    'bus_id': lambda x: isinstance(x, int) and x in [128, 256, 512, 1024],
    'stop_id': lambda x: isinstance(x, int),
    'stop_name': lambda x: isinstance(x, str) and len(x) > 0,
    'next_stop': lambda x: isinstance(x, int),
    'stop_type': lambda x: x in ['S', 'O', 'F', ""],
    'a_time': lambda x: isinstance(x, str) and re.match(r"^\d{2}:\d{2}$", x) is not None
}
error_counter = {k: 0 for k in data_type_checks.keys()}

for data in data_list:
    for key, value in data.items():
        if not data_type_checks[key](value):
            error_counter[key] += 1

result = f"""Type and required field validation: {sum(error_counter.values())} errors
bus_id: {error_counter['bus_id']}
stop_id: {error_counter['stop_id']}
stop_name: {error_counter['stop_name']}
next_stop: {error_counter['next_stop']}
stop_type: {error_counter['stop_type']}
a_time: {error_counter['a_time']}
"""

print(result)
