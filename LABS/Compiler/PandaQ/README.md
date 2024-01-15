# PandaQ

El compilador de SQL

## Usage

Aquest programa està enfocat per a ser executat en el sistema operatiu Linux Ubuntu.

Per poder executar el programa, s'ha de tenir instalat python3 i streamlit a la màquina. A més de tenir les dades localment en una carpeta anomenada "data".

Per posar en marxa el compilador, simplement s'ha de navegar amb la terminal a la carpeta amb els arxius "PandaQ.py", "pandaQ.g4", i la carpeta "data" mencionada anteriorment.

I introduïr les següents comandes:

```console

antlr4 -Dlanguage=Python3 -no-listener -visitor pandaQ.g4

streamlit run pandaQ.py

```

S'obrirà una finestra on introduir la consulta SQL. Un cop introduïda s'ha de pressionar el botó "Submit".

Qualsevol error de gramàtica (o ortografia de majúscules i minúscules) de la consulta sortirà per la terminal on s'ha posat en marxa el programa.
Qualsevol error de SQL o compilació del programa sortirà per la finestra oberta.

També es poden consultar diversos debugs per la terminal: descomentar els trossos de codi marcats amb "#DEBUG" a l'script "PandaQ.py" per a més informació diversa del programa si s'escau.

## Capacitats del programa

El programa és capaç de:

- Detectar errors de gramàtica, que sortiran per la terminal.

- Fer selects totals (amb *) en les taules. Admet tant 'select' com 'SELECT' i 'from' com 'FROM', per exemple:

```console

select * from employees;

SELECT * FROM employees;

```

- Fer selects de camps concrets en es taules, per exemple:

```console

select country_id, country_name from countries;

```

- Fer operacions ('+','-','*','/' i '^' amb o sense parèntesis) amb els camps de les taules (No sé per què, els enters sense decimals no funcionen, cal posar .0 per a un funcionament correcte)
  (NOTA: aquesta funcionalitat no és possible si es fa un select total *)
```console

select first_name, salary, salary + 100.0 as new_salary1, salary * 2.0 ^ 1.05 as new_salary2 from employees;

```

- Ordenar els resultats de les consultes amb 'order by' ascendent o descendent (fins i tot les columnes noves creades per operacions):

```console

select * from countries order by region_id;

select first_name, last_name, salary, salary * 25.0 as new_salary from employees order by new_salary;

```

- Filtrar les files (incloses de columnes calculades) amb condicions booleanes utilitzant el WHERE amb and, or i not (si s'usen nombres enters per a les condicions, s'ha de posar el .0 per a que funcioni), per exemple:

```console

select * from countries where not region_id = 1.0 and not region_id = 3.0;

select first_name, salary, salary ^ 1.005 as new_salary from employees where salary < 10000.0 or not new_salary < 20000.0;

```

- Fins aquí és el que admet el compilador, la resta de funcionalitats o estan a mig implementar o directament no hi son.

