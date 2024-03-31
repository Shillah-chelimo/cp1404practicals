from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

NAMES = ["Alice", "Bob", "Charlie", "David", "Emma"]

class DynamicLabelsApp(App):
    """Main application class."""

    def build(self):
        """Build the Kivy app."""
        layout = BoxLayout(orientation='vertical')
        self.create_labels(layout)
        return layout

    def create_labels(self, layout):
        """Create labels dynamically based on the list of names."""
        for name in NAMES:
            label = Label(text=name, font_size='20sp')
            layout.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()

