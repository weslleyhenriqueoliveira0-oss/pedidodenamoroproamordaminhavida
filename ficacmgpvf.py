#finalmente vou usar os ensimantos do roger pra alguma coisa 
import os
import sys
import random
import subprocess
import importlib
import webbrowser
import tkinter as tk


def verificar_e_instalar(modulo, pacote=None):
    try:
        importlib.import_module(modulo)
    except ImportError:
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            pacote or modulo
        ])

verificar_e_instalar("customtkinter")
verificar_e_instalar("PIL", "pillow")
verificar_e_instalar("pygame")

import customtkinter as ctk
from PIL import Image
import pygame


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("uma cartinha para a gaby <3")
app.geometry("700x760")
app.resizable(False, False)
app.configure(fg_color="#F8C8DC")

ROSA = "#E88EAF"
ROSA_CLARO = "#F8C8DC"
BRANCO = "#FFF8FC"
VINHO = "#75445A"
ROSA_ESCURO = "#D8759B"

PASTA = os.path.dirname(os.path.abspath(__file__))


musica_tocando = False
musica_disponivel = False

geracao_texto = 0
indice_linha = 0
texto_completo = False

botao_musica = None
texto_dialogo = None
botao_proximo = None

#eu nao to de rege bait viado, se ela recusar essa prr eu vou chorar e me matar e fds

try:
    pygame.mixer.init()

    caminho_musica = os.path.join(PASTA, "musica.mp3")

    if os.path.exists(caminho_musica):
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.35)
        musica_disponivel = True

except Exception as erro:
    print("Áudio indisponível:", erro)


def alternar_musica():
    global musica_tocando

    if not musica_disponivel:
        return

    if musica_tocando:
        pygame.mixer.music.pause()
        musica_tocando = False

    else:
        pygame.mixer.music.unpause()

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        musica_tocando = True

    mostrar_musica()


def mostrar_musica():
    global botao_musica

    botao_musica = ctk.CTkButton(
        app,
        text="♫ Desligar música" if musica_tocando else "♫ Ligar música",
        command=alternar_musica,
        width=130,
        height=32,
        corner_radius=15,
        fg_color=BRANCO,
        hover_color="#F0DCE5",
        text_color=VINHO,
        font=("Arial", 12, "bold")
    )

    botao_musica.place(
        relx=0.97,
        rely=0.035,
        anchor="ne"
    )



def carregar_imagem(nome, tamanho=(180, 150)):

    caminho = os.path.join(PASTA, nome)

    if not os.path.exists(caminho):

        base, extensao = os.path.splitext(caminho)

        for ext in [".png", ".jpg", ".jpeg"]:

            if os.path.exists(base + ext):
                caminho = base + ext
                break

    try:

        imagem = Image.open(caminho).convert("RGBA")

        imagem.thumbnail(
            tamanho,
            Image.Resampling.LANCZOS
        )

        fundo = Image.new(
            "RGBA",
            tamanho,
            ROSA_CLARO
        )

        x = (tamanho[0] - imagem.width) // 2
        y = (tamanho[1] - imagem.height) // 2

        fundo.alpha_composite(imagem, (x, y))

        return ctk.CTkImage(
            light_image=fundo,
            dark_image=fundo,
            size=tamanho
        )

    except Exception as erro:

        print(f"Erro ao carregar {nome}: {erro}")

        placeholder = Image.new(
            "RGB",
            tamanho,
            ROSA_CLARO
        )

        return ctk.CTkImage(
            light_image=placeholder,
            dark_image=placeholder,
            size=tamanho
        )


img_cat1 = carregar_imagem("gatoflor.png", (190, 160))
img_cat2 = carregar_imagem("gatofone", (170, 145))
img_cat3 = carregar_imagem("cat3.jpg", (190, 160))
img_sp1 = carregar_imagem("emo.png", (200, 150))
img_dog = carregar_imagem("dog.png", (190, 160))



canvas = tk.Canvas(
    app,
    bg=ROSA_CLARO,
    highlightthickness=0
)

canvas.place(
    relwidth=1,
    relheight=1
)

canvas.tk.call("lower", canvas._w)

coracoes = []

for i in range(22):

    x = random.randint(10, 680)
    y = random.randint(0, 760)

    simbolo = random.choice([
        "♡", "♥", "✧", "⋆"
    ])

    item = canvas.create_text(
        x,
        y,
        text=simbolo,
        fill=random.choice([
            "#FFFFFF",
            "#E88EAF",
            "#F3A9C5"
        ]),
        font=("Arial", random.randint(12, 23))
    )

    coracoes.append(item)


