from os import path
import struct
import sys


def resize():
    if len(sys.argv) == 4 and 0 < int(sys.argv[1]) < 100 and path.exists(sys.argv[2]) and path.exists(sys.argv[3]):
        increasing = int(sys.argv[1])
        # ----------------------------------------------------------------------------------
        # --------------------------зчитую старий header зображення-------------------------
        with open(sys.argv[2], "rb") as file_r:
            data = file_r.read()
            off_set_bits = struct.unpack('i', data[10:14])
            size_title = struct.unpack('i', data[14:18])
            width = struct.unpack('i', data[18:22])
            height = struct.unpack('i', data[22:26])
            planes = struct.unpack('h', data[26:28])
            bit_count = struct.unpack('h', data[28:30])
            compression = struct.unpack('i', data[30:34])
            x_pels_per_meter = struct.unpack('i', data[38:42])
            y_pels_per_meter = struct.unpack('i', data[42:46])
            colors_used = struct.unpack('i', data[46:50])
            colors_important = struct.unpack('i', data[50:54])
        if data[:2] == b'BM':
            # ------------------------------------------------------------------------------
            # ------------------деякі розрахунки перевів в змінні для зручності-------------

            px = int(bit_count[0] / 8)
            add_bytes = 4 - (width[0] * px * increasing) % 4
            multiplicity_by_4 = (width[0] * px * increasing) % 4
            skip_bytes = 4 - (width[0] * px) % 4

            x1 = off_set_bits[0]
            x2 = off_set_bits[0] + px
            y1 = off_set_bits[0]
            y2 = off_set_bits[0] + px

            size_image = (((width[0] * increasing * px) + add_bytes) * (abs(height[0]) * increasing)
                          if multiplicity_by_4 != 0 else width[0] * increasing * px * (abs(height[0]) * increasing))

            # -------------------------------------------------------------------------------
            # --------------------------створюю новий header зображення----------------------
            with open(sys.argv[3], "wb") as file:
                file.write(b'BM')
                file.write((size_image + off_set_bits[0]).to_bytes(4, byteorder="little"))
                file.write((0).to_bytes(2, byteorder="little"))
                file.write((0).to_bytes(2, byteorder="little"))
                file.write((off_set_bits[0]).to_bytes(4, byteorder="little"))
                file.write((size_title[0]).to_bytes(4, byteorder="little"))
                file.write((width[0] * increasing).to_bytes(4, byteorder="little"))
                file.write(struct.pack("i", height[0] * increasing))  # <-- перевертаю картинку
                file.write((planes[0]).to_bytes(2, byteorder="little"))
                file.write((bit_count[0]).to_bytes(2, byteorder="little"))
                file.write((compression[0]).to_bytes(4, byteorder="little"))
                file.write(size_image.to_bytes(4, byteorder="little"))
                file.write((x_pels_per_meter[0]).to_bytes(4, byteorder="little"))
                file.write((y_pels_per_meter[0]).to_bytes(4, byteorder="little"))
                file.write((colors_used[0]).to_bytes(4, byteorder="little"))
                file.write((colors_important[0]).to_bytes(4, byteorder="little"))
                # -----------------------------------------------------------------------------
                # ------------------------переписую саме зображення----------------------------
                count = 0
                while count != abs(height[0]):
                    for i in range(width[0]):
                        file.write(data[x1:x2] * increasing)
                        x1 += px
                        x2 += px
                    if multiplicity_by_4:
                        file.write((0).to_bytes(add_bytes, byteorder="little"))
                    for i in range(increasing - 1):
                        x1 = y1
                        x2 = y2
                        for j in range(width[0]):
                            file.write(data[x1:x2] * increasing)
                            x1 += px
                            x2 += px
                        if multiplicity_by_4:
                            file.write((0).to_bytes(add_bytes, byteorder="little"))
                    y1 = x1
                    y2 = x2
                    count += 1
                    if (width[0] * px) % 4:
                        x1 += skip_bytes
                        x2 += skip_bytes
                        y1 = x1
                        y2 = x2
        else:
            print("Картинка не є в 'BMP' форматі")
    else:
        print("Ви ввели невірні параметри")


if __name__ == '__main__':
    resize()

