import os 
import argparse
import shutil

# Parent Site class template
# 1) get destination path 
# 2) simple app template build 
# 3) advanced app template build

class Template_Build:
    def __init__(self, dest_path):
        self._dest_path = dest_path

    def build_folders(self):
        dest_path = os.path.join(self._dest_path)
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
        except:
            paths = [template_folder, static_folder, css_folder, images_folder]
            for path in paths:
                if os.path.exists(path):
                    pass 

    def simple_temp_files_writer(self):
        """
        The function builds a basic app.py and a starter html file in templates
        """ 
        dest_path = os.path.join(self._dest_path)
        #basic app.py file 
        app_file = open(dest_path + "\\" + "app.py", mode="w")
        app_file.close()
        # copy html template from snippets to project folder
        shutil.copy("flaskplate\\snippets\\layout.html", template_folder )
        # create main.css file
        main_css_file = open(css_folder + "\\" + "main.css", mode="w")
        main_css_file.close()


    def advanced_temp_build(self):
        """
        The function builds a better more seperated flask app template then the simple_template
        (sperate files for routes, run, models, forms and more...)
        """
            
        dest_path = os.path.join(self._dest_path)
        files_list = ["__init__.py", 'forms.py', 'routes.py', 'models.py', "run.py"]
        for File in files_list:
            creator = open(dest_path + "\\" + "{}".format(File), mode="w")
            creator.close()

        # copy html template from snippets to project folder
        shutil.copy("flaskplate\\snippets\\layout.html", template_folder )
        # create main.css file
        main_css_file = open(css_folder + "\\" + "main.css", mode="w")
        main_css_file.close()


if __name__ == "__main__":
    tb = Template_Build(r"C:\Users\t-mibenh\Desktop\studies\python\projects\flaskplate\test")
    tb.build_folders()
    tb.advanced_temp_build()