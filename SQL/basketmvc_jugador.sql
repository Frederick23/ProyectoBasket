-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-06-2019 a las 17:04:48
-- Versión del servidor: 10.1.36-MariaDB
-- Versión de PHP: 7.2.11

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
  `TL` int(11) NOT NULL,
  `TL_P` int(11) NOT NULL,
  `p_p` double NOT NULL,
  `partidos` int(11) NOT NULL,
  `pts` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `basketmvc_jugador`
--

INSERT INTO `basketmvc_jugador` (`id`, `nombre`, `apellido1`, `apellido2`, `fecha_nac`, `dorsal`, `equipo_id`, `AS`, `AS_p`, `DES`, `F`, `FTO`, `I_TC2`, `I_TC3`, `I_TL`, `PER`, `REBD`, `REBO`, `REBT`, `REB_p`, `REC`, `REC_p`, `TAP`, `TAP_p`, `TC2`, `TC2_P`, `TC3`, `TC3_P`, `TC_P`, `TL`, `TL_P`, `p_p`, `partidos`, `pts`) VALUES
(5, 'Marta', 'Tesoro', '', '0000-00-00', '0', 2, 0, 0, 1, 1, 1, 3, 1, 2, 1, 7, 1, 8, 8, 0, 0, 0, 0, 1, 33, 0, 0, 25, 1, 50, 3, 1, 3),
(6, 'Helena', 'Roldan', '', '0000-00-00', '5', 2, 0, 0, 2, 2, 0, 3, 1, 0, 3, 0, 2, 2, 2, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(7, 'Isabel', 'Benito', '', '0000-00-00', '7', 2, 1, 1, 1, 4, 3, 6, 3, 2, 4, 2, 1, 3, 3, 2, 2, 0, 0, 4, 66, 1, 33, 55, 2, 100, 13, 1, 13),
(8, 'Sara', 'Lialto', '', '0000-00-00', '8', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(9, 'Paula', 'Llamas', '', '0000-00-00', '9', 2, 0, 0, 0, 2, 0, 3, 2, 0, 1, 2, 1, 3, 3, 0, 0, 0, 0, 1, 33, 0, 0, 20, 0, 0, 2, 1, 2),
(10, 'Lorena', 'Herraiz', '', '0000-00-00', '10', 2, 0, 0, 0, 2, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(11, 'Maria', 'Merino', '', '0000-00-00', '13', 2, 0, 0, 1, 1, 2, 4, 4, 0, 1, 3, 2, 5, 5, 2, 2, 0, 0, 1, 25, 1, 25, 25, 0, 0, 5, 1, 5),
(12, 'Paula', 'Calderon', '', '0000-00-00', '14', 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 100, 0, 0, 0, 0, 0, 2, 1, 2),
(13, 'Aida', 'Muñoz', '', '0000-00-00', '15', 2, 1, 1, 1, 2, 0, 3, 4, 0, 2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(14, 'Maria', 'Amores', '', '0000-00-00', '18', 2, 2, 2, 0, 0, 2, 7, 3, 4, 2, 5, 3, 8, 8, 0, 0, 0, 0, 2, 28, 0, 0, 20, 2, 50, 6, 1, 6),
(15, 'Nuria', 'Gomez', '', '0000-00-00', '19', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(16, 'Regina', 'Iglesias', '', '0000-00-00', '32', 2, 0, 0, 0, 4, 4, 4, 0, 0, 2, 2, 1, 3, 3, 1, 1, 0, 0, 1, 25, 0, 0, 0, 0, 0, 2, 1, 2),
(17, 'Sin Asignar', '', '', '0000-00-00', '', 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 3, 1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(18, 'Paula', 'Prada', '', '0000-00-00', '5', 1, 8, 4, 2, 5, 2, 3, 3, 1, 2, 0, 0, 0, 0, 3, 1.5, 1, 0.5, 2, 66, 1, 33, 50, 0, 0, 3.5, 2, 7),
(19, 'Carmen', 'Benito', '', '0000-00-00', '6', 1, 3, 1.5, 2, 2, 9, 13, 1, 11, 4, 15, 4, 19, 9.5, 2, 1, 1, 0.5, 10, 76, 0, 0, 71, 8, 72, 14, 2, 28),
(20, 'Ana', 'Sesma', '', '0000-00-00', '7', 1, 6, 3, 1, 2, 0, 3, 4, 0, 1, 3, 0, 3, 1.5, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0),
(21, 'Silvia', 'Mesa', '', '0000-00-00', '10', 1, 3, 1.5, 2, 2, 4, 5, 10, 4, 4, 3, 0, 3, 1.5, 2, 1, 0, 0, 1, 20, 0, 0, 6, 4, 100, 3, 2, 6),
(22, 'Maria', 'Conejero', '', '0000-00-00', '15', 1, 4, 2, 1, 3, 5, 20, 9, 2, 4, 6, 4, 10, 5, 5, 2.5, 0, 0, 8, 40, 2, 22, 34, 2, 100, 12, 2, 24),
(23, 'Noelia', 'Olmeda', '', '0000-00-00', '16', 1, 0, 0, 0, 3, 4, 4, 9, 4, 3, 8, 2, 10, 5, 2, 1, 0, 0, 3, 75, 4, 44, 53, 2, 50, 10, 2, 20),
(24, 'Natalia', 'Gonzalez', '', '0000-00-00', '17', 1, 1, 0.5, 0, 3, 1, 16, 0, 2, 2, 9, 8, 17, 8.5, 3, 1.5, 0, 0, 8, 50, 0, 0, 0, 2, 100, 9, 2, 18),
(25, 'Teresa', 'Gracia', '', '0000-00-00', '19', 1, 2, 1, 0, 1, 3, 2, 11, 2, 1, 4, 1, 5, 2.5, 1, 0.5, 0, 0, 1, 50, 1, 9, 15, 2, 100, 3.5, 2, 7),
(26, 'Amparo', 'Lazaro', '', '0000-00-00', '33', 1, 3, 1.5, 2, 4, 11, 15, 0, 12, 2, 8, 8, 16, 8, 4, 2, 2, 1, 7, 46, 0, 0, 0, 0, 0, 7, 2, 14),
(27, 'Mª Carmen', 'Lopez', '', '0000-00-00', '40', 1, 5, 2.5, 1, 5, 1, 3, 2, 2, 2, 4, 0, 4, 2, 2, 1, 3, 1.5, 3, 100, 1, 50, 80, 0, 0, 4.5, 2, 9),
(28, 'Sin Asignar', '', '', '0000-00-00', '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 2, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0),
(29, 'Ingrid', 'M.Llamas', '', '0000-00-00', '4', 3, 0, 0, 0, 1, 1, 1, 0, 2, 0, 6, 2, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 50, 1, 1, 1),
(30, 'Kristina', 'Goncharuk', '', '0000-00-00', '5', 3, 0, 0, 0, 0, 1, 3, 5, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 20, 12, 0, 0, 3, 1, 3),
(31, 'Claudia', 'Gomez', '', '0000-00-00', '8', 3, 4, 4, 0, 3, 7, 10, 2, 5, 7, 5, 0, 5, 5, 2, 2, 0, 0, 5, 50, 0, 0, 41, 3, 60, 13, 1, 13),
(32, 'Itziar', 'Ugarte', '', '0000-00-00', '11', 3, 1, 1, 1, 4, 0, 1, 9, 0, 1, 2, 1, 3, 3, 0, 0, 0, 0, 0, 0, 2, 22, 20, 0, 0, 6, 1, 6),
(33, 'Beatriz', 'Vaillant', '', '0000-00-00', '12', 3, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(34, 'Elena', 'Muriel', '', '0000-00-00', '13', 3, 2, 2, 0, 2, 2, 6, 6, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 3, 50, 3, 50, 50, 0, 0, 15, 1, 15),
(35, 'Laura', 'Garcia', '', '0000-00-00', '14', 3, 0, 0, 1, 0, 1, 2, 0, 2, 1, 1, 1, 2, 2, 0, 0, 0, 0, 1, 50, 0, 0, 0, 1, 50, 3, 1, 3),
(36, 'Cristina', 'Amengual', '', '0000-00-00', '15', 3, 0, 0, 0, 3, 1, 1, 0, 0, 2, 1, 0, 1, 1, 0, 0, 0, 0, 1, 100, 0, 0, 0, 0, 0, 2, 1, 2),
(37, 'Alba', 'Segovia', '', '0000-00-00', '20', 3, 0, 0, 0, 3, 0, 2, 0, 0, 4, 3, 2, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(38, 'Diana', 'Maeso', '', '0000-00-00', '25', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
(39, 'Arantxa', 'Valledor', '', '0000-00-00', '55', 3, 2, 2, 0, 1, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 100, 2, 1, 2),
(40, 'Aminata', 'Brahima', '', '0000-00-00', '62', 3, 0, 0, 1, 4, 4, 9, 0, 2, 2, 11, 8, 19, 19, 4, 4, 1, 1, 6, 66, 0, 0, 0, 0, 0, 12, 1, 12),
(41, 'Sin Asignar', '', '', '0000-00-00', '', 3, 0, 0, 0, 0, 0, 1, 1, 0, 4, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

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
