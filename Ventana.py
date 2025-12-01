import sys 
from PyQt6.QtWidgets import QApplication, QWidget

class Ventana_Vacia(QWidget):  #Aca estariamos creando la clase
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(100, 100, 250, 250)  #Le damos la dimension a la ventana
        self.setWindowTitle("Mi primera ventana")
        self.show()    
        

if __name__ == "__main__":  #creo que esto simula ser el main. Me parece que hay que borrarlo 
    app = QApplication(sys.argv)
    ventana = Ventana_Vacia()
    sys.exit(app.exec())
