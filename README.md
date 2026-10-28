# Geração de Gráficos de Dispersão (OptClscTh)

Este script em Python é responsável por gerar gráficos de dispersão. O objetivo é explorar a relação de trade-off entre a variação do tempo de execução (ΔET) e a perda de qualidade (ΔPSNR) para diferentes valores do fator `OptClscTh`.

## Sobre o Projeto

O script lê um arquivo `.csv` contendo os resultados dos experimentos e gera gráficos de dispersão (scatter plots) para cada combinação de Configuração (RA, LD) e QP (22, 27, 32, 37). No total, espera-se a geração de 8 gráficos distintos.

## Estrutura dos Dados

O arquivo `.csv` de entrada deve conter 5 colunas principais (conforme especificação):
1.  **Config**: Configuração de codificação (RA, LD).
2.  **QP**: Parâmetro de Quantização (22, 27, 32, 37).
3.  **OptClscTh**: Fator de otimização (valores de 0 a 1, com passo de 0.05).
4.  **ΔET[%]**: Variação do tempo de execução em porcentagem.
5.  **ΔPSNR [db]**: Perda de qualidade (PSNR) em decibéis.

## Funcionalidades

*   **Pré-processamento de Dados**: O script converte automaticamente a coluna `ΔET[%]` de texto (removendo o caractere `%`) para valores numéricos (float), permitindo a plotagem correta.
*   **Iteração Automática**: O código identifica todas as configurações e QPs únicos presentes no CSV e itera sobre eles para gerar os gráficos.
*   **Formatação dos Eixos**: Os eixos X e Y são padronizados com limites e marcações (ticks) pré-definidos para manter a consistência visual entre os gráficos do artigo.
*   **Exportação em Lote**: Todos os gráficos gerados são salvos sequencialmente em um único arquivo PDF.

## Requisitos

Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install pandas matplotlib
