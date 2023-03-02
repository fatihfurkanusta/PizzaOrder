from PyQt5.QtWidgets import *
from PizzaOrderWindow import Ui_MainWindow
import csv
from datetime import datetime
import pizzaOrder


class main(QMainWindow):
    def __init__(self):
        self.price_pizza = 0    # seçilen pizza tabanının fiyatını tutan değişken
        self.price_sauce = 0    # seçilen sosların fiyatını tutan değişken
        self.pizza2 = ""    # seçilen pizza tabanı
        self.sauce_list = []    # seçilen sosların listesi
        self.database_list = []     # Database'ye atılacak bilgilerin listesi

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ödemeyi tamamlama butonuna metot atama
        self.ui.pushButton_finish.clicked.connect(self.FinishClicked)
        
        # CheckBoxlarına metot atama - start
        self.ui.btn_group = QButtonGroup() # Pizza boxlarını grupluyorum. Sadece tek bir tanesi seçilebilmesi için.
        self.ui.btn_group.addButton(self.ui.cbox_clasic,1)
        self.ui.btn_group.addButton(self.ui.cbox_margharita,2)
        self.ui.btn_group.addButton(self.ui.cbox_turkish,3)
        self.ui.btn_group.addButton(self.ui.cbox_simple,4)

        self.ui.cbox_clasic.toggled.connect(self.pizza) # Pizza boxları
        self.ui.cbox_margharita.toggled.connect(self.pizza)
        self.ui.cbox_turkish.toggled.connect(self.pizza)
        self.ui.cbox_simple.toggled.connect(self.pizza)

        self.ui.cbox_sauce_olive.toggled.connect(self.sauce) # Sos boxları
        self.ui.cbox_sauce_mushroom.toggled.connect(self.sauce)
        self.ui.cbox_sauce_goatCheese.toggled.connect(self.sauce)
        self.ui.cbox_sauce_meat.toggled.connect(self.sauce)
        self.ui.cbox_sauce_onion.toggled.connect(self.sauce)
        self.ui.cbox_sauce_corn.toggled.connect(self.sauce)
        # CheckBoxlar - end
    
    # CheckBoxlar ile ilgili metotlar - start
    def pizza(self): # Pizza Metotu
        choose = self.sender()
        if choose.isChecked():
            self.price_pizza = 0
            match choose:
                case self.ui.cbox_clasic:
                    self.pizza2 = "Klasik Pizza"
                    self.price_pizza += pizzaOrder.Clasic().get_cost()
                case self.ui.cbox_margharita:
                    self.pizza2 = "Margarita"
                    self.price_pizza += pizzaOrder.Margherita().get_cost()
                case self.ui.cbox_turkish:
                    self.pizza2 = "Türk Pizza"
                    self.price_pizza += pizzaOrder.Turkish().get_cost()
                case self.ui.cbox_simple:
                    self.pizza2 = "Sade Pizza"
                    self.price_pizza += pizzaOrder.Simple().get_cost()
        self.ui.line_price.setText(str(self.price_pizza + self.price_sauce)+" ₺")
    
    def sauce(self):  # Sos Metotu
        choose = self.sender()  # Seçilen checkBox'ı return eden fonksiyon
        if choose.isChecked():     
            match choose:    # match - case yapısı ile seçilen checkboxa göre işlem ataması yapıyorum
                case self.ui.cbox_sauce_olive:
                    self.sauce_list.append("Zeytin")  # Zeytin seçildiğinde sauce_list listesine ekliyorum
                    self.price_sauce += pizzaOrder.Olive().get_cost()  #pizzaOrder classından çağırdığım get_cost metodu ile zeytin tutarını genel tutara ekliyorum
                case self.ui.cbox_sauce_mushroom:
                    self.sauce_list.append("Mantar")
                    self.price_sauce += pizzaOrder.Mushroom().get_cost()
                case self.ui.cbox_sauce_goatCheese:
                    self.sauce_list.append("Keçi Peyniri")
                    self.price_sauce += pizzaOrder.GoatCheese().get_cost()
                case self.ui.cbox_sauce_meat:
                    self.sauce_list.append("Et")
                    self.price_sauce += pizzaOrder.Meat().get_cost()
                case self.ui.cbox_sauce_onion:
                    self.sauce_list.append("Soğan")
                    self.price_sauce += pizzaOrder.Onion().get_cost()
                case self.ui.cbox_sauce_corn:
                    self.sauce_list.append("Mısır")
                    self.price_sauce += pizzaOrder.Corn().get_cost()
        else:
            match choose:       # match - case yapısı ile seçiminden vazgeçilen checkboxa göre işlem ataması yapıyorum
                case self.ui.cbox_sauce_olive:
                    self.sauce_list.remove("Zeytin")    # Zeytin seçiminden vazgeçildiğinde sauce_list listesinden çıkarıyorum
                    self.price_sauce -= pizzaOrder.Olive().get_cost()   #pizzaOrder classından çağırdığım get_cost metodu ile zeytin tutarını genel tutardan çıkarıyorum
                case self.ui.cbox_sauce_mushroom:
                    self.sauce_list.remove("Mantar")
                    self.price_sauce -= pizzaOrder.Mushroom().get_cost()
                case self.ui.cbox_sauce_goatCheese:
                    self.sauce_list.remove("Keçi Peyniri")
                    self.price_sauce -= pizzaOrder.GoatCheese().get_cost()
                case self.ui.cbox_sauce_meat:
                    self.sauce_list.remove("Et")
                    self.price_sauce -= pizzaOrder.Meat().get_cost()
                case self.ui.cbox_sauce_onion:
                    self.sauce_list.remove("Soğan")
                    self.price_sauce -= pizzaOrder.Onion().get_cost()
                case self.ui.cbox_sauce_corn:
                    self.sauce_list.remove("Mısır")
                    self.price_sauce -= pizzaOrder.Corn().get_cost()
        
        self.ui.line_price.setText(str(self.price_pizza + self.price_sauce)+" ₺") # Yapılan hesabı tutarı gösteren line'ye atıyorum
    # CheckBoxlar ile ilgili metotlar - end

    # Ödemeyi Tamamla Butonu metodu - start
    def FinishClicked(self):
        
        if not(self.ui.line_price.text() and self.ui.line_name.text() and self.ui.line_id.text() and self.ui.line_credit_number.text() and self.ui.line_price.text() and self.ui.line_credit_pass.text()):
            QMessageBox.about(self, "Hata", "Lütfen tüm bilgilerinizi giriniz.") # Bilgilerin eksik girilmesi halinde kullanıcıya gönderilen hata mesajı.

        else:
            now = datetime.now()        # Datetime modülü ile tuşa basıldığı andaki zamanı aldık
            time = now.strftime("%Y-%m-%d %H:%M:%S")    # milisaniye gösterilmesini istemediğim için formatı değiştirdim

            sauce_list2 = []        
            for i in self.sauce_list:
                sauce_list2.append(i)

            user_info = {'Ad':self.ui.line_name.text(),'Soyad':self.ui.line_id.text(),'Kredi Kartı Numarası':self.ui.line_credit_number.text(),'Kredi Kartı Parolası':self.ui.line_credit_pass.text(),'Pizza Tabanı':self.pizza2,'Soslar':sauce_list2,'Tarih':time}
            self.database_list.append(user_info)
            
            with open("Orders_Database.csv", "w") as file:  # Orders_Database.csv dosyasına yazdırma işlemi yapıyorum
                fieldnames = self.database_list[0].keys()
                file_write =csv.DictWriter(file,fieldnames=fieldnames)
                file_write.writeheader()
                file_write.writerows(self.database_list) 
        
        # Butona basıldıktan sonra tekrar işlem yapılabilmesi için line ve checkboxları temizliyorum
        self.ui.cbox_sauce_olive.setChecked(False)
        self.ui.cbox_sauce_mushroom.setChecked(False)
        self.ui.cbox_sauce_goatCheese.setChecked(False)
        self.ui.cbox_sauce_meat.setChecked(False)
        self.ui.cbox_sauce_onion.setChecked(False)
        self.ui.cbox_sauce_corn.setChecked(False)
        self.ui.line_name.setText("")
        self.ui.line_id.setText("")
        self.ui.line_credit_number.setText("")
        self.ui.line_credit_pass.setText("")
        
    # Ödemeyi Tamamla Butonu metodu - end


# GUI çalıştırma işlemleri 
app = QApplication([])
window = main()
window.show()
app.exec_()    

