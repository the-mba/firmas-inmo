import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-e", "--enviar_a", dest="verbose",
                    help="Send list of people to send email. Usage:  python .\firmas-generator.py -e \"Mario\"")
args = parser.parse_args()

from pathlib import Path
from enviar_firmas_por_email import enviar_email_a

personas_a_enviar = []
if args.verbose is not None:
    personas_a_enviar = args.verbose.split(",")

texto = """<div align="{align}">
	{Saludo}
	<br>
	{Persona_y_título}
  <br>
	<span style="vertical-align: {vertical_align}px;">{opinión_google}</span>
	<a href="{link_opinión_google}" target="_blank" rel="noopener noreferrer">
		 <img style="width: 32px; height: 32px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/logo_google_32x32.png" alt="Google Logo" width="32" height="32"/></a>
	<br>
	<a href="{link}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
		<img src="http://media.ibizavende.com/fotos/firma_email/{nombre_foto}" alt="{alt_foto}" style="width: 120px; height: 120px;" width="120" height="120">
	</a>
	{abrir_comentario_html_logo}<a href="{link}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
		<img src="http://media.ibizavende.com/fotos/firma_email/{nombre_logo}" alt="{alt_logo}" style="width: {ancho_logo}px; height: 120px;" width="{ancho_logo}" height="120">
	</a>{cerrar_comentario_html_logo}
	<br>
	<a href="mailto:{email}" target="_blank" rel="noopener noreferrer">
		 {email}</a>
	<a href="{link}" target="_blank" rel="noopener noreferrer">
		 {link}
	</a>
	<br>
    {dirección}
	<br>
	<div style="margin-top:5px">
		{quitar_link_logo_whatsapp__abrir}<a href="https://wa.me/0034{tel_1}{tel_2}{tel_3}/?text=Hola%2C%20{ciudad}Vende!" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">{quitar_link_logo_whatsapp__cerrar}
			<img style="width: 32px; height: 32px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/WhatsApp_logo-color-vertical.svg" alt="WhatsApp Logo" width="32" height="32">
		{quitar_link_logo_whatsapp__abrir}</a>{quitar_link_logo_whatsapp__cerrar}
		<span style="vertical-align: {vertical_align}px;">
			&nbsp;&nbsp;&nbsp; M:&nbsp;+34&nbsp;{tel_1}&nbsp;{tel_2}&nbsp;{tel_3}{abrir_comentario_html_fijo}&nbsp;&nbsp;&nbsp; Tf:&nbsp;+34&nbsp;{fijo_1}&nbsp;{fijo_2}&nbsp;{fijo_3}&nbsp;{fijo_4}{cerrar_comentario_html_fijo}
		</span>
	</div>
	<div style="margin-top: 7px;">
		{logo_facebook_abrir}<a href="{link_facebook}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/036-facebook.svg" alt="Facebook Logo" width="32" height="31">
		</a>&nbsp;&nbsp;&nbsp;{logo_facebook_cerrar}
		{logo_instagram_abrir}<a href="{link_instagram}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/029-instagram.svg" alt="Instagram Logo" width="32" height="31">
		</a>&nbsp;&nbsp;&nbsp;{logo_instagram_cerrar}
		{logo_twitter_abrir}<a href="{link_twitter}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/008-twitter.svg" alt="Twitter Logo" width="32" height="31">
		</a>&nbsp;&nbsp;&nbsp;{logo_twitter_cerrar}
		{logo_linkedin_abrir}<a href="{link_linkedin}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/027-linkedin.svg" alt="LinkedIn Logo" width="32" height="31">
		</a>&nbsp;&nbsp;&nbsp;{logo_linkedin_cerrar}
		{logo_youtube_abrir}<a href="{link_youtube}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/001-youtube.svg" alt="YouTube Logo" width="32" height="31">
		</a>&nbsp;&nbsp;&nbsp;{logo_youtube_cerrar}
		<br>
		<div style="font-size: 10px; color: green; margin-top: 5px;">
			{Ecomensaje}
		</div>
		<div style="font-size: 8px; color: grey;">
			<p>
				{confidencial}
			</p>
			<p>
				{lopd}
			</p>
		</div>
	</div>
</div>
"""

