from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "produto1",
        "empresa1",
        "2023-03-07",
        "2023-06-07",
        121212,
        "instrucao1",
    )

    repr_data = (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )

    assert repr(product) == repr_data
