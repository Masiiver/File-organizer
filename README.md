File Organizer 🗂️

This Python script organizes files in a given directory based on their type and optionally by year. It categorizes files into predefined folders such as Images, Documents, Videos, Audios, 3D Models, and Others, using their file extensions.

How It Works

The script first checks if the directory exists.

It creates necessary folders for different file types if they don’t already exist.

It scans all files (including those in subdirectories) and moves them to the appropriate folder.

If the year-based organization option is enabled, files are further sorted into subfolders based on the year they were last modified.

Files that don’t match predefined types are moved to an Others folder.

Errors, such as permission issues, are handled gracefully to prevent interruptions.

Key Features

✅ Categorizes files based on their extensions.
✅ Supports year-based organization if the user chooses.
✅ Handles subdirectories, ensuring all files in the target directory are organized.
✅ Error handling for permission issues.

This script is useful for keeping downloads, project files, or any cluttered directories well-organized with minimal effort. 🚀
