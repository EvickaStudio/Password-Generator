import subprocess
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QSlider,
    QHBoxLayout,
    QComboBox,
)
from PyQt6.QtCore import Qt


class PasswordGeneratorApp(QWidget):
    """
    A PyQt6 application for generating secure passwords.

    Attributes:
        method_combo (QComboBox): A combo box for selecting the password generation method.
        password_label (QLabel): A label for displaying the generated password.
        password_field (QLineEdit): A text field for displaying the generated password.
        length_slider (QSlider): A slider for selecting the length of the generated password.
        length_label (QLabel): A label for displaying the length of the generated password.
        generate_button (QPushButton): A button for generating a new password.
    """

    def __init__(self):
        """
        Initializes the PasswordGeneratorApp.
        """
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface for the PasswordGeneratorApp.
        """
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        self.method_combo = QComboBox()
        self.method_combo.addItem("head -c () /dev/urandom | base64")
        self.method_combo.addItem("head -c () /dev/random | xxd -p")

        self.password_label = QLabel("Generated Password:")
        self.password_field = QLineEdit()
        self.password_field.setReadOnly(True)

        self.length_slider = QSlider(Qt.Orientation.Horizontal)
        self.length_slider.setMinimum(4)
        self.length_slider.setMaximum(64)  # Adjust the maximum length as needed
        self.length_slider.setValue(16)
        self.length_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.length_slider.setTickInterval(4)
        self.length_slider.valueChanged.connect(self.update_length_label)

        self.length_label = QLabel(str(self.length_slider.value()))

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)

        layout.addWidget(self.method_combo)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_field)

        length_layout = QHBoxLayout()
        length_layout.addWidget(QLabel("Password Length:"))
        length_layout.addWidget(self.length_slider)
        length_layout.addWidget(self.length_label)

        layout.addLayout(length_layout)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def update_length_label(self, value):
        """
        Updates the length label with the current value of the length slider.

        Args:
            value (int): The current value of the length slider.
        """
        self.length_label.setText(str(value))

    def generate_password(self):
        """
        Generates a new password using the selected method and updates the password field.
        """
        selected_method = self.method_combo.currentText()

        if selected_method == "head -c () /dev/urandom | base64":
            password = self.generate_secure_password(self.length_slider.value())
        else:
            password = self.generate_number_password(self.length_slider.value())

        self.password_field.setText(password)

    def generate_secure_password(self, length):
        """
        Generates a new secure password using /dev/urandom and base64.

        Args:
            length (int): The length of the password to generate.

        Returns:
            str: The generated password.
        """
        command = ["head", "-c", str(length), "/dev/urandom", "|", "base64"]
        return self._extracted_from_generate_number_password_3(command)

    def generate_number_password(self, length):
        """
        Generates a new password using /dev/random and xxd.

        Args:
            length (int): The length of the password to generate.

        Returns:
            str: The generated password.
        """
        command = ["head", "-c", str(length), "/dev/random", "|", "xxd", "-p"]
        return self._extracted_from_generate_number_password_3(command)

    def _extracted_from_generate_number_password_3(self, command):
        """
        Executes a shell command and returns the output.

        Args:
            command (list): A list of strings representing the command to execute.

        Returns:
            str: The output of the command.
        """
        process = subprocess.Popen(
            " ".join(command), shell=True, stdout=subprocess.PIPE
        )
        output, _ = process.communicate()
        return output.decode().strip()


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordGeneratorApp()
    window.show()
    app.exec()
