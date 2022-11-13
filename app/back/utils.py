from typing import Final, TYPE_CHECKING
from re import fullmatch

from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem,
    QDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

if TYPE_CHECKING:
    from app.ui.ui import InfoDialog


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


def is_valid_number(phone_number: str) -> bool:
    pattern = '[78][0-9]{10}'
    return fullmatch(pattern, phone_number) is not None


def set_up_info_dialog(info_dialog: QDialog, info_form: "InfoDialog", text: str, icon_path: str, img_path: str):
    info_form.label_2.setText(text)
    info_dialog.setWindowIcon(QIcon(icon_path))
    info_form.label.setPixmap(QPixmap(img_path).scaled(100, 100))
    info_dialog.exec()


def clear_table_widget(table_widget: QTableWidget):
    for row_ind in range(table_widget.rowCount() - 1, -1, -1):
        table_widget.removeRow(row_ind)


def fill_table_with_data(data: list[tuple[str, str, str, str, str]], table_widget: QTableWidget):
    if len(data) == 1 and not data[0]:
        table_widget.setRowCount(0)
    else:
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


def add_combo_items(table):
    items_texts = ["---"]
    for r in range(0, table.tableWidget.rowCount()):
        item = table.tableWidget.item(r, 0)
        items_texts.append(item.text())

    fixed_size = table.comboBox.count()
    for i in range(0, fixed_size):
        table.comboBox.removeItem(0)
    table.comboBox.addItems(items_texts)


def check_number_if_exists(update_values, app):
    try:
        if not is_valid_number(update_values["vendor_number"]):
            icon_path = app.m_win.err_icon
            image_path = app.m_win.err_img
            return f"Введены некорректные данные!", icon_path, image_path
        else:
            return None
    except KeyError:
        return None


def define_info_dialog(rows: int | None, ui):
    icon_path = ui.ok_icon
    img_path = ui.ok_img

    match rows:
        case None:
            icon_path = ui.err_icon
            img_path = ui.err_img
        case 0:
            icon_path = ui.warn_icon
            img_path = ui.warn_img
        case _:
            pass

    return icon_path, img_path


def get_vendors_update_values(table_mod_vendor):
    fields = [
        (table_mod_vendor.lineEdit_4.text(), table_mod_vendor.checkBox.checkState()),
        (table_mod_vendor.lineEdit_5.text(), table_mod_vendor.checkBox_2.checkState()),
        (table_mod_vendor.lineEdit_6.text(), table_mod_vendor.checkBox_3.checkState()),
        (table_mod_vendor.lineEdit_7.text(), table_mod_vendor.checkBox_4.checkState()),
    ]
    update_values = [pair[0] if pair[1] == 2 else None for pair in fields]
    return update_values


def modify_vendors(VendorUpdateView, filter_values, update_values, ui):
    vendor_upd = VendorUpdateView(ui.app)
    response_data = vendor_upd.update(filter_values, update_values)
    set_up_info_dialog(ui.info_dialog, ui.info_form, response_data[0], response_data[1], response_data[2])
