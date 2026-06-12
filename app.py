import streamlit as st

# ==========================
# STRATEGY DE PAGAMENTO
# ==========================

class PagamentoStrategy:
    def processar(self):
        pass


class PagamentoPix(PagamentoStrategy):
    def processar(self):
        return "Pagamento realizado via Pix."


class PagamentoCartao(PagamentoStrategy):
    def processar(self):
        return "Pagamento realizado via Cartão de Crédito."


class PagamentoBoleto(PagamentoStrategy):
    def processar(self):
        return "Boleto gerado com sucesso."


class ProcessadorPagamento:

    def __init__(self, estrategia):
        self.estrategia = estrategia

    def processar_pagamento(self):
        return self.estrategia.processar()

st.set_page_config(
    page_title="ReVeste",
    page_icon="👕",
    layout="wide"

)

st.markdown("""
<style>

/* Fundo da barra lateral */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f4fff6 0%, #e8f5ec 100%);
}

/* Título da navegação */
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3 {
    color: #1f6f3a;
}

/* Texto geral da sidebar */
[data-testid="stSidebar"] * {
    font-family: Arial, sans-serif;
}

/* Itens do radio */
[data-testid="stSidebar"] label {
    background-color: #ffffff;
    border-radius: 14px;
    padding: 10px 12px;
    margin-bottom: 8px;
    border: 1px solid #d8eadf;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
}

/* Item selecionado */{
    background-color: #dff3e5;
    border-left: 5px solid #1f7a3f;
    font-weight: bold;
}

/* Linha divisória */
hr {
    border: none;
    border-top: 1px solid #cde5d3;
}

/* Botões */
.stButton > button {
    border-radius: 10px;
    border: 1px solid #1f7a3f;
    color: #1f7a3f;
    background-color: #ffffff;
}

.stButton > button:hover {
    background-color: #e8f5ec;
    color: #155c2f;
    border-color: #155c2f;
}

</style>
""", unsafe_allow_html=True)

if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = ""

if "usuarios" not in st.session_state:
    st.session_state.usuarios = []

if "produtos" not in st.session_state:
    st.session_state.produtos = []


if "pedidos" not in st.session_state:
    st.session_state.pedidos = []

if "avaliacoes" not in st.session_state:
    st.session_state.avaliacoes = []

st.sidebar.markdown("""
# 👕 ReVeste
**Moda consciente, consumo sustentável**
---
### 🧭 Navegação
""")

pagina = st.sidebar.radio(
    "Escolha uma opção:",

    

    [
        "🔐 Login",
        "🏠 Início",
        "👤 Usuários",
        "👕 Produtos",
        "🔍 Catálogo",
        "🛒 Compras",
        "📦 Pedidos",
        "⭐ Avaliações",
        "🌱 Sustentabilidade",
        "👩‍💼 Painel da Lúcia"
    ]
)

st.sidebar.divider()

if st.session_state.logado:
    st.sidebar.success(f"Logado como: {st.session_state.usuario_logado}")

    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario_logado = ""
        st.rerun()
else:
    st.sidebar.warning("Usuário não logado")


if pagina == "🔐 Login":

    st.title("🔐 Login")

    email_login = st.text_input("E-mail")
    senha_login = st.text_input("Senha", type="password")

    st.info(
    "Não possui cadastro? Vá até a aba 👤 Usuários e crie sua conta."
)

    if st.button("Entrar"):
     st.markdown("""
### Novo por aqui?

👉 Caso ainda não tenha uma conta, acesse a aba **👤 Usuários**
e realize seu cadastro antes de fazer login.
""")

     if email_login and senha_login:

        usuario_encontrado = False

        for usuario in st.session_state.usuarios:
            if usuario["email"] == email_login:
                usuario_encontrado = True

        if usuario_encontrado:
            st.session_state.logado = True
            st.session_state.usuario_logado = email_login

            st.success("Login realizado com sucesso.")
            st.rerun()
        else:
            st.error("E-mail não cadastrado. Cadastre o usuário antes de fazer login.")

    else:
        st.error("Preencha e-mail e senha.")

