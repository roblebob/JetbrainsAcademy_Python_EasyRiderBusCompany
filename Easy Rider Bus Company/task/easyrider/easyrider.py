# Write your code here
import json
import re

pattern = re.compile(r'^\b[A-Z].*\b(Road|Avenue|Boulevard|Street)\b$')

json_as_str = input()
# json_as_str = r'[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]'
data_list = json.loads(json_as_str)
# data_type_checks = {
#     'bus_id': lambda x: isinstance(x, int) and x in [128, 256, 512],
#     'stop_id': lambda x: isinstance(x, int),
#     'stop_name': lambda x: isinstance(x, str) and pattern.search(x) is not None,
#     'next_stop': lambda x: isinstance(x, int),
#     'stop_type': lambda x: x in ['S', 'O', 'F', ""],
#     'a_time': lambda x: isinstance(x, str) and re.match(r"^([01]\d|2[0-4]):[0-5]\d$", x) is not None
# }
# error_counter = {k: 0 for k in ['stop_name', 'stop_type', 'a_time']}
#
# for data in data_list:
#     for key, value in data.items():
#         if key in error_counter.keys() and not data_type_checks[key](value):
#             error_counter[key] += 1
#


counter = dict()

for data in data_list:
    if data['bus_id'] in counter:
        counter[data['bus_id']].add(data['stop_name'])
    else:
        counter[data['bus_id']] = {data['stop_name']}


# result = f"""Type and required field validation: {sum(error_counter.values())} errors
# stop_name: {error_counter['stop_name']}
# stop_type: {error_counter['stop_type']}
# a_time: {error_counter['a_time']}
# """

print("Line names and number of stops:")
for key, value in counter.items():
    print(f"bus_id: {key}, stops: {len(value)}")
