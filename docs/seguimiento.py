# =====================================================
# seguimiento.py
#
# Email de SEGUIMIENTO de la formación (lo usa emails_automaticos).
# Se envía dos veces por semana (lunes y viernes) a todo el grupo,
# también a quien ya lo tiene al 100 %.
# No pongas fechas concretas ("quedan 4 días", "el examen es el 16
# de octubre"...): el email se repite durante todo el curso.
# Para avisos puntuales usa las otras plantillas.
# =====================================================

ASUNTO = (
    "Seguimiento de tu formación"
)


def generar_mensaje(alumno):

    nombre_completo = alumno["nombre"]

    try:
        nombre = (
            nombre_completo
            .split(",")[1]
            .strip()
            .split(" ")[0]
            .title()
        )

    except:
        nombre = nombre_completo.title()

    ufs = alumno["ufs"]

    # =====================================================
    # COLOR SEGÚN PORCENTAJE
    # =====================================================

    def color_porcentaje(valor):

        if valor >= 75:
            return "#d4edda"

        elif valor >= 25:
            return "#fff3cd"

        return "#f8d7da"

    # =====================================================
    # TABLA DE UNIDADES FORMATIVAS
    # =====================================================

    def generar_tabla_ufs():

        html = """
<table style="
    border-collapse: collapse;
    width: 100%;
    margin-top: 25px;
    margin-bottom: 30px;
    font-family: Arial, Helvetica, sans-serif;
">

<tr style="background:#f5f5f5;">

<th style="
    border:1px solid #cccccc;
    padding:12px;
    text-align:left;
">
Unidad Formativa
</th>

<th style="
    border:1px solid #cccccc;
    padding:12px;
    text-align:center;
">
Tests
</th>

<th style="
    border:1px solid #cccccc;
    padding:12px;
    text-align:center;
">
Prácticas
</th>

</tr>
"""

        for nombre_uf, datos in ufs.items():

            tests = datos.get(
                "tests",
                0
            )

            practicas = datos.get(
                "practicas",
                0
            )

            color_tests = color_porcentaje(
                tests
            )

            color_practicas = color_porcentaje(
                practicas
            )

            html += f"""
<tr>

<td style="
    border:1px solid #cccccc;
    padding:12px;
    font-size:15px;
">
{nombre_uf}
</td>

<td style="
    border:1px solid #cccccc;
    padding:12px;
    text-align:center;
    background:{color_tests};
    font-weight:bold;
">
{tests}%
</td>

<td style="
    border:1px solid #cccccc;
    padding:12px;
    text-align:center;
    background:{color_practicas};
    font-weight:bold;
">
{practicas}%
</td>

</tr>
"""

        html += "</table>"

        return html

    # =====================================================
    # HTML FINAL
    # =====================================================

    html = f"""
<div style="
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #333333;
    padding: 20px;
    max-width: 850px;
">

<p style="margin-bottom:20px;">
    Hola <strong>{nombre}</strong>,
</p>

<p style="margin-bottom:20px;">
    Te escribo para que veas <strong>cómo llevas la formación</strong>. Lo hago dos veces por semana
    para que puedas comprobar tu progreso con frecuencia y no se te acumule nada.
</p>

<p style="margin-bottom:20px;">
    Recuerda que es necesario tener realizado
    <strong>al menos el 75 % de las actividades y tests para poder presentarte al examen</strong>.
    En la siguiente tabla puedes ver tu progreso actual en cada Unidad Formativa.
</p>

{generar_tabla_ufs()}

<p style="margin-bottom:20px;">
    Si vas al día, ¡sigue así! Y si vas algo atrasado/a, no pasa nada: <strong>escríbeme y vemos
    juntos cómo organizarte</strong>. Si tienes cualquier duda o problema con alguna actividad, estoy aquí para ayudarte.
</p>

<p style="margin-top:30px;">
    Un saludo,<br>
    Alexandra
</p>

</div>
"""

    return html
