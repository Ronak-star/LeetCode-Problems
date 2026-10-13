class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder_set = set(folder)
        result = []
        for f in folder:
            is_subfolder = False

            path = []
            for part in f.split('/')[1:]:
                path.append(part)
                parent_path = "/" + "/".join(path[:-1])
                if len(path) > 1 and parent_path in folder_set:
                    is_subfolder = True
                    break
                
            if not is_subfolder:
                result.append(f)

        return result