"""CSC110 Course Project - Billy Guo and Sridhar Sairam

functions_and_classes.py

Module Description
==================
This file contains the functions required to parse database files and assist
in converting them into usable data. These functions will
import, sanitize, and sort the data in accordance with how the
dataclasses and other required structures are defined.

This module also contains all of the datatypes that will be used,
enabling the data to be easily manipulate and analyzed.

NOTES:
    - "enrollment" vs "enrolment"
      I will be spelling the word "enrollment" (with 2 'l's).

TODO: Fix line lengths and other PEP8 formatting issues
TODO: make a function that gets all of the txt files from a given folder path
TODO: add a search function for courses? (based on the courses in Course.master_course_object_list)
TODO: Figure out how pathlib.Path works, and change the functions so that they work using these paths.
    This should allow cross-platform compatability with ease.
    https://docs.python.org/3/library/pathlib.html
TODO: Write representation invariants as Python code
"""
from pathlib import Path

###############################################################################
# Classes
###############################################################################
class Course:
    """This class regarding the datatype that represents the data
    for an Ontario Secondary School Course

    *** IMPORTANT ***
    Course.get_course_object should be used when "creating" a new Course object.
    This is to prevent creating multiple <Course> objects for the same course.

    This class includes relevant methods for using Course objects.

    Class Attributes:
        - master_course_object_list: A master list of all <Course> objects.
            This is to prevent creating duplicate <Course> objects that are
            essentially equal. Using this list and the proper class method
            to create <Course> objects, aliases can be created to make checking
            for equality betweeen two courses easier.

    Instance Attributes:
        - code: The course code given by the Ministry of Education.
        - title: The course title given by the Minstry of Education.
        - grade_or_level: The grade/level of the given course.
        - pathway_or_destination: The suggestd pathway/destination the student
            should be striving for if they take this course.

    >>> # Example Course object
    >>> c = Course(code="TKQ4T",\
                   title="Healthy Cooking Made Easy",\
                   grade_or_level="Grade 12",\
                   pathway_or_destination="College Delivered (Dual Credits)")
    >>> # NOTE: use get_course_object to create a Course object (to reduce redundant Course objects)
    """
    master_course_object_list: list["Course"] = []

    code: str
    title: str
    grade_or_level: str
    pathway_or_destination: str

    def __init__(self, code: str, title: str, grade_or_level: str, pathway_or_destination: str) -> None:
        """Initializes a Course object with the given inputs."""
        self.code = code
        self.title = title  # sometimes referred to course_description
        self.grade_or_level = grade_or_level  # Ex: "Grade 9" or "Level 2"
        self.pathway_or_destination = pathway_or_destination

    def __str__(self) -> str:
        """Returns a string summarizing the object's contents"""
        return f"{self.code}: {self.title} - {self.grade_or_level} ({self.pathway_or_destination})"

    @classmethod
    def get_course_object(cls, *args) -> "Course":  # -> Course:
        """Returns a Course object, making a new one only if the course
        is not in Course.MASTER_COURSE_OBJECT_LIST
        """
        temp_obj = Course(*args)

        for co in cls.master_course_object_list:
            if vars(co) == vars(temp_obj):
                return co
        else:
            Course.master_course_object_list.append(temp_obj)
            return temp_obj

        # This will delete temp_obj's object if it's address
        # has not been returned.


