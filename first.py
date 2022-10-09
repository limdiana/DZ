def get_reg(reg):
    if "расп" in reg.lower():
        schedule()

    elif "направ" in reg.lower():
        training()

    elif "конт" in reg.lower():
        contact()

    elif "плат" in reg.lower():
        price()

    elif "тренеры" in reg.lower():
        coaches()

def schedule():
    print("Пн - 17:00-21:00, Вт - 17:00-21:00, Ср - 16:30-19:30, Чт - 16:30-19:30, Пт - 15:00-21:00, Сб - 15:00-21:00")


def price():
    print("Ценна занятий: 1800")


def training():
    print("Направления: Силовая тренировка, Растяжка, TRX, МФР")


def contact():
    print("Контакты: +79302887465")


def coaches():
    print("Тренеры: Моисеева Елизавета, Климентьева Екатерина, Захарова Полина")