import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

print(tienda.head())

print(tienda.iloc[100])

sum1 = tienda['Precio'].sum()
sum2 = tienda2['Precio'].sum()
sum3 = tienda3['Precio'].sum()
sum4 = tienda4['Precio'].sum()

print('Suma de tienda 1: '+sum1.astype(str))
print('Suma de tienda 2: '+sum2.astype(str))
print('Suma de tienda 3: '+sum3.astype(str))
print('Suma de tienda 4: '+sum4.astype(str))

## creando grafico de ventas totales de tiendas

tiendas = ['Tienda 1', 'Tienda 2','Tienda 3','Tienda 4']

datos = [sum1,sum2,sum3,sum4]

df = pd.DataFrame(
    {'Venta totales' : datos},
    index=tiendas
)

ax = df.plot(kind='bar',figsize=(12,8),color='blue')

#Formato Eje y
formatter = ticker.StrMethodFormatter('${x:,.0f}') 
# Aplica el formato al eje Y
ax.yaxis.set_major_formatter(formatter)

#dato arriba de columnas
for i, v in enumerate(datos):
    # i es el índice (posición de la barra en el eje X)
    # v es el valor (la altura de la barra en el eje Y)
    
    # ax.text(x, y, texto_a_mostrar, otras_propiedades)
    ax.text(
        x=i,           # Posición X: El índice de la barra (0, 1, 2, 3...)
        y=v + 350,     # Posición Y: Un poco más arriba que el valor de la barra (v)
        s=f'{v:,}',    # Texto: El valor (v), formateado con comas (f'{v:,}')
        ha='center',   # Alineación horizontal: Centrado sobre la barra
        fontdict={'fontsize': 10, 'weight': 'bold'}
    )

# 4. Configuración y Guardar
ax.set_title('Ventas por Tienda')
ax.set_xlabel('Tienda')
ax.set_ylabel('Monto de Ventas')
plt.xticks(rotation=0)

fig = ax.get_figure()
fig.savefig('grafico_ventas.png', bbox_inches='tight')

#plt.show()

#Venta por categoria de cada tienda
#Venta por categoria de cada tienda
def calcular_y_guardar_ventas_por_categoria(data: pd.DataFrame, nombre_archivo_salida: str, nombre_tienda: str):    
    # ... (Verificación de columnas y cálculo omitidos por brevedad) ...
    if 'Categoría del Producto' not in data.columns or 'Precio' not in data.columns:
        print("Error: El DataFrame debe contener las columnas 'Categoría del Producto' y 'Precio'.")
        return None
    
    ventas_por_categoria = data.groupby('Categoría del Producto')['Precio'].sum()
    ventas_por_categoria = ventas_por_categoria.rename('Ventas_Totales')
    
    # 3. Generar y guardar el gráfico de pastel
    try:
        fig, ax = plt.subplots(figsize=(10, 10))

        # Al usar .plot(kind='pie'), pandas ya toma el índice (las categorías) como etiquetas
        wedges, texts, autotexts = ax.pie( 
           x=ventas_por_categoria.values,
           
           # Usamos las etiquetas del índice para la leyenda
           labels=None, # Establecer labels=None para que NO aparezcan sobre el gráfico
           
           autopct='%1.1f%%',
           startangle=90
           # Nota: Ya no necesitamos el parámetro label='' porque estamos usando ax.pie() 
           # o, si usamos el plot de pandas, nos aseguramos de no pasarle labels=...
        )

        # ⭐️ PASO CLAVE: Agregar la leyenda
        ax.legend(
            wedges, # Los objetos de las porciones
            ventas_por_categoria.index, # Los nombres de las categorías (el índice)
            title="Categorías",
            loc="center left", # Ubicación: izquierda central
            bbox_to_anchor=(1, 0, 0.5, 1) # Mueve la leyenda fuera del gráfico
        )

        ax.set_title(f'Distribución de Ventas por Categoría - {nombre_tienda}', fontsize=16, pad=20) 
        ax.set_ylabel('') # Eliminamos la etiqueta del eje Y (que no aplica a pastel)

        fig.savefig(nombre_archivo_salida, bbox_inches='tight')
        plt.show()
        print(f"✅ Éxito: El gráfico de ventas por categoría se guardó en: '{nombre_archivo_salida}'")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")
        return None
        
  
# 2. Llamar a la función

