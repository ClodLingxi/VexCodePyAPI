def drive(direction):
    pass


def drive_for(direction, value, unit, wait=True):
    pass


def turn(direction):
    pass


def turn_for(direction, value, unit='degrees', wait=True):
    pass


def turn_to_heading(direction, value, unit='degrees', wait=True):
    pass


def turn_to_rotation(direction, value, unit='degrees', wait=True):
    pass


def stop(self):
    pass


def set_drive_velocity(value, unit='percent'):
    pass


def set_turn_velocity(value, unit='percent'):
    pass


def set_heading(value, unit='percent'):
    pass


def heading(unit) -> float:
    pass


def rotation(unit) -> float:
    pass


def set_rotation(value, unit='percent'):
    pass


def is_done() -> bool:
    pass


def is_moving() -> bool:
    pass
