# =====================================================
# email_sin_actividad.py
# =====================================================

ASUNTO = (
    "Te falta completar tu primera prueba evaluable"
)


def generar_mensaje(alumno=None):

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
    background:#fd7e14;
    color:#ffffff;
    padding:25px;
    border-radius:6px;
    margin-bottom:30px;
    text-align:center;
">
    <div style="font-size:14px; letter-spacing:1px; opacity:0.9;"></div>
    <div style="font-size:26px; font-weight:bold; margin-top:6px;">¡Ya casi lo tienes!</div>
    <div style="font-size:15px; margin-top:6px;">MF0227 - Programación con Lenguajes Orientados a Objetos</div>
</div>

<p style="margin-bottom:20px;">
    {saludo}
</p>

<p style="margin-bottom:20px;">
    Soy <strong>Alexandra Moltó</strong>, tu tutora del curso. Veo que ya has accedido
    correctamente al campus, ¡genial! Sin embargo, todavía no consta que hayas
    <strong>entregado la actividad, completado el test de autoevaluación o realizado la
    prueba evaluable</strong> correspondiente a este primer tramo del curso.
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#fff3cd;
    border-left:5px solid #ffc107;
">
    <strong>Importante:</strong> el <strong>test de conocimientos previos NO es válido</strong>
    como primera prueba evaluable. Es un test informativo que se realiza al principio del curso,
    pero no cuenta para la confirmación de la matrícula. Lo que necesitamos es que completes
    el <strong>test o actividad de evaluación</strong> correspondiente.
</p>

<p style="margin-bottom:20px;">
    Para ayudarte, he preparado un <strong>tutorial en PDF</strong> explicando paso a paso
    cómo localizar y realizar correctamente el test de evaluación dentro de la plataforma:
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#f5f5f5;
    border-left:5px solid #007bff;
    text-align:center;
">
    <a href="https://drive.google.com/file/d/1S_b6KszZMvhkz5_zQB5vfQdwUJoNz7eY/view?usp=sharing"
       target="_blank"
       style="
           display:inline-block;
           font-weight:bold;
           color:#ffffff;
           background:#007bff;
           padding:12px 22px;
           border-radius:5px;
           text-decoration:none;
       ">
        📄 Ver tutorial: cómo hacer el test de evaluación
    </a>
</p>

<p style="margin-bottom:20px;">
    Te recomiendo revisarlo con calma antes de entrar al campus, así evitarás confundir
    el test de conocimientos previos con la prueba evaluable que sí es necesaria.
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
    Si después de ver el tutorial sigues teniendo dudas, o encuentras cualquier problema
    al intentar realizar la prueba, puedes contactar conmigo por cualquiera de estas
    dos vías:
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
    Recuerda que esta prueba es necesaria para <strong>confirmar tu matrícula</strong>,
    así que te animo a completarla cuanto antes.
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
