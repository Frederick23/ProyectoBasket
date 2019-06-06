-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-06-2019 a las 13:46:23
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pruebabasket`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basketmvc_jugador`
--

CREATE TABLE `basketmvc_jugador` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido1` varchar(30) NOT NULL,
  `apellido2` varchar(30) NOT NULL,
  `fecha_nac` date NOT NULL,
  `dorsal` varchar(3) NOT NULL,
  `equipo_id` int(11) NOT NULL,
  `AS` int(11) NOT NULL,
  `AS_p` double NOT NULL,
  `DES` int(11) NOT NULL,
  `F` int(11) NOT NULL,
  `FTO` int(11) NOT NULL,
  `I_TC2` int(11) NOT NULL,
  `I_TC3` int(11) NOT NULL,
  `I_TL` int(11) NOT NULL,
  `PER` int(11) NOT NULL,
  `REBD` int(11) NOT NULL,
  `REBO` int(11) NOT NULL,
  `REBT` int(11) NOT NULL,
  `REB_p` double NOT NULL,
  `REC` int(11) NOT NULL,
  `REC_p` double NOT NULL,
  `TAP` int(11) NOT NULL,
  `TAP_p` double NOT NULL,
  `TC2` int(11) NOT NULL,
  `TC2_P` int(11) NOT NULL,
  `TC3` int(11) NOT NULL,
  `TC3_P` int(11) NOT NULL,
  `TC_P` int(11) NOT NULL,
  `TIEMPO` time(6) NOT NULL,
  `TL` int(11) NOT NULL,
  `TL_P` int(11) NOT NULL,
  `p_p` double NOT NULL,
  `partidos` int(11) NOT NULL,
  `pts` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `basketmvc_jugador`
--

INSERT INTO `basketmvc_jugador` (`id`, `nombre`, `apellido1`, `apellido2`, `fecha_nac`, `dorsal`, `equipo_id`, `AS`, `AS_p`, `DES`, `F`, `FTO`, `I_TC2`, `I_TC3`, `I_TL`, `PER`, `REBD`, `REBO`, `REBT`, `REB_p`, `REC`, `REC_p`, `TAP`, `TAP_p`, `TC2`, `TC2_P`, `TC3`, `TC3_P`, `TC_P`, `TIEMPO`, `TL`, `TL_P`, `p_p`, `partidos`, `pts`) VALUES
(5, 'Marta', 'Tesoro', '', '0000-00-00', '0', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(6, 'Helena', 'Roldan', '', '0000-00-00', '5', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(7, 'Isabel', 'Benito', '', '0000-00-00', '7', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(8, 'Sara', 'Lialto', '', '0000-00-00', '8', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(9, 'Paula', 'Llamas', '', '0000-00-00', '9', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(10, 'Lorena', 'Herraiz', '', '0000-00-00', '10', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(11, 'Maria', 'Merino', '', '0000-00-00', '13', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(12, 'Paula', 'Calderon', '', '0000-00-00', '14', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(13, 'Aida', 'Muñoz', '', '0000-00-00', '15', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(14, 'Maria', 'Amores', '', '0000-00-00', '18', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(15, 'Nuria', 'Gomez', '', '0000-00-00', '19', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(16, 'Regina', 'Iglesias', '', '0000-00-00', '32', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(17, 'Sin Asignar', '', '', '0000-00-00', '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(18, 'Paula', 'Prada', '', '0000-00-00', '5', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(19, 'Carmen', 'Benito', '', '0000-00-00', '6', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(20, 'Ana', 'Sesma', '', '0000-00-00', '7', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(21, 'Silvia', 'Mesa', '', '0000-00-00', '10', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(22, 'Maria', 'Conejero', '', '0000-00-00', '15', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(23, 'Noelia', 'Olmeda', '', '0000-00-00', '16', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(24, 'Natalia', 'Gonzalez', '', '0000-00-00', '17', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(25, 'Teresa', 'Gracia', '', '0000-00-00', '19', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(26, 'Amparo', 'Lazaro', '', '0000-00-00', '33', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(27, 'Mª Carmen', 'Lopez', '', '0000-00-00', '40', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0),
(28, 'Sin Asignar', '', '', '0000-00-00', '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00:00:00.000000', 0, 0, 0, 0, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `basketmvc_jugador`
--
ALTER TABLE `basketmvc_jugador`
  ADD PRIMARY KEY (`id`),
  ADD KEY `BasketMVC_jugador_equipo_id_4694b6b5_fk_BasketMVC_equipo_id` (`equipo_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `basketmvc_jugador`
--
ALTER TABLE `basketmvc_jugador`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `basketmvc_jugador`
--
ALTER TABLE `basketmvc_jugador`
  ADD CONSTRAINT `BasketMVC_jugador_equipo_id_4694b6b5_fk_BasketMVC_equipo_id` FOREIGN KEY (`equipo_id`) REFERENCES `basketmvc_equipo` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
