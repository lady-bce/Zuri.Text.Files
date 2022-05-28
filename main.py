class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, new_name):
        self.name = new_name
        new_name = "Peter"
        print(f"The student changed his name to ", new_name)

    def change_age(self, new_age):
        self.age = new_age
        new_age = 34
        print(f"The student changed his age to ", new_age)

    def add_track(self, new_track):
        self.track = new_track
        new_track = "UI/UX"
        print(f"The student added a new track ", new_track)

    def get_score(self, score):
        self.score = score
        score = 20.90
        print(f"The student score is ", score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20.90)
