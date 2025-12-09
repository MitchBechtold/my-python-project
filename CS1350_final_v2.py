#Mithel Bechtold Final Exam 
#Problem 1: File statistics 
def get_file_stats(filename):

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            line_count = len(lines)

            word_count = sum(len(line.split()) for line in lines)

            char_count = sum(len(line) for line in lines)

            return {
                'lines': line_count,
                'words': word_count,
                'characters': char_count
            }

    except FileNotFoundError:
        return None
    
#Test your function 
stats = get_file_stats("test.txt")
if stats: 
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['Characters']}")
    
#Problem 2: Student Class
class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_grade(self, grade):
        if 0 <= grade <=100:
            self.grades.append(grade)
            return True 
        return False 
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades) 
    def get_status(self): 
        if not self.grades:
            return "No grades"
        avg = self.calculate_average()
        if avg >= 70:
            return "Passing"
        else: 
            return "Failing"
        
#test your code
student = student("alice", "12345")
print(student.add_grade(85))
print(student.add_grade(92))
print(student.add_grade(150))
print(student.calculate_average())
print(student.get_status())

#Problem 3: Safe list Access 
def safe_get_element(my_list, index, default_value=None):
    try: 
        return my_list[index]
    except IndexError:
        return default_value
    except TypeError:
        return default_value
    except Exception: 
        return default_value
    
#test your function 
print(safe_get_element([1,2,3],1))
print(safe_get_element([1,2,3],10,-1))
print(safe_get_element("not list", 0, -1))

#Problem 4: Recurisve Power Function 
def recursive_power(x, n):
    if n == 0:
        return 1
    return x * recursive_power(x, n - 1)
#Test your function
print(recursive_power(2, 3))
print(recursive_power(5, 2))
print(recursive_power(10, 0))
print(recursive_power(3, 4))

