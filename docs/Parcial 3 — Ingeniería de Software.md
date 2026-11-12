Parcial 3 — Ingenieria de Software I

Estudiante: Jhon Faber Mindiola Atencio
Codigo estudiantil: 0182410099





#### **Parte 1 — Requisitos y criterios de aceptación**



###### **1.1 Parametros personalizados**



|A|B|C|D|E|F|PMAX|L1|L2|RR|RN|V|S|CAMBIO|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|4|1|0|0|9|9|50 kg|3 kg|10 kg|15 %|40 %|15 %|$2.000|1|



###### **1.2 Especificacion del calculo del costo**



**R1**. El peso debe cumplir 0 < peso ≤ 50 kg. Si no, se lanza el error “peso invalido”.

**R2**. La zona debe ser urbana, rural o nacional. El dia debe estar entre 1 y 7. Si la zona o el dia no son validos, se lanza un error.

**R3**. Tarifa base:



* Tramo 1: como D = 0 es par, incluye el limite. Para peso ≤ 3 kg, la tarifa es $6.000.
* Tramo 2: para peso > 3 kg y peso ≤ 10 kg, la tarifa es $9.000.
* Para peso > 10 kg, la tarifa es $9.000 mas $800 por cada kilogramo por encima de 10 kg.



**R4**. Recargo por zona:



* Urbana: sin recargo.
* Rural: recargo del 15 %.
* Nacional: recargo del 40 %.



**R5**. Fin de semana: el sabado, dia 6, y el domingo, dia 7, se agrega un recargo de $2.000. Como E = 9 es impar, este recargo se aplica despues de los descuentos.

**R6**. Descuentos:



* Cliente frecuente: 5 %.
* Cliente VIP: 15 %.
* Cupon ENVIO10: 10 %.
* Como B = 1 es impar, si se combinan el descuento del cliente y el cupon, se aplican ambos en secuencia: primero el descuento del cliente y luego el cupon.



**R7**. Como F = 9 es impar, un cupon desconocido produce un error. El cupon es opcional.

**R8**. El costo final no puede ser menor que $5.000. El resultado se redondea al multiplo de $100 mas cercano. Si queda exactamente a mitad entre dos centenas, los $50 se redondean hacia arriba.





###### **1.3 Historias de usuario y criterios de aceptación**



**Historia de usuario 1: calcular la tarifa de un envió**



Como cliente de EnviaYa, quiero conocer el costo de mi envio segun su peso y destino, para saber cuanto debo pagar.

Criterios de aceptacion:



* Dado un peso mayor que 0 y menor o igual que 50 kg, cua		ndo se calcula el envio, entonces el sistema debe determinar la tarifa base usando los tramos definidos en R3.
* Dado un envio con zona urbana, rural o nacional, cuando se calcula el envio, entonces el sistema debe aplicar el recargo correspondiente definido en R4.
* Dado un peso igual o menor que 0, o mayor que 50 kg, cuando se calcula el envio, entonces el sistema debe lanzar el error “peso invalido”.



**Historia de usuario 2: aplicar descuentos y recargo de fin de semana**



Como cliente de EnviaYa, quiero que el sistema aplique correctamente mi descuento, mi cupon y el recargo de fin de semana, para recibir un total calculado con las reglas del negocio.

Criterios de aceptacion:



* Dado un cliente frecuente, cuando se calcula su envio, entonces se debe aplicar un descuento del 5 %.
* Dado un cliente VIP, cuando se calcula su envio, entonces se debe aplicar un descuento del 15 %.
* Dado un cupon ENVIO10 valido, cuando se calcula el envio, entonces se debe aplicar un descuento del 10 %.
* Dado un descuento de cliente y un cupon valido, cuando ambos estan presentes, entonces se deben aplicar ambos descuentos en secuencia: primero el descuento de cliente y luego el cupon.
* Dado un envio programado para sabado o domingo, cuando se calcula el costo, entonces se debe agregar un recargo de $2.000 despues de los descuentos.
* Dado un cupon desconocido, cuando se calcula el envio, entonces el sistema debe lanzar un error.



**Historia de usuario 3: validar los datos y entregar el costo final**



Como cliente de EnviaYa, quiero que el sistema valide los datos de mi envio y muestre un costo minimo correctamente redondeado.

Criterios de aceptacion:



