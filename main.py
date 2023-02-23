from PyQt6 import QtWidgets, QtCore
import sys
import re



class Slider(QtWidgets.QSlider):
    #класс слайдера с возможностью настроить цвет
    def __init__(self, color):
        #color - отвечает за цвет ползунка
        super().__init__()
        self.setOrientation(QtCore.Qt.Orientation(False))#вертикальная ореинтация
        self.setFixedSize(QtCore.QSize(100, 200))#размер каждого слайдера
        self.setRange(0, 255)#вилка минимального и миниммального значения. т.к rgb это 8 бит, то 256 значений может быть на канал
        style = 'QSlider::handle:vertical {\nbackground-color: ' + color + ';' + '\nborder-radius: 10px;' +'\n}'#задача стилей
        self.setStyleSheet(style)#применение стилей

class Display(QtWidgets.QLabel):
    #класс дисплея
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: rgb(0, 0, 0);')#настройка изначального цвета окна: чёрный

    def set_red_color(self, ratio):
        #изменение состояния красного канала
        #достаём из стилей цифровые значения каналов в виде списка
        #применение с изменённым каналом 
        style = self.styleSheet()
        colors = re.findall('(\d+)', style)
        self.setStyleSheet(f'background-color: rgb({ratio}, {colors[1]}, {colors[2]});')
    
    def set_green_color(self, ratio):
        #изменение состояния зелёного канала
        #достаём из стилей цифровые значения каналов в виде списка
        #применение с изменённым каналом 
        style = self.styleSheet()
        colors = re.findall('(\d+)', style)
        self.setStyleSheet(f'background-color: rgb({colors[0]}, {ratio}, {colors[2]});')
    
    def set_blue_color(self, ratio):
        #изменение состояния синего канала
        #достаём из стилей цифровые значения каналов в виде списка
        #применение с изменённым каналом 
        style = self.styleSheet()
        colors = re.findall('(\d+)', style)
        self.setStyleSheet(f'background-color: rgb({colors[0]}, {colors[1]}, {ratio});')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Palette')#название окна
        self.setFixedSize(QtCore.QSize(600, 600))#фиксированный размер окна

        #экземпляры необходимых классов
        slider_red = Slider('red')
        slider_green = Slider('green')
        slider_blue = Slider('blue')
        self.display = Display()


        #подсоединение обработчиков событий на измение состояния слайдера
        slider_red.valueChanged.connect(self.change_red_color)
        slider_green.valueChanged.connect(self.change_green_color)
        slider_blue.valueChanged.connect(self.change_blue_color)

        #создание разметки окна и добавление в неё элементы
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, 3)
        layout.addWidget(slider_red, 1, 0)
        layout.addWidget(slider_green, 1, 1)
        layout.addWidget(slider_blue, 1, 2)

        #   схема разметки окна
        #         0      |       1     |        2
        #   - - - - - - -| - - - - - - |- - - - - - - ᐅ
        # 0 | display    | display     | display
        # 1 | slider_red |slider_green |slider_blue
        # 2 |            |             |
        #   ▼



        #создание главного виджета окна и инициализация разметки
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        
        #применение виджета как основоного в окне
        self.setCentralWidget(widget)
        
    def change_red_color(self, value):
        #обработчик изменеия красного слайдера
        self.display.set_red_color(value)

    def change_green_color(self, value):
        #обработчик изменеия зелёного слайдера
        self.display.set_green_color(value)

    def change_blue_color(self, value):
        #обработчик изменеия синего слайдера
        self.display.set_blue_color(value)
    

if __name__ == '__main__':
    #запуск приложения
    app = QtWidgets.QApplication(sys.argv)#инициализация контекста приложения
    window = MainWindow()#инициализация окна
    window.show()#показ окна
    app.exec()#запуск цикла приложения
