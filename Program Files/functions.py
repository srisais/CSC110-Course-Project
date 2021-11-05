"""CSC110 Course Project - Billy Guo and Sridhar Sairam

functions.py

Module Description
==================
This file contains the functions required to parse database files and assist
in converting them into usable data. These functions will
import, sanitize, and sort the data in accordance with how the
dataclasses and other required structures are defined.
"""

from data_types import *

###############################################################################
# Importing .txt files
###############################################################################
def get_text_file(file_path: str) -> list[str]:
    """Returns a list of strings of the entire text file,
    where each element of the list is a line from the text file,
    when given the input string file_path

    Preconditions:
        - file_path is a global file path to a .txt file that can be accessed
        - file_path[-4:] == ".txt"
    """

    file_lines = []

    with open(file_path, 'r') as cur_file:
        for cur_line in cur_file:
            # breakpoint()
            file_lines.append(cur_line)

    return file_lines


###############################################################################
# Parsing .txt files
###############################################################################

def split_line_into_list(line: str, delimiter: str="|") -> list[str]:
    """Splits a line from the .txt file into a list of string elements

    >>> line = "ATC1O|Dance|Grade 9|Open (Grade 9 - 12 level)|3508"
    >>> split_line_into_list(line)
    ['ATC1O', 'Dance', 'Grade 9', 'Open (Grade 9 - 12 level)', '3508']
    """

    line = line.strip()
    return line.split(delimiter)


def format_line_list_elements(line_list: list[str]) -> \
        list[str, str, int, str, int]:
    """Converts the elements of a list -- formatted like to the output
    of split_line_into_list -- to the required elements.
    (Does not mutate the original list)

    >>> line_1 = "ATC1O|Dance|Grade 9|Open (Grade 9 - 12 level)|3508"
    >>> line_1_list = split_line_into_list(line_1)
    >>> format_line_list_elements(line_1_list)
    ['ATC1O', 'Dance', 'Grade 9', 'Open (Grade 9 - 12 level)', 3508]

    >>> line_2 = "LYBBO|Arabic|Level 2|Open (Grade 9 - 12 level)|<10"
    >>> line_2_list = split_line_into_list(line_2)
    >>> format_line_list_elements(line_2_list)
    ['LYBBO', 'Arabic', 'Level 2', 'Open (Grade 9 - 12 level)', 9]
    """

    num_enrolments = line_list[4]

    for i in range(len(num_enrolments)):
        if num_enrolments[i] == "<":
            num_enrolments = num_enrolments[0:i] + num_enrolments[i + 1:]
            # I probably don't need the num_enrolments[0:i], but
            # just in case something comes before '<' in the string...

            # This loop will just remove the first instance of '<'
            # from num_enrolments

            num_enrolments = int(num_enrolments) - 1
            break
    else:
        num_enrolments = int(num_enrolments)

    # IMPORTANT NOTE ABOUT num_enrollments:
    # Since the dataset shows "<10" as the smallest values,
    # any values that show "<10" will be represented by 9.
    # As values all values in {1, 2, 3, 4, 5, 6, 7, 8, 9} satisfy <10,
    # an arbitrary value of 9 was chosen.

    return [
        line_list[0],
        line_list[1],
        line_list[2],
        line_list[3],
        num_enrolments
    ]


###############################################################################
# Creating dataclass Objects
###############################################################################

# Theses might be better as __init__ methods in their respective dataclasses...

def create_course_object(code: str, title: str, grade_or_level: str,\
                         pathway_or_destination: str) -> Course:
    """Creates and returns a Course object."""
    return Course(
        code=code,
        title=title,
        grade_or_level=grade_or_level,
        pathway_or_destination=pathway_or_destination
    )


def create_course_enrollment_object(course: Course, num_enrollments: int)\
    -> CourseEnrollment:
    """Creates and returns a CourseEnrollment object."""
    return CourseEnrollment(
        course=course,
        num_enrollments=num_enrollments
    )


def create_school_year_enrollments_object(start_year: int, end_year: int,
                                          list_of_course_enrollments:\
                                                  list[CourseEnrollment])\
        -> SchoolYearCourseEnrollments:
    """Creates and returns a SchooYearCourseEnrollment object."""
    return SchoolYearCourseEnrollments(
        start_year=start_year,
        end_year=end_year,
        list_of_course_enrollments=list_of_course_enrollments
    )

