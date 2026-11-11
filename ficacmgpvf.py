import subprocess
import sys
from pathlib import Path

def verificar_e_instalar(pacote):
    try:
        __import__(pacote)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

verificar_e_instalar("customtkinter")
verificar_e_instalar("pillow")

import customtkinter as ctk
from PIL import Image
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("com muito carinho para a gaby <3")
app.geometry("600x650")
app.resizable(False, False)
app.configure(fg_color="#F8C8DC")

rosa = "#E88EAF"
branco = "#FFF8FC"
texto_cor = "#75445A"

image_path = os.path.dirname(os.path.realpath(__file__))

def carregar_imagem(filename, size=(150, 150), bg_color=(248, 200, 220)):
    path_completo = os.path.join(image_path, filename)
    
    if not os.path.exists(path_completo):
        for ext in ['.png', '.jpg', '.jpeg']:
            if os.path.exists(path_completo + ext):
                path_completo += ext
                break

    try:
        pil_image = Image.open(path_completo)
        
        if pil_image.mode in ("RGBA", "LA") or (pil_image.mode == "P" and "transparency" in pil_image.info):
            pil_image = pil_image.convert("RGBA")
            fundo = Image.new("RGBA", pil_image.size, bg_color + (255,))
            pil_image = Image.alpha_composite(fundo, pil_image).convert("RGB")
        else:
            pil_image = pil_image.convert("RGB")

        pil_image = pil_image.resize(size, Image.Resampling.LANCZOS)

        return ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=size)
        
    except Exception as e:
        print(f"Erro ao carregar {filename}: {e}. Usando placeholder.")
        placeholder = Image.new('RGB', size, bg_color)
        return ctk.CTkImage(light_image=placeholder, dark_image=placeholder, size=size)

img_cat1 = carregar_imagem("gatoflor.png", size=(180, 150)) 
img_cat2 = carregar_imagem("gatofone", size=(160, 140)) 
img_cat3 = carregar_imagem("cat3.jpg", size=(180, 150)) 
img_sp1 = carregar_imagem("emo.png", size=(200, 150))
img_sp2 = carregar_imagem("download.png", size=(200, 150))
img_dog = carregar_imagem("dog.png", size=(180, 150))

linhas = [
    ("Kissed that first night... ", 0.08, 0.5),
    ("One last kiss ", 0.12, 0.5),
    ("I love you like an alcoholic ", 0.08, 1),
    ("One last kiss ", 0.12, 0.5),
    ("I love you like a statuette ", 0.08, 1),
    ("One last kiss ", 0.12, 0.5),
    ("I need you like I need a broken leg... ", 0.08, 1),
    ("Eu te amo como eu amo remédios ", 0.08, 1),
    (":)", 0.2, 1)
]

def escrever_texto(label, linhas, indice=0, letra=0):
    if indice >= len(linhas):
        return

    frase, velocidade, pausa = linhas[indice]
    texto_atual = label.cget("text")

    if letra < len(frase):
        label.configure(text=texto_atual + frase[letra])
        label.after(
            max(1, int(velocidade * 1000)),
            lambda: escrever_texto(label, linhas, indice, letra + 1)
        )
    else:
        label.after(
            int(pausa * 1000),
            lambda: escrever_texto(label, linhas, indice + 1, 0)
        )

def limpar_tela():
    for widget in app.winfo_children():
        widget.destroy()

def tela_inicial():
    limpar_tela()

    lbl_img_inicial = ctk.CTkLabel(app, text="", image=img_cat1)
    lbl_img_inicial.pack(pady=(35, 5))

    titulo = ctk.CTkLabel(
        app,
        text="Tenho algo para você...",
        font=("Georgia", 28, "bold"),
        text_color=texto_cor
    )
    titulo.pack(pady=(5, 20))

    envelope = ctk.CTkButton(
        app,
        text="💌",
        font=("Arial", 90),
        fg_color="transparent",
        hover_color="#F8C8DC",
        text_color=texto_cor,
        command=abrir_carta
    )
    envelope.pack(pady=10)

    instrucoes = ctk.CTkLabel(
        app,
        text="Clique no envelope para abrir sua carta",
        font=("Arial", 16),
        text_color=texto_cor
    )
    instrucoes.pack(pady=10)

def abrir_carta():
    limpar_tela()

    carta = ctk.CTkFrame(
        app,
        fg_color=branco,
        corner_radius=20,
        width=520,
        height=550
    )
    carta.pack(expand=True, padx=30, pady=20)
    carta.pack_propagate(False)

    lbl_img_carta = ctk.CTkLabel(carta, text="", image=img_cat2)
    lbl_img_carta.pack(pady=(15, 5))

    titulo = ctk.CTkLabel(
        carta,
        text="para a biby com muito carinho do twelas  💗",
        font=("Georgia", 22, "bold"),
        text_color=rosa
    )
    titulo.pack(pady=(5, 10))

    texto = ctk.CTkLabel(
        carta,
        text="",
        font=("Georgia", 15),
        text_color=texto_cor,
        justify="center",
        wraplength=450
    )
    texto.pack(pady=10)

    escrever_texto(texto, linhas)

    botao = ctk.CTkButton(
        carta,
        text="Continuar 💗",
        fg_color=rosa,
        hover_color="#D8759B",
        command=tela_pergunta
    )
    botao.pack(side="bottom", pady=15)

def tela_pergunta():
    limpar_tela()

    lbl_img_pergunta = ctk.CTkLabel(app, text="", image=img_cat3)
    lbl_img_pergunta.pack(pady=(35, 5))

    titulo = ctk.CTkLabel(
        app,
        text="Então...",
        font=("Georgia", 30, "bold"),
        text_color=texto_cor
    )
    titulo.pack(pady=(5, 15))

    pergunta = ctk.CTkLabel(
        app,
        text="Você aceita namorar comigo?",
        font=("Georgia", 22),
        text_color=texto_cor
    )
    pergunta.pack(pady=10)

    frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
    frame_botoes.pack(pady=10)

    sim = ctk.CTkButton(
        frame_botoes,
        text="SIM! 💗",
        font=("Arial", 18, "bold"),
        fg_color=rosa,
        hover_color="#D8759B",
        width=180,
        height=45,
        command=aceitou
    )
    sim.pack(side="left", padx=10)

    nao = ctk.CTkButton(
        frame_botoes,
        text="Não",
        font=("Arial", 15),
        fg_color=branco,
        hover_color="#F0DCE5",
        text_color=texto_cor,
        width=180,
        height=40,
        command=recusou
    )
    nao.pack(side="left", padx=10)

def aceitou():
    resultado("nao acreditooooooooo, vou comprar as alianças semana que vemmm:))", imagem=img_dog)

def recusou():
    resultado("espero que vc saiba que vc acabo com todos os meus sonhos e expectativas D:", imagem=img_sp1)

def resultado(mensagem, imagem):
    limpar_tela()

    lbl_img_resultado = ctk.CTkLabel(app, text="", image=imagem)
    lbl_img_resultado.pack(pady=(80, 10))

    final = ctk.CTkLabel(
        app,
        text=mensagem,
        font=("Georgia", 20, "bold"),
        text_color=texto_cor,
        wraplength=500
    )
    final.pack(pady=(10, 20))

tela_inicial()
app.mainloop()