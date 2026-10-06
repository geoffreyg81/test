from projet_dev_avance.module2 import add
from projet_dev_avance.module1 import hello_module
from projet_dev_avance.utilitaires.maths import multiply
from projet_dev_avance.utilitaires.text import to_upper_case

def dire_coucou():
    print(hello_module())
    print('2+3=', add(2,3))
    print(multiply(2,3))
    print(to_upper_case("texte"))


if __name__ == "__main__":
    dire_coucou()