from tkinter import Canvas, Tk, Button, filedialog, messagebox, PhotoImage, Label, Menu, Menubutton
import pickle

from prodraw.config import WORKSPACE_COLORS

from prodraw.controllers.workspace.color_picker_controller import ColorPickerController
from prodraw.controllers.workspace.grids_controller import GridsController
from prodraw.controllers.workspace.text_version_controller import TextVersionController
from prodraw.controllers.workspace.clear_draws_controller import ClearDrawsController
from prodraw.controllers.workspace.tools_controller import ToolsController
from prodraw.controllers.workspace.zoom_controller import ZoomController
from prodraw.controllers.workspace.logo_image_controller import LogoImageController


class Workspace:
    """Main workspace — wires up all MVC components."""

    def __init__(self, root: Tk, version):
        self.root = root
        self.bg = WORKSPACE_COLORS.get("bg")

        self.canvas = Canvas(root, bg=self.bg, highlightthickness=0,
                             relief="flat", borderwidth=0)
        # figures dict matches the shape keys used by shape controllers
        self.figures = {
            'Circle': [], 'Rectangle': [],
            'Oval': [], 'Line': [], 'FreeDraw': [], 'Square':[]
        }
        self.version = version

    def start(self):
        self.canvas.pack(fill="both", expand=True)

        # Version watermark at the bottom-left
        # TextVersionController(self.canvas, self.version).setup()

        # Dot grid — redraws on every canvas resize
        grid_ctrl = GridsController(self.canvas, self.version)
        self.canvas.bind("<Configure>", grid_ctrl.on_resize)

        # Logo image - Top side on left
        logo_image = LogoImageController(
            self.canvas, "public/icons/logo.png", self.bg)
        logo_image.setup()

        # Color picker — returns the active color StringVar
        color_ctrl = ColorPickerController(self.canvas)
        selected_color_var = color_ctrl.setup()

        # Clear-all button
        ClearDrawsController(self.canvas, self.figures).setup()

        # Toolbar with drawing tool buttons
        ToolsController(self.canvas, selected_color_var, self.figures).setup()

        # Scroll-to-zoom
        zoom_ctrl = ZoomController(self.canvas)
        self.canvas.bind("<MouseWheel>", zoom_ctrl.on_scroll)

        # def save_file(files):
        #     # Abre a janela "Salvar como" e sugere a extensão .pickle
        #     caminho_arquivo = filedialog.asksaveasfilename(
        #         defaultextension=".pickle",
        #         filetypes=[("Arquivos Pickle", "*.pickle"),
        #                    ("Todos os arquivos", "*.*")],
        #         title="Escolha onde salvar seus dados",
        #     )

        #     # Se o usuário não cancelar a janela
        #     if caminho_arquivo:
        #         try:
        #             with open(caminho_arquivo, "wb") as arquivo:
        #                 pickle.dump(files, arquivo)
        #             messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        #         except Exception as e:
        #             messagebox.showerror(
        #                 "Erro", f"Não foi possível salvar:\n{e}")

        # def carregar_arquivo():
        #     # Abre a janela "Abrir arquivo"
        #     caminho_arquivo = filedialog.askopenfilename(
        #         filetypes=[("Arquivos Pickle", "*.pickle"),
        #                    ("Todos os arquivos", "*.*")],
        #         title="Selecione o arquivo para carregar",
        #     )

        #     # Se o usuário selecionar um arquivo
        #     if caminho_arquivo:
        #         try:
        #             with open(caminho_arquivo, "rb") as arquivo:
        #                 dados_carregados = pickle.load(arquivo)
        #                 self.figures = dados_carregados

        #             # Exibe os dados carregados na tela
        #             messagebox.showinfo(
        #                 "Dados Carregados", f"Conteúdo do arquivo:\n{dados_carregados}"
        #             )
        #         except Exception as e:
        #             messagebox.showerror(
        #                 "Erro", f"Erro ao carregar o arquivo:\n{e}")

        # save_button = Button(self.canvas, text="Salvar",
        #                      # type: ignore #
        #                      command=lambda: save_file(self.figures))
        # save_button.pack()

        # load_button = Button(self.canvas, text="Carregar",
        #                      command=carregar_arquivo)  # type: ignore #
        # load_button.pack()
