
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen , NoTransition , WipeTransition
from kivy.uix.screenmanager import ScreenManager, FadeTransition, NoTransition
from kivy.uix.screenmanager import NoTransition


KV = '''
#: import NoTransition kivy.uix.screenmanager.NoTransition 

ScreenManager:
    transition: NoTransition()
    SplashScreen:
        name: 'splash'
    MainScreen:
        name: 'main'

<SplashScreen>:
    name: 'intro'
    MDFloatLayout:
        MDIconButton:
            id: my_icon
            icon_size: "110sp"
            icon: "img/logo.png"
            
            pos_hint: {"center_x": .49, "center_y": .6}
            theme_text_color: "Custom"
           # on_release: app.root.current = 'Login'

            canvas.before:
                Color:
                    rgba:  1,1,1,1  # Black color (R, G, B, A)
                Ellipse:
                    size: self.width * 0.9, self.height * 0.9
                    pos: self.x + self.width * 0.1, self.y + self.height * 0


        MDLabel:
            id: label2
            text: 'From'
            pos_hint: {"center_x": .94, "center_y": .14}
            text_color: 0.5, 0.5, 0.5, 1
            font_style: 'H5'
            font_size: "20sp"
            blod:True
            opacity: 1
            
        MDLabel:
            id: label
            text: 'Ikhwanul Muslimin'
            theme_text_color: 'Custom'
            pos_hint: {"center_x": .85, "center_y": .1}
            text_color: 0.5, 0.5, 0.5, 1
            font_style: 'Body2'
            font_size: "15sp"
            bold:True
            opacity: 1
            
            
            

<MainScreen>:
    name: 'main'
    ScrollView:
        bar_width: 0
        do_scroll_x: False
        do_scroll_y: True
        

        GridLayout:
            id: grid_layout
            cols: 1
            spacing: dp(20)
            padding: dp(10)
            size_hint_y: None  # This line is added
            height: self.minimum_height

            MDBoxLayout:
                size_hint_y: None
                height: dp(50)

                MDLabel:
                    text: 'Your'
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    font_style: 'H6'

                MDFloatLayout:
                    MDLabel:
                        text: 'Digital Tasbeeh'
                        pos_hint: {'right': 0, 'center_y': 0.1}
                        theme_text_color: 'Custom'
                        text_color: 0.5, 0.5, 0.5, 1
                        font_style: 'Body1'
                        

                        
                


                    MDIconButton:
                        icon: "img/ico.png"
                        icon_size: "70sp"
                        pos_hint: {'right': 1.15, 'top': 1.2}
                        mode: "fill"
                        # on_release: app.root.current = 'Login'
                        
                
            RelativeLayout:
                MDTextField:
                    id: search_field
                    hint_text: "         Add Your Tasbeeh"
                    icon: "magnify"
                    mode: "rectangle"
                    on_text_validate: app.on_search_enter()
                    size_hint: None, None
                    size: root.width * 0.8, dp(56)  # Set the width relative to the root layout's width
                    pos_hint: {'center_x': 0.5, 'top': 0.8}  # Position relative to parent
                    halign: "center"  # Horizontal alignment of the text
                    max_text_length: 30
                 
                MDIconButton:
                    id: search_icon
                    icon: "pencil-plus"
                    icon_size: '16dp'
                    md_bg_color: 0, 0, 0, 1
                    on_release: app.on_search_icon_press()
                    size_hint: None, None
                    size: dp(40), dp(40)  # Set fixed width and height
                    pos_hint: {'right': 0.12, 'top': 0.9}  # Position relative to parent
                    
                    
                
        

                
            



                

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(90)  # Add spacing between widgets
                padding: dp(10)  # Add padding to the BoxLayout


                MDBoxLayout:
                    size_hint: (None, None)  # Disables automatic size_hint
                    size: (50, 1)  # Sets the size of the layout to (200, 100) in pixels
                    pos_hint: {'center_x': 0.55} 



                GridLayout:
                    id: radio_box_layout
                    cols: 1
                    spacing: "20dp"
                    size_hint_y: None  # This line is added
                    height: self.minimum_height
              

                    
                        


'''

# Define SplashScreen as a Screen class
class SplashScreen(Screen):
    pass

# Define MainScreen as a Screen class
class MainScreen(Screen):
    pass


    

