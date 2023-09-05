# proyecto_coder_python

                    Mi proyecto consiste en una aplicación de control de gastos.


1) En el navbar de la aplicación encontramos en primer lugar un dropdown menú llamado "gastos"
en el desplegable se muestran dos links:

        1.1) "Ingresar nuevo gasto" - Esta es la primera funcionalidad a probar. Permite ingresar un gasto, y asociarlo a una categoría existente, o crear una nueva categoría.

        1.2) "Lista de Gastos" - Segunda funcionalidad a probar, en este link, se puede ver una lista de los gastos registrados por el usuario.

        1.3) "Buscar Gasto" - Esta es la tercer funcionalidad a probar, y permite buscar un item de los que se haya ingresado mediante el uso de la funcionalidad "(1.1 - Ingresar Nuevo Gasto)"

2) El segundo dropdown menú se llama "categorias", en cuyo desplegable se muestran dos links:

        2.1) "Registrar Categoría" - Cuarta funcionalidad a probar: mediante esta funcionalidad se puede registrar una nueva categoría de gastos, que estará disponible al momento de registrar un nuevo gasto (función link 1.1).
        
        2.2) "Lista de Categorías" - esta es la quinta funcionalidad a probar, y es sencillamente una lista de las categorías asociada al gasto ingresado por el usuario mediante el uso del primer formulario (link 1.1), o del formulario del link 2.2
        
3) Finalmente, en el Navbar se muestra un link llamado "Metas de Ahorro", la cual permite registrar metas de ahorro e indicar una fecha límite.

                                            Rúbrica: 

1) Herencia de HTML.

    - Todas las templates que se muestran en la app heredan del template "base.html".
    - La template "base.html" hereda del template "navbar.html"

2) Por lo menos 3 clases en models.

    - Hay 3 clases en models: 1) CategoriaGasto, 2) ItemGasto, y 3) MetaAhorro.

3) Un formulario para insertar datos a todas las clases de tu models.

    - Se pueden registrar datos en los tres modelos mediante formularios, a continuación se explica a detalle el modelo, la vista y el template. 

        a) Para el modelo CategoríaGasto -> view: formulario_categorias() -> template: "formulario_categorias.html",
        b) Para el modelo ItemGasto -> view: formulario_items_gastos() -> template: "formulario_item_gastos.html", 
        c) Para el modelo MetaAhorro -> view: formulario_meta_ahorro() -> template: "formulario_metas.html"

4)  Un formulario para buscar algo en la BD

    - Se puede buscar items en la BD, en este caso, se pueden buscar un gasto ingresado anteriormente.

    view: "buscar()"
    template formulario: "busqueda_items.html"
    template resultado: "resultado_busqueda.html"


5) 
    -Se adjunta readme.
