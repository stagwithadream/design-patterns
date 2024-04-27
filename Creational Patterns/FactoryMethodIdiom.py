from abc import ABC, abstractmethod

# ----------------------------------------------------------------  Factory method idiom

class ICourse(ABC):
    @abstractmethod
    def getModules(self):
        pass


class HLD(ICourse):
    def __init__(self):
        self.modules = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    def getModules(self):
        return self.modules


class LLD(ICourse):
    def __init__(self):
        self.modules = ["h", "i"]

    def getModules(self):
        return self.modules


class CourseFactory:
    def getCourse(self, courseName):
        if courseName == "HLD":
            return HLD()
        elif courseName == "LLD":
            return LLD()


class CourseManager:
    def __init__(self):
        self.courses = []

    def getModules(self, request):
        courseName = request
        courseFactory = CourseFactory()
        course = courseFactory.getCourse(courseName)
        modules = course.getModules()

        return modules

if  __name__ == "__main__":
    courseManager = CourseManager()
    modules = courseManager.getModules("HLD")
    print(modules)

    modules = courseManager.getModules("LLD")
    print(modules)