from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.ui.ui import Ui

from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from app.ui.ui import T1Form
from generated_uis.get_vendors_table import UiFrame as TableGetVendors
from generated_uis.get_vendors_table_widget import UiFrame as TableGetVendorsWidget
from app.vendor.views import VendorGetView
from app.back.utils import clear_table_widget, fill_table_with_data


class TableMaster:
    def __init__(self, parent_ui: "Ui", related_form: T1Form, table_get_vendor: TableGetVendors):
        self.parent = parent_ui
        self.base_form = related_form

        self.table_get_vendor = table_get_vendor

    def spawn_get_vendors_table(self):
        # setting up widgets
        self.table_get_vendor.setupUi(self.parent)
        self.base_form.verticalLayoutT1.addWidget(self.table_get_vendor.horizontalLayoutWidget)
        self.base_form.verticalLayoutT1.removeWidget(self.base_form.label)

        # setting up table
        self.table_get_vendor.tableWidget.setColumnCount(5)
        self.table_get_vendor.tableWidget.setHorizontalHeaderLabels([
            "ID поставщика", "Наименование организации / ФИО", "Адрес поставщика",
            "Контактный телефон", "Электронная почта E-mail"
        ])
        self.table_get_vendor.tableWidget.resizeColumnsToContents()

        self.table_get_vendor.pushButton.clicked.connect(self.listVendorsClickedEvent)

    def listVendorsClickedEvent(self):
        if self.table_get_vendor.tableWidget.rowCount() > 0:
            clear_table_widget(self.table_get_vendor.tableWidget)

        filter_params = [
            line.text() if (line.text() != "") else None for line in (
                self.table_get_vendor.lineEdit_3,
                self.table_get_vendor.lineEdit_4,
                self.table_get_vendor.lineEdit_5,
                self.table_get_vendor.lineEdit_6,
                self.table_get_vendor.lineEdit_7,
            )
        ]

        vendor_get = VendorGetView(self.parent.app)
        response_data = vendor_get.get(filter_params)

        fill_table_with_data(response_data, self.table_get_vendor.tableWidget)
