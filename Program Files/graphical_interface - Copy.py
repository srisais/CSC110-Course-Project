from tkinter import *
from tkinter import ttk



class MainWindow:
    def __init__(self, root):

        root.title("CSC110 Course Project - Highschool Courses")

        self.data_source_folder = StringVar()

        # source_folder_label = ttk.Label(root, text="Enter the directory containing the database files:")
        source_folder_entry = ttk.Entry(root, textvariable=self.data_source_folder)
        source_folder_button = ttk.Button(root, text="Enter", command=self.get_course_listings)
        # courses_listbox = Listbox(root, height=25, width=50)
        # courses_scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=courses_listbox.yview)
        # open_course_graph_regression = ttk.Button(root, text="Open Enrollment Data/Polynomial Regression Graph")
        # open_course_graph_residuals = ttk.Button(root, text="Open Differences Graph")

        # courses_listbox['yscrollcommand'] = courses_listbox.configure(yscrollcommand=courses_scrollbar.set)

        # source_folder_label.grid(row=1, column=1, sticky=(N, E, W), pady=5, padx=5)
        source_folder_entry.grid(row=2, column=1, sticky=(N, E, S, W), pady=5, padx=5)
        source_folder_button.grid(row=2, column=2, sticky=(N, E, S, W), pady=5, padx=5)
        # courses_listbox.grid(row=3, column=1, sticky=(N, E, S, W), pady=5, padx=5)
        # courses_scrollbar.grid(row=3, column=2, sticky=(N, S, E), pady=5, padx=5)
        # open_course_graph_regression.grid(row=4, column=1, sticky=(N, S), pady=5, padx=5)
        # open_course_graph_residuals.grid(row=5, column=1, sticky=(N, S), pady=5, padx=5)

        # courses_listbox.get(courses_listbox.curselection()[0])

        # for i in range(1, 5 + 1):
        #     root.columnconfigure(i, weight=1)
        # for j in range(1, 2 + 1):
        #     root.rowconfigure(j, weight=1)
        #
        # for course in self.cur_course_listings:
        #     courses_listbox.insert("end", course)
        ################
        self.feet = StringVar()

        feet_entry = ttk.Entry(root, width=7, textvariable=self.feet)
        aa = ttk.Button(root, text="Calculate", command=self.calculate)

        feet_entry.grid(column=2, row=2)
        aa.grid(column=3, row=3, sticky=W)

    def calculate(self, *args):
        print(self.feet.get())

    def get_course_listings(self, *args):
        """Gets the course listings for the current directory."""
        print(f"the thing: '{self.data_source_folder.get()}'")



if __name__ == "__main__":
    root = Tk()
    MainWindow(root)
    root.mainloop()
