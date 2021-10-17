class Lane(object):
    def __init__(self, name, vehicles_amount, priority):
        self.lane_name = name
        self.lane_vehicles_amount = vehicles_amount
        self.lane_priority = priority

    def __str__(self):
        return str(self.lane_name + " contains " + self.lane_vehicles_amount + " vehicles, with priority " +
                   self.lane_priority)

    def get_lane_priority(self):
        return int(self.lane_priority)

    def get_lane_vehicles_amount(self):
        return int(self.lane_vehicles_amount)

    def set_lane_vehicles_amount(self, amount):
        if int(self.lane_vehicles_amount) >= amount:
            lane_amount = int(self.lane_vehicles_amount) - amount
            self.lane_vehicles_amount = lane_amount
        else:
            self.lane_vehicles_amount = 0
        print("lane " + self.lane_name + " contain " + str(self.lane_vehicles_amount) + ' vehicles')

    def calculate_benefit_for_lane(self):
        return int(self.lane_vehicles_amount) * int(self.lane_priority)

