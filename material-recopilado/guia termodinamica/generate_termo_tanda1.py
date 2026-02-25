import os

tex_code = r"""\documentclass{article}
\usepackage{fullpage}
\usepackage{graphicx}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{cancel}
\usepackage{booktabs}
\usepackage{url}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{tcolorbox}

%%%%% Comandos Personalizados %%%%%
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\la}{\leftarrow}
\newcommand{\ra}{\rightarrow}
\newcommand{\lra}{\leftrightarrow}
\newcommand{\Ra}{\Rightarrow}
\newcommand{\La}{\Leftarrow}
\newcommand{\LRa}{\Leftrightarrow}
\newcommand{\sub}{\subseteq}
\newcommand{\matro}{\mathcal{M}}
%%%%% Fin Comandos Personalizados %%%%%

\title{Guía de Victorias Rápidas -- Termodinámica\\[0.3cm]
\large Tanda 1: Fundamentos y Conceptos Básicos}
\author{}
\date{\today}

\begin{document}

\maketitle

\begin{tcolorbox}[colback=blue!5!white, colframe=blue!50!black, title=Plan de Estudio -- Tanda 1]
\textbf{Objetivo:} Asegurar los puntos ``regalados'' de Termodinámica. Aquí no hay cálculos largos, solo aplicación directa de conceptos del Handbook y entendimiento básico.\\
\textbf{Nivel:} Básico. \\
\textbf{Temas cubiertos:}
\begin{enumerate}
    \item Conversión de escalas de temperatura (Pág. 1)
    \item Primera Ley en sistemas cerrados (Pág. 147)
    \item Estados de saturación (Pág. 157)
    \item Ley Cero y equilibrio térmico (Pág. 143)
    \item Propiedades de estado vs. Propiedades de trayectoria (Pág. 143)
    \item Entropía y Segunda Ley (Pág. 151)
    \item Calor sensible (Pág. 146)
    \item Gases Ideales (Pág. 145)
\end{enumerate}
\end{tcolorbox}

\newpage

%% ============================================================
%% EJERCICIO 1
%% ============================================================

\section*{Ejercicio 1 -- Escalas de Temperatura}
\textit{Fuente: Pregunta 26 -- 2016-1}

\subsection*{Enunciado}
Determine a qué temperatura son iguales (valores numéricos) las escalas Kelvin y Farenheit.

\subsection*{Solución paso a paso}

\textbf{Paso 1: Identificar las fórmulas de conversión}

En la tabla de equivalencias del Handbook encontramos cómo llevar de Celsius a las otras escalas:
\[ T_K = T_C + 273.15 \]
\[ T_F = 1.8 T_C + 32 \]

\textbf{Paso 2: Igualar ambas expresiones}

Buscamos una temperatura $X$ tal que $T_K = T_F = X$.
Despejamos $T_C$ de la primera: $T_C = X - 273.15$

Ahora reemplazamos en la segunda:
\[ X = 1.8 (X - 273.15) + 32 \]

\textbf{Paso 3: Resolver la ecuación lineal}
\[ X = 1.8X - 491.67 + 32 \]
\[ X = 1.8X - 459.67 \]
\[ 0.8X = 459.67 \implies X \approx 574.58 \]

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{Units and Conversions (Pág. 1):} Fórmulas explícitas $T_K$ y $T_F$ en función de $T_C$.
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% EJERCICIO 2
%% ============================================================

\section*{Ejercicio 2 -- Primera Ley en Sistema Cerrado}
\textit{Fuente: Pregunta 27 -- 2016-1}

\subsection*{Enunciado}
Sistema cerrado, sin trabajo de expansión/compresión. Identifique la expresión válida para la Primera Ley.

\subsection*{Solución paso a paso}

\textbf{Paso 1: Plantear la ecuación general}

Del Handbook para un "closed system":
\[ Q - W = \Delta U + \Delta KE + \Delta PE \]

\textbf{Paso 2: Simplificar con las condiciones del problema}

Nos indican expresamente que:
\begin{itemize}
    \item $W = 0$ (sin trabajo de frontera o expansión).
    \item Por omisión, un sistema termodinámico estándar estacionario tiene $\Delta KE \approx 0$ y $\Delta PE \approx 0$ (no sube montañas ni se acelera como un coche).
\end{itemize}

\textbf{Paso 3: Llegar a la expresión reducida}
\[ Q = \Delta U \]
Todo el calor transferido se va internamente en aumentar la energía interna del sistema.

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{First Law of Thermodynamics (Pág. 147):} Formula para sistemas cerrados y el caso especial de "Constant Volume" implican $Q = \Delta U$.
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% EJERCICIO 3
%% ============================================================

\section*{Ejercicio 3 -- Estados de Saturación del Agua}
\textit{Fuente: Pregunta 28 -- 2016-1}

\subsection*{Enunciado}
Corriente de agua a $200^\circ C$ y 1 MPa. Indique en qué estado termodinámico se encuentra.

\subsection*{Solución paso a paso}

\textbf{Paso 1: Entender cómo identificar la fase}

Solo necesitamos comparar la Temperatura real de nuestra muestra ($T_{real} = 200^\circ C$) frente a la Temperatura de saturación teórica ($T_{sat}$) que corresponde a la misma presión ($P = 1 \text{ MPa} = 10 \text{ bar}$) dada en la tabla.

\textbf{Paso 2: Consultar la tabla de saturación}

Al mirar la tabla de presiones de saturación para vapor de agua:
\[ \text{Para } P = 1.0 \text{ MPa}, \quad T_{sat} \approx 179.9^\circ C \]

\textbf{Paso 3: Analizar la comparación}

Como nuestro fluido está a $200^\circ C$, significa que le hemos dado calor un poco más alto que su temperatura de ebullición ideal a 1 MPa.
\[ T_{real} > T_{sat} \]
Esto dicta que el agua fue hervida al 100\% y sigue calentándose como \textbf{Vapor sobrecalentado}.

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{Steam Tables (Pág. 157):} Las tablas de propiedades te confieren $T_{sat}$ directo según la presión (Saturated specific pressure table). Con eso comparas enseguida.
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% EJERCICIO 4
%% ============================================================

\section*{Ejercicio 4 -- Temperatura de Mezclas}
\textit{Fuente: Pregunta 33 -- 2016-2}

\subsection*{Enunciado}
¿Cuál es la temperatura de un sistema en equilibrio térmico con otro sistema compuesto por una mezcla de agua y vapor de agua a 1 atm de presión?

\subsection*{Solución paso a paso}

\textbf{Paso 1: Ley Cero de Termodinámica}

Si dos cuerpos, A y B, están en ``equilibrio térmico'', significa obligatoriamente que sus barreras no dejan fluir calor de A a B. El calor detiene su flujo netamente cuando:
\[ T_{\text{sistema}} = T_{\text{mezcla}} \]

\textbf{Paso 2: Evaluar la mezcla de agua-vapor}

Siempre que tengas \textbf{agua} coexistiendo con \textbf{vapor} en la misma cuchara (estado de saturación de dos fases), todo ese potaje está a la inamovible temperatura de saturación de su ambiente. A una presión libre de $1 \text{ atm}$, el agua saturada coexiste con su vapor de forma garantizada a $100^\circ C$.

Por lo tanto, la mezcla está a $100^\circ C$, lo que obliga al sistema externo a estar a esa misma temperatura por el equilibrio decretado.

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{Zeroth Law (Pág. 143):} El equilibrio térmico exige las mismas temperaturas.
            \item \textbf{Properties of Water (Pág. 157):} P = 1 atm corresponde al punto fundamental de saturación del agua, que todos conocemos en la práctica (Pág.1 Conversiones a $100^{\circ}C$).
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% EJERCICIO 5
%% ============================================================

\section*{Ejercicio 5 -- Propiedades de Estado vs Trayectoria}
\textit{Fuente: Pregunta 34 -- 2016-2}

\subsection*{Enunciado}
Un gas ideal puede ser llevado desde el punto 2 al punto 4 de tres maneras distintas en un diagrama P-V: directo $(2 \to 4)$, curvo $(2 \to 3 \to 4)$, o rectangular $(2 \to 1 \to 4)$. ¿Cuál de sus propiedades sufre invariablemente el mismo cambio para los tres procesos?

\subsection*{Solución paso a paso}

\textbf{Paso 1: Identificar la clasificación de las magnitudes}
En termodinámica dividimos el mundo en dos bandos:
\begin{itemize}
    \item \textbf{Propiedades de Estado:} Dependen de dónde iniciaste el viaje y en qué coordenadas terminas. (Ej: Energía interna $U$, Entropía $S$, Entalpía $H$, Volumen $V$).
    \item \textbf{Propiedades de Trayectoria:} Dependen de la curvatura del recorrido en los gráficos (área bajo la curva). (Ej: Calor $Q$, Trabajo $W$).
\end{itemize}

\textbf{Paso 2: Concluir con la trayectoria}
Como los tres procesos coinciden en dónde inicial (Estado 2) y en dónde terminan (Estado 4), la variación es la misma para todas las funciones de estado ($\Delta U$). 

Sin embargo, el trabajo realizado variará puesto que representa distintas siluetas de área sobre el volumen en tu gráfico.
Concluimos que lo único idéntico será su \textbf{cambio de energía interna} ($\Delta U$, $\Delta H$, $\Delta S$).

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{Thermodynamics (Pág. 143):} NCEES enumera con total claridad a "Properties" como Point Functions (independientes del camino).
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% EJERCICIO 6
%% ============================================================

\section*{Ejercicio 6 -- La firma de la Entropía}
\textit{Fuente: Pregunta 35 -- 2016-2}

\subsection*{Enunciado}
La propiedad de una sustancia que aumenta o disminuye cuando se le suministra o retira calor, respectivamente, de una manera \emph{reversible}, es conocida como:

\subsection*{Solución paso a paso}

\textbf{Paso 1: Recobrar la formula original de la entropía}
La figura macroscópica de la entropía, concebida por Clausius para modelar reversibilidad y transferencia, dice:
\[ dS = \frac{\delta Q_{\text{revers}}}{T} \]

\textbf{Paso 2: Corroborar el texto}
Como la temperatura Kelvin $T$ siempre es positiva:
\begin{itemize}
    \item En inyectar calor reversiblemente ($\delta Q > 0$) implica que $dS > 0$. \emph{La entropía aumenta.}
    \item En retirar calor reversiblemente ($\delta Q < 0$) implica que $dS < 0$. \emph{La entropía baja.}
\end{itemize}
Esto describe exactamente a la propiedad conocida como Entropía.

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{Second Law of Thermodynamics (Pág. 151):} Fórmulita en caja mágica: $dS \ge \delta Q / T$, estipulando la igualdad explícitamente para el \textit{proceso internamente reversible}.
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% EJERCICIO 7
%% ============================================================

\section*{Ejercicio 7 -- Calor Sensible: Más allá del cálculo}
\textit{Fuente: Pregunta 34 -- 2017-1}

\subsection*{Enunciado}
¿Cuáles de las siguientes variables físicas afectan la cantidad de energía transferida en forma de "calor sensible" desde o hacia una sustancia?

\subsection*{Solución paso a paso}

\textbf{Paso 1: Entender qué es calor sensible}
"Sensible" indica que la temperatura física sufre un aumento o decaimiento *visible*, a diferencia de un cambio "latente" (derretir/evaporar material a $T$ constante).

\textbf{Paso 2: Expresión para cálculo de aumento de calor}
\[ Q = m \cdot c \cdot \Delta T \]

\textbf{Paso 3: Identificar componentes de la fórmula}
Las tres cosas que obligadamente necesitas de acuerdo con la fórmula simple, son:
\begin{itemize}
    \item \textbf{La masa} ($m$ del objeto).
    \item \textbf{Calor específico} de la materialidad ($c$, particular de la sustancia que lo compone).
    \item \textbf{Cambio en su temperatura} ($\Delta T$ a escalar).
\end{itemize}

Si te sugieren presión en la fase líquida no afecta lo suficiente, y el tiempo tampoco importa para la termodinámica clásica sin cinemática de fluidos.

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{Heat Capacity (Pág. 146):} Aparecen explícitos los calor específicos $C_p$ o $C_v$ que multiplican al $\Delta T$ y a la unidad de materia.
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% EJERCICIO 8
%% ============================================================

\section*{Ejercicio 8 -- El termómetro Celsius y Kelvin}
\textit{Fuente: Pregunta 33 -- 2017-2}

\subsection*{Enunciado}
¿Cuál de las siguientes afirmaciones acerca de las magnitudes en escalas Celsius comparadas a las relativas Kelvin es CORRECTA?

\subsection*{Solución paso a paso}

\textbf{Paso 1: Ecuación base}
Para pasar de una a la otra sólo debes sumar el valor de ajuste métrico.
\[ T_K = T_C + 273.15 \]

\textbf{Paso 2: Diferencias de los deltas}
La pendiente de esta función es $+1$. Esto significa que un incremento unitario del termómetro en Celsius siempre se replicará equivalentemente en los peldaños dictados por Lord Kelvin.
\[ \Delta T_K = \Delta T_C \]

\textbf{Paso 3: Concluir}
Por lo tanto, la magnitud del "espaciamiento de cada grado es idéntica", ambas regletas tienen el mismo calibrado diferencial, la única salvedad es que Kelvin desplazó el $0^{\circ}C$ hasta su mismísimo cero absoluto teórico.

\noindent\fbox{%
    \parbox{\textwidth}{%
        \textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:
        \begin{itemize}
            \item \textbf{Units (Pág. 1):} $T_K = T_C + 273.15^{\circ}$. Fíjese que no tiene escalar multiplicativo (o es 1) a diferencia de la conversión Farenheit donde se nota que es $1.8x$ veces distinto.
        \end{itemize}
    }%
}

\vspace{1cm}

%% ============================================================
%% RESUMEN FINAL
%% ============================================================

\section*{Resumen de Conceptos Clave}

\begin{tcolorbox}[colback=green!5!white, colframe=green!50!black, title=Lo que deberías dominar después de esta tanda]

\textbf{Conceptos Fundamentales:}
\begin{enumerate}
    \item \textbf{Equilibrio Térmico:} Igualdad estricta de las temperaturas entre dos objetos (Ley Cero).
    \item \textbf{Propiedades Termodinámicas:} Entropía ($S$), Entalpía ($H$), y Energía Interna ($U$) resuelven solo sobre un "Punto Mágico", mientras el Trabajo y Calor se deforman según la trayectoria matemática que sigas.
    \item \textbf{Primera Ley básica:} $Q - W = \Delta U$. Si dicen sistema cerrado sin trabajo, queda solo el puro calor ($Q = \Delta U$).
    \item \textbf{Reversibilidad (S):} Una subida termal de entropía reversible satisface matemáticamente que su variación en la misma ecuación de su estado puro arrojará lo que le subas al calor.
\end{enumerate}

\textbf{Formulitas clave (súper fáciles):}
\begin{enumerate}
    \setcounter{enumi}{4}
    \item \textbf{Saturación:} T $real$ \textbf{>} T $sat\_tabla$ $\rightarrow$ Vapor sobrecalentado entero.
    \item \textbf{Escala Kelvin:} Desfasada idéntico en escala (Mismo $\Delta$) perdiendo 273.
    \item \textbf{Calor sensible:} Depende de su masa, diferencial de temperatura y especificidad del residuo material.
\end{enumerate}

\end{tcolorbox}

\vfill
\begin{center}
    \small Puedes ver este repositorio en \url{https://github.com/anomvlito/respositorio-fundamentals}
\end{center}

\end{document}
"""

os.makedirs('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/preguntas faciles', exist_ok=True)
with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/preguntas faciles/guia_termodinamica_facil_tanda1.tex', 'w', encoding='utf-8') as f:
    f.write(tex_code)
