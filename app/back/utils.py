from typing import Final, TYPE_CHECKING, Tuple
from re import fullmatch

from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem,
    QDialog, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

if TYPE_CHECKING:
    from app.ui.ui import InfoDialog
    from app.base.base_accessor import BaseAccessor


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


def get_value_range(value: str) -> tuple[None, None] | tuple[str, str]:
    if value is None:
        return value, value
    params = value.replace(" ", "").split(",")
    if len(params) == 1:
        return value, value
    if len(params) == 2:
        return params[0], params[1]
    return None, None


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


def add_combo_items(combo_box: QComboBox, table_widget: QTableWidget):
    items_texts = ["---"]
    for r in range(0, table_widget.rowCount()):
        item = table_widget.item(r, 0)
        items_texts.append(item.text())

    fixed_size = combo_box.count()
    for i in range(0, fixed_size):
        combo_box.removeItem(0)
    combo_box.addItems(items_texts)


def add_combo_ids(combo_box: QComboBox, accessor: "BaseAccessor"):
    items = ["---"]
    p_keys = accessor.get_p_keys()
    for p_key in p_keys:
        items.append(str(p_key))

    fixed_size = combo_box.count()
    for i in range(0, fixed_size):
        combo_box.removeItem(0)
    combo_box.addItems(items)


def check_number_if_exists(update_number, app):
    try:
        if not is_valid_number(update_number):
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


def get_customers_update_values(table_mod_customer):
    fields = [
        (table_mod_customer.lineEdit_4.text(), table_mod_customer.checkBox.checkState()),
        (table_mod_customer.lineEdit_5.text(), table_mod_customer.checkBox_2.checkState()),
        (table_mod_customer.lineEdit_6.text(), table_mod_customer.checkBox_3.checkState()),
        (table_mod_customer.lineEdit_7.text(), table_mod_customer.checkBox_4.checkState()),
    ]
    update_values = [pair[0] if pair[1] == 2 else None for pair in fields]
    return update_values


def get_customers_filter_values(dialog_mod_customer_form):
    filter_values = [
        None,
        dialog_mod_customer_form.lineEdit.text() if dialog_mod_customer_form.lineEdit.text() != "" else None,
        dialog_mod_customer_form.lineEdit_2.text() if dialog_mod_customer_form.lineEdit_2.text() != "" else None,
        dialog_mod_customer_form.lineEdit_3.text() if dialog_mod_customer_form.lineEdit_3.text() != "" else None,
        dialog_mod_customer_form.lineEdit_4.text() if dialog_mod_customer_form.lineEdit_4.text() != "" else None,
    ]
    return filter_values


def get_vendors_update_values(table_mod_vendor):
    fields = [
        (table_mod_vendor.lineEdit_4.text(), table_mod_vendor.checkBox.checkState()),
        (table_mod_vendor.lineEdit_5.text(), table_mod_vendor.checkBox_2.checkState()),
        (table_mod_vendor.lineEdit_6.text(), table_mod_vendor.checkBox_3.checkState()),
        (table_mod_vendor.lineEdit_7.text(), table_mod_vendor.checkBox_4.checkState()),
    ]
    update_values = [pair[0] if pair[1] == 2 else None for pair in fields]
    return update_values


def get_vendors_filter_values(dialog_mod_vendor_form):
    filter_values = [
        None,
        dialog_mod_vendor_form.lineEdit.text() if dialog_mod_vendor_form.lineEdit.text() != "" else None,
        dialog_mod_vendor_form.lineEdit_2.text() if dialog_mod_vendor_form.lineEdit_2.text() != "" else None,
        dialog_mod_vendor_form.lineEdit_3.text() if dialog_mod_vendor_form.lineEdit_3.text() != "" else None,
        dialog_mod_vendor_form.lineEdit_4.text() if dialog_mod_vendor_form.lineEdit_4.text() != "" else None,
    ]
    return filter_values


def get_warehouses_update_values(table_mod_warehouse):
    fields = [(table_mod_warehouse.lineEdit_4.text(), table_mod_warehouse.checkBox.checkState()), ]
    update_values = [pair[0] if pair[1] == 2 else None for pair in fields]
    return update_values


