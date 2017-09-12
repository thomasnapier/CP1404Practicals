from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometres(App):
    """Class to convert miles to kilometres"""

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self):
        conversion_rate = 1.60934
        value = self.get_valid_number()
        total = value * conversion_rate
        self.root.ids.output_label.text = str(total)

    def handle_increment(self, change):
        value = self.get_valid_number() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_valid_number(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

ConvertMilesToKilometres().run()

