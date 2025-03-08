# 1º configurações iniciais
# importar as bibliotecas do flet para o nosso projeto
import flet as ft

# definir a função main()
def main(page: ft.Page):
    # 2º definir título para a página
    page.title = "Contador"
    # definir tamanho da janela
    page.window.width = 500
    page.window.height = 700
    page.window.center()
    
    # definir o alinhamento dos componentes na página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    # definir a cor de fundo da página
    page.bgcolor = "#FFF2F2"
    
    # definição da variável numero como textfield
    numero = ft.TextField(
        # valor inicial no textfield
        value="0",
        # comprimento do textfield
        width=300,
        # Posicionamento do textfield
        text_align=ft.TextAlign.CENTER,
        # texto em negritos
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        # tamanho da fonte
        text_size=16,
        # texto para orientação 
        label="Quantidade",
        label_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color="#2D336B"),
        # cor do background
        bgcolor="#A9B5DF",
        # bordas total ou interior
        border=ft.InputBorder.UNDERLINE,
        # espessura da borda
        border_width=1,
        # cor da borda
        border_color="#2D336B",
        # Borda com cantos arredendados
        border_radius=15,
        # cor do texto
        color="#2D336B",
        # filtro de entrada
        input_filter=ft.NumbersOnlyInputFilter(),
        # somente leitura
        read_only=True,
        # máximo de caracteres
        max_length=3,
    )
    
    # FUNÇÃO PARA SUBTRAIR 1 DO VALOR ATUAL
    def sub(e):
        if int(numero.value) > 0:
            numero.value = str(int(numero.value) - 1)
            numero.error_text = None
        else:
            # texto para erros
            numero.error_text = "VALOR INVÁLIDO"
        page.update()

    # FUNÇÃO PARA SOMAR 1 AO VALOR ATUAL
    def som(e):
        if int(numero.value) < 5:
            numero.value = str(int(numero.value) + 1)
            numero.error_text = None
        else:
            numero.error_text = "MÁXIMO 5"
        page.update()
    
    # 3º criar a área da página
    page.add(
        ft.Container(
            content=ft.Text(
                value="---Contador de Itens---",
                weight=ft.FontWeight.BOLD,
                size=24,
                color="#2D336B",
                bgcolor="#A9B5DF",
            ),
            alignment=ft.alignment.top_center,
        ),
        ft.Container(
            content=ft.Text(
                value="Clique no + para adicionar e no - para subtrair a quantidade de itens",
                weight=ft.FontWeight.NORMAL,
                size=14,
                color="#2D336B",
            ),
            alignment=ft.alignment.center,
        ),
        # 4º criar uma linha para adicionar os elementos na página
        ft.Row(
            # 5º adicionar os elementos: (-) numero (+)
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE_CIRCLE_OUTLINE, on_click=sub, icon_color="#2D336B"),
                numero,
                ft.IconButton(icon=ft.icons.ADD_CIRCLE_OUTLINE, on_click=som, icon_color="#2D336B"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    page.update()

# INICIALIZAR O APP
ft.app(target=main)