class CourseEnrollment:
    """A class regarding the data type that represents the data for
    a specific Course object and the number of students enrolled
    in that course for a specific school year.

    This class includes relevant methods for using CourseEnrollment objects.

    Instance Attributes:
        - course: A <Course> object.
        - num_enrollments: The number of enrollments for <course>
            in this school year.
        - start_year: The start year of the school year (ex: 2005)
        - end_year: The end year of the school year (ex: 2006)
        - school_year_str: A string representation of the school year
            (ex: "2005 - 2006")

    Representation Invariants:
        - start_year + 1 == end_year
        - num_enrollments >= 0

    >>> c = Course.get_course_object(\
        code="TKQ4T",\
        title="Healthy Cooking Made Easy",\
        grade_or_level="Grade 12",\
        pathway_or_destination="College Delivered (Dual Credits)"\
    )
    >>> # Example CourseEnrollment object
    >>> d = CourseEnrollment(course=c, num_enrollments=11, start_year=2011, end_year=2012)
    """
    course: Course
    num_enrollments: int
    start_year: int
    end_year: int
    school_year_str: str

    def __init__(self, course: Course, num_enrollments: int, start_year: int, end_year: int) -> None:
        """Initializes a CourseEnrollment object with the inputted
        <course>, <num_enrollments>, <start_year>, and <end_year> objects.
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


class SchoolYearAllCourseEnrollments:
    """A class regarding the data type that represents a specific school year
    and all of the courses offered in that school year
    with their enrollment numbers

    This class includes relevant methods for using SchoolYearAllCourseEnrollments objects.

    Instance Attributes:
        - start_year: The start year of the school year (ex: 2005)
        - end_year: The end year of the school year (ex: 2006)
        - school_year_str: A string representation of the school year
            (ex: "2005 - 2006")
        - list_of_course_enrollments: A list of all <CourseEnrollment> objects
            for all the courses taken in the current school year with
            start year of <start_year> and end year of <end_year>.

    Representation Invariants:
        - start_year + 1 == end_year

    >>> c1 = Course.get_course_object(\
        code="TKQ4T",\
        title="Healthy Cooking Made Easy",\
        grade_or_level="Grade 12",\
        pathway_or_destination="College Delivered (Dual Credits)"\
    )
    >>> d1 = CourseEnrollment(course=c1, num_enrollments=11, start_year=2011, end_year=2012)
    >>> c2 = Course.get_course_object(\
        code="MCV4U",\
        title="Calculus and Vectors",\
        grade_or_level="Grade 12",\
        pathway_or_destination=\
        "University Preparation (Grade 11 & 12 level)"\
    )
    >>> d2 = CourseEnrollment(course=c2, num_enrollments=38630, start_year=2011, end_year=2012)
    >>> # Example SchoolYearCourseEnrollments object
    >>> s = SchoolYearAllCourseEnrollments(start_year=2012,\
                              end_year=2013,\
                              list_of_course_enrollments=[d1, d2])
    >>> # This is example list for list_of_courses with only 2 elements.
    >>> # A typical list of list_of_courses will have ~1500 elements.
    """
    start_year: int
    end_year: int
    school_year_str: str
    list_of_course_enrollments: list[CourseEnrollment]

    def __init__(self, start_year: int, end_year: int, list_of_course_enrollments: list[CourseEnrollment]) -> None:
        """Initializes a SchoolYearCourseEnrollments object with the inputted
        <start_year>, <end_year>, and <list_of_course_enrollments>.
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


class CourseEnrollmentHistory:
    """A class regarding the data type that represents the same course and
    its enrolment data over a number of school years

    This class includes methods for utilizing CourseEnrollmentHistory objects.

    Instance Attributes:
        - course: A course object.
        - course_enrollment_list: A list of <CourseEnrollment> objects for
            <course>.

    Representation Invariants:
        - None of the CourseEnrollment objects in the list have the same school year
        - All of the CourseEnrollment objects in the list are of the same course

    >>> c = Course.get_course_object(\
        code="MCV4U",\
        title="Calculus and Vectors",\
        grade_or_level="Grade 12",\
        pathway_or_destination=\
        "University Preparation (Grade 11 & 12 level)"\
    )
    >>> d1 = CourseEnrollment(course=c, num_enrollments=38630, start_year=2012, end_year=2013)
    >>> d2 = CourseEnrollment(course=c, num_enrollments=38630, start_year=2011, end_year=2012)
    >>> # Example CourseEnrollmentHistory object
    >>> ceh = CourseEnrollmentHistory(c, [d1, d2])
    >>> # This list only has 2 CourseEnrollment objects;
    >>> # Typically, this list would have ~10 objects.
    """
    course: Course
    course_enrollment_list: list[CourseEnrollment]

    def __init__(self, course: Course, course_enrollment_list: list[CourseEnrollment]) -> None:
        """Initializes a CourseEnrollmentHistory object,
        with the inputted <course> and <course_enrollment_list> objects.
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
# Text File Data Extraction
###############################################################################

def split_line_into_list(line: str, delimiter: str = "|") -> list[str]:
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

    num_enrollments = line_list[4]
    num_enrollments = num_enrollments.replace(',', '')

    for i in range(len(num_enrollments)):
        if num_enrollments[i] == "<":
            num_enrollments = num_enrollments[0:i] + num_enrollments[i + 1:]
            # I probably don't need the num_enrollments[0:i], but
            # just in case something comes before '<' in the string...

            # This loop will just remove the first instance of '<'
            # from num_enrollments

            num_enrollments = int(num_enrollments) - 1
            break
    else:
        num_enrollments = int(num_enrollments)

    n_en = int(num_enrollments)

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
        cur_course = Course.get_course_object(
            *course[0:4]  # The * unpacks the list splice
        )

        cur_course_enrollment = CourseEnrollment(
            cur_course, int(course[4]), start_year, end_year
            # I'm not sure why Pycharm thinks course[4] is a str, rather than an int
            # I've just wrapped it in int() for redundancy...
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


def get_list_of_txt_file_paths_in_folder(folder_path: str) -> list[str]:
    """Returns a list of file paths to all .txt files within a given folder"""
    # I'm gonn
    pass

    # folder_contents = os.listdir(folder_path)
    # text_files = []
    #
    # for item in folder_contents:
    #     if item[-4:] == ".txt":
    #         text_files.append(item)

# def get_input_directory(type_of_path: str, path: str) -> Path:
#     """idk
#     type_of_path = "Windows" or "Unix" or something like that...
#
#
#     """


