import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.pdf_viewer = QWebEngineView(self)
        self.layout.addWidget(self.pdf_viewer)

        self.button_open_pdf = QPushButton("Open PDF", self)
        self.button_open_pdf.clicked.connect(self.open_pdf)
        self.layout.addWidget(self.button_open_pdf)

    def open_pdf(self):
        # Replace 'your_pdf_file.pdf' with the path to your existing PDF file
        pdf_path = 'your_pdf_file.pdf'
        pdf_url = QUrl.fromLocalFile(pdf_path)
        self.pdf_viewer.setUrl(pdf_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFViewer()
    window.show()
    sys.exit(app.exec_())
