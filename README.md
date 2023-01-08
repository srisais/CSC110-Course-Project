# CSC110 Course Project (Ontario High School Course Enrollment Tracker)
This project allows you to view the course enrollment of all Ontario (Canada) High School Courses throughout the years (provided the data exists).

For each course, you can view how the number of enrollments have fluctuated throughout the years. During the COVID-19 pandemic, the enrollment of many courses drastically changed - this tracker allows you to see a visual representation of how much the enrollment has changed, allowing one to come up with hypotheses, as to whether or not the COVID-19 pandemic impacted enrollment.

This project has been thoroughly documented and neatly coded so that if anyone would like to fork this project and build upon it, they would have an easier time.

## Database Files
This folder contains all the database files, courtesy of the [Open Government](open.canada.ca) Database.

Included are both `.txt` files and `.xlsx` files. This project uses the `.txt` files to extract the data from.

### Database Files Formatting
The `.txt` files are used as they are formatted as `CSV` files, with the delimeter being `|`, rather than a comma (`,`), making it faster to extract data from them, as opposed to using the `.xlsx` files

Each `.txt` file contains the following headers row: `Course Code|Course Description|Grade|Pathway or Destination|Enrolment`. Using this, we extract the data from each row, creating objects for each course, and so on. This can be seen further in the Program Files. 

## Phase 1
Phase 1 includes all of the relavant project proposal information (mainly the `.tex` file of the proposal, its compiled `.pdf` document, and some sample database data files).

## Program Files
This is where the heart of the project lives. Using this folder alone, you can run the entire program.

Be sure you read the `requirements.txt` file (or let your IDE do the work) to ensure that all the required modules are installed.

(This folder also includes a copy of a selection from the database files, in the folder called `database_files` - if you would like you choose different database files to analyze, you can replase the files within `database_files` to analyze those newer files. Please ensure that you put `.txt.` files, as the program is not equipped to handle analyzing `.xlsx` files -- the program will not read files that are not `.txt` files.)

### `command_line_interface.py`
This file includes all of the functions necessary to run the command line interface of the program. If run directly, this will use `PythonTA` and run the tests, as specified in the project instructions.

### `functions_and_classes.py`
INcluding all of the major classes and core functions to analyze the data, this file contains everything from the objects that represent the courses, to the creation of the graph objects that allow you to visualize the course enrollment. If run directly, this will use `PythonTA` and run the tests, as specified in the project instructions.

### `main.py`
**THIS IS THE FILE TO RUN IF YOU WANT TO RUN THE ENTIRE PROGRAM.** This file is very short, but it wraps everything together, pulling from `command_line_interface.py` and `functions_and_classes.py`, and running the main program.

### `requirements.txt`
This `.txt.` file lists the required modules needed to run the program, as formatted in the standard Python format.

## Scrap Files
If you'd like to get a small glimpse into the debugging and development of the project, this folder just includes a few scrap files that were found to be helpful to keep on hand while developing the project. They are not really of any significance to the final project, but some might find it interesting, so they are still here.

## Written Report
This folder includes the `.tex` file and the compiled `.pdf` file of the project's written report (as well as some auxillary files)
