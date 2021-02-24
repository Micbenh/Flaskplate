import os 
import shutil
import time

#*Parent Site class template
#*1) get destination path
#*2) simple app template build
#*3) advanced app template build
#*4) add menu switch flow choice

#! fix files coping code
#? there is reusability of that piece of code, maybe replace with a function?

class TemplateBuild:
    """
    This class accepts a destination folder path and builds a flask
     project template according to user choices and needs
    """
    def __init__(self):
        self._destination = None
        
    def build_folders(self, dest_path):
        """
        A funnciton that builds base flask folders to faciliate with files 
        Args:
            dest_path (str): destination path of the folder that will hold the files
        """ 
        self._destination = dest_path
        global template_folder
        template_folder = os.path.join(dest_path, "templates")
        static_folder = os.path.join(dest_path, "static")
        global css_folder
        css_folder = os.path.join(static_folder, 'css' )
        images_folder = os.path.join(static_folder, 'images')
        try:
            os.makedirs(template_folder)
            os.makedirs(static_folder)
            os.makedirs(css_folder)
            os.makedirs(images_folder)
        except OSError:
            paths = [template_folder, static_folder, css_folder, images_folder]
            for path in paths:
                if os.path.exists(path):
                    pass

    def simple_temp_files_writer(self):
        """
        The function builds a basic app.py and a starter html file in templates
        Args:
            dest_path (str): destination path of the folder that will hold the files
        """
        #basic app.py file
        app_file = open(self._destination + "\\" + "app.py", mode="w")
        app_file.close()
        # copy html template from snippets to project folder
        shutil.copy("flaskplate\\snippets\\html\\layout.html", template_folder )
        shutil.copy("flaskplate\\snippets\\html\\home.html", template_folder )
        # create main.css file
        main_css_file = open(css_folder + "\\" + "main.css", mode="w")
        main_css_file.close()


    def advanced_temp_build(self):
        """
        The function builds a better more seperated flask app template then the simple_template
        (sperate files for routes, run, models, forms and more...)
        Args:
            dest_path (str): destination path of the folder that will hold the files
        """
        files_list = ["__init__.py", 'forms.py', 'routes.py', 'models.py', "run.py"]
        for File in files_list:
            creator = open(self._destination + "\\" + "{}".format(File), mode="w")
            creator.close()

        # copy html template from snippets to project folder
        shutil.copy("flaskplate\\snippets\\html\\layout.html", template_folder )
        shutil.copy("flaskplate\\snippets\\html\\home.html", template_folder )

        # create main.css file
        main_css_file = open(css_folder + "\\" + "main.css", mode="w")
        main_css_file.close()

    @staticmethod
    def options_menu():
        """ options menu beinng printed """

        print("Welcome to Flaskplate!")
        print("Please choose one of the following options")
        print("1) Build a simple app template.")
        print("2) Build an advanced app template.")
        print("3) Build another template in a diffrent destination. - STILL DOES NOT WORK!!")
        print("4) quit")


if __name__ == "__main__":
    tb = TemplateBuild()
    destination_folder = input("Select path to write files to. \n > ")
    tb.build_folders(destination_folder)
    print()

    run_menu = True

    while run_menu:
        tb.options_menu()
        choice = str(input("> "))
        if choice == '4':
            print("THANKS FOR USING FLASKPLATE!! \ngoodbye.")
            print()
            break

        #print("destination folder: {}".format(destination_folder))
        actions_switch = {
            "1": tb.simple_temp_files_writer,
            "2": tb.advanced_temp_build,

        }

        try:
            command_action = actions_switch[choice]
            print("destination folder: {}".format(destination_folder))
        except KeyError:
            print()
            print("This choice does not exist, please try again")
            time.sleep(0.5)
            print()
        else:
            command_action(destination_folder)
