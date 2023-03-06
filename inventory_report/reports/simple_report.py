from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(companies):
        # print("companies -> ", companies)
        older_product = SimpleReport.older_fabrication(companies)
        expiration_product = SimpleReport.earlier_expiration_date(companies)
        companies_frequency = SimpleReport.most_frequent_company(companies)
        # print("companies_frequency", companies_frequency)
        return (
            f"Data de fabricação mais antiga: {older_product}\n"
            f"Data de validade mais próxima: {expiration_product}\n"
            f"Empresa com mais produtos: {companies_frequency}"
        )

    @staticmethod
    def most_frequent_company(companies):
        counter = 0
        enterprise = companies[0]["nome_da_empresa"]
        nome_das_empresas = []
        for company in companies:
            nome_das_empresas.append(company["nome_da_empresa"])
        for company in nome_das_empresas:
            current_frequency = nome_das_empresas.count(company)
            if current_frequency > counter:
                counter = current_frequency
                enterprise = company
        return enterprise

    @staticmethod
    def older_fabrication(companies):
        date_str = companies[0]["data_de_fabricacao"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        for company in companies:
            date_company_str = company["data_de_fabricacao"]
            date_company_obj = datetime.strptime(date_company_str, "%Y-%m-%d")
            if date_obj > date_company_obj:
                date_obj = date_company_obj
        date_result_str = date_obj.strftime("%Y-%m-%d")
        return date_result_str

    @staticmethod
    def earlier_expiration_date(companies):
        now = datetime.now()
        dates = []
        for company in companies:
            date_company_str = company["data_de_validade"]
            date_company_obj = datetime.strptime(date_company_str, "%Y-%m-%d")
            if date_company_obj > now:
                dates.append(date_company_obj)
        if dates:
            date_result_obj = min(dates)
            date_result_str = date_result_obj.strftime("%Y-%m-%d")
            return date_result_str

        return "Produtos vencidos"
