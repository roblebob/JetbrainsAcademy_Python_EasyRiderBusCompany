# Write your code here
import json


class Data:
    def __init__(self, raw_str):
        self.core = json.loads(raw_str)
        self.validate_arrivial_times()

    def validate_arrivial_times(self):
        result = dict()

        feedback = []

        for _data in self.core:
            _id = _data["bus_id"]
            if _id not in result:
                result[_id] = [_data]
            else:
                result[_id].append(_data)

        for bus_id in result:
            for i, stop in enumerate(result[bus_id]):
                if 0 < i < len(result[bus_id]):
                    prev = result[bus_id][i - 1]
                    if stop["a_time"] <= prev["a_time"]:
                        feedback.append(stop)
                        break

        print("Arrival time test:")
        if len(feedback) == 0:
            print("OK")
        else:
            for entry in feedback:
                _id, _name = entry["bus_id"], entry["stop_name"]
                print(f"bus_id line {_id}: wrong time on station {_name}")

    def validate_stops(self):
        result = dict()
        for _data in self.core:
            _id, _type, _name = _data["bus_id"], _data["stop_type"], _data["stop_name"]

            if _id not in result:
                result[_id] = {"Start stops": [], "Transfer stops": set(), "All stops": set(), "Finish stops": []}

            if _type == "S":
                result[_id]["Start stops"].append(_name)
            elif _type == "F":
                result[_id]["Finish stops"].append(_name)

            result[_id]["All stops"].update({_name})

        # check
        for bus_id, stops in result.items():
            if len(stops["Start stops"]) != 1 or len(stops["Finish stops"]) != 1:
                print("There is no start or end stop for the line: {}.".format(bus_id))
                return

        # calculate Transfer stops
        for bus_id in result.keys():

            other_bus_ids = list(result.keys())
            other_bus_ids.remove(bus_id)

            for other_bus_id in other_bus_ids:
                result[bus_id]["Transfer stops"].update(
                    result[bus_id]["All stops"] & result[other_bus_id]["All stops"])

        #
        feedback = {"Start stops": set(), "Transfer stops": set(), "Finish stops": set()}
        for bus_id in result.keys():
            for key in feedback.keys():
                feedback[key].update(set(result[bus_id][key]))

        # print result
        for key, val in feedback.items():
            print(f"{key}: {len(val)} {sorted(list(val))}")


data = Data(input())



















# pattern = re.compile(r'^\b[A-Z].*\b(Road|Avenue|Boulevard|Street)\b$')

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


# counter = dict()
#
# for data in data_list:
#     if data['bus_id'] in counter:
#         counter[data['bus_id']].add(data['stop_name'])
#     else:
#         counter[data['bus_id']] = {data['stop_name']}
#
