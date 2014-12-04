from django.db import models
import smtplib

# Create your models here.
class Revendedor(models.Model):
    revend_apellido = models.CharField(max_length=60)
    revend_nombre = models.CharField(max_length=60)
    revend_tel1 = models.CharField(max_length=30)
    revend_tel2 = models.CharField(max_length=30)
    revend_email = models.EmailField(max_length=100)
    revend_sitio_web = models.URLField()
    revend_facebook = models.URLField()
    revend_linkedin = models.URLField()
    revend_observaciones = models.CharField(max_length=500)

    def __unicode__(self):             # __str__ en Python 3
        return self.revend_apellido + " " + self.revend_nombre


    def enviarCorreoRevendedor():
        """"Enviar correos desde la pantalla de Revendedores"""

        server = smtplib.SMTP('smtp.gmail.com', 587) #SMTP-Server, SMTP-Port

        #Next, log in to the server
        server.login("lunafraganciasmails@gmail.com", "sanmartin1001")

        #Send the mail
        mensaje = "\nPrueba correo Luna Fragancias" #Mensaje
        server.sendmail("remit@gmail.com", "dest@example.com", msg) #Envio del mensaje


# import smtplib
#
# def sendemail(from_addr, to_addr_list, cc_addr_list,
#               subject, message,
#               login, password,
#               smtpserver='smtp.gmail.com:587'):
#
#     header  = 'From: %s\n' % from_addr
#     header += 'To: %s\n' % ','.join(to_addr_list)
#     header += 'Cc: %s\n' % ','.join(cc_addr_list)
#     header += 'Subject: %s\n\n' % subject
#     message = header + message
#
#     server = smtplib.SMTP(smtpserver)
#     server.starttls()
#     server.login(login,password)
#     problems = server.sendmail(from_addr, to_addr_list, message)
#     server.quit()