# =====================================================
# email_sin_conexion.py
# =====================================================

ASUNTO = (
    "¿Todo bien? Aún no hemos detectado tu primer acceso al campus"
)


def generar_mensaje(alumno=None):

    nombre = alumno if alumno else "Buenos días"
    saludo = f"Hola {alumno}," if alumno else "Buenos días:"

    html = f"""
<div style="
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #333333;
    padding: 20px;
    max-width: 850px;
">

<div style="
    background:#dc3545;
    color:#ffffff;
    padding:25px;
    border-radius:6px;
    margin-bottom:30px;
    text-align:center;
">
    <div style="font-size:14px; letter-spacing:1px; opacity:0.9;"></div>
    <div style="font-size:26px; font-weight:bold; margin-top:6px;">¿Necesitas ayuda para empezar?</div>
    <div style="font-size:15px; margin-top:6px;">MF0227 - Programación con Lenguajes Orientados a Objetos</div>
</div>

<p style="margin-bottom:20px;">
    {saludo}
</p>

<p style="margin-bottom:20px;">
    Soy <strong>Alexandra Moltó</strong>, tu tutora del curso. Te escribo porque, revisando
    el campus, veo que todavía <strong>no has accedido a la plataforma</strong> ni has
    realizado ninguna actividad.
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#fff3cd;
    border-left:5px solid #ffc107;
">
    <strong>¿Estás teniendo algún problema para entrar o para empezar?</strong><br>
    Puede ser algo tan sencillo como no recordar la contraseña, no encontrar el enlace
    de acceso o tener alguna duda sobre cómo funciona la plataforma. Si es así, no te
    preocupes, lo resolvemos enseguida.
</p>

<p style="margin-bottom:20px;">
    Es muy importante que accedas cuanto antes, ya que el primer acceso y la primera
    prueba evaluable son necesarios para <strong>confirmar la matrícula</strong> en el curso.
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#f5f5f5;
    border-left:5px solid #007bff;
">
    <strong>URL de acceso al campus:</strong><br>
    <a href="http://campus.corenetworks.es"
       target="_blank"
       style="
           font-weight:bold;
           color:#0066cc;
           text-decoration:none;
       ">
        http://campus.corenetworks.es
    </a>
</p>

<p style="margin-bottom:20px;">
    Si tienes cualquier problema, duda o simplemente necesitas que te echemos una mano
    para empezar, puedes contactar conmigo por <strong>cualquiera de estas dos vías</strong>:
</p>

<table style="width:100%; margin-bottom:25px; border-collapse:collapse;">
  <tr>
    <td style="
        width:50%;
        padding:15px;
        background:#f5f5f5;
        border-left:5px solid #007bff;
        vertical-align:top;
    ">
        <strong>📧 Email</strong><br>
        Respondiendo a este mismo correo, a través del email de la plataforma.
    </td>
    <td style="width:15px;"></td>
    <td style="
        width:50%;
        padding:15px;
        background:#e9f9ee;
        border-left:5px solid #25D366;
        vertical-align:top;
    ">
        <strong>💬 WhatsApp</strong><br>
        <a href="https://wa.me/34614809112"
           target="_blank"
           style="
               font-weight:bold;
               color:#1e9e52;
               text-decoration:none;
           ">
            +34 614 80 91 12
        </a>
    </td>
  </tr>
</table>

<p style="margin-bottom:20px;">
    No pasa nada si te has retrasado un poco, lo importante es que nos lo digas para
    poder ayudarte y que puedas ponerte al día sin problema.
</p>

<p style="margin-top:30px;">
    Quedo a tu disposición para lo que necesites.
</p>

<p style="margin-top:20px;">
    Un saludo,<br>
    <strong>Alexandra Moltó</strong><br>
    <span style="color:#777777;">Tutora del curso</span>
</p>

</div>
"""

    return html
