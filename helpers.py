navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar: 
                        title: 'Aaya Calculation'
                        left_action_items: [["menu", lambda x : nav_drawer.toggle_nav_drawer()]]
                        elevation: 8
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '2dp'
                padding: '2dp'

                Image:
                    id: avatar
                    source: 'vastu shastra.png'
                    size_hint: 0.4, 0.4
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
                    text: '              Aaya Calculation'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]


                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text: 'Details'
                            IconLeftWidget:
                                icon: 'account-details'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'

"""

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Santosh'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Lets upload something'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'
"""