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



\- La especificacion R1 a R8 esta escrita y personalizada para Jhon.

\- Los parametros de CONFIG corresponden al codigo 0182410099.

\- Los casos de prueba tienen entradas y resultados esperados calculados.

\- El codigo heredado esta disponible para la primera ejecucion.



###### **2.8 Criterios de salida**



\- Todos los casos planificados fueron ejecutados contra el codigo heredado.

\- Los defectos observados quedaron registrados con pasos para reproducirlos.

\- Despues de las correcciones, se repitieron los mismos casos.

\- Los resultados finales y la cobertura quedaron documentados.

\- Se conservaron las evidencias necesarias para el informe y la sustentacion.

