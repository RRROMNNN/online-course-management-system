from src.classes import Course, Student, Instructor


def main() -> None:
    course = Course(
        name="Основи Python",
        description="Базові типи даних, функції та ООП",
        duration_hours=40,
        status="Active",
    )

    student = Student(full_name="Шемигон Богдан", email="student@example.com")
    instructor = Instructor(full_name="Кузнецова Ю.А.", specialization="Програмування")

    print(course.get_course_info())
    print("Статус курсу:", course.get_status())

    student.enroll_course(course.name)
    print(student.get_student_info())

    course.update_status("Completed")
    print("Новий :", course.get_status())

    print(instructor.get_instructor_info())


if __name__ == "__main__":
    main()
