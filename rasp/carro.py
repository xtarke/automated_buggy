import pigpio
import time
import motor


def main():
    print('Olá carrinho')
    
    pinos = pigpio.pi()
    
    motores = motor.Motor(pinos)
    
    

if __name__ == '__main__':
    main()

