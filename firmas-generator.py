from pathlib import Path

texto = """<div align="{align}">
	{Saludo}
	<br>
	{Persona_y_título}
	<br>
	{opinión_google}
	<a href="{link_opinión_google}" target="_blank" rel="noopener noreferrer">
		 Google</a>.
	<br>
	<a href="{link}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
		<img src="http://media.ibizavende.com/fotos/firma_email/{nombre_foto}" alt="{alt_foto}" style="width: 120px; height: 120px;" width="120" height="120">
	</a>
	{abrir_comentario_html_logo}<a href="{link}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
		<img src="https://media.ibizavende.com/fotos/firma_email/{nombre_logo}" alt="{alt_logo}" style="width: 120px; height: 120px;" width="120" height="120">
	</a>{cerrar_comentario_html_logo}
	<br>
	<a href="mailto:{email}" target="_blank" rel="noopener noreferrer">
		 {email}
	</a>
	<a href="{link}" target="_blank" rel="noopener noreferrer">
		 {link}
	</a>
	<br>
	 Inmobiliaria Plaza de Villa 6, 1º, 07800 Ibiza
	<br>
	 ({como_llegar}, Dalt Vila)
	<br>
	<div style="margin-top:5px">
		<a href="https://wa.me/0034610544081/?text=Hola%2C%20{ciudad}Vende!" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 32px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/WhatsApp_logo-color-vertical.svg" alt="WhatsApp Logo" width="32" height="32">
		</a>
		<span style="vertical-align: 11px;">
			 M:&nbsp;+34&nbsp;{tel_1}&nbsp;{tel_2}&nbsp;{tel_3}{abrir_comentario_html_fijo} Tf:&nbsp;+34&nbsp;{fijo_1}&nbsp;{fijo_2}&nbsp;{fijo_3}&nbsp;{fijo_4}{cerrar_comentario_html_fijo}
		</span>
	</div>
	<div style="margin-top: 7px;">
		<a href="{link_facebook}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/036-facebook.svg" alt="Facebook Logo" width="32" height="31">
		</a>
		<a href="{link_instagram}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/029-instagram.svg" alt="Instagram Logo" width="32" height="31">
		</a>
		<a href="{link_twitter}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/008-twitter.svg" alt="Twitter Logo" width="32" height="31">
		</a>
		<a href="{link_linkedin}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/027-linkedin.svg" alt="LinkedIn Logo" width="32" height="31">
		</a>
		<a href="{link_youtube}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
			<img style="width: 32px; height: 31px;" src="http://media.ibizavende.com/fotos/firma_email/redes_sociales/001-youtube.svg" alt="YouTube Logo" width="32" height="31">
		</a>
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

align = {
  "Mail": "left",
  "Mobilia": "center"
}

Saludo = {
  "Español": "Muchas gracias, un saludo desde Ibiza.",
  "Inglés": "Kind regards, greetings from Ibiza."
}

opinión_google = {
  "Español": "Gracias por dejarnos tu opinión en",
  "Inglés": "We would appreciate your feedback on"
}

link_opinión_google = {
  "Ibiza": "https://g.page/Ibizavende/review?gm",
  "Madrid": "https://g.page/r/CY5PYszSdskDEAI/review"
}

link = {
  "Ibiza": "www.ibizavende.com",
  "Madrid": "www.madridvende.com"
}

abrir_comentario_html_logo = {
  "Mail": "",
  "Mobilia": "<!--"
}

nombre_logo = {
  "Ibiza": "firma_logo_ibiza.png",
  "Madrid": "firma_logo_madrid.png"
}

alt_logo = {
  "Ibiza": "IbizaVende Logo",
  "Madrid": "MadridVende Logo"
}

cerrar_comentario_html_logo = {
  "Mail": "",
  "Mobilia": "-->"
}

como_llegar = {
  "Español": "al lado del museo de Arte Contemporáneo",
  "Inglés": "beside the Museum of Contemporary Art"
}

fijo_1 = {
  "Ibiza": "971",
  "Madrid": "610"  # TODO conseguir un teléfono fijo en Madrid (para que? hace falta de verdad??)
}

fijo_2 = {
  "Ibiza": "93",
  "Madrid": "54" 
}

fijo_3 = {
  "Ibiza": "49",
  "Madrid": "40" 
}

fijo_4 = {
  "Ibiza": "88",
  "Madrid": "81" 
}

link_facebook = {
  "Ibiza": "http://www.facebook.com/ibizavende",
  "Madrid": "https://www.facebook.com/MadridVendeRealEstate"
}

link_instagram = {
  "Ibiza": "https://www.instagram.com/ibizavende",
  "Madrid": "https://www.instagram.com/madrid.vende"
}

link_twitter = {
  "Ibiza": "https://twitter.com/ibizavende",
  "Madrid": "https://twitter.com/MadridVende"
}

link_linkedin = {
  "Ibiza": "https://linkedin.com/company/ibiza-se-vende",
  "Madrid": "https://linkedin.com/company/madrid-vende"
}

link_youtube = {
  "Ibiza": "https://www.youtube.com/channel/UC72EbAx24raL6dArHs8B46g",
  "Madrid": "https://www.youtube.com/channel/UCEwHjWVPEGL80h73AQ98oRg"
}

Ecomensaje = {
  "Español": "Antes de imprimir este mensaje, asegúrate de que es necesario. El medio ambiente está en nuestra mano.",
  "Inglés": "Please consider the environment before printing this email."
}

confidencial = {
  "Español": "La información incluida en el presente correo electrónico es SECRETO PROFESIONAL Y CONFIDENCIAL, siendo para el uso exclusivo del destinatario arriba mencionado. Si usted no es el destinatario señalado o ha recibido esta comunicación por error, le informamos que está totalmente prohibida cualquier divulgación, distribución o reproducción de esta comunicación, le rogamos que nos lo notifique inmediatamente y nos devuelva el mensaje original a la dirección arriba mencionada. Gracias.",
  "Inglés": "The information contained in this e-mail is LEGALLY PRIVILEDGED AND CONFIDENTIAL and is intended only for the use of the addressee named above. If the reader of this message is not the intended recipient or have received this communication in error, please be aware that any dissemination, distribution or duplication of this communication is strictly prohibited, and please notify us immediately and return the original message. Thank you."
}

lopd = {
  "Español": "En cumplimiento con lo dispuesto en la LOPD 15/99 le informamos que sus datos han sido incluidos en nuestro fichero de base de datos,con el fin de hacer efectiva la comunicación entre ambas partes. Si lo desea puede ejercer su derecho de ACCESO, RECTIFICACIÓN, CANCELACIÓN Y OPOSICION comunicándolo a través del mail: info@ibizavende.com.",
  "Inglés": "According to the current legislation (LOPD 15/99), we inform you that the information regarding your company has been included in our database in order to make communications between us efficient. If you wish so, you have the right to access, modify, cancel or refuse via e-mail to info@ibizavende.com."
}

ciudades = ["Ibiza", "Madrid"]
personas = [
  {
    "nombre": "carol",
    "Persona_y_título": "Carolina Azcona, CEO & Founder.",
    "nombre_foto": "firma_carol_v2.jpg",
    "alt_foto": {
      "Español": "Foto retrato de Carolina Azcona",
      "Inglés": "Photo portrait of Carolina Azcona"
    },
    "email": {
      "Ibiza": "info@ibizavende.com",
      "Madrid": "info@madridvende.com"
    },
    "tel_1": "610",
    "tel_2": "544",
    "tel_3": "081",
    "abrir_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": "<!--"
    },
    "cerrar_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": "-->"
    }
  },
  {
    "nombre": "goya",
    "Persona_y_título": "Goya Balbuena, CMO & CCO.",
    "nombre_foto": "firma_goya_v2.jpg",
    "alt_foto": {
      "Español": "Foto retrato de Goya Balbuena",
      "Inglés": "Photo portrait of Goya Balbuena"
    },
    "email": {
      "Ibiza": "goya@ibizavende.com",
      "Madrid": "goya@madridvende.com"
    },
    "tel_1": "620",
    "tel_2": "634",
    "tel_3": "981",
    "abrir_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    },
    "cerrar_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    }
  },
  {
    "nombre": "mario",
    "Persona_y_título": "Mario Balbuena, CTO & CIO.",
    "nombre_foto": "firma_mario.jpg",
    "alt_foto": {
      "Español": "Foto retrato de Mario Balbuena",
      "Inglés": "Photo portrait of Mario Balbuena"
    },
    "email": {
      "Ibiza": "mario@ibizavende.com",
      "Madrid": "mario@madridvende.com"
    },
    "tel_1": "676",
    "tel_2": "861",
    "tel_3": "730",
    "abrir_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    },
    "cerrar_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    }
  },
  {
    "nombre": "enrique",
    "Persona_y_título": "Enrique Balbuena, Architect.",
    "nombre_foto": "firma_enrique.jpg",
    "alt_foto": {
      "Español": "Foto retrato de Enrique Balbuena",
      "Inglés": "Photo portrait of Enrique Balbuena"
    },
    "email": {
      "Ibiza": "enrique@ibizavende.com",
      "Madrid": "enrique@madridvende.com"
    },
    "tel_1": "649",
    "tel_2": "851",
    "tel_3": "620",
    "abrir_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    },
    "cerrar_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    }
  },
  {
    "nombre": "lorena",
    "Persona_y_título": "Lorena Dierking, Sales and Rentals",
    "nombre_foto": "firma_lorena.jpg",
    "alt_foto": {
      "Español": "Foto retrato de Lorena Dierking",
      "Inglés": "Photo portrait of Lorena Dierking"
    },
    "email": {
      "Ibiza": "lorena@ibizavende.com",
      "Madrid": "lorena@madridvende.com"
    },
    "tel_1": "661",
    "tel_2": "424",
    "tel_3": "850",
    "abrir_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    },
    "cerrar_comentario_html_fijo": {
      "Ibiza": "",
      "Madrid": ""
    }
  }
]
idiomas = ["Español", "Inglés"]
entornos = ["Mail", "Mobilia"]


for ciudad in ciudades:
  for persona in personas:
    for entorno in entornos:
      for idioma in idiomas:
        filepath = persona["nombre"] + "/"
        filename = "_".join(["firma", ciudad.lower(), persona["nombre"], entorno.lower(), idioma.lower()]) + ".html"
        keys = {
          "align": align[entorno],
          "Saludo": Saludo[idioma],
          "Persona_y_título": persona["Persona_y_título"],
          "opinión_google": opinión_google[idioma],
          "link_opinión_google": link_opinión_google[ciudad],
          "link": link[ciudad],
          "nombre_foto": persona["nombre_foto"],
          "alt_foto": persona["alt_foto"][idioma],
          "abrir_comentario_html_logo": abrir_comentario_html_logo[entorno],
          "nombre_logo": nombre_logo[ciudad],
          "alt_logo": alt_logo[ciudad],
          "cerrar_comentario_html_logo": cerrar_comentario_html_logo[entorno],
          "email": persona["email"][ciudad],
          "como_llegar": como_llegar[idioma],
          "ciudad": ciudad,
          "tel_1": persona["tel_1"],
          "tel_2": persona["tel_2"],
          "tel_3": persona["tel_3"],
          "abrir_comentario_html_fijo": persona["abrir_comentario_html_fijo"][ciudad],
          "cerrar_comentario_html_fijo": persona["cerrar_comentario_html_fijo"][ciudad],
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
          "lopd": lopd[idioma]
        }
        texto_formateado = texto.format(**keys)
        output_file = Path(filepath + filename)
        output_file.parent.mkdir(exist_ok=True, parents=True)
        output_file.write_text(texto_formateado, encoding="UTF-8")