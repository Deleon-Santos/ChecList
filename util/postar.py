import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("EMAIL"))
print(os.getenv("SMTP_SERVER"))
print(os.getenv("SMTP_PORT"))
print(os.getenv("USER_MAIL"))

class Notificacao:
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    EMAIL = os.getenv("EMAIL")
    SENHA = os.getenv("EMAIL_PASSWORD")
    USER_MAIL = os.getenv("USER_MAIL")

    def envia_notificacao(self, user, titulo, descricao, area, prioridade, status):
        try:   
            print("Enviando e-mail...")  
            assunto = f"[{prioridade}] {titulo}"
            corpo = f"""
                            Olá, {user}!
                            Você recebeu uma nova notificação de ocorrência.
                            Título: {titulo}
                            Descrição: {descricao}
                            Área: {area}
                            Prioridade: {prioridade}
                            Status: {status}

                            Acesse o sistema para mais detalhes.

                            Atenciosamente,
                            Equipe de desenvolvimento.
                            """
            print("corpo")
            mensagem = MIMEMultipart()
            mensagem["From"] = self.EMAIL
            mensagem["To"] = self.USER_MAIL
            mensagem["Subject"] = assunto
            mensagem.attach(MIMEText(corpo, "plain"))

            servidor = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            servidor.starttls()
            servidor.login(self.EMAIL, self.SENHA)
            servidor.send_message(mensagem)
            servidor.quit()

            return {
                "status": True,
                "message": "E-mail enviado com sucesso."
            }

        except Exception as e:
            
            print(type(e))
            print(e)

