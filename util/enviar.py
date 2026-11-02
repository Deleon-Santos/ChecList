from util.postar import Notificacao

def notificar(usuario_email, titulo, descricao, area, prioridade, status):
    notificacao = Notificacao()
    notificacao.envia_notificacao(usuario_email, titulo, descricao, area, prioridade, status)
    return 
