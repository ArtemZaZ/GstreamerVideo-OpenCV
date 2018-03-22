class RTCBaseError(Exception):
    """Базовый класс ошибки для модулей
    Аттрибуты:
        expression -- выражение в котором произошла ошибка
        message -- объясниние ошибки"""

    def __init__(self, expr, msg):
        if msg is None:
            msg = "Произошла ошибка в %s" % expr
        super(RTCBaseError, self).__init__(msg)
        self.expression = expr
        self.message = msg


class RTCInternalError(RTCBaseError):
    """Исключение вызывается из-за внутренней ошибки программы"""

    def __init__(self, expr, msg):
        super(RTCInternalError, self).__init__(expr, "Внутренняя ошибка программы в " + expr + ", по причине: " + msg)


"""
raise RTCInternalError("туть", "кривые руки")

try:
    raise RTCInternalError("туть", "кривые руки")
except InternalError as e:
    print(e.expression)
"""
