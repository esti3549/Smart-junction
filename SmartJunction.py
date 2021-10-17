import csv
from Lane import Lane
from ConflictSide import ConflictSide
from ClearJunction import ClearJunction


# A class that builds the smart junction
class SmartJunction:
    def __init__(self):
        self.dict_of_lanes = dict(A1="null", A2="null", B="null", C1="null", C2="null", D="null", E1="null", E2="null",
                                  F="null", G1="null", G2="null", H="null")
        self.dict_of_conflict_sides = dict()

    def check_if_key_exists(self, key):
        if key in self.dict_of_lanes:
            return True

    def create_lane_and_insert_to_dict(self, row):
        self.dict_of_lanes[row[0]] = Lane(row[0], row[1], row[2])

    def print_dict(self):
        for i in self.dict_of_conflict_sides:
            print(i, self.dict_of_conflict_sides[i])

    def build_conflict_sides(self, index, lane1, lane2, lane3=None, lane4=None):
        print("build_conflict_sides")
        conflict_side_priority = 0
        conflict_side_vehicles_amount = 0
        if lane3 is not None and lane4 is not None:
            arr = [self.dict_of_lanes[lane1], self.dict_of_lanes[lane2],
                   self.dict_of_lanes[lane3], self.dict_of_lanes[lane4]]
        else:
            if lane3 is None and lane4 is None:
                arr = [self.dict_of_lanes[lane1], self.dict_of_lanes[lane2]]

        for i in range(arr.__len__()):
            print(arr[i])
        print("\n")
        for i in arr:
            conflict_side_priority += i.get_lane_priority()
            conflict_side_vehicles_amount += i.get_lane_vehicles_amount()
        self.dict_of_conflict_sides[index] = ConflictSide(arr, conflict_side_priority, conflict_side_vehicles_amount)

    def build_junction(self, path):
        with open(path, 'r') as file:
            lanes_reader = csv.reader(file)
            for row in lanes_reader:
                if self.check_if_key_exists(row[0]):
                    self.create_lane_and_insert_to_dict(row)

        self.build_conflict_sides(1, "A1", "A2", "E1", "E2")
        self.build_conflict_sides(2, "C1", "C2", "G1", "G2")

        clear_junction = ClearJunction(self.dict_of_conflict_sides)
        clear_junction.clear_junction_by_conflict_sides_attributes_priorities()
