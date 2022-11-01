from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.ui.ui import Ui

from app.ui.ui import T1Form
from generated_uis.get_vendors_table import UiFrame as TableGetVendors


class Spawner:
    def __init__(self, parent_ui: "Ui", related_form: T1Form):
        self.parent = parent_ui
        self.base_form = related_form
        # self.

        self.table_get_vendor = TableGetVendors()

    def spawn_get_vendors_table(self):
        self.table_get_vendor.setupUi(self.parent)
        self.base_form.verticalLayoutT1.addWidget(self.table_get_vendor.horizontalLayoutWidget)
        self.base_form.verticalLayoutT1.removeWidget(self.base_form.label)
