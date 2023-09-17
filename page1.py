from inc import *

class pagesWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 600)
        self.pages = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.pages_ = ""
        self.txt_name = ["Automatic Access","USERNAME","","PASSWORD", "","REGISTER","RESET","LOGIN","Login","Forgot username/password","Accept Terms"]
        self.sizes_position_x = ["155","31","62","93","124","248","248","248","217","217","186"]
        self.sizes_position_y = ["0","31","62","93","124","250","0","250","0","250","0"]
        self.item_show = [True,True,True,True,True,True,True,False,True,False,True,True]
        self.call_function = [self.check_access,self.page01,self.page01,self.page01,self.page01,self.register_,self.reset_forms,self.login_,self.page_forms,self.forgot_forms,self.check_accept]
        self.items0 = []
        self.group_ = QGroupBox(self)
        self.group_.setTitle("Registration Form")
        self.group_.resize(500, 600)
        self.group_.move(0, 20)
        for j in range(0, 11):
            if j == 5 or j == 6 or j == 7:
                self.item0 = QPushButton(self.group_)
                self.item0.setText(str(self.txt_name[j]))
                self.item0.setEnabled(True)
                self.item0.setVisible(self.item_show[j])
                self.item0.resize(249, 30)
                self.item0.move(int(self.sizes_position_y[j]), int(self.sizes_position_x[j]))
                self.item0.setStyleSheet("border: 2px solid black;")
                self.item0.clicked.connect(self.call_function[j])
                self.items0.append(self.item0)
            elif j == 1 or j == 3:
                self.item0 = QLabel(self.group_)
                self.item0.resize(498, 30)
                self.item0.move(1, int(self.sizes_position_x[j]))
                self.item0.setStyleSheet("border: 2px solid black;border-radius: 5px;")
                self.item0.setText(str(self.txt_name[j]))
                self.items0.append(self.item0)
            elif j == 0 or j == 10:
                self.item0 = QCheckBox(self.group_)
                self.item0.resize(498, 30)
                self.item0.move(1, int(self.sizes_position_x[j]))
                #self.item0.setStyleSheet("border: 2px solid black;border-radius: 5px;")
                self.item0.setText(str(self.txt_name[j]))
                self.item0.clicked.connect(self.call_function[j])
                
                self.items0.append(self.item0)
                
            elif j == 2 or j == 4:
                self.item0 = QLineEdit(self.group_)
                self.item0.resize(498, 30)
                self.item0.move(1, int(self.sizes_position_x[j]))
                self.item0.setStyleSheet("border: 2px solid black;border-radius: 5px;")
                self.item0.setText(str(j)+" : button")
                self.items0.append(self.item0)
            elif j == 8 or j == 9:
                self.item0 = QCommandLinkButton(self.group_)
                self.item0.setText(str(self.txt_name[j]))
                self.item0.setEnabled(True)
                self.item0.setVisible(self.item_show[j])
                self.item0.resize(248, 30)
                self.item0.move(int(self.sizes_position_y[j]), int(self.sizes_position_x[j]))
                self.item0.setStyleSheet("border: 2px solid black;")
                self.item0.clicked.connect(self.call_function[j])
                self.items0.append(self.item0)

        self.count = 0
        
    def page01(self):
        if self.count == 0:
            self.items0[1].setVisible(False)
            self.count = 1
        else:
            self.items0[1].setVisible(True)
            self.count = 0
        self.pages_ = "page"
        print("enabled")

    def login_(self):
        self.pages_ = "login"
        for j in range(0, len(self.items0)):
            self.items0[j].setVisible(False)
        self.group_.setTitle("Home Page")
        print(str(self.pages_)+" page")

    def register_(self):
        self.pages_ = "register"
        for j in range(0, len(self.items0)):
            self.items0[j].setVisible(False)
        self.group_.setTitle("Home Page")
        print(str(self.pages_)+" page")
    
    def forgot_(self):
        self.pages_ = "forgot"
        for j in range(0, len(self.items0)):
            self.items0[j].setVisible(False)
        self.group_.setTitle("Home Page")
        print(str(self.pages_)+" page")

    def page_forms(self):
        if self.items0[8].text() == "Login":
            self.items0[5].setVisible(False)
            self.items0[7].setVisible(True)
            self.items0[8].setText("Register")
            self.items0[9].setVisible(True)
            self.group_.setTitle("Login Form")
            print(str(self.pages_)+" page")
        else:
            self.items0[7].setVisible(False)
            self.items0[5].setVisible(True)
            self.items0[8].setText("Login")
            self.items0[9].setVisible(False)
            self.group_.setTitle("Registration Form")
            print(str(self.pages_)+" page")

    def check_access(self):
        if self.items0[0].isChecked() == True:
            print("on")
        else:
            print("off")  

    def reset_forms(self):
        self.items0[2].setText("")
        self.items0[4].setText("")
    
    def forgot_forms(self):
        self.pages_ = "forgotten"
        #for j in range(0, len(self.items0)):
        #    self.items0[j].setVisible(False)
        self.group_.setTitle("Reset password Page")
        print(str(self.pages_)+" page")
        print("forgotten")

    def check_accept(self):
        if self.items0[10].isChecked() == True:
            print("on")
        else:
            print("off")   

if __name__ == "__main__":
    
    qtapp = QtWidgets.QApplication(sys.argv)
    qtapp.setOrganizationName(companyName)
    qtapp.setOrganizationDomain(companyDomain)
    qtapp.setApplicationName(companyName)
    qtapp.setWindowIcon(QIcon(companyIcon))
   
    
    window = pagesWin()
    #window.page01()
    window.show()
    sys.exit(qtapp.exec_())




