"""CSC110 Course Project - Billy Guo and Sridhar Sairam

data_types.py

Module Description
==================
This module contains all of the datatypes that will be used,
enabling the data to be easily manipulate and analyzed.

NOTES:
    - "enrollment" vs "enrolment"
      I will be spelling the word "enrollment" (with 2 'l's).
    - These classes are implemented as dataclasses as
      checking for equality will check their attributes,
      rather than their memory id.
      (I didn't want to mess with the __eq__ magic method)
      (I also didn't want to use the vars function, as I would need to
      remember to use it each time while checking object equality)
      (Unfortunately, this makes them unhashable)

TODO: add __str__ magic methods to the classes so debugging is much easier
      (have __str__ show all the object attributes or something)
TODO: Fix line lengths and other PEP8 formatting issues
"""
from dataclasses import dataclass

@dataclass
class Course:
    """This class regarding the datatype that represents the data
    for an Ontario Secondary School Course

    This class includes relevant methods for using Course objects.
    """
    def __init__(self, code: str, title: str, grade_or_level: str, pathway_or_destination: str) -> None:
        """Creates a Course object

        >>> # Example Course object
        >>> c = Course(code="TKQ4T",\
                       title="Healthy Cooking Made Easy",\
                       grade_or_level="Grade 12",\
                       pathway_or_destination="College Delivered (Dual Credits)")
        """

        self.code = code
        self.title = title  # sometimes referred to course_description
        self.grade_or_level = grade_or_level  # Ex: "Grade 9" or "Level 2"
        self.pathway_or_destination = pathway_or_destination

    def __str__(self) -> str:
        """Returns a string summarizing the object's contents"""
        return f"{self.code}: {self.title} - {self.grade_or_level} ({self.pathway_or_destination})"

@dataclass
class CourseEnrollment:
    """A class regarding the data type that represents the data for
    a specific Course object and the number of students enrolled
    in that course for a specific school year.

    This class includes relevant methods for using CourseEnrollment objects.
    """
    def __init__(self, course: Course, num_enrollments: int, start_year: int, end_year: int) -> None:
        """Creates a CourseEnrollment object.

        >>> c = Course(code="TKQ4T",\
                       title="Healthy Cooking Made Easy",\
                       grade_or_level="Grade 12",\
                       pathway_or_destination="College Delivered (Dual Credits)",)
        >>> # Example CourseEnrollment object
        >>> d = CourseEnrollment(course=c, num_enrollments=11, start_year=2011, end_year=2012)
        """
        self.course = course
        self.num_enrollments = num_enrollments
        # IMPORTANT NOTE ABOUT num_enrollments:
        # Since the dataset shows "<10" as the smallest values,
        # any values that show "<10" will be represented by 9.

        self.start_year = start_year
        self.end_year = end_year
        self.school_year_str = f"{self.start_year} - {self.end_year}"
    
    def __str__(self) -> str:
        """Returns a string summarizing the object's contents"""
        return self.course.__str__() + f" ||| [{self.school_year_str}]: {self.num_enrollments} enrollments"


@dataclass
class SchoolYearAllCourseEnrollments:
    """A class regarding the data type that represents a specific school year
    and all of the courses offered in that school year
    with their enrollment numbers

    This class includes relevant methods for using SchoolYearAllCourseEnrollments objects.
    """
    def __init__(self, start_year: int, end_year: int, list_of_course_enrollments: list[CourseEnrollment]) -> None:
        """Creates a SchoolYearCourseEnrollments object

        >>> c1 = Course(code="TKQ4T",\
                       title="Healthy Cooking Made Easy",\
                       grade_or_level="Grade 12",\
                       pathway_or_destination="College Delivered (Dual Credits)")
        >>> d1 = CourseEnrollment(course=c1, num_enrollments=11, start_year=2011, end_year=2012)
        >>> c2 = Course(code="MCV4U",\
                       title="Calculus and Vectors",\
                       grade_or_level="Grade 12",\
                       pathway_or_destination=\
                       "University Preparation (Grade 11 & 12 level)")
        >>> d2 = CourseEnrollment(course=c2, num_enrollments=38630, start_year=2011, end_year=2012)
        >>> # Example SchoolYearCourseEnrollments object
        >>> s = SchoolYearAllCourseEnrollments(start_year=2012,\
                                  end_year=2013,\
                                  list_of_course_enrollments=[d1, d2])
        >>> # This is example list for list_of_courses with only 2 elements.
        >>> # A typical list of list_of_courses will have ~1500 elements.
        """
        self.start_year = start_year
        self.end_year = end_year
        self.school_year_str = f"{self.start_year} - {self.end_year}"
        self.list_of_course_enrollments = list_of_course_enrollments

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        return f"[{self.school_year_str}]:" + "\n" + "\n".join(
            ['['] + [cur_course.__str__() for cur_course in self.list_of_course_enrollments] + [']']
        )


@dataclass
class CourseEnrollmentHistory:
    """A class regarding the data type that represents the same course and
    its enrolment data over a number of school years

    This class includes methods for utilizing CourseEnrollmentHistory objects.
    """
    def __init__(self, course: Course, course_enrollment_list: list[CourseEnrollment]) -> None:
        """Creates a CourseEnrollmentHistory object

        Preconditions:
            - None of the CourseEnrollment objects in the list have the same school year
            - All of the CourseEnrollment objects in the list are of the same course

        >>> c = Course(code="MCV4U",\
                       title="Calculus and Vectors",\
                       grade_or_level="Grade 12",\
                       pathway_or_destination=\
                       "University Preparation (Grade 11 & 12 level)")
        >>> d1 = CourseEnrollment(course=c, num_enrollments=38630, start_year=2012, end_year=2013)
        >>> d2 = CourseEnrollment(course=c, num_enrollments=38630, start_year=2011, end_year=2012)
        >>> # Example CourseEnrollmentHistory object
        >>> ceh = CourseEnrollmentHistory(c, [d1, d2])
        >>> # This list only has 2 CourseEnrollment objects;
        >>> # Typically, this list would have ~10 objects.
        """
        self.course = course
        self.year_str_to_course_enrollment = {
            course_enrollment.school_year_str: course_enrollment
            for course_enrollment in course_enrollment_list
        }

    def __str__(self) -> str:
        """Returns a representation of this object as a string"""
        return f"--- {self.course} ---" + "\n" + "\n".join(
            ['['] + [cur_course.__str__() for cur_course in self.year_str_to_course_enrollment.values()] + [']']
        )
