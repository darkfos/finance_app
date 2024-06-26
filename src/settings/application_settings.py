from flet import FontWeight


class ApplicationSettings:

    #General
    title_application: str = "Finance"
    weight_application: int = 800
    height_application: int = 600
    resizable_window: bool = False

    #Field
    field_width = 400

    #Error
    error_color: str = "red"
    error_text_weight: FontWeight = FontWeight.W_500

    #Buttons
    #Filled
    bg_color: str = "blue"
    color: str = "black"
    #Outline
    bd_color_outl: str = "blue"
    width_outl_btn: int = 250
    width_outl_btn_2: int = 150

    #DropDown
    dr_down_weight: int = 120