import matplotlib.pyplot as plt
import numpy
from functions_and_classes import *

a = 'C:\\Sridhar\\School\\University\\aaa Year 1 Courses\\aaa CSC110\\b Assignments\\CSC110-Course-Project\\Database Files\\Course enrolment in secondary schools\\English\\'
asdf = get_course_enrollment_history_for_all_courses_in_folder(a)
cur_course = get_course_enrollment_history_given_course_code(
    asdf, "SBI4U"
)

x_to_y = {
    year: cur_course.year_str_to_course_enrollment[year].num_enrollments
    for year in cur_course.year_str_to_course_enrollment.keys()
}



x = [int(i[:4]) for i in x_to_y.keys()]
y = [int(i) for i in x_to_y.values()]
mymodel = numpy.poly1d(numpy.polyfit(x[:-1], y[:-1], 8))
myline = numpy.linspace(min(x), max(x), 100)

# breakpoint()


plt.plot(
    myline,
    mymodel(myline),
    linewidth=5
)

plt.scatter(
    x,
    y
)
plt.plot(
    x,
    y,
    linewidth=0.5,
    label="Actual Course Enrollments"
)

plt.xlabel("School Year")
plt.ylabel("Number of Enrollments")
plt.title(cur_course.course.__str__())
plt.show()


if __name__ == "__main__":
    pass
    # main()

