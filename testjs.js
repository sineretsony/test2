
var doc = app.activeDocument;

var fileName = doc.name;

if (fileName == "001_IECHO.ai") {
    // Снимаем блокировку со всех слоев
for (var i = 0; i < doc.layers.length; i++) {
    var layer = doc.layers[i];
    layer.locked = false;
}

// Получаем слой CUT
var cutLayer = doc.layers.getByName('CUT');
// Получаем слой MARKS
var marksLayer = doc.layers.getByName('MARKS');
// Получаем слой Info
var infoLayer = doc.layers.getByName('Info');
// Получаем слой PRINT
var printLayer = doc.layers.getByName('PRINT');



// Если CUT включен - Отключаем видимость слоя CUT
if (cutLayer.visible) {
    cutLayer.visible = false;
}

// Если MARKS выключен - Включаем MARKS
if (!marksLayer) {
    marksLayer.visible = true;
}

// Если PRINT выключен - Включаем PRINT
if (!printLayer.visible) {
    printLayer.visible = true;
}


// Если документ содержит XXXXXX - Удаляем этот элемент

try {
  infoLayer = doc.layers.getByName('Info');

  // Проверяем видимость слоя
  if (infoLayer.visible) {

    // Перебираем все элементы на слое Info
    for (var i = infoLayer.pageItems.length - 1; i >= 0; i--) {
      var currentItem = infoLayer.pageItems[i];

      // Проверяем, является ли элемент текстовым фреймом
      if (currentItem.typename === 'TextFrame') {
        // Если это текстовый фрейм, проверяем его содержимое
        if (currentItem.contents === 'XXXXXX') {
          // Если содержимое текстового фрейма равно 'XXXXXX', удаляем элемент
          currentItem.remove();
        }
      }
    }

  } else {
    // Видимость слоя выключена
  }

 } catch (e) {
  // Если слой не существует, обрабатываем исключение
  // Например, можно добавить сюда код для случая отсутствия слоя
}

// Сохраняем на раб стол пдф с именем PRINT_IECHO
var desktopPath = Folder.desktop;
var pdfPath = new File(desktopPath + "/PRINT_IECHO.pdf");
var saveOpts = new PDFSaveOptions();

if (pdfPath != null) {
    doc.saveAs(pdfPath, saveOpts);
}

// Включаем слой CUT
if (cutLayer) {
    cutLayer.visible = true;
}

// Если слой info выключен - Включаем слой info
if (!infoLayer.visible) {
    infoLayer.visible = true;
}

// Удаляем слой info
if (infoLayer) {
    infoLayer.remove();
}

// Удадяем слой PRINT
if (printLayer) {
    printLayer.remove();
}

// Получаем все монтажные области
var artboards = doc.artboards;

// Оставляем только первую монтажную область
for (var i = artboards.length - 1; i > 0; i--) {
    artboards[i].remove();
}

// Обновляем документ после удаления монтажных областей
doc.artboards = artboards;

// Получаем массив всех объектов в документе
var objects = doc.pageItems;

// Получаем границы монтажной области
var artboardBounds = doc.artboards[0].artboardRect;

// Проходимся по массиву в обратном порядке
for (var i = objects.length - 1; i >= 0; i--) {
    // Получаем границы текущего объекта
    var objectBounds = objects[i].geometricBounds;

    // Проверяем, находится ли объект в монтажной области
    var insideArtboard = objectBounds[0] >= artboardBounds[0] && objectBounds[1] <= artboardBounds[1] && objectBounds[2] <= artboardBounds[2] && objectBounds[3] >= artboardBounds[3];

    // Если объект не в монтажной области, удаляем его
    if (!insideArtboard) {
        objects[i].remove();
    }
}


// Экспортируем в DXF
var saveFile = new File(doc.path + "/" + doc.name.replace(/\.[^\.]+$/, '') + ".dxf");

    // Установите параметры экспорта DXF
    var options = new ExportOptionsAutoCAD();
    options.exportFileFormat = AutoCADExportFileFormat.DXF; // Правильное значение формата
    options.version = AutoCADCompatibility.AutoCADRelease14; // Версия AutoCAD

    // Экспортируйте документ
    doc.exportFile(saveFile, ExportType.AUTOCAD, options);

//---------------------------------------------------------
//---------------------------------------------------------
//---------------------------------------------------------
//---------------------------------------------------------

} else if (fileName == "003_F-MARK.ai" || fileName == "003_F-MARK_KRAFT_320x450.ai") {
	var artboards = doc.artboards;

// Снимаем блокировку со всех слоев
for (var i = 0; i < doc.layers.length; i++) {
    var layer = doc.layers[i];
    layer.locked = false;
}

// Получаем слой CUT
var cutLayer = doc.layers.getByName('CUT');
// Получаем слой FRAME
var frameLayer = doc.layers.getByName('FRAME');
// Получаем слой INFO
//var infoLayer = doc.layers.getByName('INFO');
// Получаем слой PRINT
var printLayer = doc.layers.getByName('PRINT');

// Перекрашиваем все объекты на слое CUT в обводку C0 M0 Y0 K100 и толщиной 0.35 мм
for (var i = 0; i < cutLayer.pathItems.length; i++) {
    var pathItem = cutLayer.pathItems[i];
    pathItem.filled = false;
    pathItem.stroked = true;
    pathItem.strokeWidth = 1.00;
    pathItem.strokeColor = new CMYKColor();
    pathItem.strokeColor.cyan = 0;
    pathItem.strokeColor.magenta = 0;
    pathItem.strokeColor.yellow = 0;
    pathItem.strokeColor.black = 100;
    pathItem.strokeOverprint = false;
}

// Отключаем видимость слоя FRAME и CUT

if (frameLayer) {
    frameLayer.visible = false;
}

if (cutLayer) {
    cutLayer.visible = false;
}

/// Получаем слой INFO
var infoLayer;

try {
  infoLayer = doc.layers.getByName('INFO');

  // Проверяем видимость слоя
  if (infoLayer.visible) {

    // Перебираем все элементы на слое INFO
    for (var i = infoLayer.pageItems.length - 1; i >= 0; i--) {
      var currentItem = infoLayer.pageItems[i];

      // Проверяем, является ли элемент текстовым фреймом
      if (currentItem.typename === 'TextFrame') {
        // Если это текстовый фрейм, проверяем его содержимое
        if (currentItem.contents === 'XXXXXX') {
          // Если содержимое текстового фрейма равно 'XXXXXX', удаляем элемент
          currentItem.remove();
        }
      }
    }

  } else {
    // Видимость слоя выключена
  }

} catch (e) {
  // Если слой не существует, обрабатываем исключение
  // Например, можно добавить сюда код для случая отсутствия слоя
}

// Проверяем количество монтажных областей
if (artboards.length > 1) {
 // Проходим по всем монтажным областям
  for (var i = 0; i < artboards.length; i++) {
    // Получаем координаты монтажной области
    var artboardRect = artboards[i].artboardRect;

    // Создаем текстовый объект с номером
    var textItem = printLayer.textFrames.add();
    textItem.contents = ("000" + (i + 1)).slice(-3); // Форматируем номер в формате "001", "002"
    textItem.top = artboardRect[1] - 52; // Располагаем вверху от монтажной области
    textItem.left = artboardRect[0] + 32; // Располагаем слева от монтажной области

  }
}

// Сохраняем документ в PDF с именем "PRINT" на рабочий стол
var desktopPath = Folder.desktop;
var pdfPath = new File(desktopPath + "/PRINT.pdf");
var saveOpts = new PDFSaveOptions();

if (pdfPath != null) {
    doc.saveAs(pdfPath, saveOpts);
}

// Включаем видимость слоя FRAME - думаю можно будет удалить
if (frameLayer) {
    frameLayer.visible = true;
}

// Проходим по всем слоям в документе
for (var j = 0; j < doc.layers.length; j++) {
    var currentLayer = doc.layers[j];

    // Включаем видимость слоя, если он выключен
    if (!currentLayer.visible) {
        currentLayer.visible = true;
    }
}

// Удаляем все слои кроме MARKS и CUT
for (var i = doc.layers.length - 1; i >= 0; i--) {
    var layer = doc.layers[i];
    if (layer.name !== 'MARKS' && layer.name !== 'CUT') {
        layer.remove();
    }
}

// Включаем видимость слоя CUT
if (cutLayer) {
    cutLayer.visible = true;
}

// Получаем все монтажные области
var artboards = doc.artboards;

// Оставляем только первую монтажную область
for (var i = artboards.length - 1; i > 0; i--) {
    artboards[i].remove();
}

// Обновляем документ после удаления монтажных областей
doc.artboards = artboards;

// Получаем массив всех объектов в документе
var objects = doc.pageItems;

// Получаем границы монтажной области
var artboardBounds = doc.artboards[0].artboardRect;

// Проходимся по массиву в обратном порядке
for (var i = objects.length - 1; i >= 0; i--) {
    // Получаем границы текущего объекта
    var objectBounds = objects[i].geometricBounds;

    // Проверяем, находится ли объект в монтажной области
    var insideArtboard = objectBounds[0] >= artboardBounds[0] && objectBounds[1] <= artboardBounds[1] && objectBounds[2] <= artboardBounds[2] && objectBounds[3] >= artboardBounds[3];

    // Если объект не в монтажной области, удаляем его
    if (!insideArtboard) {
        objects[i].remove();
    }
}


// Сохраняем файл в AI формате с именем "CUT" на рабочий стол
var aiPath = new File(desktopPath + "/CUT.ai");
if (aiPath != null) {
    var aiSaveOpts = new IllustratorSaveOptions();
    aiSaveOpts.compatibility = Compatibility.ILLUSTRATOR8;
    aiSaveOpts.pdfCompatible = true;
    doc.saveAs(aiPath, aiSaveOpts);
}
} else if (fileName == "003_F-MARK.ai" || fileName == "002_MGI_IECHO_B690.ai") {
	 // Снимаем блокировку со всех слоев
for (var i = 0; i < doc.layers.length; i++) {
    var layer = doc.layers[i];
    layer.locked = false;
}
//----------------------------------------------------
// Экспорт в TIFF с использованием монтажных областей
function exportFileToTIFF(fileName) {
  if (app.documents.length > 0) {
    var exportOptions = new ExportOptionsTIFF();
    exportOptions.resolution = 360;
    exportOptions.byteOrder = TIFFByteOrder.IBMPC;
    exportOptions.IZWCompression = false;
    exportOptions.saveMultipleArtboards = true; // Экспорт нескольких монтажных областей
    exportOptions.artboardRange = ''; // Задание диапазона монтажных областей, например, с 1 по 2

    var type = ExportType.TIFF;
    var fileSpec = new File('~/Desktop/' + fileName + '.tiff');

    app.activeDocument.exportFile(fileSpec, type, exportOptions);
  }
}
//----------------------------------------------------

// Получаем слой VARNISH
var varnishLayer = doc.layers.getByName('VARNISH');
// Получаем слой FOIL
var foilLayer = doc.layers.getByName('FOIL');
// Получаем слой CUT
var cutLayer = doc.layers.getByName('CUT');
// Получаем слой IECHO_MARK
var iechomarkLayer = doc.layers.getByName('IECHO_MARK');
// Получаем слой PRINT
var printLayer = doc.layers.getByName('PRINT');
// Получаем слой MGI_MARK
var mgimarkLayer = doc.layers.getByName('MGI_MARK');

// Управляющие переменные
var varnish = false
var foil = false
var marks = false
var cut = false
var iechoMarks = false

// Если слой VARNISH включен - переменная VARNISH = true
if (varnishLayer.visible) {
    varnish = true;
}
// Если слой FOIL включен - переменная FOIL = true
if (foilLayer.visible) {
    foil = true;
}

// Если слой CUT включен - отключаем его
// Если слой CUT включен - переменная cut = true
if (cutLayer.visible) {
    cutLayer.visible = false;
	cut = true;
}
// Если слой IECHO_MARK включен — переменная iechoMarks = true
if (iechomarkLayer.visible) {
    iechoMarks = true;

// Если слой VARNISH включен — отключаем его
if (varnishLayer) {
    varnishLayer.visible = false;
}
// Если слой FOIL включен — отключаем его
if (foilLayer) {
    foilLayer.visible = false;
}

// Сохраняем в пдф на рабочий стол с именем PRINT_MGI
var desktopPath = Folder.desktop;
var pdfPath = new File(desktopPath + "/PRINT_MGI.pdf");
var saveOpts = new PDFSaveOptions();

if (pdfPath != null) {
    doc.saveAs(pdfPath, saveOpts);
}
// Если переменная VARNISH = true
// Экспортируем все монтажные области в тиф 360 точек с именами varnish-01-02 и тд
 if (varnish) {
    exportFileToTIFF('VARNISH');
}
// Если переменная FOIL = true
// Экспортируем все монтажные области в тиф 360 точек с именами foil-01-02 и тд
 if (foil) {
    exportFileToTIFF('FOIL');
}
// Отключаем слой IECHO_MARK если он включен
// Если слой IECHO_MARK был включен - переменная IECHO_MARK = true
if (iechomarkLayer.visible) {
    iechomarkLayer.visible = false;
	marks = true;
}
// Отключаем слой PRINT если он включен
if (printLayer.visible) {
    printLayer.visible = false;
}
// Отключаем слой MGI_MARK если он включен
if (mgimarkLayer.visible) {
    mgimarkLayer.visible = false;
}
// Если слой VARNISH выключен и переменная VARNISH true - Включаем слой VARNISH
// Экспортируем все монтажные области в тиф 360 точек с именами VT-01-02 и тд
// Выключаем слой VARNISH
if (!varnishLayer.visible && varnish) {
    varnishLayer.visible = true;
	exportFileToTIFF('VT');
	varnishLayer.visible = false;
}
// Если слой FOIL выключен и переменная FOIL true - Включаем слой FOIL
// Экспортируем все монтажные области в тиф 360 точек с именами FT-01-02 и тд
// Выключаем слой FOIL
if (!foilLayer.visible && foil) {
    foilLayer.visible = true;
	exportFileToTIFF('FT');
	foilLayer.visible = false;
}
// Если переменная CUT и IECHO_MARK = true
if (cut && iechoMarks) {
	// Удаляем слой PRINT
	if (printLayer) {
		printLayer.visible = true
		printLayer.remove();
	}
	// Удаляем слой MGI_MARK
	if (mgimarkLayer) {
		mgimarkLayer.visible = true
		mgimarkLayer.remove();
	}
	// Удаляем слой VARNISH
	if (varnishLayer) {
		varnishLayer.visible = true
		varnishLayer.remove();
	}

	// Удаляем слой FOIL
	if (foilLayer) {
		foilLayer.visible = true
		foilLayer.remove();
	}
	// Включаем слой CUT
	cutLayer.visible = true;
	// Включаем слой IECHO_MARK
	iechomarkLayer.visible = true;

	//----------------------------------------
	// ДО ЛУЧШИХ ВРЕМЁН

	// Группируем все оставшиеся объекты
	// Создаем группу для всех объектов
//    var mainGroup = doc.groupItems.add();

    // Проходим по всем слоям документа
    // Создаем группу для всех объектов
//    var mainGroup = doc.groupItems.add();

    // Проходим по всем слоям документа
    // Создаем группу для всех объектов
//    var mainGroup = doc.groupItems.add();

    // Проходим по всем слоям документа
//    var cutLayer = null;
//    for (var i = 0; i < doc.layers.length; i++) {
//        if (doc.layers[i].name === "CUT") {
//            cutLayer = doc.layers[i];
//            break;
//        }
//    }

    // Если слой не найден, создаем новый
//    if (cutLayer === null) {
//        cutLayer = doc.layers.add();
//        cutLayer.name = "CUT";
//    }

    // Перемещаем все объекты на слой CUT
//    for (var i = 0; i < doc.layers.length; i++) {
//        var layer = doc.layers[i];

        // Создаем массив для хранения объектов слоя
//        var itemsToMove = [];

        // Проходим по всем объектам слоя и добавляем их в массив
//        for (var j = layer.pageItems.length - 1; j >= 0; j--) {
//            itemsToMove.push(layer.pageItems[j]);
//        }

        // Перемещаем объекты из массива на слой CUT
//        for (var k = 0; k < itemsToMove.length; k++) {
//            itemsToMove[k].move(cutLayer, ElementPlacement.PLACEATEND);
//        }
//    }

    // Создаем группу для всех объектов на слое CUT
//    var mainGroup = cutLayer.groupItems.add();

    // Перемещаем все объекты из слоя CUT в группу
//    for (var l = 0; l < cutLayer.pageItems.length; l++) {
//        cutLayer.pageItems[l].move(mainGroup, ElementPlacement.PLACEATEND);
//    }



    // Вращаем главную группу на 90 градусов по часовой стрелке
//    mainGroup.rotate(90);
}

}
}

var dialog = new Window("dialog", "Done");
dialog.size = [200, 100]; // Устанавливаем размер панели

var text = dialog.add("statictext", undefined, "Files saved!");

var closeButton = dialog.add("button", undefined, "Close");
closeButton.onClick = function () {
    dialog.close();
};

dialog.show();
