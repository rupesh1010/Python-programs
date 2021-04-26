class person: 
 def person_speak(self): 
 print("Person Speaking") 
#child class student inherits the base class person 
class student(person): 
 def student_speak(self): 
 print("Students Speaking") 
s = student() 
s.student_speak() 
s.person_speak()
