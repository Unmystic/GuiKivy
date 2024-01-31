from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: (211/255, 1, 222/255, 1)

    MDButton:
        md_bg_color: (85/255, 170/255, 127/255, 1)
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Button"
            theme_font_name: "Custom"
            font_name: "segoeprint_bold.ttf"
            font_size: sp(48)
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"  # "Purple", "Red"
        return Builder.load_file("start.kv")


Example().run()