# task 2

import logging


def write_file(fill_path, data):
    try:
        with open(fill_path, "w") as file:
            logger = logging.getLogger("Calculator")
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler())
            file.write(data)
            logger.info("Успiшно записали в файл")
    except Exception as ex:
        logger.error(f"В вашем файлу {fill_path} трапилось помилка {ex}")


logging.basicConfig(level=logging.INFO)
write_file("output.txt", input("Введiть що треба вписати файл: "))
