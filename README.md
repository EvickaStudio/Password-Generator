# Password Generator`

This is a simple password generator application built using Python and PyQt6. It generates secure passwords using two methods: `/dev/urandom | base64` and `/dev/random | xxd -p.`

## Requirements

- Linux operating system
- Python 3.x
- PyQt6

## Installation

1. Clone the repository: `git clone https://github.com/EvickaStudio/Password-Generator.git`
2. Navigate to the project directory: `cd Password-Generator`
3. Install PyQT6: `pip install PyQt6` or `pipx install PyQt6` on arch `sudo pacman -S python-pyqt6`
4. Run the application: `python3 main.py`

## Usage

1. Select a method for generating the password from the dropdown menu.
2. Use the slider to set the length of the password.
3. Click on the "Generate Password" button to generate a new password.
4. The generated password will be displayed in the text field.

## Screenshots

![Screenshot](https://raw.githubusercontent.com/EvickaStudio/Password-Generator/main/screenshots/Password%20Generator.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
