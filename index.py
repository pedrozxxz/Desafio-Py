#Pedro Lucas e João Pedro
estoque_atual = {
    "canetas": 150,
    "cadernos": 95,
    "lápis": 200,
    "borrachas": 30,
    "régua": 45,
    "cola": 60,
    "tesoura": 25,
    "marcador": 75,
    "clips": 120,
    "grampos": 40
}

movimentacoes_dia = [
    ("canetas", "saída", 25),
    ("cadernos", "entrada", 10),
    ("borrachas", "saída", 50),
    ("régua", "saída", 20),
    ("cola", "entrada", 15),
    ("tesoura", "saída", 10),
    ("marcador", "entrada", 25),
    ("clips", "saída", 30),
    ("grampos", "saída", 15),
    ("lápis", "saída", 45),
    ("canetas", "entrada", 50),
    ("cadernos", "saída", 35),
    ("borrachas", "entrada", 40),
    ("régua", "entrada", 30),
    ("cola", "saída", 25)
]

def mostrar_estoque(estoque):
    """Mostra o estoque atual"""
    print("\nESTOQUE ATUAL:")
    for produto, quantidade in sorted(estoque.items()):
        print(f"{produto.capitalize():<12} | {quantidade:>4} unidades")

def adicionar_movimentacao_manual():
    """Permite que o usuário adicione movimentações manualmente"""
    movimentacoes_manuais = []
    
    print("\nAGORA VOCÊ PODE ADICIONAR SUAS PRÓPRIAS MOVIMENTAÇÕES!")
    print("Digite 'sair' para terminar")
    print("-" * 50)
    
    while True:
        produto = input("\nDigite o nome do produto (ex: canetas, cadernos): ").strip().lower()
        
        if produto == 'sair':
            break
            
        if not produto:
            print("Por favor, digite um nome de produto.")
            continue
            
        tipo = input("Digite o tipo (entrada/saída): ").strip().lower()
        if tipo not in ['entrada', 'saída']:
            print("Tipo inválido! Digite 'entrada' ou 'saída'.")
            continue
            
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero!")
                continue
        except ValueError:
            print("Por favor, digite um número válido!")
            continue
            
        movimentacoes_manuais.append((produto, tipo, quantidade))
        print(f"Movimentação adicionada: {quantidade} {produto} - {tipo}")
        
        continuar = input("\nDeseja adicionar outra movimentação? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    return movimentacoes_manuais

def processar_movimentacoes(estoque, movimentacoes):
    """Processa todas as movimentações e atualiza o estoque"""
    for movimentacao in movimentacoes:
        produto, tipo, quantidade = movimentacao
        
        if tipo == "entrada":
            if produto in estoque:
                estoque[produto] += quantidade
            else:
                estoque[produto] = quantidade
            print(f"✓ Entrada: +{quantidade} {produto}")
            
        elif tipo == "saída":
            if produto in estoque:
                if estoque[produto] >= quantidade:
                    estoque[produto] -= quantidade
                    print(f"✓ Saída: -{quantidade} {produto}")
                else:
                    print(f"⚠ Atenção: Estoque insuficiente de {produto} (tem {estoque[produto]}, precisa de {quantidade})")
            else:
                print(f"⚠ Atenção: Produto {produto} não existe no estoque")

def identificar_produtos_baixo_estoque(estoque):
    """Identifica produtos com estoque igual ou inferior a 50 unidades"""
    produtos_baixo_estoque = []
    for produto, quantidade in estoque.items():
        if quantidade <= 50:
            produtos_baixo_estoque.append((produto, quantidade))
    
    return produtos_baixo_estoque

def gerar_relatorio(estoque, produtos_baixo_estoque):
    """Gera o relatório formatado do estoque"""
    print("\n" + "="*60)
    print("RELATÓRIO FINAL DO ESTOQUE")
    
    print("\nESTOQUE ATUALIZADO:")
    print("-" * 40)
    for produto, quantidade in sorted(estoque.items()):
        status = "⚠ " if quantidade <= 50 else "✅"
        print(f"{status} {produto.capitalize():<15} | {quantidade:>4} unidades")
    
    print("\nPRODUTOS QUE PRECISAM DE REPOSIÇÃO:")
    print("-" * 55)
    if produtos_baixo_estoque:
        for produto, quantidade in sorted(produtos_baixo_estoque):
            print(f"{produto.capitalize():<15} | {quantidade:>4} unidades")
    else:
        print("Nenhum produto precisa de reposição no momento!")
    
    print("\n" + "="*60)

def main():
    """Função principal que executa todo o processo"""
    print("\nSISTEMA DE CONTROLE DE ESTOQUE")
    
    mostrar_estoque(estoque_atual)
    
    print("\nMOVIMENTAÇÕES DO DIA")
    processar_movimentacoes(estoque_atual, movimentacoes_dia)
    
    mostrar_estoque(estoque_atual)
    
    movimentacoes_usuario = adicionar_movimentacao_manual()
    
    if movimentacoes_usuario:
        print("\nSUAS MOVIMENTAÇÕES")
        print("-" * 40)
        processar_movimentacoes(estoque_atual, movimentacoes_usuario)
    
    produtos_reposicao = identificar_produtos_baixo_estoque(estoque_atual)
    
    gerar_relatorio(estoque_atual, produtos_reposicao)
    
    print("\nDICA: Experimente fazer uma grande saída de um produto")
    print("   para vê-lo aparecer na lista de reposição!")

if __name__ == "__main__":
    main()