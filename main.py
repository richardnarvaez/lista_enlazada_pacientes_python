
'''
    Autor: Richard Vinueza
    Curso: Estructura de Datos - ESPOCH
    Ejercicio: REGISTRAR PACIENTES (PYTHON 3)
    IDE: PyCharm
'''


import List as ls
import Utils as u


# Datos que contiene el objeto PACIENTE
class Paciente:
    def __init__(self, _code=None, _names=None, _lastNames=None, _address=None, _phone=None):
        self.code = _code  # campo codigo
        self.names = _names  # campo que almacena el nombre
        self.lastNames = _lastNames  # campo que almacena el apellido
        self.address = _address  # campo que almacena la direccion
        self.phone = _phone   # campo que almacena el telefono


# -------------------- MENU PRINCIPAL --------------------
def menu():
    print("\n----------------------------------------")
    print("     [    REGISTRO DE PACIENTES    ]      ")
    print("----------------------------------------\n")
    print(" 1. REGISTRAR PACIENTE                    ")
    print(" 2. ELIMINAR DATOS DE PACIENTE            ")
    print(" 3. ACTUALIZAR PACIENTES                  ")
    print(" 4. MOSTRAR LISTADO                       ")
    print(" 5. COPIAR DATOS DE UN PACIENTE A OTRO    ")
    print(" 6. SALIR                                 ")
    return input("\n Ingrese opcion : ")


# ----------------- MENU ACTUALIZAR UN DATO---------------
def menu_actualizar():
    print("\n\t\t[    ESPECIFIQUE CAMPO A ACTUALIZAR    ]\n  ")
    print("\t\t----------------------------\n\n              ")
    print(" 1. NOMBRES                                       ")
    print(" 2. APELLIDOS                                     ")
    print(" 3. DIRECCION                                     ")
    print(" 4. TELEFONO                                      ")
    print(" 5. SALIR                                         ")
    return input("\n Ingrese opcion : ")


# -------------------- REGISTRAR PACIENTES ------------------
def registrar_pacientes(lista):
    register = Paciente()
    print("\n[  REGISTRO  ]")
    print("--------------------")
    print("\nDATOS DEL PACIENTE ")
    register.code = input("CODIGO:")
    register.name = input("NOMBRES:")
    register.lastNames = input("APELLIDOS:")
    register.address = input("DIRECCION:")
    register.phone = input("TELEFONO:")

    lista.add_at_front(register)


# ------------------------ ELIMINAR PACIENTE ---------------------
def eliminar_paciente(lista):
    print("\nELIMINAR UN PACIENTE")
    code = input("INGRESE CODIGO:")
    lista.delete_node(code)


# -------------------- ACTUALIZAR PACIENTE -------------------
def actualizar_paciente(lista):
    print("ACTUALIZAR REGISTRO DE PACIENTE")
    cod = input("INGRESE CODIGO:")
    head = lista.head

    while head != None:
        dtP = head.data
        if dtP.code == cod:
            u.clear()
            print("\n\tDATOS DEL PACIENTE  ")
            print("\n\t--------------------")
            print("\n\n\tCODIGO   : ", dtP.code)
            print("\tNOMBRES  : ", dtP.names)
            print("\tAPELLIDOS: ", dtP.lastNames)
            print("\tDIRECCION: ", dtP.address)
            print("\tTELEFONO : ", dtP.phone)

            pos = menu_actualizar()

            if pos <= "0" or pos >= "6":
                print("INGRSE UNA OPCION VALIDA")
            elif pos == "1":
                dtP.names = input("INGRESE NOMBRES:")
            elif pos == "2":
                dtP.lastNames = input("INGRESE APELLIDOS:")
            elif pos == "3":
                dtP.adress = input("INGRESE DIRECCION:")
            elif pos == "4":
                dtP.phones = input("INGRESE TELEFONO:")
            elif pos == "5":
                head = None
        else:
            head = head.next



