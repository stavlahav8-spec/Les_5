import sys

from PySide6.QtWidgets import (
    QApplication,
    QAbstractSpinBox,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Start / Stop")
        self.setMinimumWidth(200)

        self.counter = 0 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet(
            "QSpinBox, QSpinBox QLineEdit { background-color: #e6e6e6; }"
        )

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self._update_button_text)

        layout = QVBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.toggle_button)

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(0,255)
        self.slider_spin_box = QSpinBox()
        self.slider_spin_box.setRange(0, 255)
        self.slider_spin_box.setReadOnly(True)
        self.slider_spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.slider)
        right_layout.addWidget(self.slider_spin_box)

        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(right_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def _update_button_text(self, started: bool) -> None:
        self.toggle_button.setText("Stop" if started else "Start")
        if started:
            self.counter = 0 
            self.timer.start(10)
        else:
            self.timer.stop()

    def timer_method(self) -> None:
        self.counter += 1
        self.spin_box.setValue(self.counter)
        if self.spin_box.value() == 500:
            self.timer.stop()
            self.toggle_button.setChecked(False)


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
