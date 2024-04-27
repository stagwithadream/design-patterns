'''

Courses Website , should return a list of requested modules of a course
Courses -> Modules

We move what client wants to client code i.e., main
'''

from abc import ABC, abstractmethod

# ---------------------------------------------------------------- factory method fully implemented

class CourseManager(ABC):
    @abstractmethod
    def createCourse(self):
        pass

    def getModules(self):
        course = self.createCourse()
        modules = course.getModules()

        return modules


class HLDCourseManager(CourseManager):
    def createCourse(self):
        return HLD()


class LLDCourseManager(CourseManager):
    def createCourse(self):
        return LLD()


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


if __name__ == "__main__":
    # I need a HLD module
    courseManager = HLDCourseManager()
    modules = courseManager.getModules()
    print(modules)

    # I need a LLD module
    courseManager = LLDCourseManager()
    modules = courseManager.getModules()
    print(modules)
