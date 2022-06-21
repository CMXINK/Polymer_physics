from control.add_cyclohexane import Add_cyclohexane
from control.check_instrument import Check_instrument
from control.check_medicine import Check_medicine
from control.configs import Configs
from control.install_instrument import Install_instrument
from control.designe_instrument import Designe_instrument
from control.experiment_conditions import Experiment_conditions
from control.formula_calculate_one import Formula_calculate_one
from control.formula_calculate_two import Formula_calculate_two
from control.get_medicine import Get_medicine
from control.get_styrene import Get_styrene
from control.logon import Logon
from PyQt5.QtWidgets import QWidget


class ShowWidget(QWidget):
    def __init__(self):
        super(ShowWidget, self).__init__()
        self.show_logon()

    def configs(self, obj):
        widget = Configs()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_get_styrene(widget))

    def show_logon(self):
        widget = Logon()
        widget.show()
        widget.logon_safelogon_btn_signal.connect(lambda: self.show_experiment_conditions(widget))

    def show_experiment_conditions(self, obj):
        widget = Experiment_conditions()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_check_medicine(widget))

    def show_check_medicine(self, obj):
        widget = Check_medicine()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_check_instrument(widget))

    def show_check_instrument(self, obj):
        widget = Check_instrument()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_formula_calculate_one(widget))

    def show_formula_calculate_one(self, obj):
        widget = Formula_calculate_one()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_formula_calculate_two(widget))

    def show_formula_calculate_two(self, obj):
        widget = Formula_calculate_two(obj)
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_install_instrument(widget))

    def show_install_instrument(self, obj):
        widget = Install_instrument()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_design_instrument(widget))

    def show_design_instrument(self, obj):
        widget = Designe_instrument()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_add_cyclohexane(widget))

    def show_add_cyclohexane(self, obj):
        widget = Add_cyclohexane(obj)
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_get_medicine(widget))

    def show_get_medicine(self, obj):
        widget = Get_medicine()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_get_styrene(widget))

    def show_get_styrene(self, obj):
        widget = Get_styrene()
        widget.show()
        obj.hide()
        widget.ensure_signal.connect(lambda: self.show_get_styrene(widget))
