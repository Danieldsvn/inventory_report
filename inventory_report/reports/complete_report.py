from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, companies):
        # print("companies ->", companies)
        simple_report = super().generate(companies)
        products_company = CompleteReport.products_per_company(companies)

        complete_report = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_company}")
        print(complete_report)
        return complete_report

    def products_per_company(companies):
        # print("'products_pr_company' foi chamada")
        nome_das_empresas = []
        qty_produtos = set()
        string = ""
        for company in companies:
            nome_das_empresas.append(company["nome_da_empresa"])
        # print("nome_das_empresas ->", nome_das_empresas)
        # Precisa alterar a ordem do nomes das empresas em "qty_produtos"
        for company in nome_das_empresas:
            company_frequency = nome_das_empresas.count(company)
            company_frequency_element = (company, company_frequency)
            qty_produtos.add(company_frequency_element)
        # print("qty_produtos", qty_produtos)
        for qty in qty_produtos:
            # print(string)
            string += f"- {qty[0]}: {qty[1]}\n"
        # print("string", string)
        return string
