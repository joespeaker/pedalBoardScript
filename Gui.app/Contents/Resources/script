from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy, QFileDialog
)
from PyQt6.QtCore import Qt
import ytpb

def on_submit_click():
    youtube_link = input_field.text()
    result_label.setText("Downloading...")
    ytpb.download(youtube_link)
    result_label.setText("Done!")

def open_file_explorer():
    directory = QFileDialog.getExistingDirectory(None, "Select Directory")
    if directory:
        file_path_input.setText(directory)

app = QApplication([])

# Create the main window and layout
window = QWidget()
layout = QVBoxLayout()
window.setWindowTitle('YouTube Pitch Bender')

# Create a QLabel and add it to the layout
label = QLabel('YouTube Link:')
layout.addWidget(label)

# Create the QLineEdit for user input and add it to the layout
input_field = QLineEdit()
layout.addWidget(input_field)

# Create a QLabel for the file path
file_label = QLabel('File Path:')
layout.addWidget(file_label)

# Create a QHBoxLayout for file path input and browse button
file_path_layout = QHBoxLayout()

# Create the QLineEdit for file path and add it to the layout
file_path_input = QLineEdit('/path/to/initial/folder')
file_path_layout.addWidget(file_path_input)

# Create a QPushButton to open the file explorer
browse_button = QPushButton('Browse')
browse_button.clicked.connect(open_file_explorer)
file_path_layout.addWidget(browse_button)

layout.addLayout(file_path_layout)

# Create the QPushButton and connect the on_submit_click function
submit_button = QPushButton('Submit')
submit_button.clicked.connect(on_submit_click)

# Set the style to make the button look native
submit_button.setStyleSheet("QPushButton { background-color: auto; }")

# Set the size policy to make the button only as wide as the text
submit_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

# Add the button to the layout
layout.addWidget(submit_button)

# Create the QLabel for displaying the result and add it to the layout
result_label = QLabel('')
layout.addWidget(result_label)

# Set the layout for the window
window.setLayout(layout)

# Set the minimum width and height
window.setMinimumSize(600, 300)

# Show the window
window.show()

app.exec()