class Tasbeeh(MDApp):
    icon_color = (0, 0, 0, 1)  # Add icon_color attribute to the Tasbeeh class
    box_counter = 0  # Initialize box_counter in the class

    def build(self):
        Window.size = [350, 750]
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.primary_color = self.theme_cls.primary_color
     
        
            
            # Load the KV string
        screen = Builder.load_string(KV)
        self.screen_manager = ScreenManager()
        self.screen_manager.transition = NoTransition() 


        
        return screen
    

    
    def setup_search_icon(self, dt):
        # Access the search_icon now that KV string has been loaded
        self.search_icon = self.root.ids.search_icon
        self.search_field = self.root.ids.search_field
        
        # Set the initial color of the icon
        self.search_icon.md_bg_color = (0, 0, 0, 1)
        
        # Bind the text color of the MDTextField to the icon color
        self.search_field.bind(focus=self.update_icon_color)
        
        
    def on_start(self):
        Clock.schedule_once(self.switch_to_main, 3.5)  # Switch to main screen after 2 seconds

    def switch_to_main(self, dt):
        # Access the ScreenManager and switch to the 'main' screen
        self.root.current = 'main'
        
        
    
    def update_icon_color(self, instance, value):
        # Update the icon color based on focus
        if value:
            self.search_icon.md_bg_color = self.search_field.theme_cls.primary_color
        else:
            self.search_icon.md_bg_color = (0, 0, 0, 1)


    
      #information 
    def on_search_icon_press(self):
        # Check the current active screen
        current_screen = self.root.current
        
        # Access the 'main' screen and its search_field
        if current_screen == 'main':
            main_screen = self.root.get_screen('main')
            search_text = main_screen.ids.search_field.text
            if search_text.strip():
                self.box_counter += 1
                box = SelectableCard(text=search_text)
                main_screen.ids.search_field.text = ""  # Clear the text field
                main_screen.ids.radio_box_layout.add_widget(box, index=0)  # Insert at the beginning
                main_screen.ids.grid_layout.minimum_height += box.height
                #self.save_widget_data()
            


    def on_search_enter(self):
        self.on_search_icon_press()
     
                

        


class SelectableCard(MDCard):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        


        self.size_hint_y = None
        self.height = "70dp"
        
        self.orientation = "horizontal"
        self.spacing = "50dp"  # Add spacing between elements
        
        

        
        self.selected = False
        self.counter = 0
        
        # Create and configure the label
        # Create and configure the label with adjusted text size, bold, different font, and color
        self.label = Label(
            text=f" {text}",
            bold=True,
            font_size='12sp',
            color=(0.5, 0.5, 0.5, 1)  # Specify the color as RGBA values (here, it's red)
        )
                
        # Create and configure the delete button
        self.delete_button = MDIconButton(
            icon="delete", size=("30dp", "30dp"), size_hint=(None, None),
            theme_text_color="Custom", text_color=(1, 0, 0, 1)  # Set the color to red (R, G, B, A)
        )
        self.delete_button.bind(on_release=self.delete_card)  # Bind the release event
        
        # Create and configure the plus button
        self.plus_button = MDIconButton(
            icon="restart", size=("30dp", "30dp"), size_hint=(None, None)
        )
        self.plus_button.bind(on_release=self.increase_counter)
        
        # Create a layout to hold the widgets
        self.layout = FloatLayout(size_hint=(None, None), size=(self.width, self.height))
        
        # Position the plus button in the center of the card
        self.layout.add_widget(self.plus_button)
        self.plus_button.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        # Bind the touch event to make the card selectable
        self.bind(on_release=self.card_selected)
        
        # Add widgets to the card
        self.add_widget(self.layout)
        self.add_widget(self.label)
        self.add_widget(self.delete_button)


        # Adjust the position of the delete button
        self.delete_button.pos_hint = {'center_y': 0.5}

    
      
   
        
   
    def card_selected(self, instance):
   
        
        self.counter += 1
        self.label.text = f"{self.counter}. {self.label.text.split('.', 1)[-1].strip()}"
        # Update the label text by removing the initial serial number and whitespace
        
    def increase_counter(self, instance):
        sound = SoundLoader.load('sound/tap.mp3')
        if sound:
            sound.play()
        # Reset the counter regardless of the current selected state
        self.counter = 0
        self.label.text = f"{self.label.text.split('.', 1)[-1].strip()}"

        # Toggle the selected state and update background color
        self.selected = not self.selected
        if self.selected:
            self.background_color = (1, 1, 1, 1)  # Example: light blue color
        else:
            # Set the background color when not selected (change as needed)
            self.background_color = (1, 1, 1, 0)  # Transparent or default color

        # Hide the label when the counter is zero
    # (You might need additional logic here)
        
       
      
        


    def delete_card(self, instance):
        self.parent.remove_widget(self)  # Remove the card from its parent
        sound = SoundLoader.load('sound/delete.mp3')
        if sound:
            sound.play()
        
        
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            return False  # Ignore scrolling

        if 'button' in touch.profile and touch.button == 'left' and self.collide_point(*touch.pos):
            if touch.button == 'left' and touch.is_double_tap:
                self.card_selected(touch)
                return True

        if hasattr(touch, 'is_keypad'):
            if touch.is_keypad and hasattr(touch, 'keycode') and 'enter' in touch.keycode:
                self.increase_counter(self.plus_button)  # Trigger increase_counter method
                return True  # Event handled

        return super().on_touch_down(touch)






# working on the last page :    
        


if __name__ == "__main__":
    
  
    Tasbeeh().run()
