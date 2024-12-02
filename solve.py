import argparse
import solver


def mostrar_acerca_de():
    print("""Killer Sudoku Solver

Script para resolver rompecabezas de Killer Sudoku, donde los rompecabezas clásicos de Sudoku se extienden con jaulas 
que pueden abarcar múltiples nonetos.
""")


def main():
    parser = argparse.ArgumentParser(description="Resolver un Killer Sudoku desde un archivo")
    parser.add_argument("--stats",
                        action="store_true",
                        help=("Si se establece, el solucionador mostrará información sobre cuántas combinaciones "
                              "fueron intentadas"))
    parser.add_argument("--show-initial-board",
                        action="store_true",
                        help="Muestra el tablero y las regiones antes de intentar resolverlo.")
    parser.add_argument("--benchmark",
                        action="store_true",
                        help=("Realiza una prueba de rendimiento con los archivos especificados, "
                              "intentando resolver los rompecabezas y mostrando el tiempo que se tardó en hacerlo"))
    parser.add_argument("--about",
                        action="store_true",
                        help="Muestra el texto que describe este script y luego sale")
    parser.add_argument("filename",
                        nargs='+',
                        help="El nombre del archivo JSON para cargar el tablero y las regiones")
    parsed_args = parser.parse_args()

    if parsed_args.about:
        return mostrar_acerca_de()

    solver.run_solver(filenames=parsed_args.filename,
                      show_stats=parsed_args.stats,
                      benchmark=parsed_args.benchmark,
                      show_initial_board=parsed_args.show_initial_board)


if __name__ == '__main__':
    main()
