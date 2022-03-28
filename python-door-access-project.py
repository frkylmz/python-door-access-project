#!/usr/bin/env python
from time import sleep
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)

GPIO.setmode(GPIO.BOARD)
buzzer=7
GPIO.setup(buzzer, GPIO.OUT)


def SetAngle(angle):
        duty = (angle / 18) + 2
        GPIO.output(11, True)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(11, False)
        pwm.ChangeDutyCycle(0)
        
        
def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return
            
reader = SimpleMFRC522()

try:
        print("Lütfen kartınızı okutunuz.")
        id, text = reader.read()
        if id == 302789228645:
            
                GPIO.output(buzzer,GPIO.HIGH)
                sleep(0.075)
                GPIO.output(buzzer,GPIO.LOW)
                sleep(0.25)
            
                print("Merhaba Faruk Yılmaz")
                time.sleep(0.25)
                print("Seçenekler açılıyor...")
                time.sleep(0.25)
                
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(18, GPIO.OUT)
                for i in range(0,1):
                    blink(18)                                       
                
                print("""
                1- Kapı
                2- Çıkış
                
                """)
                
                while True:
                    
                        cevap = int(input("Yapmak istediğiniz işlemi seçiniz:"))
                        
                        if cevap == 1:
                            
                                cevap2 = int(input("Kapıyı açmak için 1 kapatmak için 2 tuşuna basınız:"))
                                
                                if cevap2 == 1:
                                    
                                        SetAngle(0)
                                        
                                        while True:
                                            GPIO.output(buzzer,GPIO.HIGH)
                                            print("Kapı açıldı.")
                                            sleep(0.25)
                                            GPIO.output(buzzer,GPIO.LOW)
                                            sleep(1)
                                            
                                            GPIO.setmode(GPIO.BOARD)
                                            GPIO.setup(29, GPIO.OUT)
                                            for i in range(0,1):
                                                blink(29)
                                            break
                                        
                                elif cevap2 == 2:
                                        SetAngle(180)
                                        
                                        while True:
                                            
                                            GPIO.output(buzzer,GPIO.HIGH)
                                            print("Kapı kapandı.")
                                            sleep(0.25)
                                            GPIO.output(buzzer,GPIO.LOW)
                                            sleep(1)
                                            
                                            GPIO.setmode(GPIO.BOARD)
                                            GPIO.setup(31, GPIO.OUT)
                                            for i in range(0,1):
                                                blink(31)                                       
                                            break
                                        
                        elif cevap == 2:
                            
                                print("Çıkış yapılıyor...")
                                time.sleep(0.25)
                                print("Çıkış yapıldı.")
                                time.sleep(0.25)
                                
                                GPIO.output(buzzer,GPIO.HIGH)
                                sleep(0.375)
                                GPIO.output(buzzer,GPIO.LOW)
                                sleep(1)
                                break
                            
        elif id==522679468823:
            
                GPIO.output(buzzer,GPIO.HIGH)
                sleep(0.075)
                GPIO.output(buzzer,GPIO.LOW)
                sleep(0.25)
            
                print("Merhaba Tayfun Dağcı ☺")
                time.sleep(0.25)
                print("Seçenekler açılıyor...")
                time.sleep(0.25)
                
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(18, GPIO.OUT)
                for i in range(0,1):
                    blink(18)                                       
                  
                print("""
                1- Kapı
                2- Çıkış
                
                """)
                
                while True:
                        cevap = int(input("Yapmak istediğiniz işlemi seçiniz:"))
                        
                        if cevap == 1:
                            
                                cevap2 = int(input("Kapıyı açmak için 1 kapatmak için 2 tuşuna basınız:"))
                                
                                if cevap2 == 1:
                                    
                                        SetAngle(0)                              
                                        while True:
                                            GPIO.output(buzzer,GPIO.HIGH)
                                            print("Kapı açıldı.")
                                            sleep(0.25)
                                            GPIO.output(buzzer,GPIO.LOW)
                                            sleep(1)
                                            
                                            GPIO.setmode(GPIO.BOARD)
                                            GPIO.setup(29, GPIO.OUT)
                                            for i in range(0,1):
                                                blink(29)
                                            break
                                        
                                elif cevap2 == 2:
                                    
                                        SetAngle(180)
                                        
                                        while True:
                                            GPIO.output(buzzer,GPIO.HIGH)
                                            print("Kapı kapandı.")
                                            sleep(0.25)
                                            GPIO.output(buzzer,GPIO.LOW)
                                            sleep(1)
                                            
                                            GPIO.setmode(GPIO.BOARD)
                                            GPIO.setup(31, GPIO.OUT)
                                            for i in range(0,1):
                                                blink(31)                                       
                                            break
                                        
                        elif cevap == 2:
                            
                                print("Çıkış yapılıyor...")
                                time.sleep(0.25)
                                print("Çıkış yapıldı.")
                                time.sleep(0.25)
                                
                                GPIO.output(buzzer,GPIO.HIGH)
                                sleep(0.375)
                                GPIO.output(buzzer,GPIO.LOW)
                                sleep(1)
                                break
        else:
                print("Geçersiz Kart!")
                while True:
                                            
                                            GPIO.output(buzzer,GPIO.HIGH)
                                            print("Giriş izniniz yoktur!")
                                            sleep(0.625)
                                            GPIO.output(buzzer,GPIO.LOW)
                                            sleep(0.150)
                                                                                        
                                            GPIO.output(buzzer,GPIO.HIGH)
                                            sleep(0.625)
                                            GPIO.output(buzzer,GPIO.LOW)
                                            sleep(0.150)
                                            
                                            GPIO.output(buzzer,GPIO.HIGH)
                                            sleep(0.625)
                                            GPIO.output(buzzer,GPIO.LOW)
                                            sleep(0.150)
                                            
                                            GPIO.setmode(GPIO.BOARD)
                                            GPIO.setup(31, GPIO.OUT)
                                            for i in range(0,1):
                                                blink(31)
                                            break                               
finally:
        GPIO.cleanup()