class PythonClassName(SuperClassName):
    def __init__(self, ClassAttributes):
        self._ClassAttributes = ClassAttributes

    def set_ClassAttributes(self, new_ClassAttributes):
        self._ClassAttributes = new_ClassAttributes

    def get_ClassAttributes(self, new_ClassAttributes):
        return ClassAttributes

class Person(object):
    def __init__(self, name, Gender, DOB,):
        self._name = name
        self._Gender = Gender
        self._DOB, = DOB,

    def set_name(self, new_name):
        self._name = new_name

    def set_Gender(self, new_Gender):
        self._Gender = new_Gender

    def set_DOB,(self, new_DOB,):
        self._DOB, = new_DOB,

    def get_name(self, new_name):
        return name

    def get_Gender(self, new_Gender):
        return Gender

    def get_DOB,(self, new_DOB,):
        return DOB,

class Student(Person):
    def __init__(self, name, Gender, DOB, Class):
        self._name = name
        self._Gender = Gender
        self._DOB = DOB
        self._Class = Class

    def set_name(self, new_name):
        self._name = new_name

    def set_Gender(self, new_Gender):
        self._Gender = new_Gender

    def set_DOB(self, new_DOB):
        self._DOB = new_DOB

    def set_Class(self, new_Class):
        self._Class = new_Class

    def get_name(self, new_name):
        return name

    def get_Gender(self, new_Gender):
        return Gender

    def get_DOB(self, new_DOB):
        return DOB

    def get_Class(self, new_Class):
        return Class

