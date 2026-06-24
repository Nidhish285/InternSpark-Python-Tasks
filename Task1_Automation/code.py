import os
import shutil
import csv

def setup_demo(target_dir, user_text):
    """Creates a custom directory and sample files based on user input."""
    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"[LOG] Created directory: {target_dir}")

        input_file = os.path.join(target_dir, 'sample.txt')
        csv_file = os.path.join(target_dir, 'data.csv')

        # 1. Writing custom user text to a Text File
        with open(input_file, 'w') as f:
            f.write(user_text)
        print(f"[LOG] Written user text to {input_file}")

        # 2. Writing to a CSV File
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Status'])
            writer.writerow([1, 'Task_A', 'Completed'])
            writer.writerow([2, 'Task_B', 'Pending'])
        print("[LOG] Sample CSV file created successfully.")
        
        return input_file, csv_file
    except Exception as e:
        print(f"[ERROR] Error during setup: {e}")
        return None, None

def automate_files(target_dir, input_file, csv_file):
    """Demonstrates reading, renaming, and moving files with custom error handling."""
    try:
        moved_file = os.path.join(target_dir, 'archived_sample.txt')

        # 3. Reading the text file
        print("\n--- Reading File ---")
        with open(input_file, 'r') as f:
            content = f.read()
            print(f"Content read successfully: '{content}'")

        # 4. Renaming/Moving a file (Automation)
        print("\n--- Automating File Operations ---")
        if os.path.exists(input_file):
            shutil.move(input_file, moved_file)
            print(f"Moved and Renamed '{input_file}' to '{moved_file}'")

        # 5. Reading from the CSV file
        print("\n--- Reading CSV Data ---")
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"Processing Row: {row['Name']} - {row['Status']}")

    except FileNotFoundError:
        print("[ERROR] The requested file was not found.")
    except PermissionError:
        print("[ERROR] You do not have permission to access these files.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    finally:
        print("\nFile operation sequence completed.")

# --- Execution with User Input Support ---
print("=== InternSpark Task 1: Automation & File Handling ===")
user_directory = input("Enter a name for your project directory (e.g., ./my_automation): ")
user_message = input("Enter some custom text to store inside the file: ")

file_path, csv_path = setup_demo(user_directory, user_message)

if file_path and csv_path:
    automate_files(user_directory, file_path, csv_path)
  
  # # Verification: List files in the demo directory
if 'user_directory' in locals() and os.path.exists(user_directory):
    print(f"Current files in {user_directory}:")
    print(os.listdir(user_directory))
else:
    print("[ERROR] Please run Cell 1 first to define the directory name.")
