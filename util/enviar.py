from util.postar import Notificacao


class User:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


    if __name__ == "__main__":
        usuario = User(
            nome="João Silva",
            email="joao@email.com"
        )

        notificacao = Notificacao()

        notificacao.envia_notificacao(
            user=usuario,
            titulo="Chamado Atualizado",
            descricao="Seu chamado foi encaminhado para o setor responsável.",
            area="TI",
            prioridade="Alta"
        )