align = {"Mail": "left", "Mobilia": "center"}

Saludo = {
    "Spanish": "Muchas gracias, un saludo desde {ciudad}.",
    "English": "Kind regards, greetings from {ciudad}.",
    "Italian": "Grazie mille, cordiali saluti da {ciudad}.",
}

vertical_align = {"Mail": "12", "Mobilia": "0"}

opinión_google = {
    "Spanish": "Gracias por dejarnos tu opinión en",
    "English": "We would appreciate your feedback on",
    "Italian": "La ringraziamo per lasciarci una recensione su",
}

link_opinión_google = {
    "Ibiza": "https://g.page/Ibizavende/review?gm",
    "Madrid": "https://g.page/r/CY5PYszSdskDEAI/review",
}

link = {"Ibiza": "www.ibizavende.com", "Madrid": "www.madridvende.com"}

abrir_comentario_html_logo = {"Mail": "", "Mobilia": "<!--"}

nombre_logo = {"Ibiza": "firma_logo_ibiza_v3.png", "Madrid": "firma_logo_madrid.png"}

alt_logo = {"Ibiza": "IbizaVende Logo", "Madrid": "MadridVende Logo"}

ancho_logo = {"Ibiza": "120", "Madrid": "120"}

cerrar_comentario_html_logo = {"Mail": "", "Mobilia": "-->"}

dirección = {
    "Ibiza": {
        "Spanish": """Calle Pere de Portugal 5, 07800 Ibiza.""",
        "English": """Calle Pere de Portugal 5, 07800 Ibiza.""",
        "Italian": """Calle Pere de Portugal 5, 07800 Ibiza.""",
    },
    "Madrid": {
        "Spanish": """Calle Ortega y Gasset 56, Salamanca, 28006, Madrid
(Solicitar Cita Previa)""",
        "English": """Calle Ortega y Gasset 56, Salamanca, 28006, Madrid
(Solicitar Cita Previa)""",
        "Italian": """Calle Ortega y Gasset 56, Salamanca, 28006, Madrid
(Solicitar Cita Previa)""",
    },
}

fijo_1 = {
    "Ibiza": "971",
    "Madrid": "620",
}

fijo_2 = {"Ibiza": "93", "Madrid": "63"}

fijo_3 = {"Ibiza": "49", "Madrid": "49"}

fijo_4 = {"Ibiza": "88", "Madrid": "81"}

link_facebook = {
    "Ibiza": "http://www.facebook.com/ibizavende",
    "Madrid": "https://www.facebook.com/MadridVendeRealEstate",
}

link_instagram = {
    "Ibiza": "https://www.instagram.com/ibizavende",
    "Madrid": "https://www.instagram.com/madrid.vende",
}

link_twitter = {
    "Ibiza": "https://twitter.com/ibizavende",
    "Madrid": "https://twitter.com/MadridVende",
}

link_linkedin = {
    "Ibiza": "https://linkedin.com/company/ibiza-se-vende",
    "Madrid": "https://linkedin.com/company/madrid-vende",
}

link_youtube = {
    "Ibiza": "https://www.youtube.com/channel/UC72EbAx24raL6dArHs8B46g",
    "Madrid": "https://www.youtube.com/channel/UCEwHjWVPEGL80h73AQ98oRg",
}

Ecomensaje = {
    "Spanish": "Antes de imprimir este mensaje, asegúrate de que es necesario. El medio ambiente está en nuestra mano.",
    "English": "Please consider the environment before printing this email.",
    "Italian": "Si prega di considerare l'ambiente prima di stampare questa e-mail.",
}

