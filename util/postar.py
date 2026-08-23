import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import traceback
import os

load_dotenv()
class Notificacao:
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    EMAIL = os.getenv("EMAIL")
    SENHA = os.getenv("EMAIL_PASSWORD")
    USER_MAIL = os.getenv("USER_MAIL")

    def envia_notificacao(self, usuario_email, titulo, descricao, area, prioridade, status):
        user_name= usuario_email.split("@")[0] if usuario_email else "Novo Usuário" 
        destinatarios = [self.USER_MAIL, usuario_email]

        try:   
            assunto = f"[{prioridade}] {titulo}"
            corpo = f"""
                            Olá, {user_name}!

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
            
            destinatarios = [self.USER_MAIL, usuario_email]

            mensagem = MIMEMultipart()
            mensagem["From"] = self.EMAIL
            mensagem["To"] = ", ".join(destinatarios)
            mensagem["Subject"] = assunto
            mensagem.attach(MIMEText(corpo, "plain"))

            with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT, timeout=20) as servidor:
                servidor.ehlo()
                servidor.starttls()
                servidor.ehlo()
                servidor.login(self.EMAIL, self.SENHA)
                servidor.sendmail(
                    self.EMAIL,
                    destinatarios,
                    mensagem.as_string()
                )
            

            return {
                "status": True,
                "message": "E-mail enviado com sucesso."
            }

        except Exception as e:
            traceback.print_exc()
            return {
                "status": False,
                "message": str(e)
            }
