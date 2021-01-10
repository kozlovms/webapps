import statistics

groupmates = [
    {
        "name": "Алексей",
        "surname": "Сидоров",
        "exams": ["АиГ", "ИС", "КТП"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Петр",
        "surname": "Кузнецов",
        "exams": ["ИС", "ЭЭиС", "АиГ"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def input_avg_mark():
    avg_mark = 0
    while avg_mark < 1 or avg_mark > 5:
        try:
            avg_mark = int(input("Enter valid average mark: "))
        except Exception:
            pass
    return avg_mark

def formated_print(args):
    print('{:<15}{:<10}{:<30}{:<20}'.format(str(args[0]), str(args[1]), str(args[2]), str(args[3])))


def print_filtered_students(students):
    avg_mark = input_avg_mark()
    formated_print((u"Имя", u"Фамилия", u"Экзамены", u"Оценки"))
    for student in students:
        if statistics.mean(student['marks']) > avg_mark:
            formated_print(list(student.values()))
        
print_filtered_students(groupmates)