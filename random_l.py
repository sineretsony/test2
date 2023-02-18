import win32com.client

# Создаем объект Illustrator
app = win32com.client.Dispatch('Illustrator.Apres_plication')

# Создаем новый документ
doc = app.Documents.Add()

# Устанавливаем размер документа
doc.Width = 94
doc.Height = 54