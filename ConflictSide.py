from Lane import Lane


class ConflictSide(object):
    def __init__(self, lanes, conflict_side_priority, conflict_side_vehicles_amount,
                 conflict_side_starvation_value=0, conflict_side_time=60):
        self.conflict_side_priority = conflict_side_priority
        self.conflict_side_vehicles_amount = conflict_side_vehicles_amount
        self.conflict_side_starvation_value = conflict_side_starvation_value
        self.conflict_side_time = conflict_side_time
        self.lanes = [None] * len(lanes)
        for i in range(0, len(lanes)):
            self.lanes[i] = lanes[i]
        self.conflict_side_waiting_time = 1

    def get_conflict_side_priority(self):
        return self.conflict_side_priority

    def reset_conflict_side_starvation_value(self):
        self.conflict_side_starvation_value = 0

    def get_conflict_side_starvation_value(self):
        return self.conflict_side_starvation_value

    def get_conflict_side_time(self):
        return self.conflict_side_time

    def get_conflict_side_vehicles_amount(self):
        return self.conflict_side_vehicles_amount

    def calculate_benefit_for_conflict_side(self):
        benefit = 0
        if self.conflict_side_vehicles_amount == 0:
            return 0
        for lane in self.lanes:
            benefit += lane.calculate_benefit_for_lane()
        benefit += self.conflict_side_starvation_value
        return benefit

    def set_conflict_side_starvation_value(self, value):
        self.conflict_side_starvation_value += value

    def set_conflict_side_waiting_time(self, value):
        self.conflict_side_waiting_time += value

    def remove_vehicles(self, amount):
        print("conflict side contain: " + str(self.conflict_side_vehicles_amount) + ' vehicles')
        vehicles_counter = 0
        for lane in self.lanes:
            lane.set_lane_vehicles_amount(amount)
            vehicles_counter += lane.get_lane_vehicles_amount()
        self.conflict_side_vehicles_amount = vehicles_counter
        print("conflict side contain: " + str(self.conflict_side_vehicles_amount) + ' vehicles')

    def show_waiting_time(self):
        return str(self.conflict_side_waiting_time)
