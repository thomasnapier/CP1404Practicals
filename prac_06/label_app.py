from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class LabelApp(App):
    def __init__(self):
        super().__init__()
        self.names = ["John", "Bob", "Alex", "Jack", "Robin", "Renekton"]

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Label App"
        self.root = Builder.load_file('label_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)


LabelApp().run()
