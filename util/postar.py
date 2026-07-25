import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Notificacao:

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL = ""
    SENHA = ""

    def envia_notificacao(self, user, titulo, descricao, area, prioridade):
        try:
      
            assunto = f"[{prioridade}] {titulo}"

            corpo = f"""
                            Olá, {user}!

                            Você recebeu uma nova notificação.

                            Título: {titulo}
                            Descrição: {descricao}
                            Área: {area}
                            Prioridade: {prioridade}

                            Acesse o sistema para mais detalhes.

                            Atenciosamente,
                            Equipe do Sistema
                            """
            print("msn criada")
            mensagem = MIMEMultipart()
            mensagem["From"] = self.EMAIL
            mensagem["To"] = "exemplo@gmail.com"
            mensagem["Subject"] = assunto

            mensagem.attach(MIMEText(corpo, "plain"))
            print("scopo criado")
            

        
            servidor = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            servidor.starttls()
            servidor.login(self.EMAIL, self.SENHA)

            servidor.send_message(mensagem)
            servidor.quit()
            print(mensagem)

            return {
                "success": True,
                "message": "E-mail enviado com sucesso."
            }

        except Exception as e:
            print( {
                "success": False,
                "message": str(e)
            })


    