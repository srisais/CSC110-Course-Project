import matplotlib.pyplot as plt
from functions_and_classes import *

a = 'C:\\Sridhar\\School\\University\\aaa Year 1 Courses\\aaa CSC110\\b Assignments\\CSC110-Course-Project\\Database Files\\Course enrolment in secondary schools\\English\\'
asdf = get_course_enrollment_history_for_all_courses_in_folder(a)
cur_course = get_course_enrollment_history_given_course_code(
    asdf, "SPH4U"
)

x_to_y = {
    year: cur_course.year_str_to_course_enrollment[year].num_enrollments
    for year in cur_course.year_str_to_course_enrollment.keys()
}
plt.plot(
    x_to_y.keys(),
    x_to_y.values()
)

plt.xlabel("School Year")
plt.ylabel("Number of Enrollments")
plt.title(cur_course.course.__str__())
plt.show()


if __name__ == "__main__":
    pass
    # main()

