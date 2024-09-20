﻿################################################################################
## Initialization
################################################################################

init offset = -1
default persistent.ClaerChapter = False

init python:

    def Confirm_yes(string, action):
        return Confirm(string, action, None)

    def SelectChaper_before_Ending( isclear, i ):
        if isclear:
            return Confirm('해당 에피소드를 불러옵니다',  Start(f"chapter_{i}"), NullAction())
        else:
            return Confirm_yes('엔딩 후에 이전 항목 돌아가기가 활성화됩니다',  NullAction()) #Notify("엔딩 후에 이전 항목 돌아가기가 활성화됩니다")


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



default persistent.Likeability = {'hean':0, 'eren':0, 'adrian':0, 'nox':0}

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/box_dia.png", xalign=0.5, yalign=1.0)
    #background Image("gui/phone/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    vbox:
        yalign 0.9
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    variant "touch"
    $ Icon_big = (100,100)
    $ Icon_small = (70,70)
    zorder 100
    #xalign 0.5
    ##yalign .025
    #yoffset -40
    if quick_menu:
        imagebutton idle "gui/BookIcon.png" :
            at transform:
                xalign .83
                yalign 0.0
                xysize Icon_big
            action ShowMenu("select_chapter")

        imagebutton idle "gui/PrefIcon.png" :
            at transform:
                xalign .95
                yalign 0.0
                xysize Icon_big
            action Show("in_game_preferences")

        imagebutton idle "gui/AutoIcon.png" :
            at transform:
                xalign .95
                yalign .07
                xysize Icon_small
            action Preference("auto-forward", "toggle")

        imagebutton idle "gui/SkipIcon.png" :
            at transform:
                xalign .95 
                yalign .11
                xysize Icon_small
            action Skip() alternate Skip(fast=True, confirm=True)

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    if renpy.get_screen("main_menu"):
        vbox:
            style_prefix "navigation"

            xalign 0.5
            yalign 0.7

            spacing gui.navigation_spacing

            textbutton _("Start") action ShowMenu("select_chapter")  #Start()

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Options") action ShowMenu("preferences")

            textbutton _("About") action ShowMenu("about")
    elif renpy.get_screen("select_chapter"):
        null height 0
    ########################################################################
    else:
        vbox:
            xalign 0.5
            yalign 0.8

            style_prefix "navigation"

            spacing gui.navigation_spacing

            hbox:
                textbutton _("Save") action ShowMenu("save")
                textbutton _("History") action ShowMenu("history")


            
            hbox:

                textbutton _("Load") action ShowMenu("load")
                textbutton _("Main Menu") action MainMenu()


            
            hbox:
                textbutton _("Options") action ShowMenu("preferences")

                textbutton _("About") action ShowMenu("about")



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

default show_TouchToStart = True

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    if show_TouchToStart:
        vbox:
            xalign 0.5
            yalign 0.7
            text _("Touch to start") at blink(0.5)

        ## full_screen button
        button:
            xysize(1080,1920)
            action [ ShowMenu("select_chapter"), SetVariable("show_TouchToStart", False) ]
            
    else:
        use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

transform blink(fq = 0.5, maxAlpha = 1, minAlpha = 0):
    alpha 0
    linear fq alpha maxAlpha
    linear fq alpha minAlpha
    repeat

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 237
    yfill True

# background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -16
    xmaximum 675
    yalign 1.0
    yoffset -16

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        
                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
    if renpy.get_screen("select_chapter") == None:
        use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 26
    top_padding 102

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 287
    yfill True

style game_menu_content_frame:
    xalign 0.5
    yalign 1.0
    top_margin 50

    

style game_menu_viewport:
    xsize None

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 9

style game_menu_label:
    xalign 0.5
    ysize 102
    ypos 20

style game_menu_label_text:
    size 60
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -25


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"
        vbox:
            xpos 170
            xsize 800

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text


style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid 1 4:
                style_prefix "slot"

                xalign 0.5
                yalign 0.2

                spacing gui.slot_spacing

                for i in range(1 * 4):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        # add FileScreenshot(slot) xalign 1

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.0
                yoffset 70

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 5):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text:
    xoffset 100
    yoffset 75
style slot_name_text is slot_button_text:
    xoffset 100

