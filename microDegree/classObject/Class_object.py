class Student:

    def __init__(self, maths,science,social):
        self.maths = maths
        self.science = science
        self.social = social

    def getMathsMarks(self):
        return self.maths

    def getScienceMarks(self):
        return self.science

    def getSocialMarks(self):
        return self.social