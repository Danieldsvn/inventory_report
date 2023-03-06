from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, companies):
        simple_report = super().generate(companies)
        products_company = CompleteReport.products_per_company(companies)

        complete_report = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_company}"
        )

        return complete_report

    def products_per_company(companies):
        nome_das_empresas = []
        qty_produtos = []
        report_line = ""
        for company in companies:
            nome_das_empresas.append(company["nome_da_empresa"])

        dict_aux = dict.fromkeys(nome_das_empresas)
        nome_das_empresas_no_rep = list(dict_aux)

        for company in nome_das_empresas_no_rep:
            company_frequency = nome_das_empresas.count(company)
            company_frequency_element = (company, company_frequency)
            qty_produtos.append(company_frequency_element)

        for qty in qty_produtos:
            report_line += f"- {qty[0]}: {qty[1]}\n"

        return report_line
