from random import choice


class RandomWalk():
    """a class to generate random walk data"""

    def __init__(self, num_points=5000):
        """init attributes """
        self.num_points = num_points
        # start from (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate random walk points"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
    def get_step(self):
        direction = choice([-1, 1])
        distance = choice(list(range(0, 8)))
        return direction * distance