style page_label:
    xpadding 43
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox:
            ypos 50
            xpos 200

            #hbox:
            #    box_wrap True
            #
            #
            #    vbox:
            #        style_prefix "check"
            #        label _("Skip")
            #        textbutton _("Unseen Text") action Preference("skip", "toggle")
            #        textbutton _("After Choices") action Preference("after choices", "toggle")
            #        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
            #
            #    ## Additional vboxes of type "radio_pref" or "check_pref" can be
            #    ## added here, to add additional creator-defined preferences.
            #
            #null height (4 * gui.pref_spacing)

            vbox:
                frame:
                    background "#f0f0f044"
                    vbox:
                        
                        style_prefix "slider"
                        box_wrap True

                        label _("자동 진행 속도")

                        bar value Preference("auto-forward time")

                        label _("텍스트 속도")

                        bar value Preference("text speed")

                null height (4 * gui.pref_spacing)        
                frame:
                    background "#f0f0f03f"
                    vbox:
                        style_prefix "slider"
                        if config.has_music:
                            label _("배경음")

                            hbox:
                                bar value Preference("music volume")

                        if config.has_sound:

                            label _("효과음")

                            hbox:
                                bar value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                    #    label _("Voice Volume")
                    #
                    #    hbox:
                    #        bar value Preference("voice volume")
                    #
                    #        if config.sample_voice:
                    #            textbutton _("Test") action Play("voice", config.sample_voice)

                    #if config.has_music or config.has_sound or config.has_voice:
                    #    null height gui.pref_spacing
                    #
                    #    textbutton _("Mute All"):
                    #        action Preference("all mute", "toggle")
                    #        style "mute_all_button"
screen in_game_preferences():

    tag menu
    modal True
    frame:
        background "#2c2c2ca2"
        yalign .5
        xalign .5
        
        vbox:
            

            vbox:
                frame:
                    background "#f0f0f044"
                    vbox:
                        
                        style_prefix "slider"
                        box_wrap True

                        label _("자동 진행 속도")

                        bar value Preference("auto-forward time")

                        label _("텍스트 속도")

                        bar value Preference("text speed")

                null height (4 * gui.pref_spacing)        
                frame:
                    background "#f0f0f03f"
                    vbox:
                        style_prefix "slider"
                        if config.has_music:
                            label _("배경음")

                            hbox:
                                bar value Preference("music volume")

                        if config.has_sound:

                            label _("효과음")

                            hbox:
                                bar value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)
                hbox:
                    xalign .5
                    textbutton "호감도" :
                        action ShowMenu("affection")
                        
                    null width 100
                    textbutton "메인메뉴" :
                        action MainMenu()
                        
    textbutton _("X"):
        style "return_button"
        action Hide("in_game_preferences")
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label:
    xalign 0.5
    xoffset 90
style check_label_text is pref_label_text
style check_button is gui_button:
    xoffset 90
    xalign 0.5
style check_button_text is gui_button_text:
    size 47
style check_vbox is pref_vbox

style slider_label is pref_label:
    xalign 0.5
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text

style mute_all_button is check_button:
    xalign 0.5
    xoffset -10
style mute_all_button_text is check_button_text


style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 500


style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 700

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 9

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize None


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 13

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 7

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 211
    right_padding 17

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action = None):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 26

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 85

                textbutton _("Yes") action yes_action
                if no_action is None:
                    textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action



style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "KoPubWorld Dotum Light.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0
                
                

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/phone/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

screen select_chapter():
    tag menu
    add gui.game_menu_background
    
    frame:
        style "game_menu_outer_frame"
        xalign 0.5
        hbox:
            xalign 0.5
            frame:
                xalign 0.5
                style "game_menu_content_frame"
                viewport:
                    xalign 0.5
                    ysize 0.9
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    vbox:
                        xalign 0.5
                        yalign 0.5
                            
                        for i in range(0, 20):

                            if i < persistent.ClaerChapter: #
                                textbutton _("Chapter [i]"):
                                    action SelectChaper_before_Ending(persistent.isClear, i)
                                    text_color color_yellow
                                    
                            elif i == persistent.ClaerChapter: # 현재 열려있는 에피소드
                                textbutton _("Chapter [i]"):
                                    action Confirm( '해당 에피소드를 불러옵니다',  Start(f"chapter_{i}"), NullAction() )  
                                    text_color color_yellow
                                    
                            else: # 개방안됨
                                textbutton _("Chapter [i]"):
                                    action Confirm_yes("아직 개방되지 않은 에피소드입니다", NullAction())
                                
                            #style 
                            null height 10
    
    label _("Select Chapter"):
        style "game_menu_label"

    textbutton _("Return"):
        style "return_button"
        action Return()

style affrectionTextbutton_button_text is text:
    size 45

