from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox, QComboBox, QWidget
from src.database.DataBaseManager import DataBaseManager
from src.ui.main_ui import Ui_MainWindow
from src.ui.task_add import Ui_Form as t_add
from src.ui.task_change import Ui_Form as t_change

TableHeaders = {"Task": ["ID", "Статус Заявки", "Прибор", "Описание"]}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db = DataBaseManager("service.db")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedData.setCurrentIndex(0)
        self.ui.stackedData.setVisible(False)

        self.ui.enter.clicked.connect(self.login)
        self.ui.reg.clicked.connect(self.register)
        self.ui.reg_a.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.cancel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.stats.clicked.connect(self.show_stats)
        self.ui.s_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.logout.clicked.connect(self.logout)

        self.data_window = QWidget()

    def login(self):
        data = self.db.login(self.ui.login.text(), self.ui.password.text())
        if not data:
            self.ui.auth_tip.setText("Неверный логин или пароль")
            return
        match data[0][5]:
            case 1:  # Пользователь
                self.ui.change.setVisible(False)
                self.ui.remove.setVisible(False)
                #self.data_window.
            case 2:  # Специалист
                self.ui.add.setVisible(False)
                self.ui.remove.setVisible(False)
            case 3 | 4:  # Оператор | Менеджер
                pass
        self.show_table()
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_table(self):
        data = self.db.get_tasks()
        table = self.ui.tableWidget
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))
        table.setHorizontalHeaderLabels(TableHeaders["Task"])
        table.setColumnWidth(0, 60)

        colum_index = 0
        for values in data:
            for item in values:
                for i in range(len(data[0])):
                    table.setItem(i, colum_index, QTableWidgetItem(str(item)))
                colum_index += 1
        table.resizeColumnsToContents()

    def fill_combobox(self, combobox: QComboBox, data):
        pass

    def show_stats(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.label.setText(f"Выполненых заявок: {self.db.complete_sum()}")

    def register(self):
        if self.ui.r_login.text() == "" or self.ui.r_password.text() == "":
            print("логин или пароль пусты")
            return

        if self.db.check_login(self.ui.r_login.text()):
            print("логин уже занят")
            return

        data = {
            "fio": self.ui.fio.text(),
            "phone_number": self.ui.phone.text(),
            "login": self.ui.r_login.text(),
            "password": self.ui.r_password.text(),
            "user_type_id": self.ui.user_type.currentIndex() + 1
        }
        self.db.create("Users", data)
        self.ui.stackedWidget.setCurrentIndex(0)

    def logout(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.auth_tip.setText("")


# Блок схема / спецификация
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
