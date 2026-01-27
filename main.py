import serial
import struct

ser = serial.Serial('COM4', 115200, timeout=1)


def decode_frame(frame):
    # 1. Usuń Byte Stuffing
    decoded = bytearray()
    i = 1  # Pomiń start 0x7E
    while i < len(frame) - 1:
        if frame[i] == 0x7D:
            decoded.append(frame[i + 1] ^ 0x20)
            i += 2
        else:
            decoded.append(frame[i])
            i += 1

    if len(decoded) < 3: return  # Za krótka ramka

    addr = decoded[0]
    data = decoded[1:-2]
    crc = decoded[-2:]

    if addr == 0x31 and len(data) == 4:
        temp = struct.unpack('<f', data)[0]  # Dekoduj float (Little Endian)
        return temp
    return None


# Główna pętla odbierania
buffer = bytearray()
while True:
    byte = ser.read(1)
    if not byte: continue

    buffer.extend(byte)
    if byte == b'\x7e' and len(buffer) > 1:
        # Mamy potencjalną ramkę
        temperature = decode_frame(buffer)
        if temperature is not None:
            print(f"Odebrana temperatura historyczna: {temperature:.2f} °C")
        buffer = bytearray([0x7e])  # Zacznij nową ramkę od tego samego znaku