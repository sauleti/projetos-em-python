from tkinter import *

class Appllication:
    def __init__(self,master=None):
        self.fonte_padrao = ('Arial', '10')
        self.primeiro_container = Frame(master)
        self.primeiro_container['pady'] = 10
        self.primeiro_container.pack()

        self.segundo_container = Frame(master)
        self.segundo_container['padx'] = 20
        self.segundo_container.pack()

        self.terceiro_container = Frame(master)
        self.terceiro_container['padx'] = 20
        self.terceiro_container.pack()
        
        self.quarto_container = Frame(master)
        self.quarto_container['pady'] = 20
        self.quarto_container.pack()

        self.titulo = Label(self.primeiro_container, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nome_label = Label(self.segundo_container, text = 'Nome', font=self.fonte_padrao)
        self.nome_label.pack(side=LEFT)
        """
        self.nome = Entry(self.segundo_container)
        self.nome['width'] = 30
        self.nome['font'] = self.fonte_padrao
        self.nome.pack(side=LEFT)
        """
        self.senha_label = Label(self.terceiro_container, text='Senha', font=self.fonte_padrao)
        self.senha_label.pack(side=LEFT)

        self.senha = Entry(self.terceiro_container)
        self.senha['width'] = 30
        self.senha['font'] = self.fonte_padrao
        self.senha['show'] = '*'
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quarto_container)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Calibri', '8')
        self.autenticar['width'] = 12
        self.autenticar['command'] = self.verificar_senha
        self.autenticar.pack()

        self.mensagem = Label(self.quarto_container,text='', font= self.fonte_padrao)
        self.mensagem.pack()

    def verificar_senha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == 'dev' and senha == '123':
            self.mensagem['text'] = 'Autenticado'
        else:
            self.mensagem['text'] = 'Erro na autenticaço'


      




janela = Tk()
Appllication(janela)
janela.mainloop()