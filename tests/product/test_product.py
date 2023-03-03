from inventory_report.inventory.product import Product


# Iniciando projeto
def test_cria_produto():
    product = Product(
        "1",
        "Torradeira",
        "Arno",
        "03/03/2023",
        "03/06/2023",
        121314,
        "instruções",
    )

    assert product.id == "1"
    assert product.nome_do_produto == "Torradeira"
    assert product.nome_da_empresa == "Arno"
    assert product.data_de_fabricacao == "03/03/2023"
    assert product.data_de_validade == "03/06/2023"
    assert product.numero_de_serie == 121314
    assert product.instrucoes_de_armazenamento == "instruções"