* Dada una zona distinta de urbana, rural o nacional, cuando se calcula el envio, entonces el sistema debe lanzar un error.
* Dado un dia menor que 1 o mayor que 7, cuando se calcula el envio, entonces el sistema debe lanzar un error.
* Dado un costo calculado menor que $5.000, cuando se obtiene el total, entonces el sistema debe usar $5.000 como costo minimo.
* Dado un costo que debe redondearse, cuando se obtiene el resultado final, entonces el sistema debe redondearlo al multiplo de $100 mas cercano y redondear los $50 hacia arriba.



###### **1.4 Matriz de trazabilidad inicial**



|Requisito|Historia de usuario|Casos de prueba asociados|
|-|-|-|
|R1|Historia de usuario 1|P01, P02, P03|
|R2|Historia de usuario 3|P10, P11, P12, P13, P16, P17|
|R3|Historia de usuario 1|P04, P05, P06, P07|
|R4|Historia de usuario 1|P10, P14, P15|
|R5|Historia de usuario 2|P16, P18, P25|
|R6|Historia de usuario 2|P19, P20, P21, P22, P23|
|R7|Historia de usuario 2|P24|
|R8|Historia de usuario 3|P07, P25, P26|





#### **Parte 2 — Plan de pruebas**



###### **2.1 Alcance**



El plan verifica el calculo del costo de envio de EnvíaYa de acuerdo con los requisitos R1 a R8 de la Parte 1. Se probaran el peso, la zona, el dia, el tipo de cliente, el cupon, la tarifa base, los recargos, los descuentos, el costo minimo y el redondeo.



En esta parte, las pruebas se ejecutaran primero contra el codigo heredado para registrar los defectos observados. Despues de corregir el codigo, se repetiran los mismos casos como pruebas de regresion.



###### **2.2 Niveles de prueba**



| Nivel | Aplicacion en este proyecto |

|---|---|

| Unidad | Probar la funcion de calculo con entradas individuales y comprobar el resultado o error esperado. |

| Integracion | Comprobar que la funcion de calculo usa correctamente la configuracion personalizada de Jhon y las reglas de zona, cliente   y cupon. |

| Sistema | Probar el flujo completo de ingreso de peso, zona, cliente, dia y cupon hasta obtener el costo final. |

| Aceptacion | Comprobar que los resultados cumplen las reglas R1 a R8 de la especificacion personalizada. |



###### **2.3 Estrategia de pruebas**



Se usaran particiones de equivalencia, valores limite, tablas de decision y pruebas de caja blanca.



Se probaran entradas validas e invalidas para cada dato. Para el peso se revisaran los limites 0, L1 = 3 kg, L2 = 10 kg y PMAX = 50 kg. Tambien se probaran las combinaciones de cliente, cupon y fin de semana que afectan el orden de los descuentos y recargos.



Los resultados esperados se calcularan manualmente antes de ejecutar los casos. La suite se ejecutara contra el codigo heredado y, despues de corregir los defectos, contra la version refactorizada.



###### 2.4 Ambiente y herramientas



* Sistema operativo: Windows.
* Lenguaje: Python.
* Framework de pruebas: pytest.
* Medicion de cobertura: pytest-cov.
* Control de versiones: Git y GitHub.
* Archivo bajo prueba: envios.py.
* Archivo con el codigo heredado: se conservara separado para comparar su comportamiento.



###### 2.5 Roles



| Rol | Responsabilidad |

|---|---|

| Estudiante y responsable de pruebas | Jhon Faber Mindiola Atencio: define los casos, calcula los resultados esperados, automatiza las pruebas, registra defectos y corrige el codigo. |

| Revisor de requisitos | Verifica que los casos y resultados correspondan a la especificacion personalizada. |

| Usuario de aceptacion | Comprueba que el costo final siga las reglas de negocio de EnvíaYa. |



###### 2.6 Riesgos y mitigaciones



| Riesgo | Mitigacion |

|---|---|

| Usar parametros de otro estudiante | Verificar que el informe y CONFIG usen el codigo 0182410099. |

| Calcular mal el orden de recargos y descuentos | Aplicar el orden definido por B = 1 y E = 9, y mostrar calculos manuales. |

| No probar exactamente los limites de peso | Incluir casos en 0, 3, 10 y 50 kg, ademas de valores inmediatamente inferiores o superiores. |

