-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Nov-2024 às 22:45
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
-- Banco de dados: `biblioteca_bd`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `livro`
--

CREATE TABLE `livro` (
  `LivroID` int(11) NOT NULL,
  `TituloLivro` varchar(50) DEFAULT NULL,
  `Preco` decimal(6,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `livro`
--

INSERT INTO `livro` (`LivroID`, `TituloLivro`, `Preco`) VALUES
(201, 'O Senhor do Anéis', '50.00'),
(202, 'Harry Potter', '40.00'),
(203, 'O Hobbit', '30.00'),
(204, 'Dracula', '75.00'),
(205, 'Morte no Nilo', '80.00'),
(206, 'Assassinato no Expresso Oriente', '85.00');

-- --------------------------------------------------------

--
-- Estrutura da tabela `telefone`
--

CREATE TABLE `telefone` (
  `TelefoneID` int(11) NOT NULL,
  `ClienteNome` varchar(50) DEFAULT NULL,
  `CLienteTelefone` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `telefone`
--

INSERT INTO `telefone` (`TelefoneID`, `ClienteNome`, `CLienteTelefone`) VALUES
(1, 'Ana', '(11) 9999-9999'),
(2, 'João', '(21) 8888-8888'),
(3, 'Carine', '(31) 7777-7777'),
(4, 'Júlia', '(74) 6666-6666'),
(5, 'Leonardo', '(32) 5555-5555'),
(6, 'Oswald', '(69) 4444-4444');

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendas`
--

CREATE TABLE `vendas` (
  `PedidoID` int(11) NOT NULL,
  `VendasID` int(11) DEFAULT NULL,
  `ClienteID` int(11) DEFAULT NULL,
  `telefoneID` int(11) DEFAULT NULL,
  `LivroID` int(11) DEFAULT NULL,
  `Quantidade` int(11) DEFAULT NULL,
  `Total` decimal(6,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `vendas`
--

INSERT INTO `vendas` (`PedidoID`, `VendasID`, `ClienteID`, `telefoneID`, `LivroID`, `Quantidade`, `Total`) VALUES
(1, 1, 1, 1, 201, 2, '100.00'),
(2, 2, 2, 4, 204, 3, '225.00'),
(3, 3, 6, 6, 206, 2, '170.00'),
(4, 4, 3, 3, 205, 1, '80.00');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `livro`
--
ALTER TABLE `livro`
  ADD PRIMARY KEY (`LivroID`);

--
-- Índices para tabela `telefone`
--
ALTER TABLE `telefone`
  ADD PRIMARY KEY (`TelefoneID`);

--
-- Índices para tabela `vendas`
--
ALTER TABLE `vendas`
  ADD PRIMARY KEY (`PedidoID`),
  ADD KEY `telefoneID` (`telefoneID`),
  ADD KEY `LivroID` (`LivroID`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `vendas`
--
ALTER TABLE `vendas`
  ADD CONSTRAINT `vendas_ibfk_1` FOREIGN KEY (`telefoneID`) REFERENCES `telefone` (`TelefoneID`),
  ADD CONSTRAINT `vendas_ibfk_2` FOREIGN KEY (`LivroID`) REFERENCES `livro` (`LivroID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
