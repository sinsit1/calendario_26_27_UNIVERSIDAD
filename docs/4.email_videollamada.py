# =====================================================
# email_videollamada.py
# =====================================================

ASUNTO = (
    "Videollamada de bienvenida - Martes 13 a las 19:00"
)


def generar_mensaje(alumno=None):

    # Email general para todo el grupo, sin personalizar

    html = """
<div style="
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #333333;
    padding: 20px;
    max-width: 850px;
">

<div style="
    background:#007bff;
    color:#ffffff;
    padding:25px;
    border-radius:6px;
    margin-bottom:30px;
    text-align:center;
">
    <div style="font-size:14px; letter-spacing:1px; opacity:0.9;">VIDEOLLAMADA DE BIENVENIDA</div>
    <div style="font-size:26px; font-weight:bold; margin-top:6px;">Martes 13 a las 19:00</div>
    <div style="font-size:15px; margin-top:6px;">MF0227 - Programación con Lenguajes Orientados a Objetos</div>
</div>

<p style="margin-bottom:20px;">
    Buenos días a todos/as:
</p>

<p style="margin-bottom:20px;">
    Como os comenté en el email de bienvenida, vamos a realizar una
    <strong>videollamada de bienvenida</strong> para presentarnos y hacer un pequeño
    recorrido por la plataforma, de manera que todos sepamos dónde encontrar los
    diferentes recursos y actividades.
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#fff3cd;
    border-left:5px solid #ffc107;
">
    <strong>Fecha:</strong> martes 13<br>
    <strong>Hora:</strong> 19:00
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#f5f5f5;
    border-left:5px solid #007bff;
">
    <strong>Enlace de acceso a la videollamada:</strong><br>
    <a href="https://us06web.zoom.us/j/85099377962?pwd=3IDfSLbPiwbj9S235hCJIcPcjeCpQa.1"
       target="_blank"
       style="
           font-weight:bold;
           color:#0066cc;
           text-decoration:none;
       ">
        Acceder a la videollamada
    </a>
</p>

<p style="margin-bottom:20px;">
    La asistencia no es obligatoria, pero os animo a participar: es una buena
    oportunidad para resolver dudas y empezar el curso con las cosas más claras.
</p>

<p style="margin-bottom:20px;">
    Si tenéis cualquier duda, podéis escribirme sin problema a través del
    <strong>email de la plataforma</strong> o por el <strong>grupo de WhatsApp</strong>.
</p>

<p style="margin-bottom:20px;">
    Un saludo,
</p>

<p style="margin-top:20px;">
    <strong>Alexandra Moltó</strong><br>
    <span style="color:#777777;">Tutora del curso</span>
</p>

</div>
"""

    return html
