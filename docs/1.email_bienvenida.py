# =====================================================
# email_bienvenida.py
# =====================================================

ASUNTO = (
    "Bienvenida al curso Programación con Lenguajes Orientados a Objetos"
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
    <div style="font-size:14px; letter-spacing:1px; opacity:0.9;"></div>
    <div style="font-size:26px; font-weight:bold; margin-top:6px;">¡Bienvenidos/as!</div>
    <div style="font-size:15px; margin-top:6px;">MF0227 - Programación con Lenguajes Orientados a Objetos</div>
</div>

<p style="margin-bottom:20px;">
    Buenos días a todos/as:
</p>

<p style="margin-bottom:20px;">
    Mi nombre es <strong>Alexandra Moltó</strong> y voy a ser vuestra tutora durante los
    próximos meses en el curso <strong>“MF0227 - Programación con Lenguajes Orientados a Objetos”</strong>,
    que comienza hoy, <strong>05/10/2026</strong>, y finalizará el <strong>21/12/2026</strong>.
</p>

<p style="margin-bottom:20px;">
    Quería aprovechar este primer mensaje para daros la bienvenida y presentarme. Durante el
    desarrollo del curso estaré a vuestra disposición para acompañaros en el aprendizaje,
    resolver vuestras dudas, corregir las actividades y realizar el seguimiento de vuestro
    progreso. Mi objetivo es ayudaros a aprovechar al máximo la formación y avanzar de una
    manera organizada y llevadera.
</p>

<p style="margin-bottom:20px;">
    Os recomiendo que <strong>accedáis cuanto antes al campus</strong> para comprobar que podéis
    entrar correctamente y empezar a familiarizaros con la plataforma.
</p>

<p style="
    margin-bottom:25px;
    padding:15px;
    background:#fff3cd;
    border-left:5px solid #ffc107;
">
    <strong>Recordad:</strong> el primer acceso y la primera prueba evaluable deben realizarse antes del <strong>10/10/2026</strong>
</p>

<h3 style="color:#0066cc; margin-top:30px; margin-bottom:10px;">
    ¿Qué es eso de la primera prueba evaluable?
</h3>

<p style="margin-bottom:20px;">
    Es muy sencillo 😊. Durante los <strong>primeros 5 días del curso</strong> tendréis que
    entregar <strong>una práctica o realizar un test</strong> de cara a que se confirme la matrícula.
</p>

<p style="margin-bottom:25px;">
    No es necesario esperar al último momento: podéis acceder ya al contenido y comprobar
    qué actividad o prueba tenéis disponible para realizar.
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
    En los próximos días os haré llegar un <strong>cronograma orientativo</strong> para que
    podamos tener una referencia de lo que deberíamos ir completando cada semana.
</p>

<p style="
    margin-bottom:20px;
    padding:15px;
    background:#f5f5f5;
    border-left:5px solid #007bff;
">
    Os recuerdo también que la formación es <strong>100 % online</strong>, aunque habrá un
    <strong>examen presencial el último día del curso</strong>.
</p>

<p style="margin-bottom:20px;">
    Para cualquier duda relacionada con los contenidos o el desarrollo del curso, podéis
    escribirme sin problema a través del <strong>email de la plataforma.</strong>.
</p>

<p style="margin-bottom:20px;">
    Además, en los próximos días realizaremos una <strong>videollamada de bienvenida</strong>,
    en la que aprovecharemos para presentarnos y hacer un pequeño recorrido por la plataforma,
    de manera que todos sepamos dónde encontrar los diferentes recursos y actividades.
</p>

<p style="margin-bottom:20px;">
    Os deseo mucho ánimo en esta nueva etapa formativa. Espero que tengamos un curso muy
    productivo y que podamos disfrutar del aprendizaje.
</p>

<p style="margin-top:30px;">
    <strong>¡Bienvenidos/as!</strong>
</p>

<p style="margin-top:20px;">
    Un saludo,<br>
    <strong>Alexandra Moltó</strong><br>
    <span style="color:#777777;">Tutora del curso</span>
</p>

</div>
"""

    return html





