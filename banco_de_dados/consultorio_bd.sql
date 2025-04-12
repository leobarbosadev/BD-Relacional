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
-- Banco de dados: `consultorio_bd`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `consulta`
--

CREATE TABLE `consulta` (
  `id` int(11) NOT NULL,
  `data_consulta` date DEFAULT NULL,
  `horario` time DEFAULT NULL,
  `id_medico` int(11) DEFAULT NULL,
  `id_paciente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `consulta`
--

INSERT INTO `consulta` (`id`, `data_consulta`, `horario`, `id_medico`, `id_paciente`) VALUES
(1, '2019-10-10', '15:00:00', 1, 1),
(2, '2020-05-01', '16:00:00', 3, 3),
(3, '2021-03-05', '17:00:00', 3, 6),
(4, '2018-01-07', '11:00:00', 1, 3),
(5, '2021-11-23', '09:00:00', 2, 2),
(6, '2019-12-11', '18:00:00', 5, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `medico`
--

CREATE TABLE `medico` (
  `id` int(11) NOT NULL,
  `nome_medico` varchar(50) NOT NULL,
  `especialidade` varchar(50) DEFAULT NULL,
  `crm` char(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `medico`
--

INSERT INTO `medico` (`id`, `nome_medico`, `especialidade`, `crm`) VALUES
(1, 'Dr João Batista', 'Cardiologista', '45123'),
(2, 'Dr Marcos Rosa', 'Gastro', '34570'),
(3, 'Dr Fernando Silva', 'Pneumologista', '46787'),
(4, 'Dra Sara Ferreira', 'Psiquiatra', '21558'),
(5, 'Dra Juliana Souza', 'Neuroradiologista', '50006'),
(6, 'Dr Drauzio Varella', 'Clínico Geral', '17630'),
(7, 'Dra Beatriz Gomes', 'Ginecologista', '29440');

-- --------------------------------------------------------

--
-- Estrutura da tabela `paciente`
--

CREATE TABLE `paciente` (
  `id` int(11) NOT NULL,
  `nome_paciente` varchar(50) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  `tipo_sanguineo` varchar(3) DEFAULT NULL,
  `peso` decimal(5,2) DEFAULT NULL,
  `altura` decimal(3,2) DEFAULT NULL,
  `nacionalidade` varchar(20) DEFAULT 'Brasil'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `paciente`
--

INSERT INTO `paciente` (`id`, `nome_paciente`, `data_nascimento`, `tipo_sanguineo`, `peso`, `altura`, `nacionalidade`) VALUES
(1, 'Monica Bellucci', '1964-09-30', 'O+', '65.50', '1.71', 'Itália'),
(2, 'Amy Adams', '1974-08-20', 'A+', '60.50', '1.63', 'Inglaterra'),
(3, 'Anne Hathaway', '1982-11-12', 'A+', '55.00', '1.73', 'EUA'),
(4, 'Paolla Oliveira', '1982-04-14', 'A-', '57.00', '1.70', 'Brasil'),
(5, 'Dandara Mariana', '1988-05-13', 'B', '50.00', '1.57', 'Brasil'),
(6, 'Erika Januza', '1985-05-07', 'B', '54.00', '1.66', 'Brasil'),
(7, 'Carla Perez', '1977-07-16', 'O-', '58.00', '1.66', 'Brasil');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_medico` (`id_medico`),
  ADD KEY `id_paciente` (`id_paciente`);

--
-- Índices para tabela `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome_medico` (`nome_medico`);

--
-- Índices para tabela `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome_paciente` (`nome_paciente`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `consulta`
--
ALTER TABLE `consulta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `medico`
--
ALTER TABLE `medico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id`),
  ADD CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