| Corregir el codigo antes de registrar los defectos heredados | Ejecutar primero las pruebas contra la version heredada y guardar sus resultados. |

| Cambiar una regla al refactorizar | Ejecutar de nuevo la misma suite como regresion despues de cada cambio. |

| No tener evidencia de pruebas o historial Git | Guardar capturas y hacer commits al completar cada avance real. |



###### **2.7 Criterios de entrada**



* La especificacion R1 a R8 esta escrita y personalizada para Jhon.
* Los parametros de CONFIG corresponden al codigo 0182410099.
* Los casos de prueba tienen entradas y resultados esperados calculados.
* El codigo heredado esta disponible para la primera ejecucion.



###### **2.8 Criterios de salida**



* Todos los casos planificados fueron ejecutados contra el codigo heredado.
* Los defectos observados quedaron registrados con pasos para reproducirlos.
* Despues de las correcciones, se repitieron los mismos casos.
* Los resultados finales y la cobertura quedaron documentados.
* Se conservaron las evidencias necesarias para el informe y la sustentacion.



#### **Parte 3 — Diseño de casos de caja negra**



###### **3.1 Particiones de equivalencia**



Una particion de equivalencia agrupa entradas que deberian recibir el mismo tratamiento. Se probaran valores de cada grupo para verificar que el sistema responda segun la especificacion R1–R8.



| Entrada | Particiones validas | Particiones invalidas o especiales |

|---|---|---|

| Peso | 0 < peso ≤ 3 kg; 3 kg < peso ≤ 10 kg; 10 kg < peso ≤ 50 kg | Peso ≤ 0 y peso > 50 kg. Debe producirse el error de peso indicado en R1. |

| Zona | urbana, rural y nacional | Cualquier valor distinto de esas tres zonas. R2 exige un error. |

| Cliente | normal, frecuente y vip | Un tipo distinto de esos tres queda fuera del dominio descrito. El enunciado no define que resultado debe producir; se registrara esta ambiguedad y no se asignara un resultado esperado como si fuera una regla del profesor. |

| Dia | Dias habiles del 1 al 5; sabado 6; domingo 7 | Valores menores que 1 y mayores que 7. R2 exige un error. |

| Cupon | Sin cupon; cupon ENVIO10 | Cualquier cupon desconocido. Como F = 9 es impar, R7 exige un error. |



###### **3.2 Valores limite del peso**



El valor L1 es 3 kg y se incluye en el primer tramo porque D = 0 es par. L2 es 10 kg y se incluye en el segundo tramo. PMAX es 50 kg y tambien se acepta.



| Limite | Por debajo | En el limite | Por encima |

|---|---|---|---|

| 0 kg | -0,01 kg — P02 | 0 kg — P01 | 0,01 kg — P08 |

| L1 = 3 kg | 2,99 kg — P28 | 3 kg — P04 | 3,01 kg — P05 |

| L2 = 10 kg | 9,99 kg — P29 | 10 kg — P06 | 10,01 kg — P30 |

| PMAX = 50 kg | 49,99 kg — P31 | 50 kg — P09 | 50,01 kg — P03 |



P30 permite revisar el peso inmediatamente superior a L2. Su incremento de tarifa base es de $8, pero al redondear a la centena mas cercana el resultado urbano sigue siendo $9.000. Por eso tambien se incluye P07, cuyo peso permite observar el cobro proporcional en el resultado final.



###### **3.3 Tabla de decision: cliente, cupon y fin de semana**



A representa la tarifa base despues de aplicar el recargo de zona. Como B = 1 es impar, los descuentos de cliente y cupon se aplican ambos y en secuencia: primero el descuento del cliente y luego el cupon. Como E = 9 es impar, el recargo de fin de semana se suma despues de los descuentos.



| Cliente | Cupon | Dias 1–5 | Dias 6–7 |

|---|---|---|---|

| Normal | Ausente | A | A + $2.000 |

| Normal | ENVIO10 | A × 0,90 | A × 0,90 + $2.000 |

| Normal | Desconocido | Error | Error |

| Frecuente | Ausente | A × 0,95 | A × 0,95 + $2.000 |

| Frecuente | ENVIO10 | A × 0,95 × 0,90 | A × 0,95 × 0,90 + $2.000 |

| Frecuente | Desconocido | Error | Error |

