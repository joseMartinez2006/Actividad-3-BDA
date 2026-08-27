from database import conectar


def mostrar_jobs():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM JOBS")

    jobs = cursor.fetchall()

    if len(jobs) == 0:
        print("No hay jobs registrados.")
    else:
        for job in jobs:
            print(job)

    cursor.close()
    conexion.close()


def agregar_job():
    job_id = input("Ingrese el ID del job: ")
    job_title = input("Ingrese el nombre del job: ")
    min_salary = int(input("Ingrese el salario mínimo: "))
    max_salary = int(input("Ingrese el salario máximo: "))

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO JOBS (JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY)
        VALUES (:1, :2, :3, :4)
    """

    cursor.execute(sql, (job_id, job_title, min_salary, max_salary))

    conexion.commit()

    print("Job agregado correctamente.")

    cursor.close()
    conexion.close()


def actualizar_job():
    job_id = input("Ingrese el ID del job que desea actualizar: ")
    job_title = input("Ingrese el nuevo nombre del job: ")
    min_salary = int(input("Ingrese el nuevo salario mínimo: "))
    max_salary = int(input("Ingrese el nuevo salario máximo: "))

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        UPDATE JOBS
        SET JOB_TITLE = :1,
            MIN_SALARY = :2,
            MAX_SALARY = :3
        WHERE JOB_ID = :4
    """

    cursor.execute(sql, (job_title, min_salary, max_salary, job_id))

    conexion.commit()

    print("Job actualizado correctamente.")

    cursor.close()
    conexion.close()


def eliminar_job():
    job_id = input("Ingrese el ID del job que desea eliminar: ")

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        DELETE FROM JOBS
        WHERE JOB_ID = :1
    """

    cursor.execute(sql, (job_id,))

    conexion.commit()

    print("Job eliminado correctamente.")

    cursor.close()
    conexion.close()


while True:
    print("\n===== CRUD DE JOBS =====")
    print("1. Mostrar jobs")
    print("2. Agregar job")
    print("3. Actualizar job")
    print("4. Eliminar job")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_jobs()

    elif opcion == "2":
        agregar_job()

    elif opcion == "3":
        actualizar_job()

    elif opcion == "4":
        eliminar_job()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")