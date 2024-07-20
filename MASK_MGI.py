# import cv2
# import numpy as np
#
# # Открываем первый файл VARNISH и временный файл temp_v
# varnish_image = cv2.imread('VARNISH.tif', cv2.IMREAD_UNCHANGED)
# temp_v_image = cv2.imread('temp_v.tif', cv2.IMREAD_UNCHANGED)
#
# # Преобразуем оба изображения в градации серого
# varnish_gray = cv2.cvtColor(varnish_image, cv2.COLOR_BGR2GRAY) if len(varnish_image.shape) == 3 else varnish_image
# temp_v_gray = cv2.cvtColor(temp_v_image, cv2.COLOR_BGR2GRAY) if len(temp_v_image.shape) == 3 else temp_v_image
#
# # Создаем новый альфа-канал
# alpha_channel = np.zeros_like(varnish_gray)
#
# # Вставляем временный файл в альфа-канал
# alpha_channel[temp_v_gray > 0] = 255
#
# # Объединяем изображение VARNISH с новым альфа-каналом
# result_image = cv2.merge([varnish_gray, varnish_gray, varnish_gray, alpha_channel])
#
# # Сохраняем результат
# cv2.imwrite('result.tif', result_image)

import cv2
import numpy as np
from PIL import Image

# Открываем первый файл VARNISH и временный файл temp_v
varnish_image = cv2.imread('VARNISH.tif', cv2.IMREAD_UNCHANGED)
temp_v_image = cv2.imread('temp_v.tif', cv2.IMREAD_UNCHANGED)

# Преобразуем оба изображения в градации серого
varnish_gray = cv2.cvtColor(varnish_image, cv2.COLOR_BGR2GRAY) if len(varnish_image.shape) == 3 else varnish_image
temp_v_gray = cv2.cvtColor(temp_v_image, cv2.COLOR_BGR2GRAY) if len(temp_v_image.shape) == 3 else temp_v_image

# Создаем новый альфа-канал
alpha_channel = np.zeros_like(varnish_gray)

# Вставляем временный файл в альфа-канал
alpha_channel[temp_v_gray > 0] = 255

# Конвертируем изображения в формат Pillow
varnish_pil = Image.fromarray(varnish_gray, mode='L')  # Градации серого
alpha_pil = Image.fromarray(alpha_channel, mode='L')  # Альфа-канал

# Создаем новый TIFF файл с двумя каналами (L = градации серого, A = альфа-канал)
tiff_image = Image.merge('LA', (varnish_pil, alpha_pil))

# Сохраняем изображение в формате TIFF
tiff_image.save('result.tif', format='TIFF')

