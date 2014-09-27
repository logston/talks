class Cat(object):
    def __init__(self, name, color, breed, leg_count=4):
        self.name = name
        self.color = color
        self.breed = breed
        self.leg_count = leg_count
     
    def meow(self, meow_count=1):
        print 'MEOW' * meow_count

    def travel_time_to_milk(self, distance):
        ref_speed = 2
        actual_speed = (float(self.leg_count) / 4) * ref_speed
        return distance / actual_speed 

