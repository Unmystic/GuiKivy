from kivy.lang import Builder
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)


def show_about_dialog(self):
        
        Builder.load_string(
'''
<MDDialog>
    theme_bg_color: "Custom"
    md_bg_color: (211/255, 1, 222/255, 1)
    theme_shadow_color: "Custom"
    shadow_color: (211/255, 1, 222/255, 1)
    radius: [dp(5), dp(5), dp(5), dp(5)]

    
'''
       )


        MDDialog(
             
  
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="information-outline",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="League Simulation GUI",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text="Developed by "
                "Dmitry Platonychev "
                ,
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="material-ui",
                    ),
                    MDListItemSupportingText(
                        text="Material Icons by Google",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color="white",
                ),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="palette",
                    ),
                    MDListItemSupportingText(
                        text="Midjourney",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color="white",
                ),
                MDDivider(),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Ok"),
                    style="text",
                ),
       
            ),
            scrim_color=(211/255, 1, 222/255, 1)
            # -------------------------------------------------------------
        ).open()


KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_about_dialog()

        MDButtonText:
            text: "Show dialog"
'''


class DialogW(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_about_dialog(self):
        MDDialog(
            
  
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="information-outline",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="League Simulation GUI",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text="Developed by "
                "Dmitry Platonychev "
                ,
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="material-ui",
                    ),
                    MDListItemSupportingText(
                        text="Material Icons by Google",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color="white",
                ),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="palette",
                    ),
                    MDListItemSupportingText(
                        text="Midjourney",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color="white",
                ),
                MDDivider(),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Ok"),
                    style="text",
                ),
       
            ),
            # -------------------------------------------------------------
        ).open()

if __name__ == "__main__":
     DialogW().run()