def animar_coracoes():

    for item in coracoes:

        x, y = canvas.coords(item)

        canvas.move(
            item,
            0,
            random.uniform(0.5, 1.5)
        )

        if y > 770:

            canvas.coords(
                item,
                random.randint(10, 680),
                -10
            )

    app.after(45, animar_coracoes)



def criar_titulo(pai, texto, tamanho=28):

    return ctk.CTkLabel(
        pai,
        text=texto,
        font=("Georgia", tamanho, "bold"),
        text_color=VINHO
    )


def criar_botao(pai, texto, comando, largura=220):

    return ctk.CTkButton(
        pai,
        text=texto,
        command=comando,
        width=largura,
        height=45,
        corner_radius=18,
        fg_color=ROSA,
        hover_color=ROSA_ESCURO,
        text_color=BRANCO,
        font=("Arial", 15, "bold"),
        cursor="hand2"
    )
#pedir pro mateus como fazer pra limpar a tela

def limpar_tela():

    global geracao_texto

    geracao_texto += 1

    for widget in app.winfo_children():

        if widget != canvas:
            widget.destroy()


def tela_inicial():

    limpar_tela()
    mostrar_musica()

    subtitulo = ctk.CTkLabel(
        app,
        text="✧ uma pequena surpresa ✧",
        font=("Georgia", 15, "italic"),
        text_color=VINHO
    )

    subtitulo.pack(pady=(75, 10))

    imagem = ctk.CTkLabel(
        app,
        text="",
        image=img_cat1
    )

    imagem.pack(pady=10)

    titulo = criar_titulo(
        app,
        "Tenho algo para você...",
        30
    )

    titulo.pack(pady=15)

    descricao = ctk.CTkLabel(
        app,
        text="Preparei uma coisinha especial com muito carinho.",
        font=("Georgia", 14),
        text_color=VINHO
    )

    descricao.pack(pady=5)

    envelope = ctk.CTkButton(
        app,
        text="💌",
        font=("Arial", 90),
        fg_color="transparent",
        hover_color=ROSA_CLARO,
        text_color=VINHO,
        command=abrir_carta,
        cursor="hand2"
    )

    envelope.pack(pady=20)

    botao = criar_botao(
        app,
        "Abrir minha cartinha ♡",
        abrir_carta
    )

    botao.pack(pady=10)

    rodape = ctk.CTkLabel(
        app,
        text="feito com carinho ♡",
        font=("Georgia", 12, "italic"),
        text_color=VINHO
    )

    rodape.pack(
        side="bottom",
        pady=25
    )


linhas = [

    "eu acho que ta bem obvio que eu so tenho olhos pra ti ne",

    "pra tudo que eu olho eu te vejo se eu vejo valorant eu lembro de ti se eu vejo uma flor eu lembro de ti se eu vejo um lanche eu lembro de ti",

    "Talvez eu não consiga expressar tudo em palavras,",

    "mas quero que saiba que você é muito especial.",

    "Gosto muito de ter você por perto.",

    "como vc sabe eu sou um fudido pra falar pra ti o quanto eu gosto de ti mas eu quero q vc saiba que eu fico o dia inteiro pensando em vc",

    "se vc quiser eu to pronto pra assistir star wars com vc.♡",

    "com muito carinho, twutwu"

]


def escrever_texto():

    global texto_completo

    texto_completo = False

    texto_dialogo.configure(text="")

    frase = linhas[indice_linha]

    geracao_atual = geracao_texto

    botao_proximo.configure(
        text="Pular mensagem ♡"
    )

    def digitar(letra=0):

        global texto_completo

        if geracao_atual != geracao_texto:
            return

        if letra < len(frase):

            texto_dialogo.configure(
                text=frase[:letra + 1]
            )

            app.after(
                35,
                lambda: digitar(letra + 1)
            )

        else:

            texto_completo = True

            botao_proximo.configure(
                text="Próxima mensagem ♡"
            )

    digitar()


def proximo_dialogo():

    global indice_linha, texto_completo

    if not texto_completo:

        texto_dialogo.configure(
            text=linhas[indice_linha]
        )

        texto_completo = True

        botao_proximo.configure(
            text="Próxima mensagem ♡"
        )

        return

    indice_linha += 1

    if indice_linha >= len(linhas):

        tela_pergunta()
        return

    escrever_texto()