def get_warehouses_filter_values(dialog_mod_warehouse_form):
    filter_values = [
        None, dialog_mod_warehouse_form.lineEdit.text() if dialog_mod_warehouse_form.lineEdit.text() != "" else None,
    ]
    return filter_values


def get_products_update_values(table_mod_products):
    fields = [
        (table_mod_products.lineEdit_4.text(), table_mod_products.checkBox.checkState()),
        (table_mod_products.lineEdit_5.text(), table_mod_products.checkBox_2.checkState()),
        (table_mod_products.lineEdit_6.text(), table_mod_products.checkBox_3.checkState()),
        (table_mod_products.comboBox_3.currentText(), table_mod_products.checkBox_4.checkState()),
        (table_mod_products.comboBox_4.currentText(), table_mod_products.checkBox_6.checkState()),
        (table_mod_products.comboBox_4.currentText(), table_mod_products.checkBox_8.checkState()),
    ]
    update_values = [pair[0] if pair[1] == 2 else None for pair in fields]
    return update_values


def get_products_filter_values(dialog_mod_product_form):
    filter_values = [
        None,
        dialog_mod_product_form.lineEdit.text() if dialog_mod_product_form.lineEdit.text() != "" else None,
        dialog_mod_product_form.lineEdit_2.text() if dialog_mod_product_form.lineEdit_2.text() != "" else None,
        dialog_mod_product_form.lineEdit_3.text() if dialog_mod_product_form.lineEdit_3.text() != "" else None,
        dialog_mod_product_form.comboBox.currentText() if dialog_mod_product_form.comboBox.currentText() != "---"
        else None,
        dialog_mod_product_form.comboBox_2.currentText() if dialog_mod_product_form.comboBox_2.currentText() != "---"
        else None,
        dialog_mod_product_form.comboBox_3.currentText() if dialog_mod_product_form.comboBox_3.currentText() != "---"
        else None,
    ]
    return filter_values


def get_categories_update_values(table_mod_products):
    fields = [(table_mod_products.lineEdit_14.text(), table_mod_products.checkBox_10.checkState()), ]
    update_values = [pair[0] if pair[1] == 2 else None for pair in fields]
    return update_values


def get_categories_filter_values(dialog_mod_category_form):
    filter_values = [
        None, dialog_mod_category_form.lineEdit.text() if dialog_mod_category_form.lineEdit.text() != "" else None,
    ]
    return filter_values


def modify_customers(CustomerUpdateView, filter_values, update_values, ui):
    customer_upd = CustomerUpdateView(ui.app)
    response_data = customer_upd.update(filter_values, update_values)
    set_up_info_dialog(ui.info_dialog, ui.info_form, response_data[0], response_data[1], response_data[2])


def modify_vendors(VendorUpdateView, filter_values, update_values, ui):
    vendor_upd = VendorUpdateView(ui.app)
    response_data = vendor_upd.update(filter_values, update_values)
    set_up_info_dialog(ui.info_dialog, ui.info_form, response_data[0], response_data[1], response_data[2])


def modify_warehouses(WarehouseUpdateView, filter_values, update_values, ui):
    warehouse_upd = WarehouseUpdateView(ui.app)
    response_data = warehouse_upd.update(filter_values, update_values)
    set_up_info_dialog(ui.info_dialog, ui.info_form, response_data[0], response_data[1], response_data[2])


def modify_products(ProductUpdateView, filter_values, update_values, ui):
    product_upd = ProductUpdateView(ui.app)
    response_data = product_upd.update(filter_values, update_values)
    set_up_info_dialog(ui.info_dialog, ui.info_form, response_data[0], response_data[1], response_data[2])


def modify_categories(ProductCategoryUpdateView, filter_values, update_values, ui):
    category_upd = ProductCategoryUpdateView(ui.app)
    response_data = category_upd.update(filter_values, update_values)
    set_up_info_dialog(ui.info_dialog, ui.info_form, response_data[0], response_data[1], response_data[2])


def modify_managers(ManagerUpdateView, filter_values, update_values, ui):
    manager_upd = ManagerUpdateView(ui.app)
    response_data = manager_upd.update(filter_values, update_values)
    set_up_info_dialog(ui.info_dialog, ui.info_form, response_data[0], response_data[1], response_data[2])
