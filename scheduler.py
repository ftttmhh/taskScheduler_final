import schedule
import time
import shutil

def backup_files(source_directory, backup_directory):
    try:
        shutil.copytree(source_directory, backup_directory)
        return "Backup completed successfully!"
    except Exception as e:
        return f"Error during backup: {e}"

def schedule_daily_backup(source_directory, backup_directory):
    # Schedule the backup task to run daily at 10:00 AM
    schedule.every().day.at("10:00").do(backup_files, source_directory, backup_directory)

    # Run the scheduler loop to execute tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

# Example usage:
if __name__ == "__main__":
    source_dir = input("Enter source directory path: ")
    backup_dir = input("Enter backup directory path: ")
    schedule_daily_backup(source_dir, backup_dir)
