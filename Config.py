import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13429768"))
    API_HASH = os.environ.get("API_HASH", "63b6d07b85e038eae4183c2902c4347b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5530267539:AAEIOpKp9wHuqOsdmZOY0-1I0kOTrAHW7lA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKABuz7hCxPm_gqqX4fsbacvt8l2WnYUhGDUJNmdeCQGJRXrR-SgQk_40PlX1JtG8ATNRD2LkhPwxphEKS2GYovLayGRW07fq4gG3FQwsnGxa0TgJ5ZE94-SbmWJ3yD8-tS70TZdauPC7Ws6Jza32QRX_BmGCcJ154MwQuM4diesyXsx5_icNisBpnZxbKPfmkH7i8jPHj6_jc8gej2dv0QFIaFBER347FwV6GY1BisQDLEnNvycnTlWFIWBuQZRijAMiQB568sKQe24is-IokBCkLU986wboQuFKlmctPMYOK1znXgR9Vl5maUPpW63Bhy4wHbySAYlUt9pQCclfLU=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", True)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "its_kang69_bot")
    SUPPORT = os.environ.get("SUPPORT", "") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5592036777")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
