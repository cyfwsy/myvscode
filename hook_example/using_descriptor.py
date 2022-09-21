from weakref import WeakKeyDictionary
class Grade:
    def __init__(self):
        self._value = WeakKeyDictionary()
    
    def __get__(self,instance,owener):
        if instance is None:
            return self
        return self._value.get(instance,0)
    
    def __set__(self,instance,value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value[instance] = value
        
class Exam:
    math_grade = Grade()  # descriptor
    writing_grade = Grade()
    science_grade = Grade()
    
exam1 = Exam()
exam2 = Exam()
print('exam1.math_grade >>>>',exam1.math_grade)
print('exam2.math_grade >>>>',exam2.math_grade)
exam1.math_grade = 70
exam2.math_grade = 100
print('exam1.math_grade >>>>',exam1.math_grade)
print('exam2.math_grade >>>>',exam2.math_grade)

exam1.science_grade = 90
print('exam1.math_grade,exam1.science_grade >>>>',exam1.math_grade,\
    exam1.science_grade)
exam2.science_grade = 120


    

    