def abrir_carta():

    global indice_linha
    global texto_dialogo
    global botao_proximo

    indice_linha = 0

    limpar_tela()
    mostrar_musica()

    carta = ctk.CTkFrame(
        app,
        width=580,
        height=610,
        fg_color=BRANCO,
        corner_radius=25,
        border_width=2,
        border_color="#F1B4CA"
    )

    carta.place(
        relx=0.5,
        rely=0.53,
        anchor="center"
    )

    carta.pack_propagate(False)

    ctk.CTkLabel(
        carta,
        text="♡ uma cartinha especial ♡",
        font=("Georgia", 14, "italic"),
        text_color=ROSA_ESCURO
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        carta,
        text="",
        image=img_cat2
    ).pack(pady=5)

    criar_titulo(
        carta,
        "Para a Biby 💗",
        26
    ).pack(pady=10)

    ctk.CTkLabel(
        carta,
        text="com muito carinho, do Twelas",
        font=("Georgia", 14, "italic"),
        text_color=ROSA_ESCURO
    ).pack()

    texto_dialogo = ctk.CTkLabel(
        carta,
        text="",
        font=("Georgia", 17),
        text_color=VINHO,
        wraplength=460,
        justify="center",
        height=110
    )

    texto_dialogo.pack(
        pady=20,
        padx=35
    )

    botao_proximo = criar_botao(
        carta,
        "Pular mensagem ♡",
        proximo_dialogo
    )

    botao_proximo.pack(
        side="bottom",
        pady=25
    )

    escrever_texto()



def tela_pergunta():

    limpar_tela()
    mostrar_musica()

    ctk.CTkLabel(
        app,
        text="♡",
        font=("Arial", 35),
        text_color=ROSA_ESCURO
    ).pack(pady=(65, 0))

    ctk.CTkLabel(
        app,
        text="",
        image=img_cat3
    ).pack(pady=10)

    criar_titulo(
        app,
        "Então...",
        34
    ).pack(pady=15)

    pergunta = ctk.CTkLabel(
        app,
        text="Você aceita namorar comigo?",
        font=("Georgia", 23),
        text_color=VINHO
    )

    pergunta.pack(pady=15)

    ctk.CTkLabel(
        app,
        text="Escolha com o coração ♡",
        font=("Georgia", 14, "italic"),
        text_color=ROSA_ESCURO
    ).pack(pady=5)

    frame_botoes = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    frame_botoes.pack(pady=30)

    criar_botao(
        frame_botoes,
        "SIM! 💗",
        aceitou,
        190
    ).pack(
        side="left",
        padx=10
    )

    nao = ctk.CTkButton(
        frame_botoes,
        text="Não",
        command=recusou,
        width=190,
        height=45,
        corner_radius=18,
        fg_color=BRANCO,
        hover_color="#F0DCE5",
        text_color=VINHO,
        font=("Arial", 15, "bold"),
        cursor="hand2"
    )

    nao.pack(
        side="left",
        padx=10
    )




def abrir_playlist(url):

    try:
        webbrowser.open(url)

    except Exception as erro:
        print("Não foi possível abrir a playlist:", erro)


def aceitou():

    abrir_playlist(
        "https://open.spotify.com/playlist/5uoHvATQK6bq1EeMplKLrf"
    )

    resultado(
        "EU NÃO ACREDITO ME BEIJA DNV PORAAAAAAAAAAA!! 💗",
        "vai ter que conhcer meus pais agr rsrsrsrrsl!",
        img_dog
    )


def recusou():

    abrir_playlist(
        "https://open.spotify.com/playlist/342gh4BmsgkvInyVX5cdw7"
    )

    resultado(
        "Tudo bem... ♡",
        "vc acabou cmg vou chorar um pouco mas td bem amo-te msm assim disgraça",
        img_sp1
    )




def resultado(titulo, mensagem, imagem):

    limpar_tela()
    mostrar_musica()

    ctk.CTkLabel(
        app,
        text="✧ ♡ ✧",
        font=("Arial", 35),
        text_color=ROSA_ESCURO
    ).pack(pady=(80, 10))

    ctk.CTkLabel(
        app,
        text="",
        image=imagem
    ).pack(pady=15)

    criar_titulo(
        app,
        titulo,
        27
    ).pack(pady=15)

    ctk.CTkLabel(
        app,
        text=mensagem,
        font=("Georgia", 17),
        text_color=VINHO,
        wraplength=500,
        justify="center"
    ).pack(pady=15)

    criar_botao(
        app,
        "Voltar ao início ♡",
        tela_inicial
    ).pack(pady=25)

    ctk.CTkLabel(
        app,
        text="feito com carinho pelo Twelas",
        font=("Georgia", 12, "italic"),
        text_color=ROSA_ESCURO
    ).pack(
        side="bottom",
        pady=25
    )



def fechar_aplicativo():

    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except Exception:
        pass

    app.destroy()


app.protocol(
    "WM_DELETE_WINDOW",
    fechar_aplicativo
)

animar_coracoes()
tela_inicial()

app.mainloop()
#nunca mais quero codar na minha vida
#maldita hora que eu inventei de fazer isso sem chat