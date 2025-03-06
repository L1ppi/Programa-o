# 1º configurações iniciais
# importar as bibliotecas do flet para o nosso projeto
import flet as ft

# definir a função main()
def main(page: ft.Page):
    # 2º definir título para a página
    page.title = "Contador"
    
    # definir o alinhamento dos componentes na página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    # definir a cor de fundo da página
    page.bgcolor = "#A9B5DF"
    
    # definição da variável numero como textfield
    numero = ft.TextField(
        #valor inicial no textfield
        value="0",
        #comprimento do textfield
        width=120,
        #Posicionamento do textfield
        text_align=ft.TextAlign.CENTER,
        #texto em negritos
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        #tamanho da fonte
        text_size=30,
        #texto para orientação 
        label="Quantidade",
        label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        #cor do background
        bgcolor=ft.colors.CYAN,
        #bordas total ou interior
        border=ft.InputBorder.OUTLINE,
        #espessura da borda
        border_width=1,
        #cor da borda
        border_color=ft.colors.BLUE,
        #Borda com cantos arredendados
        border_radius=15,
        #cor do texto
        color=ft.colors.YELLOW,
        #TEXTO INDICATIVO
        counter_text="Maximo 10",
        #texto para erros
        error_text="Valor inválido",
        #filtro de entrada
        input_filter=ft.NumbersOnlyInputFilter(),
        #máximo de caracteres
        max_length=3,
    )
    
    # FUNÇÃO PARA SUBTRAIR 1 DO VALOR ATUAL
    def sub(e):
        numero.value = str(int(numero.value) - 1)
        page.update()
    
    # FUNÇÃO PARA SOMAR 1 AO VALOR ATUAL
    def som(e):
        numero.value = str(int(numero.value) + 1)
        page.update()
    
    # 3º criar a área da página
    page.add(
        # 4º criar uma linha para adicionar os elementos na página
        ft.Row(
            # 5º adicionar os elementos: (-) numero (+)
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE_CIRCLE_OUTLINE, on_click=sub),
                numero,
                ft.IconButton(icon=ft.icons.ADD_CIRCLE_OUTLINE, on_click=som),
            ]
        )
    )
    
    page.update()

# INICIALIZAR O APP
ft.app(target=main)