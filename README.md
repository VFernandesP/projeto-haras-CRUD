# 🐎 Haras do Vale - CRUD de Cavalos

**Trabalho prático da disciplina Programação Back-End**  
Centro Universitário de Itajubá (FEPI)  
Curso: Sistemas de Informação  
Professor: Adriano  

---

## 👥 Integrantes
- Vinicius Fernandes

---

## 📖 Descrição do Tema

Sistema de gerenciamento para um haras, permitindo o cadastro, consulta, atualização e exclusão de cavalos.  
O sistema armazena informações como nome, raça, cor, sexo, data de nascimento, valor, status (ativo/inativo), observações, número de registro e foto.

---

## 🗂️ Campos do Model `Cavalo`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | CharField | Nome do cavalo |
| `raca` | CharField | Raça do cavalo |
| `cor` | CharField | Cor da pelagem |
| `sexo` | CharField (choices) | Sexo (M/F) |
| `data_nascimento` | DateField | Data de nascimento |
| `valor` | DecimalField | Valor de mercado (R$) |
| `ativo` | BooleanField | Indica se o cavalo está ativo no haras |
| `registro` | CharField (unique) | Número de registro único |
| `foto` | ImageField | Foto do cavalo (opcional) |

---

## 🚀 Instruções de Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/VFernandesP/projeto-haras-CRUD.git
   cd projeto-haras-CRUD