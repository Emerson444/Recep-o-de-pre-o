# Monitor de Planilha de Produtos com Atualização Automática no MySQL

<p>Este sistema monitora automaticamente alterações em uma planilha Excel (Produtos_Planilha1_.xlsx) e atualiza os dados da tabela preco em um banco de dados MySQL. Ideal para automações em ambientes de controle de estoque, preços ou catálogos de produtos.</p>

<b>
  Monitora modificações no arquivo Produtos_Planilha1_.xlsx.
Ao detectar alterações, atualiza os dados no banco de dados MySQL.
Substitui completamente a tabela preco com os novos dados.
Loga as atividades e possíveis erros no terminal.
</b>

🛠️ Tecnologias Utilizadas:
Python 3
pandas
SQLAlchemy
watchdo
MySQL