init python:
    import json

    data_name = ['eren','nox','hean','adrian']

    class affection_data:
        def __init__(self):
            self.name = ''
            self.image_path = ''
            self.age = 0
            self.height = 0
            self.weight = 0
            self.say = ''

        def load_affection_data(self, name):
            with renpy.open_file(f"affection_data/{name}.json") as f:
                data = json.load(f)
                self.name = data['name']
                self.image_path = data['image_path']
                self.age = data['age']
                self.height = data['height']
                self.weight = data['weight']
                self.say = data['say']
            
        
    character_data = affection_data()
    character_data.load_affection_data(data_name[0])

screen affection():
    tag menu
    add gui.game_menu_background


    frame: #select button
        xsize 0.8
        ysize 0.045
        xalign 0.5
        yalign 0.055
        background "#ff000081"
        hbox:
            spacing 100
            xalign 0.5
            textbutton _(data_name[0]):
                style_prefix "affrectionTextbutton"
                action Function(character_data.load_affection_data, data_name[0])
            textbutton _(data_name[1]):
                style_prefix "affrectionTextbutton"
                action Function(character_data.load_affection_data, data_name[1])
            textbutton _(data_name[2]):
                style_prefix "affrectionTextbutton"
                action Function(character_data.load_affection_data, data_name[2])
            textbutton _(data_name[3]):
                style_prefix "affrectionTextbutton"
                action Function(character_data.load_affection_data, data_name[3])
    
    default viewport_width = 1080 * 0.9
    default viewport_offset = (1080 - viewport_width)/2   
    viewport:
        
        xoffset viewport_offset
        yoffset 187
        #child_size (viewport_width,4000)
        xalign .5
        #yalign .06
        xfill False
        yfill True
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
    
        vbox:
            
            
            frame:
                #xsize 0.95
                xsize .9
                xalign 0.5
                ysize 1000
                yalign 0.45
                background "#00000054" 
                frame: # image frame
                    background "#ffffff52" 
                    xalign 0.1
                    yalign 0.05
                    xsize 0.4
                    $ image_size_mult = 1.2
                    imagebutton idle "char serena.png" at transform:
                        size (300 * image_size_mult, 400 * image_size_mult)
                        xalign 0.5
                        yalign 0.5
                        
                frame: #info frame
                    background "#52525241" 
                    
                    xsize 0.4
                    xalign 0.9
                    yalign 0.05
                    vbox:
                        null height 20
                        text '이름: [character_data.name]' 
                        null height 20
                        text '나이: [character_data.age]세'
                        null height 20
                        text '신장: [character_data.height]cm'
                        null height 20
                        text '몸무게: [character_data.weight]kg'
                        null height 20
                    
                frame: # say frame
                    background "#8412b9ef" 
                    xalign 0.5
                    yalign 0.83
                    xsize 0.9
                    ysize 0.3
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        text "[character_data.say]":
                            xalign 0.5
                            size 55
                        
                        
                frame: # Likeability frame
                    background "#000000ff"
                    xsize 0.9
                    ysize 0.04
                    xalign 0.5
                    yalign 0.95
                    frame:
                        background "#f00"
                        xsize .7 #todo: persistent.Likeability['hean']
                        ysize .99
                        xalign 0
                        yalign .5
                        text str(persistent.Likeability[character_data.name]) :
                            size 35
                            xalign .999
                            yalign .5
            frame: #image frame
                xsize 0.9
                #ysize .35
                xalign 0.5
                #yalign 0.98
                background "#00eeff88"
                $ imagenum = 20
                vbox:
                    xsize 1
                    spacing 10
                    xalign .5
                    yalign .5
                    for row in range(0, imagenum, 2):
                        hbox:
                            xalign .5
                            yalign .5
                            spacing 100  # 버튼 간의 간격
                            for col in range(2):
                                #null width 20
                                if row + col < imagenum:
                                    imagebutton idle "char serena.png":
                                        action Show('full_image_screen', dissolve)
                                        at transform:
                                            size (300 * image_size_mult, 400 * image_size_mult)
                                            xalign 0.5
                                            yalign 0.5
                                        
                        #null height 150

            null height 100
        
    label _("호감도"):
        style "game_menu_label"

    textbutton _("Return"):
        style "return_button"
        action Return()

screen full_image_screen():
    add "black"
    # 전체 화면에 이미지 표시
    imagebutton idle "char serena.png" :
        action Hide('full_image_screen', dissolve)
        at transform:
            size(1080,1920)
            xalign 0.5
            yalign 0.5
        