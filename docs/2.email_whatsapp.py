# =====================================================
# email_whatsapp.py
# =====================================================

ASUNTO = (
    "Únete al grupo de apoyo de WhatsApp del curso"
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
    background:#25d366;
    color:#ffffff;
    padding:25px;
    border-radius:6px;
    margin-bottom:30px;
    text-align:center;
">
    <div style="font-size:14px; letter-spacing:1px; opacity:0.9;">GRUPO DE APOYO</div>
    <div style="font-size:26px; font-weight:bold; margin-top:6px;">Grupo de WhatsApp del curso</div>
</div>

<p style="margin-bottom:20px;">
    Buenos días a todos/as:
</p>

<p style="margin-bottom:20px;">
    He creado un <strong>grupo de apoyo en WhatsApp</strong> para los alumnos del curso.
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#f5f5f5;
    border-left:5px solid #25d366;
">
    La participación en el grupo <strong>no es obligatoria, pero sí muy recomendable</strong>.
</p>

<p style="margin-bottom:20px;">
    En este tipo de formación online es bastante habitual que surjan dudas, bloqueos o momentos
    en los que uno puede sentir que está avanzando solo, sobretodo fuera de los horarios de las tutorías. Tener contacto con otros compañeros
    puede ayudar mucho a que la experiencia sea más cercana, dinámica y llevadera.
</p>

<p style="margin-bottom:20px;">
    Además de poder plantearme dudas directamente, en el grupo podréis:
</p>

<ul style="margin-bottom:25px; padding-left:22px;">
    <li style="margin-bottom:8px;">Ayudaros entre vosotros/as.</li>
    <li style="margin-bottom:8px;">Compartir soluciones, recursos y avisos.</li>
    <li style="margin-bottom:8px;">Daros ánimos y motivaros durante estos meses de formación.</li>
    <li style="margin-bottom:8px;">Conocer a otras personas del sector, crear contactos y empezar a construir una
        pequeña <strong>red profesional</strong> que os pueda resultar útil de cara a futuras oportunidades laborales.</li>
</ul>

<p style="margin-bottom:20px;">
    En otros cursos este tipo de grupos suelen funcionar muy bien y terminan creando un ambiente
    estupendo entre compañeros.
</p>

<p style="margin-bottom:10px;">
    Os dejo aquí el enlace para uniros al grupo:
</p>

<p style="margin-bottom:30px; text-align:center;">
    <a href="https://chat.whatsapp.com/JlOZ6wHsg31EIf2vJ5LqlJ"
       target="_blank"
       style="
           display:inline-block;
           background:#25d366;
           color:#ffffff;
           font-weight:bold;
           padding:14px 28px;
           border-radius:6px;
           text-decoration:none;
       ">
        Unirme al grupo de WhatsApp
    </a>
</p>

<p style="margin-bottom:20px;">
    Si alguno tiene problemas con el enlace que me escriba y se lo mando yo por whatsapp
</p>

<p style="margin-bottom:20px;">
    Espero que os animéis a entrar y que entre todos/as podamos crear un buen grupo de apoyo
    durante el curso.
</p>

<p style="margin-top:30px;">
    Un saludo,<br>
    <strong>Alexandra Moltó</strong><br>
    <span style="color:#777777;">Tutora del curso</span>
</p>

</div>
"""

    return html


