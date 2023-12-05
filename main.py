from enigma import Enigma
from constantes import lista_de_letras, lista_de_rotores, lista_de_posicoes_dos_rotores
from tkinter import END
import customtkinter

combo_box_justify = "center"
combo_box_width = 75
combo_box_state = "readonly"

posicao_label_pares = [0,1]
posicao_inicial_pares = [1,[1,2]]
posicao_label_rotores = [6, 0]
posicao_inicial_rotores = [7,0]
posicao_do_titulo_inicial_rotores = [8,0]
posicao_do_label_da_posicao_inicial_rotores = [9,0]
posicao_da_posicao_inicial_rotores = [10,0]
posicao_label_caixa_de_texto = [0,3]
posicao_caixa_de_texto = [1, 3]
posicao_campo_mensagem = [10,3]

escolha_de_rotores = ["I","II","III"]
escolha_de_rotores_int = [1,2,3]
escolha_de_posicao_rotores = ["1","1","1"]
pares = [""] * 5
mensagem_digitada = ""

primeiro_rotor = [escolha_de_rotores_int[0], int(escolha_de_posicao_rotores[0])-1]
segundo_rotor = [escolha_de_rotores_int[1], int(escolha_de_posicao_rotores[1])-1]
terceiro_rotor = [escolha_de_rotores_int[2], int(escolha_de_posicao_rotores[2])-1]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x475")
        self.title("Enigma")
        self.grid_columnconfigure(3,weight=3)
        self.event_add("<<Digitou_Mensagem>>","<KeyPress>")
        self.enigma = Enigma(pares,primeiro_rotor,segundo_rotor,terceiro_rotor)

        # Campo de entrada de texto
        self.mensagem = customtkinter.CTkEntry(self, placeholder_text="Mensagem")
        self.mensagem.bind("<<Digitou_Mensagem>>",self.digitou)
        self.mensagem.grid(row=posicao_campo_mensagem[0], column=posicao_campo_mensagem[1], columnspan=3, padx=10, pady=10, sticky = "ew")

        # Labels dos Pares
        self.label_pares = customtkinter.CTkLabel(self, text="Pares de Letras")
        self.label_pares.grid(row=posicao_label_pares[0], column=posicao_label_pares[1], pady=(10,0), columnspan=2)

        self.label_par_1 = customtkinter.CTkLabel(self, text="1° Par:")
        self.label_par_1.grid(row=posicao_inicial_pares[0], column=posicao_inicial_pares[1][0]-1, padx=(10,0))

        self.label_par_2 = customtkinter.CTkLabel(self, text="2° Par:")
        self.label_par_2.grid(row=posicao_inicial_pares[0]+1, column=posicao_inicial_pares[1][0]-1, padx=(10,0))

        self.label_par_3 = customtkinter.CTkLabel(self, text="3° Par:")
        self.label_par_3.grid(row=posicao_inicial_pares[0]+2, column=posicao_inicial_pares[1][0]-1, padx=(10,0))

        self.label_par_4 = customtkinter.CTkLabel(self, text="4° Par:")
        self.label_par_4.grid(row=posicao_inicial_pares[0]+3, column=posicao_inicial_pares[1][0]-1, padx=(10,0))

        self.label_par_5 = customtkinter.CTkLabel(self, text="5° Par:")
        self.label_par_5.grid(row=posicao_inicial_pares[0]+4, column=posicao_inicial_pares[1][0]-1, padx=(10,0))

        # Combo box da escolha dos plugs
        self.plug_1 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_1.grid(row=posicao_inicial_pares[0], column=posicao_inicial_pares[1][0], padx=10, pady=10, sticky = "w")

        self.plug_2 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_2.grid(row=posicao_inicial_pares[0], column=posicao_inicial_pares[1][1], padx=10, pady=10, sticky = "w")

        self.plug_3 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_3.grid(row=posicao_inicial_pares[0]+1, column=posicao_inicial_pares[1][0], padx=10, pady=10, sticky = "w")

        self.plug_4 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_4.grid(row=posicao_inicial_pares[0]+1, column=posicao_inicial_pares[1][1], padx=10, pady=10, sticky = "w")

        self.plug_5 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_5.grid(row=posicao_inicial_pares[0]+2, column=posicao_inicial_pares[1][0], padx=10, pady=10, sticky = "w")

        self.plug_6 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_6.grid(row=posicao_inicial_pares[0]+2, column=posicao_inicial_pares[1][1], padx=10, pady=10, sticky = "w")

        self.plug_7 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_7.grid(row=posicao_inicial_pares[0]+3, column=posicao_inicial_pares[1][0], padx=10, pady=10, sticky = "w")

        self.plug_8 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_8.grid(row=posicao_inicial_pares[0]+3, column=posicao_inicial_pares[1][1], padx=10, pady=10, sticky = "w")

        self.plug_9 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_9.grid(row=posicao_inicial_pares[0]+4, column=posicao_inicial_pares[1][0], padx=10, pady=10, sticky = "w")

        self.plug_10 = customtkinter.CTkComboBox(self, command=self.escolha_pares,values=lista_de_letras, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.plug_10.grid(row=posicao_inicial_pares[0]+4, column=posicao_inicial_pares[1][1], padx=10, pady=10, sticky = "w")

        # Label dos Rotores
        self.label_rotor_1 = customtkinter.CTkLabel(self, text="1° Rotor")
        self.label_rotor_1.grid(row=posicao_label_rotores[0], column=posicao_label_rotores[1], padx=(10,0), sticky = "we")

        self.label_rotor_2 = customtkinter.CTkLabel(self, text="2° Rotor")
        self.label_rotor_2.grid(row=posicao_label_rotores[0], column=posicao_label_rotores[1]+1, padx=(10,0), sticky = "we")

        self.label_rotor_3 = customtkinter.CTkLabel(self, text="3° Rotor")
        self.label_rotor_3.grid(row=posicao_label_rotores[0], column=posicao_label_rotores[1]+2, padx=(10,0), sticky = "we")
        
        # Escolha dos Rotores
        self.rotor_1 = customtkinter.CTkComboBox(self, command=self.escolha_rotor, values=lista_de_rotores, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.rotor_1.grid(row=posicao_inicial_rotores[0], column=posicao_inicial_rotores[1], padx=10, pady=10, sticky = "we")
        self.rotor_1.set("I")

        self.rotor_2 = customtkinter.CTkComboBox(self, command=self.escolha_rotor,values=lista_de_rotores, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.rotor_2.grid(row=posicao_inicial_rotores[0], column=posicao_inicial_rotores[1]+1, padx=10, pady=10, sticky = "we")
        self.rotor_2.set("II")

        self.rotor_3 = customtkinter.CTkComboBox(self, command=self.escolha_rotor,values=lista_de_rotores, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.rotor_3.grid(row=posicao_inicial_rotores[0], column=posicao_inicial_rotores[1]+2, padx=10, pady=10, sticky = "we")
        self.rotor_3.set("III")

        # Label da Posição Inicial dos Rotores
        self.titulo_posicao_rotores = customtkinter.CTkLabel(self, text="Posição Inicial dos Rotores")
        self.titulo_posicao_rotores.grid(row=posicao_do_titulo_inicial_rotores[0], column=posicao_do_titulo_inicial_rotores[1], pady=(10,0), columnspan=3, sticky="we")
        
        self.texto_posicao_rotor_1 = customtkinter.CTkLabel(self, text="1° Rotor")
        self.texto_posicao_rotor_1.grid(row=posicao_do_label_da_posicao_inicial_rotores[0], column=posicao_do_label_da_posicao_inicial_rotores[1], padx=(10,0), sticky = "we")

        self.texto_posicao_rotor_2 = customtkinter.CTkLabel(self, text="2° Rotor")
        self.texto_posicao_rotor_2.grid(row=posicao_do_label_da_posicao_inicial_rotores[0], column=posicao_do_label_da_posicao_inicial_rotores[1]+1, padx=(10,0), sticky = "we")

        self.texto_posicao_rotor_3 = customtkinter.CTkLabel(self, text="3° Rotor")
        self.texto_posicao_rotor_3.grid(row=posicao_do_label_da_posicao_inicial_rotores[0], column=posicao_do_label_da_posicao_inicial_rotores[1]+2, padx=(10,0), sticky = "we")

        # Escolha dos Rotores
        self.posicao_rotor_1 = customtkinter.CTkComboBox(self, command=self.escolha_posicao, values=lista_de_posicoes_dos_rotores, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.posicao_rotor_1.grid(row=posicao_da_posicao_inicial_rotores[0], column=posicao_da_posicao_inicial_rotores[1], padx=10, pady=10, sticky = "we")
        self.posicao_rotor_1.set("1")

        self.posicao_rotor_2 = customtkinter.CTkComboBox(self, command=self.escolha_posicao,values=lista_de_posicoes_dos_rotores, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.posicao_rotor_2.grid(row=posicao_da_posicao_inicial_rotores[0], column=posicao_da_posicao_inicial_rotores[1]+1, padx=10, pady=10, sticky = "we")
        self.posicao_rotor_2.set("1")

        self.posicao_rotor_3 = customtkinter.CTkComboBox(self, command=self.escolha_posicao,values=lista_de_posicoes_dos_rotores, justify=combo_box_justify, width=combo_box_width, state=combo_box_state)
        self.posicao_rotor_3.grid(row=posicao_da_posicao_inicial_rotores[0], column=posicao_da_posicao_inicial_rotores[1]+2, padx=10, pady=10, sticky = "we")
        self.posicao_rotor_3.set("1")

        # Label Caixa do texto Encriptado/Decriptado
        self.label_caixa_de_texto = customtkinter.CTkLabel(self, text="Mensagem Encriptada/Decriptada")
        self.label_caixa_de_texto.grid(row=posicao_label_caixa_de_texto[0], column=posicao_label_caixa_de_texto[1], pady=(10,0), columnspan=3, sticky="we")

        # Caixa do texto Encriptado/Decriptado
        self.caixa_de_texto = customtkinter.CTkTextbox(self, width=100, height=50, corner_radius=25)
        self.caixa_de_texto.grid(row=posicao_caixa_de_texto[0], column=posicao_caixa_de_texto[1], padx=10, pady=10, columnspan=3, rowspan=8, sticky="nsew")

    # Funções do App
    def inicializa_enigma(self):
        # print(pares,primeiro_rotor,segundo_rotor,terceiro_rotor)
        self.enigma = Enigma(pares,primeiro_rotor,segundo_rotor,terceiro_rotor)

    def inicializa_rotores(self):
        primeiro_rotor[0] = escolha_de_rotores_int[0]
        primeiro_rotor[1] = int(escolha_de_posicao_rotores[0])-1
        segundo_rotor[0] = escolha_de_rotores_int[1]
        segundo_rotor[1] = int(escolha_de_posicao_rotores[1])-1
        terceiro_rotor[0] = escolha_de_rotores_int[2]
        terceiro_rotor[1] = int(escolha_de_posicao_rotores[2])-1
    
    def digitou(self, event):
        criptografia = ""
        if event.char != "\x08":
            criptografia = self.enigma.digitar(event.char)
        self.escrever(criptografia, event)
    
    def escrever(self, texto, event):
        if event.char == "\x08":
            self.caixa_de_texto.delete("end-2c","end")
        self.caixa_de_texto.insert("end",texto)

    def escolha_rotor(self, event):
        escolha_de_rotores[0] = self.rotor_1.get()
        escolha_de_rotores[1] = self.rotor_2.get()
        escolha_de_rotores[2] = self.rotor_3.get()
        # print(escolha_de_rotores)
        for rotor in escolha_de_rotores:
            escolha_de_rotores_int.pop(0)
            if rotor == "I":
                escolha_de_rotores_int.append(1)
            if rotor == "II":
                escolha_de_rotores_int.append(2)
            if rotor == "III":
                escolha_de_rotores_int.append(3)
            if rotor == "IV":
                escolha_de_rotores_int.append(4)
            if rotor == "V":
                escolha_de_rotores_int.append(5)
        # print(escolha_de_rotores_int)
        self.inicializa_rotores()
        self.inicializa_enigma()

    def escolha_posicao(self, event):
        escolha_de_posicao_rotores[0] = self.posicao_rotor_1.get()
        escolha_de_posicao_rotores[1] = self.posicao_rotor_2.get()
        escolha_de_posicao_rotores[2] = self.posicao_rotor_3.get()
        # print(escolha_de_posicao_rotores)
        self.inicializa_rotores()
        self.inicializa_enigma()

    def escolha_pares(self, event):
        existe = 0
        for i in range(5):
            if i == 0 and self.plug_1.get() != "" and self.plug_2.get() != "" and self.plug_1.get() != self.plug_2.get():
                ligacao = self.plug_1.get()+self.plug_2.get()
                for combinacao in pares:
                    if combinacao.find(ligacao[0]) != -1 or combinacao.find(ligacao[1]) != -1:
                        existe = 1
                if existe == 0:   
                    pares[i] = ligacao
            if i == 0 and self.plug_1.get() == "" and self.plug_2.get() == "":
                pares[i] = ""
            existe = 0
            if i == 1 and self.plug_3.get() != "" and self.plug_4.get() != "" and self.plug_3.get() != self.plug_4.get():
                ligacao = self.plug_3.get()+self.plug_4.get()
                for combinacao in pares:
                    if combinacao.find(ligacao[0]) != -1 or combinacao.find(ligacao[1]) != -1:
                        existe = 1
                if existe == 0:   
                    pares[i] = ligacao
            if i == 1 and self.plug_3.get() == "" and self.plug_4.get() == "":
                pares[i] = ""
            existe = 0
            if i == 2 and self.plug_5.get() != "" and self.plug_6.get() != "" and self.plug_5.get() != self.plug_6.get():
                ligacao = self.plug_5.get()+self.plug_6.get()
                for combinacao in pares:
                    if combinacao.find(ligacao[0]) != -1 or combinacao.find(ligacao[1]) != -1:
                        existe = 1
                if existe == 0:   
                    pares[i] = ligacao
            if i == 2 and self.plug_5.get() == "" and self.plug_6.get() == "":
                pares[i] = ""
            existe = 0
            if i == 3 and self.plug_7.get() != "" and self.plug_8.get() != "" and self.plug_7.get() != self.plug_8.get():
                ligacao = self.plug_7.get()+self.plug_8.get()
                for combinacao in pares:
                    if combinacao.find(ligacao[0]) != -1 or combinacao.find(ligacao[1]) != -1:
                        existe = 1
                if existe == 0:   
                    pares[i] = ligacao
            if i == 3 and self.plug_7.get() == "" and self.plug_8.get() == "":
                pares[i] = ""
            existe = 0
            if i == 4 and self.plug_9.get() != "" and self.plug_10.get() != "" and self.plug_9.get() != self.plug_10.get():
                ligacao = self.plug_9.get()+self.plug_10.get()
                for combinacao in pares:
                    if combinacao.find(ligacao[0]) != -1 or combinacao.find(ligacao[1]) != -1:
                        existe = 1
                if existe == 0:   
                    pares[i] = ligacao
            if i == 4 and self.plug_9.get() == "" and self.plug_10.get() == "":
                pares[i] = ""
        # print(pares)
        self.inicializa_enigma()

app = App()
app.mainloop()