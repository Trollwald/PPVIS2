class ExercisePlan:

    def __init__(self, num_practice, intensity, num_exercises):
        self.num_practice = num_practice
        self.intensity = intensity
        self.num_exercises =num_exercises
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def next_training(self):
        pass

    def add_training(self):
        pass

    def del_training(self):
        pass

    def get_num_practice(self):
        return self.num_practice

    def get_intensity(self):
        return self.intensity

    def get_num_exercises(self):
        return self.num_exercises

    def get_exercises(self):
        return self.exercises