| VIP | Ausente | A × 0,85 | A × 0,85 + $2.000 |

| VIP | ENVIO10 | A × 0,85 × 0,90 | A × 0,85 × 0,90 + $2.000 |

| VIP | Desconocido | Error | Error |



Despues de aplicar la regla correspondiente, el costo minimo es $5.000 y el resultado se redondea al multiplo de $100 mas cercano. Los $50 se redondean hacia arriba.



###### **3.4 Matriz de casos de prueba**



Las entradas aparecen en este orden: peso, zona, cliente, dia y cupon. Los resultados esperados se calcularon con los parametros de Jhon.



| ID | Requisito | Entradas | Resultado esperado calculado a mano | Tecnica |

|---|---|---|---|---|

| P01 | R1 | 0 kg, urbana, normal, dia 3, sin cupon | Error de peso. R1 especifica el mensaje “peso inválido”. | Limite |

| P02 | R1 | -0,01 kg, urbana, normal, dia 3, sin cupon | Error de peso. | Limite |

| P03 | R1 | 50,01 kg, urbana, normal, dia 3, sin cupon | Error de peso. | Limite |

| P04 | R3 | 3 kg, urbana, normal, dia 5, sin cupon | $6.000 | Limite L1 |

| P05 | R3 | 3,01 kg, urbana, normal, dia 5, sin cupon | $9.000 | Limite L1 |

| P06 | R3 | 10 kg, urbana, normal, dia 5, sin cupon | $9.000 | Limite L2 |

| P07 | R3, R8 | 11,3125 kg, urbana, normal, dia 5, sin cupon | Base: $9.000 + (1,3125 × $800) = $10.050. Resultado: $10.100. | Tarifa proporcional y redondeo |

| P08 | R1, R3 | 0,01 kg, urbana, normal, dia 5, sin cupon | $6.000 | Particion valida |

| P09 | R1, R3 | 50 kg, urbana, normal, dia 5, sin cupon | $41.000 | Limite PMAX |

| P10 | R2 | 2 kg, costera, normal, dia 3, sin cupon | Error de zona | Particion invalida |

| P11 | R2 | 2 kg, rural, normal, dia 0, sin cupon | Error de dia | Limite |

| P12 | R2 | 2 kg, rural, normal, dia 8, sin cupon | Error de dia | Limite |

| P13 | R2 | 2 kg, urbana, normal, dia -1, sin cupon | Error de dia | Particion invalida |

| P14 | R4 | 4 kg, rural, normal, dia 5, sin cupon | $9.000 × 1,15 = $10.350. Resultado: $10.400. | Particion de zona |

| P15 | R4 | 4 kg, nacional, normal, dia 5, sin cupon | $9.000 × 1,40 = $12.600. Resultado: $12.600. | Particion de zona |

| P16 | R2, R5 | 4 kg, urbana, normal, dia 5, sin cupon | $9.000. No hay recargo de fin de semana. | Particion de dia |

| P17 | R2, R5 | 4 kg, urbana, normal, dia 7, sin cupon | $9.000 + $2.000 = $11.000. | Domingo |

| P18 | R5 | 4 kg, urbana, normal, dia 6, sin cupon | $9.000 + $2.000 = $11.000. | Sabado |

| P19 | R6 | 4 kg, urbana, frecuente, dia 5, sin cupon | $9.000 × 0,95 = $8.550. Resultado: $8.600. | Particion de cliente |

| P20 | R6 | 4 kg, urbana, vip, dia 5, sin cupon | $9.000 × 0,85 = $7.650. Resultado: $7.700. | Particion de cliente |

| P21 | R6 | 4 kg, urbana, normal, dia 5, ENVIO10 | $9.000 × 0,90 = $8.100. | Particion de cupon |

| P22 | R6 | 4 kg, urbana, vip, dia 5, ENVIO10 | $9.000 × 0,85 × 0,90 = $6.885. Resultado: $6.900. | Tabla de decision |

| P23 | R6 | 4 kg, urbana, frecuente, dia 5, ENVIO10 | $9.000 × 0,95 × 0,90 = $7.695. Resultado: $7.700. | Tabla de decision |

| P24 | R7 | 4 kg, urbana, normal, dia 5, OTRO | Error por cupon desconocido, porque F = 9 es impar. | Particion especial |

