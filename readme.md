
# Password Generator and Manager

This Python application helps you securely generate and manage strong passwords for your online accounts.

Key Features:

Password Generation:
Creates strong passwords with a mix of letters, numbers, and symbols.
Allows for customization of password length and complexity.
Password Management:
Stores website credentials (website name, email/username, and password) in a secure text file.
Provides options to view, add, and delete saved credentials.
User-Friendly Interface:
Features a simple and intuitive graphical user interface (GUI) built with Tkinter.
Offers clear instructions and prompts for user interaction.
How it Works:

Password Generation:

The pass_gen.py module contains functions to generate random passwords based on user-defined criteria.
The generate_password() function constructs passwords using random selections from character sets.
Password Management:

The pass_manager.py module handles the GUI and password storage.
It allows users to:
Generate passwords using the generate_password_button.
Enter website credentials.
Save credentials to the passwords.txt file using the save() function.
View saved credentials (not implemented in the provided code).
To Use the Application:

Install the required libraries: pip install tk
Run the pass_manager.py script: python pass_manager.py
Security Considerations:

While this application provides a basic level of password management, it's essential to follow best practices for password security:
Use unique, strong passwords for each online account.
Consider using a password manager with advanced security features for more sensitive information.
Additional Notes:

The provided code includes a placeholder for a logo image (password-512.png). Ensure the image path is correct or remove the image feature.