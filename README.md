Um sistema Python para gerenciamento de estoque desenvolvido para a Armazém Central, uma distribuidora de produtos de papelaria.

🚀 Funcionalidades
Gestão de Estoque: Controle de entradas e saídas de produtos

Processamento Automático: Processa movimentações diárias automaticamente

Alertas Inteligentes: Identifica produtos com estoque baixo (≤ 50 unidades)

Interface Interativa: Permite adicionar movimentações manualmente

Relatórios Detalhados: Gera relatórios formatados do estoque atualizado

📋 Requisitos
Python 3.6 ou superior

Nenhuma biblioteca externa necessária

🛠️ Como Usar
1. Clone ou baixe o arquivo
bash
git clone <url-do-repositorio>
cd controle-estoque-python
2. Execute o programa
bash
python estoque.py
3. Siga as instruções interativas
O programa irá:

Mostrar o estoque inicial

Processar movimentações automáticas

Permitir que você adicione suas próprias movimentações

Gerar um relatório final completo

🎯 Exemplos de Uso
Movimentações que você pode testar:
Entrada de novo produto:

text
Produto: folhas
Tipo: entrada
Quantidade: 100
Saída de produto existente:

text
Produto: canetas  
Tipo: saída
Quantidade: 100
Teste de estoque insuficiente:

text
Produto: tesoura
Tipo: saída
Quantidade: 50
📊 Estrutura dos Dados
Estoque Inicial
python
estoque_atual = {
    "canetas": 150,
    "cadernos": 95,
    "lápis": 200,
    "borrachas": 30,      # ⚠️ Precisa de reposição
    "régua": 45,          # ⚠️ Precisa de reposição
    "cola": 60,
    "tesoura": 25,        # ⚠️ Precisa de reposição
    "marcador": 75,
    "clips": 120,
    "grampos": 40         # ⚠️ Precisa de reposição
}
Movimentações
Cada movimentação é uma tupla com:

python
("nome_do_produto", "tipo_movimentacao", quantidade)
📝 Regras de Negócio
✅ Entradas: Aumentam o estoque do produto

✅ Saídas: Diminuem o estoque do produto

✅ Produtos Novos: São criados automaticamente na primeira entrada

✅ Estoque Insuficiente: O sistema previne saídas maiores que o estoque disponível

✅ Alerta de Reposição: Produtos com ≤ 50 unidades são sinalizados

🎨 Saída do Programa
O programa gera um relatório formatado com:

text
📦 ESTOQUE ATUALIZADO:
----------------------------------------
✅ Canetas         |  125 unidades
⚠️ Borrachas       |   30 unidades
⚠️ Grampos         |   25 unidades

🔴 PRODUTOS QUE PRECISAM DE REPOSIÇÃO:
---------------------------------------
Borrachas       |   30 unidades
Grampos         |   25 unidades
🔧 Personalização
Modificar Estoque Inicial
Edite o dicionário estoque_atual no código:

python
estoque_atual = {
    "seu_produto": quantidade,
    # ... outros produtos
}
Modificar Movimentações Automáticas
Edite a lista movimentacoes_dia:

python
movimentacoes_dia = [
    ("produto", "entrada/saída", quantidade),
    # ... outras movimentações
]
Alterar Limite de Reposição
Modifique o valor na função identificar_produtos_baixo_estoque:

python
if quantidade <= 50:  # Altere este número
🧪 Testes Sugeridos
Teste de Entrada: Adicione um produto novo

Teste de Saída: Remova quantidades de produtos existentes

Teste de Limite: Force produtos para abaixo de 50 unidades

Teste de Erro: Tente remover mais do que tem no estoque

📞 Suporte
Em caso de dúvidas ou problemas:

Verifique se está usando Python 3.6+

Confirme a sintaxe das movimentações

Certifique-se de digitar números válidos para quantidades

📄 Licença
Este projeto foi desenvolvido como parte de um desafio Python para fins educacionais.

