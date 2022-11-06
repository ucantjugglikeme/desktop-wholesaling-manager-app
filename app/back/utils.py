from typing import Final, TYPE_CHECKING
from re import fullmatch
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QDialog, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

if TYPE_CHECKING:
    from app.ui.ui import InfoDialog, Ui
    from app.ui.table_masters import TableMaster


def in_rect(p_x: int, p_y: int, r_x: int, r_y: int, r_w: int, r_h: int) -> bool:
    # Menu Bar takes 20 pixels
    MBAR_MARGIN: Final[int] = 20

    if p_x in range(r_x, r_x + r_w) and \
       p_y in range(
        MBAR_MARGIN + r_y, MBAR_MARGIN + r_y + r_h
    ):
        return True
    else:
        return False


def is_valid_psw(password: str) -> bool:
    """
    (?=^.{8,}$) -- at least 8 symbols
    ((?=.*\d)|(?=.*\W+)) -- 0 or more symbols and 1 digit or 1 or more non-digital non-latin letter symbols
    (?![.\n]) -- no \n or . before string
    (?=.*[A-Z]) -- any Capital latin letter after string
    (?=.*[a-z]) -- any small latin letter after string
    .*$ -- one or more symbols before the end of string
    """
    pattern = '(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
    return fullmatch(pattern, password) is not None


def set_up_info_dialog(info_dialog: QDialog, info_form: "InfoDialog", text: str, icon_path: str, img_path: str):
    info_form.label_2.setText(text)
    info_dialog.setWindowIcon(QIcon(icon_path))
    info_form.label.setPixmap(QPixmap(img_path).scaled(100, 100))
    info_dialog.exec()


def set_new_main_window(parent: "Ui", table_form, main_layout: QWidget, func=None):
    table_form.setupUi(parent)
    parent.setCentralWidget(main_layout)
    if func:
        func()


def clear_table_widget(table_widget: QTableWidget):
    for row_ind in range(table_widget.rowCount() - 1, -1, -1):
        table_widget.removeRow(row_ind)


def fill_table_with_data(data: list[tuple[str, str, str, str, str]], table_widget: QTableWidget):
    table_widget.setRowCount(len(data))
    r, c = 0, 0
    for row in data:
        for field in row:
            cur_item = QTableWidgetItem(field)
            cur_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table_widget.setItem(r, c, cur_item)
            table_widget.item(r, c).setToolTip(field)
            c += 1
        c = 0
        r += 1
