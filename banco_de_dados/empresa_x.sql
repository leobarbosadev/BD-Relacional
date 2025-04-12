-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Nov-2024 às 22:46
-- Versão do servidor: 10.4.24-MariaDB
-- versão do PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `empresa_x`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionarios`
--

CREATE TABLE `funcionarios` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `data_nascimento` date NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `salario` decimal(10,2) NOT NULL,
  `data_contratacao` date NOT NULL,
  `departamento` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `funcionarios`
--

INSERT INTO `funcionarios` (`id`, `nome`, `data_nascimento`, `cargo`, `salario`, `data_contratacao`, `departamento`) VALUES
(1, 'João Silva', '1985-03-15', 'Gerente de Projetos', '7500.00', '2015-05-10', 'TI'),
(2, 'Maria Souza', '1990-07-22', 'Analista Financeiro', '5200.00', '2017-08-14', 'Financeiro'),
(3, 'Carlos Lima', '1978-11-10', 'Diretor de Vendas', '12000.00', '2010-02-05', 'Vendas'),
(4, 'Ana Costa', '1988-09-30', 'Coordenadora de Marketing', '6800.00', '2018-03-01', 'Marketing'),
(5, 'Pedro Almeida', '1995-01-12', 'Desenvolvedor de Software', '4800.00', '2019-06-20', 'TI'),
(6, 'Fernanda Ramos', '1983-12-05', 'Gerente de RH', '7200.00', '2024-09-25', 'Recursos Humanos'),
(7, 'Lucas Ferreira', '1992-04-18', 'Consultor de Vendas', '4500.00', '2021-01-10', 'Vendas'),
(8, 'Paula Mello', '1987-08-23', 'Analista de Marketing', '5100.00', '2020-11-15', 'Marketing'),
(9, 'Ricardo Oliveira', '1980-02-08', 'Gerente Financeiro', '9800.00', '2012-12-03', 'Financeiro'),
(10, 'Juliana Farias', '1993-02-08', 'Analista de RH', '4300.00', '2022-07-18', 'Recursos Humanos');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `funcionarios`
--
ALTER TABLE `funcionarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `funcionarios`
--
ALTER TABLE `funcionarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
