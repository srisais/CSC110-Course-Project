"""CSC110 Course Project - Billy Guo and Sridhar Sairam

functions.py

Module Description
==================
This file contains the functions required to parse database files and assist
in converting them into usable data. These functions will
import, sanitize, and sort the data in accordance with how the
dataclasses and other required structures are defined.

TODO: Fix line lengths and other PEP8 formatting issues
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
        list[str, str, str, str, int]:
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

    n_en = int(num_enrolments)

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
        n_en
    ]


def get_school_year_from_file_path(file_path: str) -> tuple[int, int]:
    """Extracts and returns a tuple of the start and end year of the
    current text file using the file path

    Preconditions:
    - The file name is preceeded either by '/' or '\'
    - The file title beginning follows the following format:
        f"mdc_enrol_{XXYY}"

    >>> get_school_year_from_file_path("mdc_enrol_1314_en_supp_2")
    (2013, 2014)
    >>> path_1 = "C:\\Bob\\mdc_enrol_1516_en_supp.txt"
    >>> get_school_year_from_file_path(path_1)
    (2015, 2016)
    >>> path_2 = "/System/Potato/mdc_enrol_1819_en_supp.txt"
    >>> get_school_year_from_file_path(path_2)
    (2018, 2019)
    """
    # Example file title: "mdc_enrol_1314_en_supp_2"
    text_file_title = ""
    for i in range(-1, -len(file_path) - 1, -1):  # Goes from last to first char
        if file_path[i] == '\\' or file_path[i] == '/':
            # Remember, i is a negative index
            text_file_title = file_path[i + 1:]
            break
    else:
        text_file_title = file_path

    default_century = 2000
    year_nums = text_file_title[10:14]  # Ex: "1213"
    start_year = default_century + int(year_nums[0:2])
    end_year = default_century + int(year_nums[2:])

    return (start_year, end_year)


def get_school_year_all_course_enrollments(file_path: str) -> SchoolYearAllCourseEnrollments:
    """Gets the data from a text file (part of the database)
    and formats it and returns a SchoolYearAllCourseEnrollments
    for that text file's respective year

    TODO: Add doctests for this function
    >>>
    """

    text_file_lines = get_text_file(file_path)[1:]  # Excluding the first line (of table headers)
    text_file_list = []

    for line in text_file_lines:
        text_file_list.append(
            format_line_list_elements(
                split_line_into_list(line)
            )
        )

    start_year, end_year = get_school_year_from_file_path(file_path)

    course_enrollment_list = []

    for course in text_file_list:
        cur_course = Course(
            *course[0:4]  # The * unpacks the list
        )

        cur_course_enrollment = CourseEnrollment(
            cur_course, course[4], start_year, end_year  # I'm not sure why Pycharm thinks course[4] is a str, rather than an int
        )

        course_enrollment_list.append(
            cur_course_enrollment
        )

    return SchoolYearAllCourseEnrollments(
        start_year,
        end_year,
        course_enrollment_list
    )


def get_course_enrollment_history_for_all_courses(list_of_file_paths: list[str]) -> list[CourseEnrollmentHistory]:
    """Returns a massive list of CourseEnrollmentHistory objects, one per course

    TODO: test this function? or add doctests... ? see if it works properly, somehow
    """

    course_enrollment_history_for_all_courses_list = []
    course_enrollment_history_for_all_courses_dict = {}
    school_year_all_course_enrollments_list = []

    for file_path in list_of_file_paths:
        school_year_all_course_enrollments_list.append(
            get_school_year_all_course_enrollments(file_path)
        )

    # Fills up the dict with the keys being Course objects
    # and the values being lists of CourseEnrollment objects
    for school_year in school_year_all_course_enrollments_list:
        for course_enrollment in school_year.list_of_course_enrollments:
            if course_enrollment.course not in course_enrollment_history_for_all_courses_dict:
                course_enrollment_history_for_all_courses_dict[course_enrollment.course] = []
            course_enrollment_history_for_all_courses_dict[course_enrollment.course].append(
                course_enrollment
            )

    for course, course_enrollment_history in course_enrollment_history_for_all_courses_dict.items():
        course_enrollment_history_for_all_courses_list.append(
            CourseEnrollmentHistory(
                course,
                course_enrollment_history
            )
        )

    return course_enrollment_history_for_all_courses_list








