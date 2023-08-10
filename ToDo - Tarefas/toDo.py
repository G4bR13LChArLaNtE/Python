# - Bibliotecas
import flet
from flet import *
from datetime import datetime
import sqlite3



"""
    App To-Do creado with Flet.
        Principais tópicos:
            1. Biblioteca e Função principal;
            2. Configurando o app;
            3. Classe para o formulário UI;
            4. Animação do formulário UI;
            5. Classe para gerar as tarefas;
            6. Tela das Tarefas;
            7. Deletar + Editar Tarefa;
            8. Banco de dados.
    """



# - Banco de dados:
class Database:
    def Connection():
        try:
            db = sqlite3.connect('tarefas.db')
            c = db.cursor()
            c.execute("CREATE TABLE if not exists tarefa(id INTEGER PRIMARY KEY, DESCRICAO VARCHAR(255) NOT NULL, DATA VARCHAR(255) NOT NULL)")
            return db
        except Exception as e:
            print('Houve um erro no Banco de dados - Erro:'+ e)

    def ReadDb(db):
        c = db.cursor()
        c.execute('SELECT DESCRICAO, DATA FROM TAREFA')
        registros = c.fetchall()
        return registros


    def InsertDb(db, dados):
        c = db.cursor()
        c.execute('INSERT INTO TAREFA (DESCRICAO, DATA) VALUES (?, ?)', dados)
        db.commit()


    def DeleteDb(db, dado):
        c = db.cursor()
        c.execute('DELETE FROM TAREFA WHERE DESCRICAO = ?', dado)
        db.commit()


    def updateDb(db, dado):
        c = db.cursor()
        c.execute('UPDATE TAREFA SET DESCRICAO = ? WHERE DESCRICAO = ?', dado)
        db.commit()




#Vamos criar a primeira classe formulário:
class FormContainer(UserControl):
    
    #Nesse ponto, nós podemos passar uma função para o main() e expandir ou minimizar o formulário.
    def __init__(self, func):
        self.func = func
        super().__init__()
    
    
    def build(self):
        return Container(
            width=280,
            height=80,
            #bgcolor="#ADC7F7",
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["#7d0b5f", "#004195", "#c0d1ff",],),
            opacity=0,
            border_radius=40,
            margin=margin.only(left=-20, right=-20),
            animate=animation.Animation(400, "decelerate"),
            animate_opacity=200,
            padding=padding.only(top=45, bottom=45),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=48,
                        width=255,
                        filled=True,
                        text_size=12,
                        border_color="transparent",
                        hint_text="Descrição...",
                        hint_style=TextStyle(size=12, color="black"),
                            ),
                    IconButton(
                        content=Text("Add Tarefa"),
                            width=180,
                            height=44,
                            on_click=self.func,
                            style=ButtonStyle(
                                bgcolor={"": 'black'},
                                shape={
                                    "": RoundedRectangleBorder(radius=8),
                                       },
                                    
                                ),
                            ),
                        ]
                    ),
        )






# - classe para gerar as tarefas
class CreateTask(UserControl):
    def __init__(self, task:str, date:str, func1, func2):
        self.task = task
        self.date = date
        self.func1 = func1
        self.func2 = func2
        super().__init__()


    def TaskDeleteEdit(self, name, color, func):
        return IconButton(
            icon=name,
            width=30,
            icon_size=18,
            icon_color=color,
            opacity=0,
            animate_opacity=200,
            # Para usá-la, nós precisamos pegar fora dos botões delete e edit
            on_click=lambda e: func(self.GetContainerInstance())
        )


    def GetContainerInstance(self):
        return self #Retorna a instancia self

    

    def ShowIcons(self, e):
        if e.data == 'true':
            # Esses são os índices de cada ícone
            (e.control.content.controls[1].controls[0].opacity,
            e.control.content.controls[1].controls[1].opacity
            ) = (1, 1)
            e.control.content.update()
        else:
            (e.control.content.controls[1].controls[0].opacity,
            e.control.content.controls[1].controls[1].opacity
            ) = (0, 0)
            e.control.content.update()
    
    
    def build (self):
        return Container(
            width=280,
            height=60,
            border=border.all(0.85, "white54"),
            border_radius=8,
            on_hover=lambda e:self.ShowIcons(e),
            clip_behavior=ClipBehavior.HARD_EDGE,
            padding=10,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    #Coluna da Descrição da tarefa e da data
                    Column(
                        spacing=1,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(value=self.task, size=10),
                            Text(value=self.date, size=9, color="white54"),
                        ],
                    ),
                    #Linha dos Icones para Deletar e Editar
                    Row(
                        spacing=0,
                        alignment=MainAxisAlignment.END,
                        controls=[
                            self.TaskDeleteEdit(
                                icons.DELETE_ROUNDED, 'red700', self.func1),
                            self.TaskDeleteEdit(
                                icons.EDIT_ROUNDED, 'white70', self.func2),
                        ]
                    )
                ],
            ),
        )





