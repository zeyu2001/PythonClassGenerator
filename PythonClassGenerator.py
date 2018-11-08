class PythonClass:

    def __init__(self, class_name, super_class_name, attr_list):
        self._class_name = class_name
        self._super_class_name = super_class_name
        self._attr_list = attr_list

    def get_class_name(self):
        return self._class_name

    def get_super_class_name(self):
        return self._super_class_name

    def get_attr_list(self):
        return self._attr_list

    def __str__(self):
        result = ''
        result += 'class [{}] inherits from class [{}]\nAttributes: '\
                  .format(self._class_name, self._super_class_name)
        result += str(self._attr_list[0]) + '\n'
        for attr in self._attr_list[1:]:
            result += '{:>12}'.format(' ') + str(attr) + '\n'
        return result[:-1]
    
# print(PythonClass('Person', 'object', ['Name', 'Gender', 'DOB']))


def ReadPythonClass(filename):
    
    PythonClass_list = []
    
    with open (filename, 'r') as f:
        line = f.readline()[:-1]
        while line:
            info_list = line.split('; ')
            class_name, super_class_name, attr_list = info_list[0],\
                                                      info_list[1],\
                                                      info_list[2]
            attr_list = attr_list.split(', ')
            PyClass = PythonClass(class_name, super_class_name, attr_list)
            PythonClass_list.append(PyClass)
            line = f.readline()[:-1]
            
    f.close()
    
    return PythonClass_list

test = ReadPythonClass('class_info.csv')
'''
for clss in test:
    print(clss)
    print()
'''

def WritePythonClass(filename, PythonClass_list):
    
    result = ''

    for clss in PythonClass_list:

        # CLASS DECLARATION
        define = 'class {}({}):\n'.format(clss.get_class_name(), clss.get_super_class_name())

        # INITIALIZER
        init = '{:>4}'.format(' ') + 'def __init__(self'
        for attr in clss.get_attr_list():
            init += ', {}'.format(str(attr))
        init += '):\n'
        for attr in clss.get_attr_list():
            init += '{:>8}'.format(' ') + 'self._{a} = {a}'.format(a = attr) + '\n'
        init += '\n'
        result += define + init

        # MUTATOR FUNCTIONS
        mutators = ''
        for attr in clss.get_attr_list():
            mutators += '{:>4}'.format(' ') + 'def set_{a}(self, new_{a}):\n'\
                        .format(a = attr)
            mutators += '{:>8}'.format(' ') + 'self._{a} = {b}'\
                        .format(a = attr, b = 'new_{}'.format(attr)) + '\n'
            mutators += '\n'
        result += mutators

        # ACCESSOR FUNCTIONS
        accessors = ''
        for attr in clss.get_attr_list():
            accessors += '{:>4}'.format(' ') + 'def get_{a}(self, new_{a}):\n'\
                        .format(a = attr)
            accessors += '{:>8}'.format(' ') + 'return {}'\
                        .format(attr)+ '\n'
            accessors += '\n'
        result += accessors
 
    with open(filename, 'w') as f:
        f.write(result)
    
WritePythonClass("python_oop.py",test)





    
