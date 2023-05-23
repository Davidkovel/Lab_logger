# task 3

import logging
import random


def real_data(file_path):
    try:
        with open(file_path, "w") as file:
            logger = logging.getLogger("File")
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler())
            rand = [str(random.randint(0, 100)) for i in range(5)]
            file.write("\n".join(rand))
            logger.info("Успiшно записали в файл")
    except Exception as ex:
        logging.error(f"Помилка {ex}")


logging.basicConfig(level=logging.INFO)
real_data(input("Введiть назву файл: "))