# - Função principal:

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    
    def AddTaskToScreen(e):
        #Teremos 2 dados relevantes aqui: A data e a Tarefa
        dateTime = datetime.now().strftime("%d %b, %Y %H:%M")
        
        
        db = Database.Connection()
        Database.InsertDb(db, (form.content.controls[0].value, dateTime))
        db.close()
        
        
        
        
        if form.content.controls[0].value:
            _main_column_.controls.append(
                #Aqui podemos criar uma instância da classe CreateTask()
                CreateTask(
                    form.content.controls[0].value, #Descrição da tarefa
                    dateTime, #Data, hora e minuto da postagem da tarefa
                    DeleteFunction,
                    UpdateFunction
                )
            )
            _main_column_.update()
            
            CreateToDoTask(e)
        else:
            db.close()

    
    # - Deletar + Editar Tarefa:
    
    #Função Delete
    def DeleteFunction(e):
        
        db = Database.Connection()
        Database.DeleteDb(db, (e.controls[0].content.controls[0].controls[0].value, ))
        
        db.close()
        
        #Quando quisermos deletar a tarefa, lembramos que essa instância(tarefa) está em uma lista =>
        # isso significa que podemos simplismente remover quando quisermos.
        _main_column_.controls.remove(e)
        _main_column_.update()
    
    # Função Editar:
    def UpdateFunction(e):
        
        form.height, form.opacity = 200, 1 #Mostra o formulário
        (
            form.content.controls[0].value,
            #Aqui nós estamos transformando o botão e o nome da função...
            #Nós precisamos mudar de add tarefa para update...
            form.content.controls[1].content.value,
            form.content.controls[1].on_click
        ) = (
            #Essa é a instância value da Tarefa
            e.controls[0].content.controls[0].controls[0].value,
            'Update',
            lambda _: FinalizeUpdate(e),
            
        )
        form.update()
        
        # Uma vez que é editada a tarefa, precisamos enviar o dado correto de volta
    
    
    def FinalizeUpdate(e):
        
        db = Database.Connection()
        Database.updateDb(db, 
                          (form.content.controls[0].value,
                           e.controls[0].content.controls[0].controls[0].value,
                         ),
                          )
        
        #Podemos inverter o valor de tudo
        e.controls[0].content.controls[0].controls[0].value = form.content.controls[0].value
        
        e.controls[0].content.update()
        
        CreateTask(e)
    
    
    # - Animação do formulário:
    
    #função para mostrar/esconder o container do formulário
    def CreateToDoTask(e):
        #Quando nós clicamos no iconbuttom Add ...
        if form.height != 200:
            form.height, form.opacity = 200, 1
            form.update()
        else:
            form.height, form.opacity = 80, 0
            #Precisamos remover os valores do textfield também...
            form.content.controls[0].value = None
            form.content.controls[1].content.value = "Add Tarefa"
            form.content.controls[1].on_click = lambda e: AddTaskToScreen(e)
            form.update()






    _main_column_ = Column(
        scroll="hidden",
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text(
                        "ToDo - Tarefas",
                        size=18,
                        weight="bold",
                    ),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        on_click=lambda e: CreateToDoTask(e),
                    ),
                ],
            ),
            Divider(height=8, color="white24"),
        ],
    )



    # - Configurando o app:
    page.add(
        Container(
            width=1500,
            height=900,
            margin=-10,
            #bgcolor='bluegrey800',
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=[
                    "#00527e",
                    "#005185",
                    "#00508b",
                    "#004f90",
                    "#004d94",
                    "#004b96",
                    "#004897",
                    "#004597",
                    "#004195",
                    "#003d92",
                    "#30388e",
                    "#463388",
                    "#562d81",
                    "#63267a",
                    "#6d1e71",
                    "#761668",
                    "#7d0b5f",
                    "#820055",
                    "#86004b"
                ],
            ),
            alignment=alignment.center,
            padding=padding.only(right=110),
            content=Row(
                alignment=MainAxisAlignment.END,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    #Container principal
                    Container(
                        width=280,
                        height=600,
                        bgcolor='#0f0f0f',
                        border_radius=40,
                        border=border.all(0.5, "white70"),
                        padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE,
                        content=Column(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            controls=[
                                #Coluna principal...
                                _main_column_,
                                # Classe formulário
                                FormContainer(lambda e: AddTaskToScreen(e)),
                            ],
                        ),
                    )
                ],
            ),
            
        )
    )
    page.update()
    
    
    
    #O container do fomulário necessita ser indexado
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]


    db = Database.Connection()
    
    #Usando [:-1] inverte a ordem de uma lista...
    #Usando [::-1] inverte a ordem de uma tupla...
    for tarefa in Database.ReadDb(db)[::-1]:
        _main_column_.controls.append(
            CreateTask(
                tarefa[0],
                tarefa[1],
                DeleteFunction,
                UpdateFunction,
            )
        )
    _main_column_.update()


if __name__ == "__main__":
    flet.app(port=9000, target=main)