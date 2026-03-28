# Move blocos literais tirando-os dinamicamente na apresentação linear formatando simulacros em redes instantâneas comunicacionais efêmeras.
def mensage(mensagens):
    for mensagem in mensagens:
        msg = (mensagem.title())
        print (msg)
        
msgs = ['olá', 'boa tarde', 'boa noite'] 
mensage(msgs)

def send_messages(msgs, sent_mensages):
    perfil = input("Digite seu nome de usuário: ")
    while msgs:  
        current_message = msgs.pop()
        print(f"{perfil}: {current_message}")
        sent_mensages.append(current_message)
sent_mensages = []
send_messages(msgs, sent_mensages)
print(f"\nMensagens enviadas {sent_mensages}")




mensage(sent_mensages[:])