# # /*--------------- FUNCION COPIAR DATOS DE UN PACIENTEA OTRO ------------------*/
# void copiar_datos_paciente(PLista lista){
#
#     int cod1,cod2, x;
#     PLista p,q,t;
#     p=lista;
#     q=lista;
#     char dato[maxchar];
#
#     cout<<"\n\n\n\tCOPIAR DATOS DE PACIENTE A OTRO";
#     cout<<"\n\n\n\t--------------------------------";
#     cout<<"\n\n\tINGRESE CODIGO DE PACIENTE A COPIAR:"; cin>>cod1;
#     cout<<"\n\n\tINGRESE CODIGO DE PACIENTE A SUSTITUIR:";cin>>cod2;
#     system("cls");
#
#     while(p!=NULL){
#
#             if(p->codigo==cod1){
#                 t=p;
#                 cout<<"\n\tDATOS DEL PACIENTE  COPIAR ";
#                 cout<<"\n\t---------------------------";
#                 cout<<"\n\n\tCODIGO   : "<<p->codigo<<endl;
#                 cout<<"\n\tNOMBRES  : "<<p->nombres<<endl;
#                 cout<<"\tAPELLIDOS: "<<p->apellidos<<endl;
#                 cout<<"\tDIRECCION: "<<p->direccion<<endl;
#                 cout<<"\tTELEFONO : "<<p->telefono<<endl;
#
#             }
#                 p=p->sgte;
#
#         }
#     while(q!=NULL){
#
#             if(q->codigo==cod2){
#
#                 cout<<"\n\tDATOS DEL PACIENTE A SUSITUIR ";
#                 cout<<"\n\t--------------------";
#                 cout<<"\n\n\tCODIGO   : "<<q->codigo<<endl;
#                 cout<<"\n\tNOMBRES  : "<<q->nombres<<endl;
#                 cout<<"\tAPELLIDOS: "<<q->apellidos<<endl;
#                 cout<<"\tDIRECCION: "<<q->direccion<<endl;
#                 cout<<"\tTELEFONO : "<<q->telefono<<endl;
#
#                 menu_actualizar();
#                 cin>>x;
#
#                 switch(x){
#
#                     case 1: strcpy(dato,t->nombres);
#                             strcpy(q->nombres,dato);
#                             break;
#
#                     case 2: strcpy(dato,t->apellidos);
#                             strcpy(q->apellidos,dato);
#                             break;
#
#                     case 3: strcpy(dato,t->direccion);
#                             strcpy(q->direccion,dato);
#                             break;
#
#                     case 4: q->telefono=t->telefono;
#                             break;
#
#                     default: cout<<"\nINGRESE UNA OPCION VALIDA...\n"; break;
#
#                 }
#                 cout<<"\n\n\tREGISTRO ACTUALIZADO...!!!!!\n";
#
#                 return;
#
#             }else {
#
#
#                 q=q->sgte;
#
#         }
#
#     }
#
#     if(q==NULL)
#         cout<<"\n\tCODIGO INCORRECTO...!!\n";


# /*------------------------- FUNCION PRINCIPAL -------------------*/
def main():
    out = False
    listPacientes = ls.List()

    while not out:

        u.clear()
        option = menu()
        u.clear()

        if option <= "0" or option >= "7":
            print("\nINGRESE UNA OPCION VALIDA...\n")

        elif option == "1":
            registrar_pacientes(listPacientes)

        elif option == "2":
            if listPacientes.is_empty():
                u.emptyData()
            else:
                eliminar_paciente(listPacientes)
        elif option == "3":
            print(option)
            if listPacientes.is_empty():
                u.emptyData()
            else:
                actualizar_paciente(listPacientes)
        elif option == "4":
            if listPacientes.is_empty():
                u.emptyData()
            else:
                listPacientes.print_list()
        elif option == "5":
            print(option)
            if listPacientes.is_empty():
                u.emptyData()
            else:
                print("Proximamente...")
                #copiar_datos_paciente(listPacientes)

        if option != "6":
            u.pause()
        else:
            print("Saliendo...")
            out = True


if __name__ == '__main__':
    main()
