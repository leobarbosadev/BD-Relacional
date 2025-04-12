-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Nov-2024 às 22:51
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
-- Banco de dados: `mercado`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

CREATE TABLE `produtos` (
  `id_produto` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `unidade` char(3) NOT NULL,
  `quantidade` int(11) NOT NULL,
  `marca` varchar(20) DEFAULT NULL,
  `preco` decimal(7,2) NOT NULL,
  `estoque` int(11) NOT NULL,
  `validade` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`id_produto`, `nome`, `unidade`, `quantidade`, `marca`, `preco`, `estoque`, `validade`) VALUES
(1, 'Arroz', 'pct', 1, 'Sepé', '4.79', 100, '2022-10-15'),
(2, 'Feijão', 'pct', 1, 'Fartura', '6.49', 70, '2022-10-06'),
(3, 'Açúcar', 'pct', 1, 'União', '3.46', 120, '2022-11-12'),
(4, 'Fubá', 'pct', 1, 'Yoky', '3.19', 40, '2023-10-10'),
(5, 'Arroz', 'pct', 1, 'Prato Fino', '6.99', 100, '2022-07-12'),
(6, 'Farinha de Trigo', 'pct', 1, 'Dona Benta', '3.89', 70, '2022-10-04'),
(7, 'Café', 'pct', 1, 'Toko', '9.98', 60, '2023-07-10'),
(8, 'Macarrão', 'pct', 1, 'Santa Amália', '3.78', 200, '2022-05-05'),
(9, 'Café', 'pct', 1, 'Melita', '8.30', 120, '2023-05-23'),
(10, 'Feijão', 'pct', 1, 'Canil', '7.25', 150, '2022-06-23'),
(11, 'Leite em pó', 'pct', 1, 'Ninho', '13.66', 80, '2023-08-20');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`id_produto`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `id_produto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