confidencial = {
    "Spanish": "La información incluida en el presente correo electrónico es SECRETO PROFESIONAL Y CONFIDENCIAL, siendo para el uso exclusivo del destinatario arriba mencionado. Si usted no es el destinatario señalado o ha recibido esta comunicación por error, le informamos que está totalmente prohibida cualquier divulgación, distribución o reproducción de esta comunicación, le rogamos que nos lo notifique inmediatamente y nos devuelva el mensaje original a la dirección arriba mencionada. Gracias.",
    "English": "The information contained in this e-mail is LEGALLY PRIVILEDGED AND CONFIDENTIAL and is intended only for the use of the addressee named above. If the reader of this message is not the intended recipient or have received this communication in error, please be aware that any dissemination, distribution or duplication of this communication is strictly prohibited, and please notify us immediately and return the original message. Thank you.",
    "Italian": "Le informazioni contenute in questa e-mail sono LEGALMENTE PRIVILEGIATE E CONFIDENZIALI e sono destinate solo all'uso del destinatario sopra indicato. Se il lettore di questo messaggio non è il destinatario previsto o ha ricevuto questa comunicazione per errore, si prega di essere a conoscenza che qualsiasi diffusione, distribuzione o duplicazione di questa comunicazione è severamente vietata e si prega di avvisarci immediatamente e restituire il messaggio originale. Grazie.",
}

lopd = {
    "Spanish": "En cumplimiento con lo dispuesto en la LOPD 15/99 le informamos que sus datos han sido incluidos en nuestro fichero de base de datos,con el fin de hacer efectiva la comunicación entre ambas partes. Si lo desea puede ejercer su derecho de ACCESO, RECTIFICACIÓN, CANCELACIÓN Y OPOSICION comunicándolo a través del mail: {email_arco}.",
    "English": "According to the current legislation (LOPD 15/99), we inform you that the information regarding your company has been included in our database in order to make communications between us efficient. If you wish so, you have the right to access, modify, cancel or refuse via e-mail to {email_arco}.",
    "Italian": "In conformità alla LOPD 15/99, ti informiamo che i tuoi dati sono stati inclusi nel nostro database al fine di rendere efficace la comunicazione tra le due parti. Se lo desideri, puoi esercitare il tuo diritto di ACCESSO, RETTIFICA, CANCELLAZIONE E OPPOSIZIONE comunicandolo via e-mail a {email_arco}.",
}

email_arco = {"Ibiza": "info@ibizavende.com", "Madrid": "info@madridvende.com"}

