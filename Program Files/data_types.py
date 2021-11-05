"""CSC110 Course Project - Billy Guo and Sridhar Sairam

data_types.py

Module Description
==================
This module contains all of the datatypes that will be used,
enabling the data to be easily manipulate and analyzed.

NOTE: "enrollment" vs "enrolment"
      I will be spelling the word "enrollment" (with 2 'l's).
"""
from dataclasses import dataclass

,
@dataclass
class Course:
    """A data type that represents the data for
    an Ontario Secondary School Course

    >>> # Example Course object
    >>> c = Course(code="TKQ4T",\
                   title="Healthy Cooking Made Easy",\
                   grade_level=12,\
                   pathway_or_destination="College Delivered (Dual Credits)")
    """
    code: str
    title: str  # sometimes referred to course_description
    grade_or_level: str  # Ex: "Grade 9" or "Level 2"
    pathway_or_destination: str


@dataclass
class CourseEnrollment:
    """A data type that represents the data for
    a specific Course object and the number of students enrolled
    in that course

    >>> c = Course(code="TKQ4T",\
                   title="Healthy Cooking Made Easy",\
                   grade_level=12,\
                   pathway_or_destination="College Delivered (Dual Credits)")
    >>> # Example CourseEnrollment object
    >>> d = CourseEnrollment(course=c, num_enrollments=11)
    """
    course: Course
    num_enrollments: int
    # IMPORTANT NOTE ABOUT num_enrollments:
    # Since the dataset shows "<10" as the smallest values,
    # any values that show "<10" will be represented by 9.


@dataclass
class SchoolYearCourseEnrollments:
    """A data type that represents a specific school year
    and all of the courses offered in that school year
    with their enrollment numbers

    >>> c1 = Course(code="TKQ4T",\
                   title="Healthy Cooking Made Easy",\
                   grade_level=12,\
                   pathway_or_destination="College Delivered (Dual Credits)")
    >>> d1 = CourseEnrollment(course=c1, num_enrollments=11)
    >>> c2 = Course(code="MCV4U",\
                   title="Calculus and Vectors",\
                   grade_level=12,\
                   pathway_or_destination=\
                   "University Preparation (Grade 11 & 12 level)")
    >>> d2 = CourseEnrollment(course=c2, num_enrollments=38630)
    >>> # Example SchoolYearCourseEnrollments object
    >>> s = SchoolYearCourseEnrollments(start_year=2012,\
                              end_year=2013,\
                              list_of_courses=[d1, d2])
    >>> # This is example list for list_of_courses with only 2 elements.
    >>> # A typical list of list_of_courses will have ~1500 elements.
    """
    start_year: int
    end_year: int
    list_of_course_enrollments: list[CourseEnrollment]



@dataclass
class CourseEnrollment over the years?... {a better name}:
    """A data type """


# some data type that kinda is like this dict:
"""

{   <year>: <CourseEnrollment object>,
    ...
}


"""
