from kivy.app import App
from kivy.lang import Builder


class PassOrFailApp(App):
    def build(self):
        self.title = "Calculate Pass or Fail"
        self.root = Builder.load_file('pass_or_fail.kv')
        return self.root

    def handle_calculate(self):
        # print("test")
        value = self.root.ids.input_score.text
        if 50 <= int(value) <= 100:
            self.root.ids.output_label.text = str("Pass")
        else:
            self.root.ids.output_label.text = str("Fail")
PassOrFailApp().run()