ciudades = ["Ibiza", "Madrid"]
personas = [
    {
        "nombre": "Carol",
        "Persona_y_título": {
            "Spanish": "Carolina Azcona, CEO & Founder.",
            "English": "Carolina Azcona, CEO & Founder.",
            "Italian": "Carolina Azcona, CEO & Founder.",
        },
        "sedes": ["Ibiza", "Madrid"],
        "nombre_foto": "firma_carol_v4.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Carolina Azcona",
            "English": "Photo portrait of Carolina Azcona",
            "Italian": "Photo portrait of Carolina Azcona",
        },
        "email": {"Ibiza": "info@ibizavende.com", "Madrid": "info@madridvende.com"},
        "tel_1": "610",
        "tel_2": "544",
        "tel_3": "081",
        "logo_whatsapp_con_link": False,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": "<!--"},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": "-->"},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Goya",
        "Persona_y_título": {
            "Spanish": "Goya Balbuena, Sales and Rental Manager.",
            "English": "Goya Balbuena, Sales and Rental Manager.",
            "Italian": "Goya Balbuena, Sales and Rental Manager.",
        },
        "sedes": ["Ibiza", "Madrid"],
        "nombre_foto": "firma_goya_v4.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Goya Balbuena",
            "English": "Photo portrait of Goya Balbuena",
            "Italian": "Photo portrait of Goya Balbuena",
        },
        "email": {"Ibiza": "goya@ibizavende.com", "Madrid": "info@madridvende.com"},
        "tel_1": "620",
        "tel_2": "634",
        "tel_3": "981",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "LinkedIn"],
            "Italian": ["Facebook", "Instagram", "LinkedIn"],
        },
    },
    {
        "nombre": "Mario",
        "Persona_y_título": {
            "Spanish": "Mario Balbuena, CTO & CIO.",
            "English": "Mario Balbuena, CTO & CIO.",
            "Italian": "Mario Balbuena, CTO & CIO.",
        },
        "sedes": ["Ibiza", "Madrid"],
        "nombre_foto": "firma_mario.jpg",
        "alt_foto": {
            "Spanish": "Foto retrato de Mario Balbuena",
            "English": "Photo portrait of Mario Balbuena",
            "Italian": "Photo portrait of Mario Balbuena",
        },
        "email": {"Ibiza": "mario@ibizavende.com", "Madrid": "mario@madridvende.com"},
        "tel_1": "676",
        "tel_2": "861",
        "tel_3": "730",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Enrique",
        "Persona_y_título": {
            "Spanish": "Enrique Balbuena, Architect.",
            "English": "Enrique Balbuena, Architect.",
            "Italian": "Enrique Balbuena, Architect.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_enrique.jpg",
        "alt_foto": {
            "Spanish": "Foto retrato de Enrique Balbuena",
            "English": "Photo portrait of Enrique Balbuena",
            "Italian": "Photo portrait of Enrique Balbuena",
        },
        "email": {
            "Ibiza": "enrique@ibizavende.com",
            "Madrid": "enrique@madridvende.com",
        },
        "tel_1": "649",
        "tel_2": "851",
        "tel_3": "620",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Lorena",
        "Persona_y_título": {
            "Spanish": "Lorena Dierking, Senior Sales and Rentals Manager.",
            "English": "Lorena Dierking, Senior Sales and Rentals Manager.",
            "Italian": "Lorena Dierking, Senior Sales and Rentals Manager.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_lorena_v3.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Lorena Dierking",
            "English": "Photo portrait of Lorena Dierking",
            "Italian": "Photo portrait of Lorena Dierking",
        },
        "email": {"Ibiza": "lorena@ibizavende.com", "Madrid": "lorena@madridvende.com"},
        "tel_1": "679",
        "tel_2": "757",
        "tel_3": "684",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Clara",
        "Persona_y_título": {
            "Spanish": "Clara de la Fuente, Sales and Rentals.",
            "English": "Clara de la Fuente, Sales and Rentals.",
            "Italian": "Clara de la Fuente, Sales and Rentals.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_clara_v3.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Clara de la Fuente",
            "English": "Photo portrait of Clara de la Fuente",
            "Italian": "Photo portrait of Clara de la Fuente",
        },
        "email": {
            "Ibiza": "clara@ibizavende.com",
            "Madrid": "clara@madridvende.com",
        },
        "tel_1": "648",
        "tel_2": "478",
        "tel_3": "458",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Lara",
        "Persona_y_título": {
            "Spanish": "Lara Slanzi, Sales and Rentals.",
            "English": "Lara Slanzi, Sales and Rentals.",
            "Italian": "Lara Slanzi, Vendite e Affitti.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_lara_v3.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Lara Slanzi",
            "English": "Photo portrait of Lara Slanzi",
            "Italian": "Photo portrait of Lara Slanzi",
        },
        "email": {"Ibiza": "lara@ibizavende.com", "Madrid": "lara@madridvende.com"},
        "tel_1": "636",
        "tel_2": "497",
        "tel_3": "119",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "María Clara",
        "Persona_y_título": {
            "Spanish": "María Clara Torres, Sales and Rentals.",
            "English": "María Clara Torres, Sales and Rentals.",
            "Italian": "María Clara Torres, Sales and Rentals.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_mariaclara.jpg",
        "alt_foto": {
            "Spanish": "Foto retrato de Maria Clara Torres",
            "English": "Photo portrait of Maria Clara Torres",
            "Italian": "Photo portrait of Maria Clara Torres",
        },
        "email": {
            "Ibiza": "mariaclara@ibizavende.com",
            "Madrid": "mariaclara@madridvende.com",
        },
        "tel_1": "695",
        "tel_2": "364",
        "tel_3": "572",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Joaquín",
        "Persona_y_título": {
            "Spanish": "Joaquín Marí Marrodan, Sales and Rentals Manager.",
            "English": "Joaquín Marí Marrodan, Sales and Rentals Manager.",
            "Italian": "Joaquín Marí Marrodan, Sales and Rentals Manager.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_joaquin_v3.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Joaquín Marí Marrodan",
            "English": "Photo portrait of Joaquín Marí Marrodan",
            "Italian": "Photo portrait of Joaquín Marí Marrodan",
        },
        "email": {"Ibiza": "jmari@ibizavende.com", "Madrid": "jmari@madridvende.com"},
        "tel_1": "639",
        "tel_2": "505",
        "tel_3": "212",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Cristina",
        "Persona_y_título": {
            "Spanish": "Cristina Santos, Sales and Rentals.",
            "English": "Cristina Santos, Sales and Rentals.",
            "Italian": "Cristina Santos, Sales and Rentals.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_cristina_v3.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Cristina Santos",
            "English": "Photo portrait of Cristina Santos",
            "Italian": "Photo portrait of Cristina Santos",
        },
        "email": {
            "Ibiza": "cristina@ibizavende.com",
            "Madrid": "cristina@madridvende.com",
        },
        "tel_1": "682",
        "tel_2": "531",
        "tel_3": "188",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
    {
        "nombre": "Valentín",
        "Persona_y_título": {
            "Spanish": "Valentín Limousin, Junior Sales and Rentals.",
            "English": "Valentín Limousin, Junior Sales and Rentals.",
            "Italian": "Valentín Limousin, Junior Sales and Rentals.",
        },
        "sedes": ["Ibiza"],
        "nombre_foto": "firma_valentin_v3.png",
        "alt_foto": {
            "Spanish": "Foto retrato de Valentin Limousin",
            "English": "Photo portrait of Valentin Limousin",
            "Italian": "Photo portrait of Valentin Limousin",
        },
        "email": {
            "Ibiza": "valentin@ibizavende.com",
            "Madrid": "valentin@madridvende.com",
        },
        "tel_1": "660",
        "tel_2": "131",
        "tel_3": "164",
        "logo_whatsapp_con_link": True,
        "abrir_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "cerrar_comentario_html_fijo": {"Ibiza": "", "Madrid": ""},
        "logos_redes": {
            "Spanish": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "English": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
            "Italian": ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube"],
        },
    },
]
idiomas = ["Spanish", "English", "Italian"]
entornos = ["Mail", "Mobilia"]


for persona in personas:
    firmas = []
    nombre_para_paths = persona["nombre"].lower().replace(" ", "")
    for ciudad in ciudades:
        if ciudad not in persona["sedes"]:
            continue
        for entorno in entornos:
            for idioma in idiomas:
                filepath = nombre_para_paths + "/"
                filename = (
                    "_".join(
                        [
                            "firma",
                            ciudad.lower(),
                            nombre_para_paths,
                            entorno.lower(),
                            idioma.lower(),
                        ]
                    )
                    + ".html"
                )
                keys = {
                    "align": align[entorno],
                    "Saludo": Saludo[idioma].format(ciudad=ciudad),
                    "Persona_y_título": persona["Persona_y_título"],
                    "vertical_align": vertical_align[entorno],
                    "opinión_google": opinión_google[idioma],
                    "link_opinión_google": link_opinión_google[ciudad],
                    "link": link[ciudad],
                    "nombre_foto": persona["nombre_foto"],
                    "alt_foto": persona["alt_foto"][idioma],
                    "abrir_comentario_html_logo": abrir_comentario_html_logo[entorno],
                    "nombre_logo": nombre_logo[ciudad],
                    "alt_logo": alt_logo[ciudad],
                    "ancho_logo": ancho_logo[ciudad],
                    "cerrar_comentario_html_logo": cerrar_comentario_html_logo[entorno],
                    "email": persona["email"][ciudad],
                    "dirección": dirección[ciudad][idioma],
                    "ciudad": ciudad,
                    "tel_1": persona["tel_1"],
                    "tel_2": persona["tel_2"],
                    "tel_3": persona["tel_3"],
                    "quitar_link_logo_whatsapp__abrir": (
                        "" if persona["logo_whatsapp_con_link"] else "<!--"
                    ),
                    "quitar_link_logo_whatsapp__cerrar": (
                        "" if persona["logo_whatsapp_con_link"] else "-->"
                    ),
                    "abrir_comentario_html_fijo": persona["abrir_comentario_html_fijo"][
                        ciudad
                    ],
                    "cerrar_comentario_html_fijo": persona[
                        "cerrar_comentario_html_fijo"
                    ][ciudad],
                    "fijo_1": fijo_1[ciudad],
                    "fijo_2": fijo_2[ciudad],
                    "fijo_3": fijo_3[ciudad],
                    "fijo_4": fijo_4[ciudad],
                    "link_facebook": link_facebook[ciudad],
                    "link_instagram": link_instagram[ciudad],
                    "link_twitter": link_twitter[ciudad],
                    "link_linkedin": link_linkedin[ciudad],
                    "link_youtube": link_youtube[ciudad],
                    "Ecomensaje": Ecomensaje[idioma],
                    "confidencial": confidencial[idioma],
                    "lopd": lopd[idioma].format(email_arco=email_arco[ciudad]),
                    "logo_facebook_abrir": (
                        "" if "Facebook" in persona["logos_redes"][idioma] else "<!--"
                    ),
                    "logo_facebook_cerrar": (
                        "" if "Facebook" in persona["logos_redes"][idioma] else "-->"
                    ),
                    "logo_instagram_abrir": (
                        "" if "Instagram" in persona["logos_redes"][idioma] else "<!--"
                    ),
                    "logo_instagram_cerrar": (
                        "" if "Instagram" in persona["logos_redes"][idioma] else "-->"
                    ),
                    "logo_twitter_abrir": (
                        "" if "Twitter" in persona["logos_redes"][idioma] else "<!--"
                    ),
                    "logo_twitter_cerrar": (
                        "" if "Twitter" in persona["logos_redes"][idioma] else "-->"
                    ),
                    "logo_linkedin_abrir": (
                        "" if "LinkedIn" in persona["logos_redes"][idioma] else "<!--"
                    ),
                    "logo_linkedin_cerrar": (
                        "" if "LinkedIn" in persona["logos_redes"][idioma] else "-->"
                    ),
                    "logo_youtube_abrir": (
                        "" if "YouTube" in persona["logos_redes"][idioma] else "<!--"
                    ),
                    "logo_youtube_cerrar": (
                        "" if "YouTube" in persona["logos_redes"][idioma] else "-->"
                    ),
                }
                texto_formateado = texto.format(**keys)
                output_file = Path(filepath + filename)
                output_file.parent.mkdir(exist_ok=True, parents=True)
                output_file.write_text(texto_formateado, encoding="UTF-8")
                # print(f"Generada firma para {persona['nombre']} en {ciudad} en idioma {idioma} en entorno {entorno}")

                firmas.append(output_file)

    if persona["nombre"] in personas_a_enviar:
        enviar_email_a(persona["email"]["Ibiza"], persona["nombre"], firmas)
