
'''
    Autor: Richard Vinueza
    Curso: Estructura de Datos - ESPOCH
    Ejercicio: REGISTRAR PACIENTES (PYTHON 3)
    IDE: PyCharm
'''


import List as ls
import Utils as u


class Data:
    def __init__(self, _code=None, _names=None, _lastNames=None, _address=None, _phone=None):
        self.code = _code  # campo codigo
        self.names = _names  # campo que almacena el nombre
        self.lastNames = _lastNames  # campo que almacena el apellido
        self.address = _address  # campo que almacena la direccion
        self.phone = _phone   # campo que almacena el telefono

    def getData(self):
        print("Data")

    def set(self):
        print("setDAta")


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
    return input ("\n Ingrese opcion : ")


# ----------------- MENU ACTUALIZAR UN DATO---------------
def menu_actualizar():
    print ("\n\t\t[    ESPECIFIQUE CAMPO A ACTUALIZAR    ]\n  ")
    print ("\t\t----------------------------\n\n              ")
    print (" 1. NOMBRES                                       ")
    print (" 2. APELLIDOS                                     ")
    print (" 3. DIRECCION                                     ")
    print (" 4. TELEFONO                                      ")
    print (" 5. SALIR                                         ")
    return input("\n Ingrese opcion : ")


# -------------------- REGISTRAR PACIENTES ------------------
def registrar_pacientes(lista):
    register = Data()
    print("\n\n\t\t[  REGISTRO  ]\n")
    print("\t\t--------------------")
    print("\n\tDATOS DEL PACIENTE ")
    register.code = input("\n\n\tCODIGO:")
    register.name = input("\n\tNOMBRES:")
    register.last_name = input("\tAPELLIDOS:")
    register.address = input("\tDIRECCION:")
    register.phone = input("\n\tTELEFONO:")

    lista.add_at_front(register)


# ------------------------ ELIMINAR PACIENTE ---------------------
def eliminar_paciente(lista):
    # int cod;
    # PLista q,t;
    # q=lista;

    print("\n\n\n\tELIMINAR UN PACIENTE")
    print("\n\n\tINGRESE CODIGO:")


# -------------------- ACTUALIZAR PACIENTE -------------------
def actualizar_paciente(lista):
    print("")
    # int cod, x;
    # PLista q;
    # q=lista;

    # cout<<"\n\n\n\tACTUALIZAR REGISTRO DE PACIENTE";
    # cout<<"\n\n\tINGRESE CODIGO:"; cin>>cod;
    #
    # while(q!=NULL){
    #
    #         if(q->codigo==cod){
    #             system("cls");
    #             cout<<"\n\tDATOS DEL PACIENTE  ";
    #             cout<<"\n\t--------------------";
    #             cout<<"\n\n\tCODIGO   : "<<q->codigo<<endl;
    #             cout<<"\n\tNOMBRES  : "<<q->nombres<<endl;
    #             cout<<"\tAPELLIDOS: "<<q->apellidos<<endl;
    #             cout<<"\tDIRECCION: "<<q->direccion<<endl;
    #             cout<<"\tTELEFONO : "<<q->telefono<<endl;
    #
    #             menu_actualizar();
    #             cin>>x;
    #
    #             switch(x){
    #
    #                 case 1: cout<<"\n\n\tINGRESE NOMBRES:";
    #                         cin.ignore(); cin.getline(q->nombres,maxchar);
    #                         break;
    #
    #                 case 2: cout<<"\n\n\tINGRESE APELLIDOS:";
    #                         cin.ignore(); cin.getline(q->apellidos,maxchar);
    #                         break;
    #
    #                 case 3: cout<<"\n\n\tINGRESE DIRECCION:";
    #                         cin.ignore(); cin.getline(q->direccion,maxchar);
    #                         break;
    #
    #                 case 4: cout<<"\n\n\tINGRESE TELEFONO:";
    #                         cin>>q->telefono;
    #                         break;
    #
    #                 default: cout<<"\nINGRESE UNA OPCION VALIDA...\n"; break;
    #
    #             }
    #             cout<<"\n\n\tREGISTRO ACTUALIZADO...!!!!!\n";
    #
    #             return;
    #
    #         }else {
    #
    #
    #             q=q->sgte;
    #
    #     }
    #
    # }
    # if(q==NULL)
    #     cout<<"\n\tCODIGO INCORRECTO...!!\n";

# /*---------------------- FUNCION MOSTRAR PACIENTE -------------------*/
# def mostrar_pacientes(q):
#
#     int i=1;
#
#     while(q!=NULL){
#
#         cout<<"\n\tDATOS DEL PACIENTE ["<<i<<"] ";
#         cout<<"\n\t------------------------";
#         cout<<"\n\n\tCODIGO   : "<<q->codigo<<endl;
#         cout<<"\n\tNOMBRES  : "<<q->nombres<<endl;
#         cout<<"\tAPELLIDOS: "<<q->apellidos<<endl;
#         cout<<"\tDIRECCION: "<<q->direccion<<endl;
#         cout<<"\tTELEFONO : "<<q->telefono<<endl;
#
#         q=q->sgte;
#
#         i++;
#     }
#
#
#
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
    list = ls.List()

    # PLista lista=NULL;
    while not out:

        u.clear()
        option = menu()
        u.clear()
        if option == "1":
            registrar_pacientes(list)
        elif option == "2":
            list.print_list()
            # if list.isEmty():
            #     emptyData()
            # else:
            #     eliminar_paciente(lista)
        elif option == "3":
            print(option)
            # if list.isEmty():
            #     emptyData()
            # else:
            #     actualizar_paciente(lista)
        elif option == "4":
            print(option)
            # if list.isEmty():
            #     emptyData()
            # else:
            #     mostrar_pacientes(lista)
        elif option == "5":
            print(option)
            # if list.isEmty():
            #     emptyData()
            # else:
            #     copiar_datos_paciente(lista)
        elif option <= "0" or option >= "7":
            print("\nINGRESE UNA OPCION VALIDA...\n")

        if option != "6":
            u.pause()
        else:
            print("Saliendo...")
            out = True


if __name__ == '__main__':
    main()
