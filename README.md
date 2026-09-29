# SECURETEXT: Caesar Cipher

A simple Python-based project that implements **Caesar Cipher Encryption and Decryption** using string manipulation, loops, functions, and modular arithmetic.

## 1. Project Overview

The Caesar Cipher is a basic encryption technique in which each letter in a message is shifted by a fixed number of positions in the alphabet.

For example, with a shift value of `3`:

```text
HELLO → KHOOR
```

The project allows the user to:

* Encrypt a message
* Decrypt an encrypted message
* Choose a custom shift value
* Preserve spaces, numbers, and special characters
* Continue using the program until the user chooses to exit

## 2. Technologies Used

* **Programming Language:** Python 3
* **Concepts Used:**

  * Strings
  * Loops
  * Conditional statements
  * Functions
  * `ord()` and `chr()`
  * Modular arithmetic
  * User input

## 3. Requirements

Before running the project, make sure Python 3 is installed on your computer.

No external Python libraries or packages are required.

## 4. Check Python Installation

Open a terminal or command prompt and run:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

You should see a Python 3 version such as:

```text
Python 3.x.x
```

## 5. Download or Clone the Repository

Clone the repository using:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Then move into the project folder:

```bash
cd <PROJECT_FOLDER_NAME>
```

You can also download the repository as a ZIP file from GitHub and extract it.

## 6. Project Structure

The repository should contain the following files:

```text
SECURETEXT-Caesar-Cipher/
│
├── README.md
└── caesar_cipher.py
```

## 7. Run the Project

Open the project folder in a terminal.

Run the Python program using:

```bash
python caesar_cipher.py
```

If your system uses `python3`, run:

```bash
python3 caesar_cipher.py
```

## 8. Using the Program

After running the program, a menu will appear:

```text
===== CAESAR CIPHER =====
1. Encrypt
2. Decrypt
3. Exit
```

### To Encrypt

1. Enter `1`.
2. Enter the message you want to encrypt.
3. Enter the shift value.
4. The program will display the encrypted message.

Example:

```text
Enter your choice: 1
Enter message: Hello World
Enter shift value: 3

Encrypted message: Khoor Zruog
```

### To Decrypt

1. Enter `2`.
2. Enter the encrypted message.
3. Enter the same shift value used during encryption.
4. The program will display the original message.

Example:

```text
Enter your choice: 2
Enter encrypted message: Khoor Zruog
Enter shift value: 3

Decrypted message: Hello World
```

### To Exit

Enter:

```text
3
```

The program will terminate.

## 9. How the Program Works

The program processes each character of the input message one by one.

For encryption:

```text
New Position = (Current Position + Shift) % 26
```

For decryption:

```text
New Position = (Current Position - Shift) % 26
```

The `ord()` function is used to convert characters into numerical values, while `chr()` converts the numerical value back into a character.

The modulo operator `% 26` makes sure that the alphabet wraps around after `Z`.

For example:

```text
Z + 3 → C
```

Spaces, numbers, and special characters are kept unchanged.

## 10. Configuration

The project does not require any configuration files, API keys, environment variables, or external services.

The shift value is entered by the user when the program is running.

## 11. Dependencies

There are no external dependencies.

The project uses only Python's built-in functionality, so commands such as:

```bash
pip install ...
```

are not required.

## 12. Limitations

The Caesar Cipher is a simple educational encryption technique and should not be considered secure for protecting sensitive or confidential information.

Because the number of possible shifts is small, the encrypted message can be easily decoded using trial and error.

## 13. Future Improvements

Possible improvements include:

* Adding a graphical user interface (GUI)
* Adding file encryption and decryption
* Adding stronger encryption algorithms
* Adding automatic shift detection
* Adding a history of encrypted and decrypted messages

## 14. Author

**Chandan Yadav**

**Registration No.: 26BCE11351**

**Course:** CSE1021 — Introduction to Problem Solving and Programming

**Faculty:** Professor R Senthilkumar

**Designation:** Senior Associate Professor
