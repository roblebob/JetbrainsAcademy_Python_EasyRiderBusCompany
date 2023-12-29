# Write your code here
import json


class Data:
    def __init__(self, raw_str):
        self.result = dict()
        self.core = json.loads(raw_str)

        for _data in self.core:
            _id = _data["bus_id"]
            if _id not in self.result:
                self.result[_id] = [_data]
            else:
                self.result[_id].append(_data)

        self.transfer_lanes = self.get_transfer_lanes()

        self.validate_stop_types()

    def validate_stop_types(self):
        feedback = []
        for bus_id in self.result:
            for i, stop in enumerate(self.result[bus_id]):
                if i == 0:
                    if stop["stop_type"] != "S":
                        feedback.append(stop["stop_name"])
                elif 0 < i < len(self.result[bus_id]) - 1:
                    if stop["stop_type"] == "O" and stop["stop_name"] in self.transfer_lanes:
                        feedback.append(stop["stop_name"])
                else:
                    if stop["stop_type"] != "F":
                        feedback.append(stop["stop_name"])

        print("On demand stops test:")
        if len(feedback) == 0:
            print("OK")
        else:
            print("Wrong stop type:", sorted(feedback))

    def get_transfer_lanes(self):
        all_stops = dict()
        transfer_lanes = set()
        for bus_id in self.result.keys():
            all_stops[bus_id] = set()
            for stop in self.result[bus_id]:
                all_stops[bus_id].update({stop["stop_name"]})

        for bus_id in self.result.keys():
            other_bus_ids = set(self.result.keys())
            other_bus_ids.remove(bus_id)
            for other_bus_id in other_bus_ids:
                transfer_lanes.update(all_stops[bus_id] & all_stops[other_bus_id])

        return transfer_lanes


if __name__ == "__main__":
    data = Data(input())
