import glob as g
import os

""" for things like sorting, deleting, copying files, and dealing with directories """

class FileSorting:

    def __init__(self, directory: str = ..., filetype: str = ...):
        """Clas object for filtering and sorting files in a specific directory

        Args:
            directory (str, optional): target directory. Defaults to ....
            filetype (str, optional): target filetype. Defaults to ....
        """
        self.directory = directory
        self.directory_list = os.listdir(self.directory)
        self.filetype = filetype

    def delete_filetype(folder: str = ..., *filetypes: str):
        """Deletes files of specific type

        Args:
            folder (str, optional): target directory. Defaults to ....
        """
        directory = os.listdir(folder)
        removed = []
        for file in directory:
            file = os.path.join(folder, file)
            if file.split(".")[-1] in filetypes:
                removed.append(file)
                os.remove(file)

    @classmethod
    def filter(cls, directory: str = None, filetype: str = ..., **kwargs):
        """Filters target directory based on filetype

        Args:
            directory (str, optional): target directory. Defaults to None.
            filetype (str, optional): target filetype. Defaults to ....

        Returns:
            _type_: _description_
        """
        if directory is None:
            directory = cls.directory

        return g.glob(os.path.join(directory, filetype), **kwargs)


class Directories:

    def mkdir(*paths: str, display: bool = False):
        """Makes directory if it does not exist

        Args:
            paths (list): enter enter each individual arguments for each path (i.e., "path1", "path1", etc.)
            display (bool, optional): option to print its creation in terminal. Defaults to False.
        """

        for path in paths:
            if not os.path.exists(path):
                os.mkdir(path)
                if display:
                    print(f'Directory created {path}')

    def generate_unique_name(
        filename: str = ...,
        path: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), # CWD
        copy_pattern: str = 'Run '
        ):
        """Static function for producing updating enumeration of consecutive log files

		Args:
			filename (str): original name of file. Defaults to ...
			path (str, optional): defualt directory for saving log files. Defaults to os.path.dirname(os.path.dirname(os.path.abspath(__file__))).
			copy_pattern (str): appended pattern. Defaults to "Run"

		Returns:
			str: filename with unique number identifier appended to original filename
		"""
        # FIXME - fix rest argument for path
        base_name, ext = os.path.splitext(filename)
        unique_name, counter = filename, 1
        while os.path.exists(os.path.join(path, unique_name)):
            counter += 1
            unique_name = f'{base_name} ({copy_pattern}{counter}){ext}'

        return unique_name, counter


class FileFetching:

    def fetch_all_files(parent_folder: str):
        # returns a list of all files that are part of directory
        target_files = []
        for path, subdirs, files in os.walk(parent_folder):
            for name in files:
                target_files.append(os.path.join(path, name))
        return target_files
