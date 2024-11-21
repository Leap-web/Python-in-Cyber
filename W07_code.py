print("\nExercise 1")
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        try:
            with open(self.filename, 'x'):
                print(f"File {self.filename} created successfully")
        except FileExistsError:
            print(f"File {self.filename} already exists.")
        finally:
            print("File creation process completed.")

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                print(f"\nFile Content:")
                print(file.read())
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        finally:
            print(f"File '{self.filename}' read successfully.")
            print("Read operation completed.")

    def write_file(self, items):
        try:
            with open(self.filename, 'w') as file:
                for item in items:
                    file.write(f"{item}\n")
                print(f"\nData written successfully to {self.filename}.")  
        except Exception as e:
            print(e)
        finally:
            print("Write operation completed.")


filename = r"C:\/Users\/USER\/Desktop\/CyberSecurity T1\/Python Cys\/week7\/W07_text.txt"
manager = FileManager(filename) 

manager.create_file()
items = input("Enter items separated by commas: ").split(',')
manager.write_file([item.strip() for item in items])
manager.read_file()

print("\nExercise 2")
class FileUpdater(FileManager):
    def __init__(self, filename):
        super().__init__(filename)

    def read_file(self):
        try:
            file_items = {}
            with open(self.filename, 'r') as file:
                for index, line in enumerate(file, start=1):
                    item = line.strip()
                    file_items[index] = item
            print(f"Current Data: {file_items}")
        except FileNotFoundError as k:
            print(k)
        except ValueError as v:
            print(v)

    def update_file(self):
        action = input("Choose an action (add, update, delete): ")

        if action == 'add':
            new_item = input("Enter a new item: ")
            with open(self.filename, 'a') as file:  
                file.write(f"{new_item}\n")
            print(f"File '{self.filename}' updated successfully.")

        elif action == 'update':
            self.read_file()
            index = int(input("Enter the ID to update value: "))
            new_item = input("Enter the new value: ")
            try:
                with open(self.filename, 'r') as file:
                    lines = file.readlines()
                lines[index - 1] = f"{new_item}\n"
                with open(self.filename, 'w') as file:
                    file.writelines(lines)
                print(f"File '{self.filename}' updated successfully.")
                print("Update operation completed.")
            except IndexError as f:
                print(f)
                
        elif action == 'delete':
            self.read_file()
            index = int(input("Enter the ID to delete value: "))
            try:
                with open(self.filename, 'r') as file:
                    lines = file.readlines()
                del lines[index - 1]
                with open(self.filename, 'w') as file:
                    file.writelines(lines)
                print(f"File '{self.filename}' updated successfully.")
            except IndexError as f:
                print(f)
        else:
            print("Invalid action")

filename = r"C:\/Users\/USER\/Desktop\/CyberSecurity T1\/Python Cys\/week7\/W07_text.txt"
updater = FileUpdater(filename) 

updater.read_file()
updater.update_file()
manager.read_file()
