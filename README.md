 Agrotech Cana-de-Açúcar - Monitoramento de Perdas

Sistema Python para redução de perdas na colheita mecânica de cana-de-açúcar, que podem chegar a **15%**.  
**Tecnologias**: Python, Oracle, JSON.

##  Funcionalidades
- Registro de dados de colheita (área, toneladas colhidas, perdas)
- Cálculo automático do percentual de perdas
- Armazenamento em banco de dados Oracle
- Recomendações para otimização

##  Como Executar
1. **Pré-requisitos**:
   - Python 3.8+
   - Oracle Database (ou XE)
   - Bibliotecas: `cx_Oracle`, `matplotlib`

2. **Instalação**:
   ```bash
   git clone https://github.com/FelipeTFiore/agrotech-cana.git
   cd agrotech-cana
   pip install -r requirements.txt
   ```

3. **Configuração**:
   - Edite `database.py` com suas credenciais Oracle
   - Crie a tabela no Oracle usando o script `schema.sql`

4. **Uso**:
   ```bash
   python main.py
   ```
