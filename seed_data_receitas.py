# ARQUIVO PARA CADASTRAR CATEGORIAS E RECEITAS E INSERIR DADOS FICTÍCIOS NAS RECEITAS
from django.core.files import File
import os
import django

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE para o arquivo settings do seu projeto Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# Inicialize o Django.
django.setup()

from PIL import Image
def enviar_imagem(caminho_imagem):
    with open(caminho_imagem, 'rb') as img_file:
        imagem = File(img_file)        
from receitas.models import Receita, Categoria


def seed_data_receitas():
    # Limpando todas as receitas existentes
    Receita.objects.all().delete()

    # Categoria 'Grelhados'
    grelhados = Categoria.objects.get_or_create(nome='Grelhados')[0]

    Receita.objects.create(
        categoria=grelhados,
        imagem='receitas/frango-grelhado.jpg',
        titulo="Frango Grelhado",
        subtitulo="Uma receita simples de frango grelhado, perfeita para um almoço saudável.",
        ingredientes="Ingredientes:\n- 4 peitos de frango\n- Sal e pimenta a gosto\n- 2 colheres de azeite\n- 1 dente de alho picado\n- Suco de 1 limão",
        modo_preparo="Modo de Preparo:\n1. Tempere os peitos de frango com sal, pimenta, alho e suco de limão.\n2. Aqueça o azeite em uma frigideira e grelhe o frango até dourar dos dois lados.\n3. Sirva quente e aproveite!"
    )

    Receita.objects.create(
        categoria=grelhados,
        imagem='receitas/salmão-grelhado.jpg',
        titulo="Salmão Grelhado",
        subtitulo="Uma deliciosa receita de salmão grelhado com um toque de limão e ervas.",
        ingredientes="Ingredientes:\n- 4 filés de salmão\n- Sal e pimenta a gosto\n- Suco de 1 limão\n- Ervas frescas a gosto (tomilho, alecrim, etc.)\n- Azeite de oliva",
        modo_preparo="Modo de Preparo:\n1. Tempere os filés de salmão com sal, pimenta, suco de limão e ervas frescas.\n2. Aqueça o azeite em uma frigideira e grelhe o salmão até que esteja cozido e com a pele crocante.\n3. Sirva com mais limão e ervas por cima."

    )

    Receita.objects.create(
        categoria=grelhados,
        imagem='receitas/carne-grelhada.jpg',
        titulo="Carne Grelhada",
        subtitulo="Uma suculenta carne grelhada, perfeita para churrascos e encontros com amigos.",
        ingredientes="Ingredientes:\n- 1 peça de carne (picanha, contrafilé, etc.)\n- Sal e pimenta a gosto\n- Chimichurri a gosto\n- Carvão e grelha",
        modo_preparo="Modo de Preparo:\n1. Tempere a carne com sal, pimenta e chimichurri.\n2. Acenda o carvão e prepare a grelha.\n3. Grelhe a carne até atingir o ponto desejado.\n4. Descanse a carne por alguns minutos antes de cortar e servir."
    )

    Receita.objects.create(
        categoria=grelhados,
        imagem='receitas/espetinho-de-frango.jpg',
        titulo="Espetinho de Frango",
        subtitulo="Um espetinho saboroso de frango com legumes, perfeito para grelhar em churrascos.",
        ingredientes="Ingredientes:\n- Peitos de frango em cubos\n- Pimentões coloridos em pedaços\n- Cebola em pedaços\n- Sal, pimenta e azeite\n- Palitos de churrasco",
        modo_preparo="Modo de Preparo:\n1. Monte os espetinhos alternando pedaços de frango, pimentão e cebola.\n2. Tempere com sal, pimenta e azeite.\n3. Grelhe os espetinhos até que o frango esteja cozido e os legumes estejam dourados.\n4. Sirva quente."

    )

    # Categoria 'Aperitivos'
    aperitivos = Categoria.objects.get_or_create(nome='Aperitivos')[0]

    Receita.objects.create(
        categoria=aperitivos,
        imagem='receitas/aperitivo-camarao.jpg',
        titulo="Aperitivo de Camarão",
        subtitulo="Um delicioso aperitivo de camarão, perfeito para servir em festas e eventos.",
        ingredientes="Ingredientes:\n- 500g de camarões\n- 4 dentes de alho picados\n- Suco de 1 limão\n- Sal e pimenta a gosto\n- Salsinha picada\n- Azeite de oliva",
        modo_preparo="Modo de Preparo:\n1. Tempere os camarões com alho, suco de limão, sal e pimenta.\n2. Aqueça o azeite em uma frigideira e grelhe os camarões até que fiquem rosados e cozidos.\n3. Polvilhe com salsinha picada e sirva quente."
    )

    Receita.objects.create(
        categoria=aperitivos,
        imagem='receitas/pasteis.jpg',
        titulo="Pastéis Crocantes",
        subtitulo="Deliciosos pastéis crocantes recheados com queijo e ervas frescas.",
        ingredientes="Ingredientes:\n- Massa para pastel\n- Queijo muçarela\n- Ervas frescas (manjericão, salsinha, etc.)\n- Óleo para fritura",
        modo_preparo="Modo de Preparo:\n1. Abra a massa para pastel e coloque uma fatia de queijo e algumas ervas frescas.\n2. Dobre a massa e feche bem as bordas.\n3. Frite os pastéis em óleo quente até dourarem.\n4. Escorra em papel toalha e sirva quente."
    )

    Receita.objects.create(
        categoria=aperitivos,
        imagem='receitas/tapas.jpg',
        titulo="Tapas Espanholas",
        subtitulo="Um mix de tapas espanholas, incluindo patatas bravas, jamón serrano e croquetas.",
        ingredientes="Ingredientes:\n- Batatas\n- Presunto serrano\n- Croquetas\n- Molho de tomate picante\n- Azeite de oliva",
        modo_preparo="Modo de Preparo:\n1. Prepare as patatas bravas com molho de tomate picante.\n2. Sirva fatias de presunto serrano.\n3. Aqueça as croquetas no forno e sirva com azeite de oliva."
    )

    Receita.objects.create(
        categoria=aperitivos,
        imagem='receitas/camarao-panado.jpg',
        titulo="Camarão Panado",
        subtitulo="Camarões panados e crocantes, ideais para mergulhar em molho de pimenta.",
        ingredientes="Ingredientes:\n- Camarões\n- Farinha de rosca\n- Ovos batidos\n- Sal e pimenta a gosto\n- Molho de pimenta",
        modo_preparo="Modo de Preparo:\n1. Passe os camarões em farinha de rosca, depois nos ovos batidos e novamente na farinha de rosca.\n2. Frite os camarões em óleo quente até que fiquem dourados.\n3. Sirva com molho de pimenta a gosto."
    )

    # Categoria 'Sopas'
    sopas = Categoria.objects.get_or_create(nome='Sopas')[0]

    Receita.objects.create(
        categoria=sopas,
        imagem='receitas/sopa-de-tomate.jpg',
        titulo="Sopa de Tomate",
        subtitulo="Uma sopa de tomate deliciosa, perfeita para os dias mais frios.",
        ingredientes="Ingredientes:\n- 1kg de tomates maduros\n- 1 cebola picada\n- 2 dentes de alho picados\n- Manjericão fresco\n- Caldo de legumes\n- Creme de leite\n- Sal e pimenta a gosto",
        modo_preparo="Modo de Preparo:\n1. Refogue a cebola e o alho em azeite até ficarem macios.\n2. Adicione os tomates e manjericão, cozinhando até que os tomates se desmanchem.\n3. Adicione o caldo de legumes, sal e pimenta a gosto.\n4. Use um liquidificador para fazer a sopa ficar cremosa.\n5. Sirva com um fio de creme de leite e mais manjericão."
    )

    Receita.objects.create(
        categoria=sopas,
        imagem='receitas/sopa-de-legumes.jpg',
        titulo="Sopa de Legumes",
        subtitulo="Uma sopa saudável e reconfortante, repleta de legumes frescos.",
        ingredientes="Ingredientes:\n- Abobrinha\n- Cenoura\n- Batata\n- Ervilhas\n- Caldo de legumes\n- Cebola picada\n- Alho picado\n- Azeite de oliva",
        modo_preparo="Modo de Preparo:\n1. Refogue a cebola e o alho em azeite até ficarem macios.\n2. Adicione os legumes picados e refogue por alguns minutos.\n3. Adicione o caldo de legumes e cozinhe até que os legumes estejam macios.\n4. Use um liquidificador para fazer a sopa ficar cremosa.\n5. Sirva quente."
    )

    Receita.objects.create(
        categoria=sopas,
        imagem='receitas/sopa-de-feijao.jpg',
        titulo="Sopa de Feijão",
        subtitulo="Uma sopa de feijão deliciosa, perfeita para os dias mais frios.",
        ingredientes="Ingredientes:\n- Feijão cozido\n- Bacon\n- Cebola\n- Alho\n- Caldo de galinha\n- Sal e pimenta a gosto",
        modo_preparo="Modo de Preparo:\n1. Em uma panela, refogue o bacon, a cebola e o alho até dourarem.\n2. Adicione o feijão cozido e o caldo de galinha.\n3. Cozinhe até que a sopa esteja bem quente e os sabores se misturem.\n4. Tempere com sal e pimenta a gosto."
    )

    Receita.objects.create(
        categoria=sopas,
        imagem='receitas/caldo-de-peixe.jpg',
        titulo="Caldo de Peixe",
        subtitulo="Um caldo de peixe rico em sabor, ideal como base para pratos de frutos do mar.",
        ingredientes="Ingredientes:\n- Peixes brancos (linguado, pargo, etc.)\n- Cebola\n- Alho\n- Tomate\n- Vinho branco\n- Ervas frescas (tomilho, louro, etc.)\n- Caldo de peixe\n- Sal e pimenta a gosto",
        modo_preparo="Modo de Preparo:\n1. Refogue cebola, alho e tomate em azeite até dourarem.\n2. Adicione o vinho branco e deixe reduzir.\n3. Adicione os peixes, ervas frescas e caldo de peixe.\n4. Cozinhe até que o peixe esteja desmanchando.\n5. Coe o caldo e utilize como base para outros pratos de frutos do mar."
    )

    # Categoria 'Sobremesas'
    sobremesas = Categoria.objects.get_or_create(nome='Sobremesas')[0]
    
    Receita.objects.create(
        categoria=sobremesas,
        imagem='receitas/pizza.jpg',
        titulo="Pizza de Chocolate",
        subtitulo="Uma deliciosa pizza de chocolate com cobertura de morango e creme.",
        ingredientes="Ingredientes:\n- Massa para pizza\n- Chocolate ao leite picado\n- Morangos frescos\n- Creme de chocolate\n- Açúcar de confeiteiro (para polvilhar)",
        modo_preparo="Modo de Preparo:\n1. Abra a massa de pizza em um formato redondo.\n2. Espalhe o chocolate ao leite picado sobre a massa.\n3. Asse no forno até que o chocolate derreta e a massa fique dourada.\n4. Retire do forno e cubra com morangos frescos e creme de chocolate.\n5. Polvilhe com açúcar de confeiteiro e sirva quente."
    )

    Receita.objects.create(
        categoria=sobremesas,
        imagem='receitas/brigadeiro.jpg',
        titulo="Brigadeiro",
        subtitulo="Um clássico doce brasileiro, perfeito para qualquer ocasião.",
        ingredientes="Ingredientes:\n- 2 latas de leite condensado\n- 4 colheres de sopa de chocolate em pó\n- 2 colheres de sopa de manteiga\n- Chocolate granulado (para decorar)",
        modo_preparo="Modo de Preparo:\n1. Em uma panela, misture o leite condensado, o chocolate em pó e a manteiga.\n2. Leve ao fogo baixo, mexendo continuamente, até a mistura desgrudar do fundo da panela.\n3. Retire do fogo e deixe esfriar um pouco.\n4. Com as mãos untadas, faça pequenas bolas com a mistura.\n5. Passe as bolas no chocolate granulado para decorar.\n6. Deixe esfriar completamente e sirva."
    )

    Receita.objects.create(
        categoria=sobremesas,
        imagem='receitas/torta-de-morango.jpg',
        titulo="Torta de Morango",
        subtitulo="Uma deliciosa torta de morango com creme e geleia.",
        ingredientes="Ingredientes:\n- Massa para torta\n- Morangos frescos\n- Creme de confeiteiro\n- Geleia de morango\n- Açúcar de confeiteiro (para polvilhar)",
        modo_preparo="Modo de Preparo:\n1. Prepare a massa da torta e asse até dourar.\n2. Cubra a massa com uma camada de creme de confeiteiro.\n3. Disponha os morangos sobre o creme.\n4. Aqueça a geleia de morango e pincele sobre os morangos.\n5. Polvilhe com açúcar de confeiteiro e sirva frio."
    )

    Receita.objects.create(
        categoria=sobremesas,
        imagem='receitas/pudim.jpg',
        titulo="Pudim de Leite",
        subtitulo="Um pudim de leite cremoso e irresistível.",
        ingredientes="Ingredientes:\n- Leite condensado\n- Leite\n- Ovos\n- Açúcar (para a calda)",
        modo_preparo="Modo de Preparo:\n1. Prepare a calda de açúcar e despeje no fundo de uma forma.\n2. Bata o leite condensado, leite e ovos no liquidificador.\n3. Despeje a mistura sobre a calda na forma.\n4. Asse em banho-maria até o pudim firmar.\n5. Deixe esfriar e leve à geladeira antes de desenformar."
    )

    Receita.objects.create(
        categoria=sobremesas,
        imagem='receitas/bolo-chocolate.jpg',
        titulo="Bolo de Chocolate",
        subtitulo="Um bolo de chocolate incrivelmente fofinho e saboroso.",
        ingredientes="Ingredientes:\n- Farinha de trigo\n- Cacau em pó\n- Açúcar\n- Ovos\n- Leite\n- Fermento em pó\n- Chocolate em barra",
        modo_preparo="Modo de Preparo:\n1. Misture os ingredientes secos (farinha, cacau, açúcar) em uma tigela.\n2. Adicione os ovos, leite e fermento, mexendo até obter uma massa homogênea.\n3. Quebre pedaços de chocolate e misture na massa.\n4. Asse o bolo até que um palito saia limpo."
    )

    Receita.objects.create(
        categoria=sobremesas,
        imagem='receitas/tiramisu.jpg',
        titulo="Tiramisu",
        subtitulo="Um clássico tiramisu, com camadas de biscoitos e creme de mascarpone.",
        ingredientes="Ingredientes:\n- Biscoitos savoiardi\n- Mascarpone\n- Café forte\n- Gemas de ovo\n- Açúcar\n- Cacau em pó",
        modo_preparo="Modo de Preparo:\n1. Mergulhe os biscoitos no café e coloque no fundo de um prato.\n2. Faça uma mistura de mascarpone, gemas e açúcar, e espalhe sobre os biscoitos.\n3. Repita as camadas e termine com uma camada de cacau em pó.\n4. Deixe na geladeira por algumas horas antes de servir."
    )

    # Categoria 'Massas'
    massas = Categoria.objects.get_or_create(nome='Massas')[0]

    Receita.objects.create(
        categoria=massas,
        imagem='receitas/espaguete-carbonara.jpg',
        titulo="Espaguete à Carbonara",
        subtitulo="Uma clássica e deliciosa receita de espaguete carbonara.",
        ingredientes="Ingredientes:\n- Espaguete\n- Ovos\n- Queijo pecorino ou parmesão ralado\n- Pancetta ou bacon\n- Pimenta preta moída",
        modo_preparo="Modo de Preparo:\n1. Cozinhe o espaguete até ficar al dente.\n2. Em uma frigideira, frite a pancetta ou bacon até ficar crocante.\n3. Misture os ovos, queijo e pimenta em uma tigela.\n4. Escorra o espaguete e misture imediatamente com a mistura de ovos e pancetta. Sirva quente."
    )

    Receita.objects.create(
        categoria=massas,
        imagem='receitas/lasanha.jpg',
        titulo="Lasanha à Bolonhesa",
        subtitulo="Uma lasanha recheada com carne moída e molho à bolonhesa.",
        ingredientes="Ingredientes:\n- Massa para lasanha\n- Carne moída\n- Molho de tomate\n- Queijo ricota\n- Queijo muçarela\n- Parmesão ralado",
        modo_preparo="Modo de Preparo:\n1. Cozinhe a carne moída e adicione o molho de tomate.\n2. Monte camadas alternadas de massa, carne, queijo ricota e muçarela.\n3. Repita as camadas até a forma estar cheia.\n4. Finalize com queijo parmesão ralado e asse até dourar."
    )

    Receita.objects.create(
        categoria=massas,
        imagem='receitas/ravioli.jpg',
        titulo="Ravioli de Queijo",
        subtitulo="Deliciosos ravioli recheados com queijo e servidos com molho de tomate.",
        ingredientes="Ingredientes:\n- Ravioli de queijo\n- Molho de tomate\n- Parmesão ralado\n- Manjericão fresco",
        modo_preparo="Modo de Preparo:\n1. Cozinhe o ravioli de acordo com as instruções da embalagem.\n2. Aqueça o molho de tomate e misture com o ravioli cozido.\n3. Sirva com parmesão ralado e folhas de manjericão."
    )

    Receita.objects.create(
        categoria=massas,
        imagem='receitas/penne-alfredo.jpg',
        titulo="Penne Alfredo",
        subtitulo="Um prato de massa penne com um cremoso molho Alfredo.",
        ingredientes="Ingredientes:\n- Penne\n- Creme de leite\n- Manteiga\n- Queijo parmesão ralado\n- Noz-moscada",
        modo_preparo="Modo de Preparo:\n1. Cozinhe o penne até ficar al dente.\n2. Em uma panela, derreta a manteiga e adicione o creme de leite.\n3. Misture o queijo parmesão ralado e noz-moscada.\n4. Misture o molho com o penne cozido e sirva."
    )

    # Categoria 'Saladas'
    saladas = Categoria.objects.get_or_create(nome='Saladas')[0]

    Receita.objects.create(
        categoria=saladas,
        imagem='receitas/salada-caprese.jpg',
        titulo="Salada Caprese",
        subtitulo="Uma salada simples e refrescante com tomates, muçarela e manjericão.",
        ingredientes="Ingredientes:\n- Tomates maduros\n- Queijo muçarela\n- Folhas de manjericão\n- Azeite de oliva\n- Vinagre balsâmico\n- Sal e pimenta a gosto",
        modo_preparo="Modo de Preparo:\n1. Corte os tomates e muçarela em rodelas.\n2. Arrume em um prato alternando com folhas de manjericão.\n3. Regue com azeite de oliva e vinagre balsâmico.\n4. Tempere com sal e pimenta a gosto."
    )

    Receita.objects.create(
        categoria=saladas,
        imagem='receitas/salada-de-frutas.jpg',
        titulo="Salada de Frutas",
        subtitulo="Uma salada de frutas colorida e refrescante.",
        ingredientes="Ingredientes:\n- Frutas variadas (morangos, kiwis, uvas, etc.)\n- Suco de laranja\n- Mel",
        modo_preparo="Modo de Preparo:\n1. Corte as frutas em pedaços.\n2. Misture as frutas com suco de laranja e um pouco de mel.\n3. Sirva frio."
    )

    Receita.objects.create(
        categoria=saladas,
        imagem='receitas/salada-grega.jpg',
        titulo="Salada Grega",
        subtitulo="Uma salada tradicional grega com pepino, tomate, azeitonas e queijo feta.",
        ingredientes="Ingredientes:\n- Pepino\n- Tomate\n- Azeitonas pretas\n- Queijo feta\n- Azeite de oliva\n- Orégano",
        modo_preparo="Modo de Preparo:\n1. Corte o pepino, tomate e queijo feta em cubos.\n2. Misture com azeitonas pretas e regue com azeite de oliva.\n3. Polvilhe com orégano e sirva."
    )

    Receita.objects.create(
        categoria=saladas,
        imagem='receitas/salada-caesar.jpg',
        titulo="Salada Caesar",
        subtitulo="Uma salada Caesar clássica com croutons e molho Caesar.",
        ingredientes="Ingredientes:\n- Alface romana\n- Croutons\n- Peito de frango grelhado (opcional)\n- Queijo parmesão ralado\n- Molho Caesar",
        modo_preparo="Modo de Preparo:\n1. Lave e rasgue as folhas de alface.\n2. Adicione croutons e, se desejar, peito de frango grelhado.\n3. Polvilhe com queijo parmesão ralado e regue com molho Caesar."
    )


seed_data_receitas()
