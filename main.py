id2 = 0
basic.show_number(0)
huskylens.init_i2c()
basic.show_number(1)
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
basic.show_number(2)
OLED.init(128, 64)
basic.show_number(3)
name = ["Anson Lo", "Lokman", "Edan Lui", "Anson Kong"]
basic.show_number(4)
led.enable(False)

def on_forever():
    global id2
    huskylens.request()
    id2 = huskylens.readBox_s(Content3.ID)
    if id2 > 0:
        basic.pause(100)
        basic.show_number(id2)
        OLED.clear()
        OLED.write_string_new_line(name[id2 - 1])
        pins.digital_write_pin(DigitalPin.P6, 1)
        basic.pause(1000)
        pins.digital_write_pin(DigitalPin.P6, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P8, 0)
    else:
        pins.digital_write_pin(DigitalPin.P7, 1)
        basic.pause(1000)
        pins.digital_write_pin(DigitalPin.P7, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P8, 0)
basic.forever(on_forever)
