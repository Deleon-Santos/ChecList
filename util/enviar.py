
from util.postar import Notificacao

def notificar(user, titulo, descricao, area, prioridade, status):
    notificacao = Notificacao()
    resultado = notificacao.envia_notificacao(
        user=user,
        titulo=titulo,
        descricao=descricao,
        area=area,
        prioridade=prioridade,
        status=status
    )
    return resultado
