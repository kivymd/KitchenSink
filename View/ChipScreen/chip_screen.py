from kivymd.uix.screen import MDScreen

from View.ChipScreen.components import CustomChip


class ChipScreenView(MDScreen):
    def on_enter(self):
        if not self.ids.chip_size_box.children:
            self.create_chips_size()

    def create_chips_size(self):
        for i in range(2, 10):
            if not i % 2:
                chip = CustomChip(text=f"{('0' if i < 10 else '') + str(i)}")
                chip.bind(active=self.removes_marks_all_chips)
                self.ids.chip_size_box.add_widget(chip)

    def removes_marks_all_chips(
        self, selected_instance_chip, active_state: bool
    ) -> None:
        for instance_chip in self.ids.chip_size_box.children:
            if instance_chip != selected_instance_chip:
                instance_chip.active = False