| P25 | R5, R8 | 4 kg, urbana, vip, dia 6, sin cupon | $9.000 × 0,85 + $2.000 = $9.650. Resultado: $9.700. | Orden y redondeo |

| P26 | R6, R8 | 2 kg, urbana, vip, dia 5, ENVIO10 | $6.000 × 0,85 × 0,90 = $4.590. Se aplica el minimo: $5.000. | Minimo |

| P27 | R4–R8 | 4 kg, rural, vip, dia 6, ENVIO10 | $9.000 × 1,15 × 0,85 × 0,90 + $2.000 = $9.917,75. Resultado: $9.900. | Tabla de decision |

| P28 | R3 | 2,99 kg, urbana, normal, dia 5, sin cupon | $6.000 | Limite L1 |

| P29 | R3 | 9,99 kg, urbana, normal, dia 5, sin cupon | $9.000 | Limite L2 |

| P30 | R3, R8 | 10,01 kg, urbana, normal, dia 5, sin cupon | Base: $9.000 + (0,01 × $800) = $9.008. Resultado redondeado: $9.000. | Limite L2 |

| P31 | R3, R8 | 49,99 kg, urbana, normal, dia 5, sin cupon | Base: $9.000 + (39,99 × $800) = $40.992. Resultado: $41.000. | Limite PMAX |



###### **3.5 Calculos detallados de resultados esperados**



**Caso P07**



El peso es 11,3125 kg, por lo que supera L2 = 10 kg. El exceso es 11,3125 − 10 = 1,3125 kg.



Tarifa base = $9.000 + (1,3125 × $800) = $10.050.



La zona es urbana, no hay descuentos ni recargo de fin de semana. El costo es mayor que el minimo de $5.000. Como termina exactamente en $50, se redondea hacia arriba.



Resultado esperado: $10.100.



**Caso P14**



El peso de 4 kg pertenece al segundo tramo, asi que la tarifa base es $9.000.



Recargo rural = $9.000 × 0,15 = $1.350.



Subtotal = $9.000 + $1.350 = $10.350.



El valor esta a mitad entre $10.300 y $10.400; los $50 se redondean hacia arriba.



Resultado esperado: $10.400.



**Caso P22**



El peso de 4 kg pertenece al segundo tramo. La tarifa base urbana es $9.000.



Descuento VIP = $9.000 × 0,85 = $7.650.



Cupon ENVIO10, aplicado despues del descuento VIP = $7.650 × 0,90 = $6.885.



No hay recargo de fin de semana y el costo es mayor que el minimo.



Resultado esperado redondeado: $6.900.



**Caso P25**



La tarifa base para 4 kg en zona urbana es $9.000.



Descuento VIP = $9.000 × 0,85 = $7.650.



El dia 6 es sabado. Como E = 9 es impar, el recargo de $2.000 se agrega despues de los descuentos.



Subtotal = $7.650 + $2.000 = $9.650.



Los $50 se redondean hacia arriba.



Resultado esperado: $9.700.



**Caso P26**



El peso de 2 kg pertenece al primer tramo, cuya tarifa es $6.000.



Descuento VIP = $6.000 × 0,85 = $5.100.



Cupon ENVIO10, aplicado despues del descuento VIP = $5.100 × 0,90 = $4.590.



El resultado es menor que el costo minimo.



Resultado esperado: $5.000.



**Caso P27**



El peso de 4 kg tiene tarifa base de $9.000.



Recargo rural = $9.000 × 1,15 = $10.350.



Descuento VIP = $10.350 × 0,85 = $8.797,50.



Cupon ENVIO10 = $8.797,50 × 0,90 = $7.917,75.



Como es sabado y E = 9 es impar, se agregan $2.000 despues de los descuentos.



Subtotal = $7.917,75 + $2.000 = $9.917,75.



El multiplo de $100 mas cercano es $9.900.



Resultado esperado: $9.900.



###### **3.6 Observaciones de la especificacion**



El enunciado no define que debe ocurrir si el tipo de cliente no es normal, frecuente o vip. En esta matriz no se asigna un resultado esperado para ese caso, porque no se debe inventar una regla que el profesor no especifico.



Los resultados de esta matriz se calcularon segun R1–R8 para Jhon. Al ejecutar los mismos casos contra el codigo heredado, algunos fallaran; esos resultados obtenidos se registraran despues en la Parte 5 como defectos.

