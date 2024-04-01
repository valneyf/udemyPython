'''
Maria pegou um empréstimo de 1.000.000
    para realizar o pagamento em 5 anos.
A data em que ela pegou o empréstimo foi
    20/12/2020 e o vencimento de cada parcela
    é no dia 20 de cada mês.
- Crie a data do empréstimo
- Crie a data final do empréstimo
- Mostre todas as datas de venimento 
    e o valor de cada parcela
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta

total_loan = 1_000_000 # o _ pode ser usado para validar visualmente as casas decimais sem influenciar no valor

initial_date = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)
final_date = initial_date + delta_years

date_payments = []
payment_day = initial_date

while payment_day < final_date:
    date_payments.append(payment_day)
    payment_day += relativedelta(months=+1)

payments_number = len(date_payments)
payment_value = total_loan / payments_number

for dt_payment in date_payments:
    print(dt_payment.strftime('%d/%m/%Y'), f'R$ {payment_value:,.2f}')

print(
    f'\nVocê obteve R${total_loan:,.2f} para pagar '
    f'em {delta_years.years} anos '
    f'({payments_number} meses) em parcelas de '
    f'R${payment_value:,.2f}.'
    )