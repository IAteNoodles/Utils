import pickle


class Classwork:
    def __init__(self):
        self.path = input("Enter path: ")
        pass

    def store_data(self):
        file_handle = open(self.path, "wb")  # Creates a file_handle and a file with the given filepath
        student_data = {1: ["Abhijit", 83],  # Creates a list containing the student's data
                        2: ["Sujal", 95],
                        3: ["Bhavesh", 69],
                        4: ["Grishe", 39]}
        pickle.dump(student_data, file_handle)
        file_handle.close()
        print('The Records are:\n{0}'.format(student_data), sep="")
        roll = int(input("Enter roll number: "))
        if roll not in student_data:
            print("No Such Records Found!!!")
        else:
            student_data[roll][1] = int(input("Enter marks: "))
            file_handle = open(self.path, "wb+")
            pickle.dump(student_data, file_handle)
            file_handle.close()

    def display_student_data(self):
        try:
            file_handle = open(self.path, "rb")
            student_data = pickle.load(file_handle)
            for student in student_data:
                print(student, ":", student_data[student])
        except EOFError and FileNotFoundError as e:
            print("Error Occurred")


if __name__ == "__main__":
    obj = Classwork()
    obj.store_data()
    obj.display_student_data()
