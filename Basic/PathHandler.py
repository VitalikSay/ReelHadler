import os


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BasicPathHandler(metaclass=Singleton):
    def __init__(self):
        self._project_name = "reelhadler"
        self._games_result_data_folder = "Data"
        self._project_folder = ""
        self._FindProjectFolderPath()

    def GetResultDataFilePath(self, game_name: str, file_name: str, *inner_folders):
        self._FindProjectFolderPath()
        relative_folder_path = os.path.join(self._project_name, self._games_result_data_folder, game_name, *inner_folders)
        absolute_save_file_path = self._project_folder

        return os.path.join(self._ProcessRelativeFolderPath(relative_folder_path, absolute_save_file_path), file_name)

    def _FindProjectFolderPath(self):
        dir_path_prev, base_name_prev = os.path.split(os.getcwd())
        while True:
            if base_name_prev.lower() == self._project_name.lower():
                self._project_name = base_name_prev
                self._project_folder = dir_path_prev
                break
            else:
                dir_path_prev, base_name_prev = os.path.split(dir_path_prev)

    def _ProcessRelativeFolderPath(self, relative_folder_path: str, absolute_head_path: str):
        path, base = os.path.split(relative_folder_path)
        folders = []
        while base != "":
            folders.append(base)
            path, base = os.path.split(path)
        folders.reverse()

        for folder in folders:
            absolute_head_path = os.path.join(absolute_head_path, folder)
            if not os.path.exists(absolute_head_path):
                os.makedirs(absolute_head_path)
        return absolute_head_path


if __name__ == '__main__':
    path_hand = BasicPathHandler()
    print(path_hand.GetResultDataFilePath('BHF', 'my_file.xml', 'first', 'second'))