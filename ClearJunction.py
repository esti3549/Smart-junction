from ConflictSide import ConflictSide
import constant


class ClearJunction(object):
    def __init__(self, junction):
        self.junction = junction
        self.amount_of_vehicles_in_junction = self.set_amount_of_vehicles_in_junction()

    def set_amount_of_vehicles_in_junction(self):
        count = 0
        for key, conflict_side in self.junction.items():
            count += conflict_side.get_conflict_side_vehicles_amount()
        return count

    # Input: a smart junction, maximal green light time per conflict side.
    def clear_junction_by_conflict_sides_attributes_priorities(self):
        count_green_light_conflict_1 = 0
        count_green_light_conflict_2 = 0

        chosen = -1
        green_light_counter = 0

        # for each conflict side initialize the starvation parameter to 0:
        for key, conflict_side in self.junction.items():
            conflict_side.reset_conflict_side_starvation_value()
        print("the junction contain: " + str(self.amount_of_vehicles_in_junction) + ' vehicles')
        while self.amount_of_vehicles_in_junction > 0:
            green_light_counter += 1
            chosen = self.open_green_light(constant.STARVATION_MAX_VALUE)
            if chosen == 1:
                count_green_light_conflict_1 += 1
            elif chosen == 2:
                count_green_light_conflict_2 += 1

            print("the chosen conflict side is: " + str(chosen))
            self.junction[chosen].remove_vehicles(constant.NUMBER_OF_VEHICLES_PASSING_PER_MINUTE)
            self.amount_of_vehicles_in_junction = self.set_amount_of_vehicles_in_junction()
            print("the junction contain: " + str(self.amount_of_vehicles_in_junction) + ' vehicles')

            self.set_conflict_side_waiting_time()
            print("---------------------------------------")
            # for each conflict side update the starvation counter:
            self.set_starvation_value(chosen)

        print("The total amount of green light until the junction is cleared: " + str(green_light_counter))
        print("The amount of green light for conflict side 1: " + str(count_green_light_conflict_1))
        print("The amount of green light for conflict side 2: " + str(count_green_light_conflict_2))
        self.show_conflict_side_waiting_time()

    # Input: a smart junction and maximum starvation value.
    # Output: the number of the conflict side that gets green light.
    def open_green_light(self, starvation_max_value):
        max_benefit = 0
        chosen = 0
        max_starve = -1
        # For each conflict side check if CSi is the most starved
        for key, conflict_side in self.junction.items():
            if conflict_side.get_conflict_side_vehicles_amount() == 0:
                break
            if conflict_side.get_conflict_side_starvation_value() >= starvation_max_value:
                if conflict_side.get_conflict_side_starvation_value() > max_starve:
                    max_starve = conflict_side.get_conflict_side_starvation_value()
                    chosen = key
        if max_starve > -1:
            return chosen
        #  For each conflict side check if CSi has the largest benefit:
        for key, conflict_side in self.junction.items():
            if max_benefit < conflict_side.calculate_benefit_for_conflict_side():
                max_benefit = conflict_side.calculate_benefit_for_conflict_side()
                chosen = key
            # print("name of conflict " + str(key))
        return chosen

    def set_starvation_value(self, chosen):
        for key, conflict_side in self.junction.items():
            if key != chosen:
                conflict_side.set_conflict_side_starvation_value(1)
            else:
                conflict_side.reset_conflict_side_starvation_value()

    def set_conflict_side_waiting_time(self):
        for key, conflict_side in self.junction.items():
            if conflict_side.get_conflict_side_vehicles_amount() > 0:
                conflict_side.set_conflict_side_waiting_time(1)

    def show_conflict_side_waiting_time(self):
        str1 = ""
        for key, conflict_side in self.junction.items():
            str1 += "finish time for conflict side " + str(key) + ": " + conflict_side.show_waiting_time()
            print(str1)
            str1 = ""
