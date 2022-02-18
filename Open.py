def main():
    try:
    
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No pudimos encontrar el archivo  'config.txt'")
    except IsADirectoryError:
        print("Se encontro el archivo, pero no se puede leer")
    

if __name__ == '__main__':
    main()