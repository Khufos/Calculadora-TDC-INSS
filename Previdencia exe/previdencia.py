from PyQt5 import QtWidgets, uic
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys
from PyQt5.QtCore import Qt

lista = []


def opcao_selecionada():
    global total, dia, mes, ano, dia1, mes1, ano1, d1, d2, diff, soma_anos

    try:
        dia = tela.comboBox.currentText()
        mes = tela.comboBox_2.currentText()
        ano = tela.lineEdit.text()
        dia1 = tela.comboBox_3.currentText()
        mes1 = tela.comboBox_4.currentText()
        ano1 = tela.lineEdit_2.text()
        d1 = datetime(int(ano), int(mes), int(dia))
        d2 = datetime(int(ano1), int(mes1), int(dia1))
        # diferença entre d1 e d2
        diff = relativedelta(d2, d1)
        total = (f"{diff.years} anos, {diff.months} meses, {diff.days} dias")
        tela.label.setText(total)
        dias_divisao = f"{diff.days / 30:.3f}"
        mes_soma = f"{float(diff.months) + float(dias_divisao)}"
        div_doze = f"{float(mes_soma) / 12:.3f}"
        soma_anos = f"{float(diff.years) + float(div_doze)}"

    except:
        tela.label_5.setText("Você esqueceu de digitar algo!!!")


def lista_dados():
    try:
        tela.listWidget.addItem(
            f"DATA/INICIO: {str(dia)}/{str(mes)}/{str(ano)}|DATA/SAIDA: {str(dia1)}/{str(mes1)}/{str(ano1)} | {total} | {soma_anos}")
    except:
        tela.label_5.setText("Você esqueceu de digitar algo!!!")


def deletar():
    tela.listWidget.clear()


def apagar():
    tela.listWidget.takeItem(tela.listWidget.currentRow())


def total_tempo():
    total_num = 0
    try:
        md = tela.lineEdit_3.text()
        lista.append(md)  # 1
        for valor in lista:
            total_num += float(valor)
        rest = f"{total_num:.3f}"
        tela.listWidget_2.addItem(str(rest))

    except:
        tela.label_5.setText("Você esqueceu de digitar algo!!!")


def limpar():
    global lista
    lista = []
    tela.listWidget_2.clear()


def total_total():
    try:
        valor_total = float(tela.lineEdit_4.text())
        doze = 12
        valor = str(valor_total)
        a = valor.split("-")
        valor = float(a[0][2:])
        valor_mes = (valor * doze)
        valor_int = int(valor_mes)
        d = (valor_mes - (valor_int * 1.000))
        dias = (f"{d:.3f}")
        dias_div = float(dias)
        dias_cor = (dias_div * 30)
        pra = (f"{dias_cor:.1f}")
        tela.label_7.setText(f"{a[0][:2]} Anos  {valor_int} meses  {pra[:2]} dias")
    except:
        tela.label_5.setText(
            "Você esqueceu de digitar algo ou está usando vírgula invés de ponto para fazer o calculo.")


def sair():
    tela.close()



app = QtWidgets.QApplication([])
tela = uic.loadUi("listaa.ui")
"""tela.setWindowFlag(Qt.FramelessWindowHint)"""
tela.comboBox.addItems(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
                        "13", "14", "15", "16", "17", "18", "19", "20", "21", "22",
                        "23", "24", "25", "26", "27", "28", "29", "30", "31"])
tela.comboBox_2.addItems(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "12"])
tela.comboBox_3.addItems(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
                          "13", "14", "15", "16", "17", "18", "19", "20", "21", "22",
                          "23", "24", "25", "26", "27", "28", "29", "30", "31"])
tela.comboBox_4.addItems(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "12"])

tela.pushButton.clicked.connect(opcao_selecionada)
tela.pushButton_2.clicked.connect(lista_dados)
tela.pushButton_4.clicked.connect(deletar)
tela.pushButton_3.clicked.connect(apagar)
tela.pushButton_5.clicked.connect(total_tempo)
tela.pushButton_6.clicked.connect(limpar)
tela.pushButton_7.clicked.connect(total_total)
tela.pushButton_8.clicked.connect(sair)
tela.show()
app.exec()