""" 
archivo_de_salida1 = 'ventas_por_categoria1.png'
nombre_tienda1 = 'Tienda 1'
calcular_y_guardar_ventas_por_categoria(tienda, archivo_de_salida1,nombre_tienda1)

archivo_de_salida2 = 'ventas_por_categoria2.png'
nombre_tienda2 = 'Tienda 2'
calcular_y_guardar_ventas_por_categoria(tienda2, archivo_de_salida2,nombre_tienda2)

archivo_de_salida3 = 'ventas_por_categoria3.png'
nombre_tienda3 = 'Tienda 3'
calcular_y_guardar_ventas_por_categoria(tienda3, archivo_de_salida3,nombre_tienda3)

archivo_de_salida4 = 'ventas_por_categoria4.png'
nombre_tienda4 = 'Tienda 4'
calcular_y_guardar_ventas_por_categoria(tienda4, archivo_de_salida4,nombre_tienda4)

 """

#Valoracion media por tienda

promedio_calificacion_tienda1 = tienda['Calificación'].mean().round(3)
promedio_calificacion_tienda2 = tienda2['Calificación'].mean().round(3)
promedio_calificacion_tienda3 = tienda3['Calificación'].mean().round(3)
promedio_calificacion_tienda4 = tienda4['Calificación'].mean().round(3)

print('Calificación promedio Tienda 1: '+ promedio_calificacion_tienda1.astype(str))
print('Calificación promedio Tienda 2: '+ promedio_calificacion_tienda2.astype(str))
print('Calificación promedio Tienda 3: '+ promedio_calificacion_tienda3.astype(str))
print('Calificación promedio Tienda 4: '+ promedio_calificacion_tienda4.astype(str))

#Productos mas vendidos y menos vendidos
def producto_mas_y_menos_vendido(tienda: pd.DataFrame, nombre_tienda: str):
    NOMBRE_COLUMNA_PRODUCTO = 'Producto' 
    conteo_ventas = tienda[NOMBRE_COLUMNA_PRODUCTO].value_counts()
    producto_mas_vendido = conteo_ventas.head(1)
    producto_menos_vendido = conteo_ventas.tail(1)

    nombre_producto_mas = producto_mas_vendido.index[0]
    cantidad_producto_mas = producto_mas_vendido.iloc[0]

    nombre_producto_menos = producto_menos_vendido.index[0]
    cantidad_producto_menos = producto_menos_vendido.iloc[0]

    # Mostrar Resultados
    
    print('PRODUCTO MÁS VENDIDO '+nombre_tienda+' : '+nombre_producto_mas+', Cantidad : '+cantidad_producto_mas.astype(str))
    print('PRODUCTO MENOS VENDIDO '+nombre_tienda+' : '+nombre_producto_menos+', Cantidad : '+cantidad_producto_menos.astype(str))


producto_mas_y_menos_vendido(tienda,'Tienda 1')
producto_mas_y_menos_vendido(tienda2,'Tienda 2')
producto_mas_y_menos_vendido(tienda3,'Tienda 3')
producto_mas_y_menos_vendido(tienda4,'Tienda 4')

#Valor envio promedio

import pandas as pd

def calcular_envio_promedio(data: pd.DataFrame, nombre_tienda: str, columna_envio: str = 'Costo de envío'):
    
    
    # 1. Verificar si la columna de envío existe
    if columna_envio not in data.columns:
        print(f"❌ Error: El DataFrame de {nombre_tienda} no tiene la columna '{columna_envio}'.")
        return None

    # 2. Calcular el promedio y redondear
    try:
        promedio_envio = data[columna_envio].mean().round(2)
        
        # 3. Imprimir el resultado
        print(f"✅ El valor de envío promedio para {nombre_tienda} es: {promedio_envio:.2f}")
        return promedio_envio
        
    except TypeError:
        print(f"❌ Error de cálculo: La columna '{columna_envio}' debe contener solo valores numéricos en {nombre_tienda}.")
        return None


calcular_envio_promedio(tienda, 'Tienda 1', 'Costo de envío')
calcular_envio_promedio(tienda2, 'Tienda 2', 'Costo de envío')
calcular_envio_promedio(tienda3, 'Tienda 3', 'Costo de envío')
calcular_envio_promedio(tienda4, 'Tienda 4', 'Costo de envío')


