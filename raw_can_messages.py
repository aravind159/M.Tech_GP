from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int


def rpm(messages):
    """ decoder for RPM messages """
    d = messages[0].data
    v = bytes_to_int(d) / 4.0
    return v * Unit.RPM


def rpm_raw_canned():
    cmd = OBDCommand("RPM", "Engine RPM", b"010C", 2, rpm, ECU.ENGINE, True)
    print(cmd.decode())
