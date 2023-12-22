import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'

empleados = requests.get(url).json()

total_empleados = 0
total_salario = 0
total_edad = 0
salario_minimo = float('inf')
salario_maximo = float('-inf')
edad_minima = float('inf')
edad_maxima = float('-inf')

if empleados and 'data' in empleados:
    empleados_lista = empleados['data']


    for empleado in empleados_lista:
        total_empleados += 1

        if 'employee_salary' in empleado and 'employee_age' in empleado:
            salario = float(empleado['employee_salary'])
            edad = float(empleado['employee_age'])

            total_salario += salario
            salario_minimo = min(salario_minimo, salario)
            salario_maximo = max(salario_maximo, salario)


            total_edad += edad
            edad_minima = min(edad_minima, edad)
            edad_maxima = max(edad_maxima, edad)


promedio_salario = round(total_salario / total_empleados, 2) if total_empleados > 0 else 0
promedio_edad = round(total_edad / total_empleados) if total_empleados > 0 else 0


print(f"La cantidad de empleados es: {total_empleados}")
print(f"El promedio de salario es: {promedio_salario}")
print(f"El promedio de edad es: {promedio_edad}")
print(f"El salario mínimo es: {salario_minimo:}")
print(f"El salario máximo es: {salario_maximo:}")
print(f"La edad mínima es: {int(edad_minima)}")
print(f"La edad máxima es: {int(edad_maxima)}")
