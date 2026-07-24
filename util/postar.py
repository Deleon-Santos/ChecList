import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Notificacao:

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL = "seu_email@gmail.com"
    SENHA = "sua_senha_de_app"

    def envia_notificacao(self, user, titulo, descricao, area, prioridade):
        """
        user deve possuir ao menos:
            user.nome
            user.email
        """

        assunto = f"[{prioridade}] {titulo}"

        corpo = f"""
Olá, {user.nome}!

Você recebeu uma nova notificação.

Título: {titulo}
Descrição: {descricao}
Área: {area}
Prioridade: {prioridade}

Acesse o sistema para mais detalhes.

Atenciosamente,
Equipe do Sistema
"""

        mensagem = MIMEMultipart()
        mensagem["From"] = self.EMAIL
        mensagem["To"] = user.email
        mensagem["Subject"] = assunto

        mensagem.attach(MIMEText(corpo, "plain"))

        try:
            servidor = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            servidor.starttls()
            servidor.login(self.EMAIL, self.SENHA)

            servidor.send_message(mensagem)
            servidor.quit()

            return {
                "success": True,
                "message": "E-mail enviado com sucesso."
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }


    