elif pagina == "🏠 Início":

    st.title("👕 ReVeste")
    st.subheader("Moda consciente, consumo sustentável")

    st.write("""
    Bem-vindo ao ReVeste! Aqui você encontra roupas e itens usados,
    pode pesquisar produtos, acompanhar categorias e simular compras de forma simples.
    """)

    st.divider()

    busca_inicio = st.text_input("🔎 Pesquisar produto no brechó")

    categorias = ["Roupas", "Calçados", "Acessórios", "Outros"]

    st.subheader("Categorias disponíveis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("👕 Roupas")

    with col2:
        st.info("👟 Calçados")

    with col3:
        st.info("👜 Acessórios")

    with col4:
        st.info("📦 Outros")

    st.divider()

    st.subheader("🛍️ Produtos em destaque")

    if len(st.session_state.produtos) == 0:
        st.warning("Nenhum produto cadastrado ainda. Cadastre produtos na aba 👕 Produtos.")
    else:
        encontrados = 0

        for produto in st.session_state.produtos:

            if busca_inicio.lower() in produto["produto"].lower():
                encontrados += 1

                with st.container():
                    col_img, col_info = st.columns([1, 3])

                    with col_img:
                        if produto["imagem"] is not None:
                            st.image(produto["imagem"], width=160)
                        else:
                            st.write("📷 Sem imagem")

                    with col_info:
                        st.markdown(f"### {produto['produto']}")
                        st.write(f"📂 Categoria: {produto['categoria']}")
                        st.write(f"📦 Estado: {produto['estado']}")
                        st.write(f"💰 Preço: R$ {produto['preco']:.2f}")
                        st.write(produto["descricao"])

                    st.divider()

        if encontrados == 0:
            st.warning("Nenhum produto encontrado na pesquisa.")

    st.subheader("🛒 Carrinho")

    if len(st.session_state.pedidos) == 0:
        st.info("Seu carrinho ainda está vazio. Vá até a aba 🛒 Compras para realizar uma compra.")
    else:
        st.success(f"Você possui {len(st.session_state.pedidos)} pedido(s) registrado(s).")

elif pagina == "👤 Usuários":
    st.title("👤 Cadastro de Usuários")

    nome = st.text_input("Nome do usuário")
    email = st.text_input("E-mail")
    tipo = st.selectbox("Tipo de usuário", ["Comprador", "Vendedor"])

    if st.button("Cadastrar usuário"):
        if nome and email:
            novo_usuario = {
                "nome": nome,
                "email": email,
                "tipo": tipo
            }

            st.session_state.usuarios.append(novo_usuario)

            st.success(f"Usuário {nome} cadastrado como {tipo}.")
        else:
            st.error("Preencha nome e e-mail.")

    st.divider()

    st.subheader("Usuários cadastrados")

    if len(st.session_state.usuarios) == 0:
        st.info("Nenhum usuário cadastrado ainda.")
    else:
        for usuario in st.session_state.usuarios:
            st.write(f"**Nome:** {usuario['nome']}")
            st.write(f"**E-mail:** {usuario['email']}")
            st.write(f"**Tipo:** {usuario['tipo']}")
            st.write("---")

elif pagina == "👕 Produtos":

    st.title("👕 Cadastro de Produtos")

    produto = st.text_input("Nome do produto")

    descricao = st.text_area("Descrição")

    imagem = st.file_uploader(
    "Imagem do produto",
    type=["png", "jpg", "jpeg"]
)

    categoria = st.selectbox(
        "Categoria",
        ["Roupas", "Calçados", "Acessórios", "Outros"]
    )

    estado = st.selectbox(
        "Estado de conservação",
        ["Novo", "Seminovo", "Usado"]
    )

    preco = st.number_input(
        "Preço",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("Cadastrar produto"):

        novo_produto = {
            "produto": produto,
            "descricao": descricao,
            "categoria": categoria,
            "estado": estado,
            "preco": preco,
            "imagem": imagem
}

        st.session_state.produtos.append(novo_produto)

        st.success(f"Produto '{produto}' cadastrado com sucesso.")

    st.divider()

    st.subheader("Produtos cadastrados")

    if len(st.session_state.produtos) == 0:

        st.info("Nenhum produto cadastrado.")

    else:
        
        for indice, p in enumerate(st.session_state.produtos):

            if p["imagem"] is not None:
                st.image(
                    p["imagem"],
                    width=200
                )

            st.write(f"**Produto:** {p['produto']}")
            st.write(f"**Categoria:** {p['categoria']}")
            st.write(f"**Estado:** {p['estado']}")
            st.write(f"**Preço:** R$ {p['preco']:.2f}")

            if st.button(
                f"❌ Excluir {p['produto']}",
                key=f"excluir_{indice}"
            ):
                st.session_state.produtos.pop(indice)
                st.rerun()

            st.divider()


elif pagina == "🔍 Catálogo":

    st.title("🔍 Catálogo de Produtos")

    busca = st.text_input("Buscar produto pelo nome")

    filtro_categoria = st.selectbox(
        "Filtrar por categoria",
        ["Todos", "Roupas", "Calçados", "Acessórios", "Outros"]
    )

    st.divider()

    if len(st.session_state.produtos) == 0:
        st.info("Nenhum produto cadastrado no catálogo.")
    else:
        produtos_encontrados = 0

        for produto in st.session_state.produtos:

            nome_combina = busca.lower() in produto["produto"].lower()

            categoria_combina = (
                filtro_categoria == "Todos" or 
                produto["categoria"] == filtro_categoria
            )

            if nome_combina and categoria_combina:
                produtos_encontrados += 1

                with st.container():

                 if produto["imagem"] is not None:
                    st.image(produto["imagem"], width=250)

                    st.markdown(f"### 👕 {produto['produto']}")

                    st.write(f"📂 Categoria: {produto['categoria']}")
                    st.write(f"📦 Estado: {produto['estado']}")
                    st.write(f"💰 Preço: R$ {produto['preco']:.2f}")

                    st.write(produto["descricao"])

                    st.divider()

                if produtos_encontrados == 0:
                    st.warning("Nenhum produto encontrado com esses filtros.")

elif pagina == "🛒 Compras":

    st.title("🛒 Realizar Compra")

    if len(st.session_state.produtos) == 0:
        st.info("Nenhum produto disponível para compra.")
    else:
        nomes_produtos = [produto["produto"] for produto in st.session_state.produtos]

        produto_escolhido = st.selectbox(
            "Escolha um produto",
            nomes_produtos
        )

        forma_pagamento = st.selectbox(
            "Forma de pagamento",
            ["Pix", "Cartão de Crédito", "Boleto"]
        )

        endereco = st.text_input("Endereço de entrega")

        if st.button("Confirmar compra"):
            if endereco:
                produto_detalhes = None

                for produto in st.session_state.produtos:
                    if produto["produto"] == produto_escolhido:
                        produto_detalhes = produto

                novo_pedido = {
                    "produto": produto_detalhes["produto"],
                    "categoria": produto_detalhes["categoria"],
                    "preco": produto_detalhes["preco"],
                    "pagamento": forma_pagamento,
                    "endereco": endereco,
                    "status": "Aguardando envio"
                }

                st.session_state.pedidos.append(novo_pedido)

                if forma_pagamento == "Pix":
                    estrategia = PagamentoPix()
                elif forma_pagamento == "Cartão de Crédito":
                    estrategia = PagamentoCartao()
                else:
                    estrategia = PagamentoBoleto()

                processador = ProcessadorPagamento(estrategia)
                mensagem_pagamento = processador.processar_pagamento()

                st.success(f"Compra do produto '{produto_escolhido}' realizada.")
                st.info(mensagem_pagamento)

            else:
                st.error("Informe o endereço de entrega.")

elif pagina == "📦 Pedidos":

    st.title("📦 Pedidos")

    if len(st.session_state.pedidos) == 0:

        st.info("Nenhum pedido realizado.")

    else:

        for pedido in st.session_state.pedidos:

            st.subheader(pedido["produto"])

            st.write(f"**Categoria:** {pedido['categoria']}")
            st.write(f"**Preço:** R$ {pedido['preco']:.2f}")
            st.write(f"**Pagamento:** {pedido['pagamento']}")
            st.write(f"**Endereço:** {pedido['endereco']}")
            st.write(f"**Status:** {pedido['status']}")

            st.divider()

elif pagina == "⭐ Avaliações":

    st.title("⭐ Avaliações")

    vendedor = st.text_input("Nome do vendedor")

    nota = st.slider("Nota", 1, 5)

    comentario = st.text_area("Comentário")

    if st.button("Enviar avaliação"):

        if vendedor and comentario:

            nova_avaliacao = {
                "vendedor": vendedor,
                "nota": nota,
                "comentario": comentario
            }

            st.session_state.avaliacoes.append(nova_avaliacao)

            st.success("Avaliação enviada com sucesso.")

    st.divider()

    st.subheader("Avaliações registradas")

    for avaliacao in st.session_state.avaliacoes:

        st.write(f"**Vendedor:** {avaliacao['vendedor']}")
        st.write(f"**Nota:** {avaliacao['nota']} ⭐")
        st.write(f"**Comentário:** {avaliacao['comentario']}")

        st.divider()

elif pagina == "🌱 Sustentabilidade":

    st.title("🌱 Impacto Sustentável")

    total_produtos = len(st.session_state.produtos)
    total_pedidos = len(st.session_state.pedidos)

    st.write("""
    O ReVeste incentiva o consumo consciente ao promover a reutilização de roupas
    e itens usados. Cada produto comprado representa uma peça que ganhou uma nova
    oportunidade de uso, contribuindo para a redução do descarte e para a economia circular.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Produtos cadastrados", total_produtos)

    with col2:
        st.metric("Itens reutilizados", total_pedidos)

    with col3:
        st.metric("Consumo consciente", "Ativo")

    st.divider()

    st.subheader("♻️ Mensagem de impacto")

    if total_pedidos == 0:
        st.info("Ainda não há itens reutilizados. Realize uma compra para gerar impacto sustentável.")
    else:
        st.success(
            f"{total_pedidos} item(ns) ganharam uma nova chance de uso por meio do ReVeste."
        )

    st.write("""
    Além de facilitar a compra e venda de produtos usados, o sistema ajuda a valorizar
    práticas sustentáveis, reduzindo o desperdício e incentivando escolhas de consumo
    mais responsáveis.
    """)

elif pagina == "👩‍💼 Painel da Lúcia":

    st.title("👩‍💼 Painel Administrativo da Lúcia")

    total_usuarios = len(st.session_state.usuarios)
    total_produtos = len(st.session_state.produtos)
    total_pedidos = len(st.session_state.pedidos)
    total_avaliacoes = len(st.session_state.avaliacoes)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Usuários cadastrados", total_usuarios)
        st.metric("Produtos cadastrados", total_produtos)

    with col2:
        st.metric("Pedidos realizados", total_pedidos)
        st.metric("Avaliações recebidas", total_avaliacoes)

    st.divider()

    st.subheader("📊 Resumo do Sistema")

    st.write(f"👤 Usuários: {total_usuarios}")
    st.write(f"👕 Produtos: {total_produtos}")
    st.write(f"📦 Pedidos: {total_pedidos}")
    st.write(f"⭐ Avaliações: {total_avaliacoes}")

    st.divider()

    st.subheader("🌱 Impacto Sustentável")

    if total_pedidos == 0:
        st.info("Nenhum item reutilizado até o momento.")
    else:
        st.success(
            f"{total_pedidos} item(ns) foram reutilizados através do ReVeste."
        )